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
        super().__init__(parent)

        self.__flat = flat if flat else False
        self.__checkable = checkable if checkable else False
        self.__checked = True
        self.__align = alignment if alignment else Qt.AlignLeft | Qt.AlignBottom
        self.__shortcutId = 0
        self.__hover = False
        self.__overCheckBox = False
        self.__pressedControl = QStyle.SC_None
        self.__title = None #have to set self now so setTitle doesn't get upset
        self.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, 
                                       QSizePolicy.Preferred, 
                                       QSizePolicy.GroupBox))
#        if action: self.setDefaultAction(action)
        
        #self handles calls to __calculateFrame(), update(), and updateGeometry()
        if title: self.setTitle(title)
        
    def initStyleOption(self, opt : QStyleOptionGroupBox) -> None:
        window = self.window()
        opt.version = 1
        opt.type = QStyleOption.SO_GroupBox
        
        opt.direction = self.layoutDirection()
        opt.fontMetrics = self.fontMetrics()
        opt.palette = self.palette()
        opt.rect = self.rect()
        
        opt.state = QStyle.State_None
        if self.isEnabled():
            opt.state |= QStyle.State_Enabled
        if self.hasFocus():
            opt.state |= QStyle.State_HasFocus
        if window.testAttribute(Qt.WA_KeyboardFocusChange):
            opt.state |= QStyle.State_KeyboardFocusChange
        if self.underMouse():
            opt.state |= QStyle.State_MouseOver
        if window.isActiveWindow():
            opt.state |= QStyle.State_Active
        if self.isWindow():
            opt.state |= QStyle.State_Window
        if self.__hover:
            opt.state |= QStyle.State_MouseOver
