from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ToolGroupBox(QWidget):
    clicked = pyqtSignal(bool)
    toggled = pyqtSignal(bool)
    
    def __init__(self, 
                 title : str = None, 
                 parent : QWidget = None, 
#                 action : ExtendedAction = None, 
                 alignment : Qt.Alignment = Qt.AlignHCenter, 
                 flat : bool = False, 
                 checkable : bool = False):
        super(QWidget, self).__init__(parent)
        
        if alignment: self.__align = alignment
        else: self.__align = Qt.AlignLeft | Qt.AlignTop
        
        if flat: self.__flat = flat
        else: self.__flat = False
        
        self.__checkable = checkable
        self.__checked = True
        
#        if action:        
#            self.setDefaultAction(action)
        
        # QGroupBox's normally private attributes
        self.__shortcutId = 0
        self.__hover = False
        self.__overCheckBox = False
        self.__pressedControl = QStyle.SC_None
        self.__title = None
        
        self.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, 
                                       QSizePolicy.Preferred, 
                                       QSizePolicy.GroupBox))
        # Note: calling setTitle last eliminates the need to call __calculateFrame(), 
        # update(), and updateGeometry()
        if title:
            self.setTitle(title)

    def initStyleOption(self, opt : QStyleOptionGroupBox) -> None:
        if not opt:
            return
        
        # since this is a custom class, initFrom doesn't work so well
        opt.state = QStyle.State_None
        opt.direction = self.layoutDirection()
        opt.rect = self.rect()
        opt.palette = self.palette()
        opt.fontMetrics = self.fontMetrics()
        opt.text = self.__title
        opt.lineWidth = 1
        opt.midLineWidth = 0
        opt.textAlignment = Qt.Alignment(self.__align)
        opt.activeSubControls |= self.__pressedControl
        opt.subControls = QStyle.SC_GroupBoxFrame
        
        if self.__hover:
            opt.state |= QStyle.State_MouseOver
        else:
            opt.state &= ~QStyle.State_MouseOver

        if self.__flat:
            opt.features |= QStyleOptionFrameV2.Flat
        else:
            opt.features |= 0x00

        if self.__checkable:
            opt.subControls |= QStyle.SC_GroupBoxCheckBox
            opt.state |= QStyle.State_On if self.__checked else QStyle.State_Off

            if (self.__pressedControl == QStyle.SC_GroupBoxCheckBox \
                    or self.__pressedControl == QStyle.SC_GroupBoxLabel) \
                    and (self.__hover or self.__overCheckBox):
                opt.state |= QStyle.State_Sunken
        if not opt.palette.isBrushSet((QPalette.Active if self.isEnabled() else QPalette.Disabled), QPalette.WindowText):
            opt.textColor = QColor(self.style().styleHint(QStyle.SH_GroupBox_TextLabelColor,
                                       opt, self));

        if self.__title:
            opt.subControls |= QStyle.SC_GroupBoxLabel

    def minimumSizeHint(self) -> QSize:
        opt = QStyleOptionGroupBox()
        self.initStyleOption(opt)

        metrics = QFontMetrics(self.fontMetrics())
        baseWidth = metrics.width(self.__title) + metrics.width(' ')
        baseHeight = metrics.height()
        style = self.style()
        if self.__checkable:
            baseWidth += style.pixelMetric(QStyle.PM_IndicatorWidth)
            baseWidth += style.pixelMetric(QStyle.PM_CheckBoxLabelSpacing)
            baseHeight = (baseHeight\
                    if style.pixelMetric(QStyle.PM_IndicatorHeight) < baseHeight\
                    else style.pixelMetric(QStyle.PM_IndicatorHeight))

        size = style.sizeFromContents(QStyle.CT_GroupBox, opt, 
                                      QSize(baseWidth, baseHeight), self)
        return size.expandedTo(super().minimumSizeHint())

    #################################################
    # Event Handlers                                #
    #################################################
    def paintEvent(self, ev: QPaintEvent) -> None:
        p = QStylePainter(self)
        opt = QStyleOptionGroupBox()
        self.initStyleOption(opt)
        p.drawComplexControl(QStyle.CC_GroupBox, opt)

    def event(self, ev : QEvent) -> bool:
        if ev.type() == QEvent.Shortcut:
            if ev.shortcutId() == self.__shortcutId:
                if not self.isCheckable():
                    self.__fixFocus(Qt.ShortcutFocusReason)
                else:
                    self.__click()
                    self.setFocus(Qt.ShortcutFocusReason)
                return true

        box = QStyleOptionGroupBox()
        self.initStyleOption(box)
        
        if ev.type() == QEvent.HoverEnter or ev.type() == QEvent.HoverMove:
            control = self.style().hitTestComplexControl(QStyle.CC_GroupBox, 
                                                         box, ev.pos(), self)
            oldHover = self.__hover;
            self.__hover = self.checkable() and \
                (control == QStyle.SC_GroupBoxLabel or control == QStyle.SC_GroupBoxCheckBox)
            if oldHover != self.__hover:
                rect = self.style().subControlRect(QStyle.CC_GroupBox, box, QStyle.SC_GroupBoxCheckBox, self) \
                             | style().subControlRect(QStyle.CC_GroupBox, box, QStyle.SC_GroupBoxLabel, self)
                self.update(rect)
            return True
        elif ev.type() == QEvent.HoverLeave:
            self.__hover = false
            if self.checkable():
                rect = style().subControlRect(QStyle.CC_GroupBox, box, QStyle.SC_GroupBoxCheckBox, self) \
                             | style().subControlRect(QStyle.CC_GroupBox, box, QStyle.SC_GroupBoxLabel, self)
                self.update(rect)
            return True
        elif ev.type() == QEvent.KeyPress:
            if ev.isAutoRepeat() and (ev.key() == Qt.Key_Select or ev.key() == Qt.Key_Space):
                self.__pressedControl = QStyle.SC_GroupBoxCheckBox
                self.update(style().subControlRect(QStyle.CC_GroupBox, box, QStyle.SC_GroupBoxCheckBox, self))
                return True
        elif ev.type() == QEvent.KeyRelease:
            if ev.isAutoRepeat() and (ev.key() == Qt.Key_Select or ev.key() == Qt.Key_Space):
                toggle = self.__pressedControl == QStyle.SC_GroupBoxLabel \
                        or self.__pressedControl == QStyle.SC_GroupBoxCheckBox
                self.__pressedControl = QStyle.SC_None
                if toggle:
                    self.__click()
                return True
        return super(QWidget, self).event(ev)
        
    def focusInEvent(self, ev : QFocusEvent) -> None:
        if self.focusPolicy() == Qt.NoFocus:
            self.__fixFocus(ev.reason())
        else:
            super(QWidget, self).focusInEvent(ev)
            
    def changeEvent(self, ev : QEvent) -> None:
        if ev.type() == QEvent.EnabledChange and self.__checkable \
                and self.isEnabled() and not self.__checked:
            # we are being enabled - disable children
            self.__setChildrenEnabled(False)
        elif ev.type() == QEvent.FontChange or ev.type() == QEvent.StyleChange:
            self.__calculateFrame()
        super(self, QWidget).changeEvent(ev)

    def mousePressEvent(self, ev : QMouseEvent) -> None:
        if ev.button() != Qt.LeftButton:
            ev.ignore()
            return
    
        box = QStyleOptionGroupBox()
        self.initStyleOption(box)
        self.__pressedControl = \
                self.style().hitTestComplexControl(QStyle.CC_GroupBox, box, ev.pos(), self)

        if self.__checkable and (self.__pressedControl == QStyle.SC_GroupBoxCheckBox \
                or self.__pressedControl == QStyle.SC_GroupBoxLabel):
            self.__overCheckBox = True
            self.update(self.style().subControlRect(QStyle.CC_GroupBox, box, 
                                                    QStyle.SC_GroupBoxCheckBox, self))

    def mouseMoveEvent(self, ev : QMouseEvent) -> None:
        box = QStyleOptionGroupBox()
        self.initStyleOption(box);
        style = self.style()
        pressed = style.hitTestComplexControl(QStyle.CC_GroupBox, box, ev.pos(), self)
        oldOverCheckBox = self.__overCheckBox
        if pressed == QStyle.SC_GroupBoxCheckBox or pressed == QStyle.SC_GroupBoxLabel:
            self.__overCheckBox = True
        else:
            self.__overCheckBox = False
        if self.__checkable and (self.__pressedControl == QStyle.SC_GroupBoxCheckBox \
                or self.__pressedControl == QStyle.SC_GroupBoxLabel)\
                and self.__overCheckBox != oldOverCheckBox:
            self.update(style.subControlRect(QStyle.CC_GroupBox, box, 
                                             QStyle.SC_GroupBoxCheckBox, self))

    def mouseReleaseEvent(self, ev : QMouseEvent) -> None:
        if (ev.button() != Qt.LeftButton):
            ev.ignore()
            return
        
        box = QStyleOptionGroupBox()
        self.initStyleOption(box)
        
        released = self.style().hitTestComplexControl(QStyle.CC_GroupBox, box,
                                                      event.pos(), self)
        toggle = self.__checkable and (released == QStyle.SC_GroupBoxLabel \
                                       or released == QStyle.SC_GroupBoxCheckBox)
        
        self.__pressedControl = QStyle.SC_None
        self.__overCheckBox = False
        
        if toggle:
            self.__click()
        elif self.__checkable:
            self.update(self.style().subControlRect(QStyle.CC_GroupBox, box, 
                                                    QStyle.SC_GroupBoxCheckBox, self))

    #################################################
    # Getters                                       #
    #################################################

    def alignment(self) -> Qt.Alignment:
        return Qt.Alignment(self.__align)
            
    def isCheckable(self) -> bool:
        if self.__checkable: return True
        return False
        
    def isChecked(self) -> bool:
        if self.__checkable and self.__checked: return True
        return False
        
    def isFlat(self) -> bool:
        if self.__flat: return True
        return False
        
    def title(self) -> str:
        return str(self.__title)

    #################################################
    # Setters                                       #
    #################################################

    def setAlignment(self, align : Qt.Alignment = Qt.AlignLeft):
        self.__align = align
        self.updateGeometry()
        self.update()

    def setFlat(self, b = False) -> None:
        if self.__flat == b:
            return
        self.__flat = b
        self.updateGeometry()
        self.update()

    def setCheckable(self, checkable = False) -> None:
        wasCheckable = self.__checkable
        self.__checkable = checkable

        if checkable:
            self.setChecked(True)
            if not wasCheckable:
                self.setFocusPolicy(Qt.StrongFocus)
                self.__setChildrenEnabled(True)
                self.updateGeometry()
        else:
            if wasCheckable:
                self.setFocusPolicy(Qt.NoFocus)
                self.__setChildrenEnabled(True);
                updateGeometry();
            self.__setChildrenEnabled(True)

        if wasCheckable != checkable:
            self.__calculateFrame();
            self.update()
    
    @pyqtSlot(bool)
    def setChecked(self, b = False) -> None:
        if self.__checkable and b != self.__checked:
            self.update()
            self.__checked = b;
            self.__setChildrenEnabled(b)
            self.toggled.emit(b)
        
    def setTitle(self, title : str = None) -> None:
        if self.__title == title:
            return
        self.__title = title
        self.releaseShortcut(self.__shortcutId)
        self.__shortcutId = self.grabShortcut(QKeySequence.mnemonic(title))
        self.__calculateFrame()
        self.update()
        self.updateGeometry()