#        else:
#            opt.state &= ~QStyle.State_MouseOver;
        opt.text = self.__title
        opt.lineWidth = 1
        opt.midLineWidth = 0
        opt.textAlignment = Qt.Alignment(self.__align)
        opt.activeSubControls = QStyle.SC_All | self.__pressedControl
        opt.subControls = QStyle.SC_GroupBoxFrame

        if self.__flat:
            opt.features = QStyleOptionFrameV2.Flat
        else:
            opt.features = QStyleOptionFrameV2.FrameFeatures(0x00)

        if self.__checkable:
            opt.subControls |= QStyle.SC_GroupBoxCheckBox
            opt.state |= QStyle.State_On if self.__checked else QStyle.State_Off
            if (self.__pressedControl == QStyle.SC_GroupBoxCheckBox
                    or self.__pressedControl == QStyle.SC_GroupBoxLabel) \
                    and (self.__hover or self.__overCheckBox):
                opt.state |= QStyle.State_Sunken;

        if not opt.palette.isBrushSet(\
                (QPalette.Active if self.isEnabled() else QPalette.Disabled), QPalette.WindowText):
            opt.textColor = QColor(self.style().styleHint(QStyle.SH_GroupBox_TextLabelColor,
                                       opt, self))

        if self.__title:
            opt.subControls |= QStyle.SC_GroupBoxLabel
        
    def minimumSizeHint(self) -> QSize:
        opt = QStyleOptionGroupBox()
        self.initStyleOption(opt)
        style = self.style()
        metrics = self.fontMetrics()

        baseWidth = metrics.width(self.__title) + metrics.width(' ')
        baseHeight = metrics.height()
        if self.__checkable:
            baseWidth += style.pixelMetric(QStyle.PM_IndicatorWidth)
            baseWidth += style.pixelMetric(QStyle.PM_CheckBoxLabelSpacing)
            if baseHeight < style.pixelMetric(QStyle.PM_IndicatorHeight):
                baseHeight = style.pixelMetric(QStyle.PM_IndicatorHeight)

        size = style.sizeFromContents(QStyle.CT_GroupBox, opt, 
                                      QSize(baseWidth, baseHeight), self)
        return size.expandedTo(super().minimumSizeHint())

    #################################################
    # Event Handling Reimplementations              #
    #################################################
    def event(self, ev : QEvent) -> bool:
        if ev.type() == QEvent.Shortcut and ev.shortcutId() == self.__shortcutId:
            if not self.isCheckable():
                self.__fixFocus(Qt.ShortcutFocusReason)
            else:
                self.__click()
                self.setFocus(Qt.ShortcutFocusReason)
            return True

        opt = QStyleOptionGroupBox()
        self.initStyleOption(opt)
        style = self.style()
        
        if ev.type() == QEvent.HoverEnter or ev.type() == QEvent.HoverMove:
            control = style.hitTestComplexControl(QStyle.CC_GroupBox, 
                                                         opt, ev.pos(), self)
            oldHover = self.__hover;
            self.__hover = self.checkable() and \
                (control == QStyle.SC_GroupBoxLabel or control == QStyle.SC_GroupBoxCheckBox)
            if oldHover != self.__hover:
                rect = style.subControlRect(QStyle.CC_GroupBox, opt, QStyle.SC_GroupBoxCheckBox, self) \
                             | style.subControlRect(QStyle.CC_GroupBox, opt, QStyle.SC_GroupBoxLabel, self)
                self.update(rect)
            return True
        elif ev.type() == QEvent.HoverLeave:
            self.__hover = False
            if self.checkable():
                rect = style.subControlRect(QStyle.CC_GroupBox, box, QStyle.SC_GroupBoxCheckBox, self) \
                             | style.subControlRect(QStyle.CC_GroupBox, box, QStyle.SC_GroupBoxLabel, self)
                self.update(rect)
            return True
        elif ev.type() == QEvent.KeyPress:
            if ev.isAutoRepeat() and (ev.key() == Qt.Key_Select or ev.key() == Qt.Key_Space):
                self.__pressedControl = QStyle.SC_GroupBoxCheckBox
                self.update(style.subControlRect(QStyle.CC_GroupBox, box, QStyle.SC_GroupBoxCheckBox, self))
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
    
    def changeEvent(self, ev : QEvent):
        # Determine if we're being enabled/disabled, we have a checkbox,
        # we are presently enabled and not currently checked
        if ev.type() == QEvent.EnabledChange and self.__checkable \
                and self.isEnabled() and not self.__checked:
                    self.___setChildrenEnabled(False)
        elif (ev.type() == QEvent.FontChange or ev.type() == QEvent.StyleChange):
            self.__calculateFrame()
        super(QWidget, self).changeEvent(ev)
    
    def childEvent(self, ev : QChildEvent) -> None:
        if ev.type() != QEvent.ChildAdded or not ev.child().isWidgetType():
            return
        if self.__checkable:
            w = ev.child()
            if self.__checked and not w.testAttribute(Qt.WA_ForceDisabled):
                w.setEnabled(True)
            elif w.isEnabled():
                w.setEnabled(False);
                w.setAttribute(Qt.WA_ForceDisabled, False)

    def focusInEvent(self, ev : QFocusEvent) -> None:
        if self.focusPolicy() == Qt.NoFocus:
            self.__fixFocus(ev.reason())
        else:
            super(QWidget, self).focusInEvent(ev)

    def mousePressEvent(self, ev : QMouseEvent) -> None:
        if ev.button() != Qt.LeftButton:
            ev.ignore()
            return

        opt = QStyleOptionGroupBox()
        self.initStyleOption(opt)
        style = self.style()
        self.__pressedControl = style.hitTestComplexControl(QStyle.CC_GroupBox, opt,
                                                            ev.pos(), self)
        if self.__checkable and (self.__pressedControl & (QStyle.SC_GroupBoxCheckBox | QStyle.SC_GroupBoxLabel)):
            self.__overCheckBox = True
            self.update(style.subControlRect(QStyle.CC_GroupBox, opt, 
                                             QStyle.SC_GroupBoxCheckBox, self))

    def mouseMoveEvent(self, ev : QMouseEvent) -> None:
        opt = QStyleOptionGroupBox()
        self.initStyleOption(opt)
        style = self.style()
        pressed = style.hitTestComplexControl(QStyle.CC_GroupBox, opt,
                                                 ev.pos(), self)
        oldOverCheckBox = self.__overCheckBox;
        self.__overCheckBox = (pressed == QStyle.SC_GroupBoxCheckBox or pressed == QStyle.SC_GroupBoxLabel)
        
        # Are we checkable, was the label or checkbox clicked, and are we or were we over the checkbox?
        if (self.__checkable) \
                and (self.__pressedControl == QStyle.SC_GroupBoxCheckBox or self.__pressedControl == QStyle.SC_GroupBoxLabel) \
                and (self.__overCheckBox != oldOverCheckBox):
            self.update(style.subControlRect(QStyle.CC_GroupBox, opt, 
                                             QStyle.SC_GroupBoxCheckBox, self))

    def mouseReleaseEvent(self, ev: QMouseEvent) -> None:
        if ev.button() != Qt.LeftButton:
            ev.ignore()
            return
        opt = QStyleOptionGroupBox()
        self.initStyleOption(opt)
        style = self.style()
        released = style.hitTestComplexControl(QStyle.CC_GroupBox, opt,
                                               ev.pos(), self)
        toggle = self.__checkable and (released == QStyle.SC_GroupBoxLabel \
                                       or released == QStyle.SC_GroupBoxCheckBox)
        self.__pressedControl = QStyle.SC_None;
        self.__overCheckBox = False;
        if toggle:
            self.__click()
        elif self.__checkable:
            self.update(style.subControlRect(QStyle.CC_GroupBox, opt, 
                                             QStyle.SC_GroupBoxCheckBox, self))

    def paintEvent(self, ev: QPaintEvent) -> None:
        p = QPainter(self)
        opt = QStyleOptionGroupBox()
        self.initStyleOption(opt)
#        p.drawComplexControl(QStyle.CC_GroupBox, opt)
        proxy = self.style().proxy()

        # Draw frame
        textRect = proxy.subControlRect(CC_GroupBox, opt, SC_GroupBoxLabel, self)
        checkBoxRect = proxy.subControlRect(CC_GroupBox, opt, SC_GroupBoxCheckBox, self)
        if opt.subControls & QStyle.SC_GroupBoxFrame:
            frame = QStyleOptionFrameV2(opt)
            frame.features = opt.features
            frame.lineWidth = opt.lineWidth
            frame.midLineWidth = opt.midLineWidth
            frame.rect = proxy.subControlRect(CC_GroupBox, opt, SC_GroupBoxFrame, widget)
            p.save()
            region = QRegion(opt.rect)
            if opt.text:
                ltr = opt.direction == Qt.LeftToRight
                finalRect = QRect()
                if opt.subControls & QStyle.SC_GroupBoxCheckBox:
                    finalRect = checkBoxRect.united(textRect)
                    finalRect.adjust((-4 if ltr else 0), 0, (0 if ltr else 4), 0)
                else:
                    finalRect = textRect
                region -= finalRect;
            p.setClipRegion(region)
            proxy.drawPrimitive(PE_FrameGroupBox, frame, p, widget)
            p.restore()

        # Draw title
        if (opt.subControls & QStyle.SC_GroupBoxLabel) and opt.text:
            textColor = opt.textColor
            if textColor.isValid():
                p.setPen(textColor)
            alignment = int(opt.textAlignment)
            if not proxy.styleHint(QStyle.SH_UnderlineShortcut, opt, self):
                alignment |= Qt.TextHideMnemonic

            proxy.drawItemText(p, textRect,  Qt.TextShowMnemonic | Qt.AlignHCenter | alignment,
                         opt.palette, opt.state & QStyle.State_Enabled, opt.text,
                         ( QPalette.NoRole if textColor.isValid() else QPalette.WindowText))

            if opt.state & State_HasFocus:
                fropt = QStyleOptionFocusRect(opt)
                fropt.rect = textRect
                proxy.drawPrimitive(PE_FrameFocusRect, fropt, p, self)

        # Draw checkbox
        if opt.subControls & SC_GroupBoxCheckBox:
            box = QStyleOptionButton(opt)
            box.rect = checkBoxRect
            proxy.drawPrimitive(PE_IndicatorCheckBox, box, p, self)


    # Python will automagically pass self to the super(), but we'll implement
    # it anyway for consistancy
    def resizeEvent(self, ev : QResizeEvent) -> None:
        return super(QWidget, self).resizeEvent(ev)
                
    #################################################
    # Getters                                       #
    #################################################
    def alignment(self) -> Qt.Alignment:
        return Qt.Alignment(self.__align)
    
    def isCheckable(self) -> bool:
        return True if self.__checkable else False
        
    def isChecked(self) -> bool:
        return True if (self.__checkable and self.__checked) else False
        
    def isFlat(self) -> bool:
        return True if self.__flat else False
        
    def title(self) -> str:
        return str(self.__title) if self.__title else None

    #################################################
    # Setters                                       #
    #################################################
    def setAlignment(self, alignment : Qt.Alignment) -> None:
        if alignment == self.__align:
            return
        self.__align = alignment
        self.updateGeometry()
        self.update()
    
    def setFlat(self, b = False) -> None:
        if self.__flat == b:
            return
        self.__flat = True if b else False
        self.updateGeometry()
        self.update()

    def setCheckable(self, b = False) -> None:
        wasCheckable = self.__checkable
        self.__checkable = b

        if b:
            self.setChecked(True)
            if not wasCheckable:
                self.setFocusPolicy(Qt.StrongFocus)
                self.__setChildrenEnabled(True)
                self.updateGeometry()
        elif wasCheckable:
                self.setFocusPolicy(Qt.NoFocus)
                self.__setChildrenEnabled(True)
                self.updateGeometry()
        else:
            self.__setChildrenEnabled(True)

        if wasCheckable != checkable:
            self.__calculateFrame()
            self.update()

    def setChecked(self, b = False) -> None:
        if self.__checkable and b != self.__checked:
            self.update()
            self.__checked = b
            self.__setChildrenEnabled(b)
            # Shouldn't update() be down here?
            self.toggled.emit(b)

    def setTitle(self, title : str) -> None:
        if title == self.__title:
            return
        self.__title = title
        self.releaseShortcut(self.__shortcutId)
        self.__shortcutId = self.grabShortcut(QKeySequence.mnemonic(title)) if title else 0
        self.__calculateFrame()
        self.update()
        self.updateGeometry()

    #################################################
    # Private Methods                               #
    #################################################
    def __calculateFrame(self) -> None:
        opt = QStyleOptionGroupBox()
        self.initStyleOption(opt)
        contentsRect = self.style().subControlRect(QStyle.CC_GroupBox, opt,
                                                   QStyle.SC_GroupBoxContents, self)
        self.setContentsMargins(contentsRect.left() - opt.rect.left(),
                                contentsRect.top() - opt.rect.top(),
                              opt.rect.right() - contentsRect.right(), 
                              opt.rect.bottom() - contentsRect.bottom())