#        QAccessible.updateAccessibility(self, None, QAccessible.NameChanged)
        
    #################################################
    # Private Methods                               #
    #################################################
    def __calculateFrame(self) -> None:
        box = QStyleOptionGroupBox()
        self.initStyleOption(box)
        contentsRect = self.style().subControlRect(QStyle.CC_GroupBox, box, 
                                                   QStyle.SC_GroupBoxContents, self)
        self.setContentsMargins(contentsRect.left() - box.rect.left(),
                                contentsRect.top() - box.rect.top(),
                                box.rect.right() - contentsRect.right(),
                                box.rect.bottom() - contentsRect.bottom())
#        self.setLayoutItemMargins(QStyle.SE_GroupBoxLayoutItem, box)
        
    def __fixFocus(self, reason : Qt.FocusReason) -> None:
        fw = self.focusWidget()
        if not fw or self == fw:
            best = None
            candidate = None
            w = self.nextInFocusChain()
            while w != self:
                if self.isAncestorOf(w) and (w.focusPolicy() & Qt.TabFocus) == Qt.TabFocus and w.isVisibleTo(self):
                    if not best and isinstance(w, QRadioButton) and w.isChecked():
                        # we prefer a checked radio button or a widget that
                        # already has focus, if there is one
                        best = w
                    elif not candidate:
                        # but we'll accept anything that takes focus
                        candidate = w
            if best:
                fw = best
            elif candidate:
                fw = candidate
            w = w.nextInFocusChain()
        if fw:
            fw.setFocus(reason)

    def __skip(self) -> None:
        pass
    
    def __setChildrenEnabled(self, b : bool) -> None:
        childList = self.children()
        for child in childList:
            if child.isWidgetType():
                if b and not child.testAttribute(Qt.WA_ForceDisabled):
                    child.setEnabled(true);
                elif child.isEnabled():
                    child.setEnabled(False)
                    child.setAttribute(Qt.WA_ForceDisabled, False)
        
    def __click(self) -> None:
        if self.__checked:
            self.setChecked(False)
            self.checked.emit(False)
        else:
            self.setChecked(True)
            self.checked.emit(True)
            
class GenericDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setObjectName('dialog')
        self.setWindowTitle('QGroupBox Test')
        self.resize(371, 151)
        self.setFont(QFont('Segoe UI', 9))
        
        self.__setupUi()
        
        self.buttonBox.accepted.connect(self.accept)
        
    def __setupUi(self):
        self.layout = QVBoxLayout(self)
        self.layout.setObjectName('layout')
        
        tgb = ToolGroupBox(title='Test', 
                           parent=self, 
#                           checkable=True, 
                           flat=True)
        tgb.setFixedSize(100, 100)
        self.layout.addWidget(tgb)
        
        gb = QGroupBox('Test2', self)
        gb.setFixedSize(100, 100)
        self.layout.addWidget(gb)
        
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok, 
                                          Qt.Horizontal, self)
        self.layout.addWidget(self.buttonBox)
        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = GenericDialog()
    dialog.show()
    sys.exit(app.exec_())