#        setLayoutItemMargins(QStyle.SE_GroupBoxLayoutItem, opt)
#        self.updateGeometry()
    
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
                        # already has focus, if there is one -- Qt
                        best = w
                    elif not candidate:
                        # but we'll accept anything that takes focus -- Qt
                        candidate = w
                w = w.nextInFocusChain()
            if best:
                fw = best
            elif candidate:
                fw = candidate
        if fw:
            fw.setFocus(reason)

    # sets all children of the group box except the qt_groupbox_checkbox
    # to either disabled/enabled -- Qt
    def __setChildrenEnabled(self, b : bool) -> None:
        for child in self.children():
            if child.isWidgetType():
                if b and not child.testAttribute(Qt.WA_ForceDisabled):
                    child.setEnabled(True);
                elif child.isEnabled():
                    child.setEnabled(False);
                    child.setAttribute(Qt.WA_ForceDisabled, False)

    def __click(self) -> None:
        self.setChecked(not self.checked())
        self.clicked.emit(self.checked())
        
class GenericDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setObjectName('dialog')
        self.setWindowTitle('Sheet Test')
        self.resize(371, 151)
        self.setFont(QFont('Segoe UI', 9))
        
        self.__setupUi()
        
        self.buttonBox.accepted.connect(self.accept)
        
    def __setupUi(self):
        self.layout = QVBoxLayout(self)
        self.layout.setObjectName('layout')
        
        toolGroupBox = ToolGroupBox(title = 'Test', parent = self)
        toolGroupBox.setFixedSize(200, 100)
        self.layout.addWidget(toolGroupBox)
        toolGroupBox.paintEvent(QPaintEvent(toolGroupBox.rect()))
        
        grpBox = QGroupBox('Test2', self)
        grpBox.setFixedSize(200, 100)
        self.layout.addWidget(grpBox)
        
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok, 
                                          Qt.Horizontal, self)
        self.layout.addWidget(self.buttonBox)
        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = GenericDialog()
    dialog.show()
    sys.exit(app.exec_())
