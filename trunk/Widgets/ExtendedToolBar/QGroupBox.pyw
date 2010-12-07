from PyQt4.QtCore import *
from PyQt4.QtGui import *

controls = [QStyle.SC_GroupBoxFrame, 
            QStyle.SC_GroupBoxLabel, 
            QStyle.SC_GroupBoxCheckBox, 
            QStyle.SC_GroupBoxContents]

class ToolGroupBox(QGroupBox):
    
    def __init__(self, 
                 title : str = None, 
                 parent : QWidget = None, 
#                 action : ExtendedAction = None, 
                 alignment : Qt.Alignment = Qt.AlignHCenter | Qt.AlignBottom, 
                 checkable : bool = False, 
                 flat : bool = False):
        if title:
            super().__init__(title, parent)
        else:
            super().__init__(parent)
            
        self.setAlignment(alignment)
        self.setCheckable(checkable)
        self.setFlat(flat)
        
        self.__overCheckBox = False
        self.__hover = False
        

#    def initStyleOption(self, opt : QStyleOptionGroupBox) -> None:
#        if not opt:
#            return
#        
#        # since this is a custom class, initFrom doesn't work so well
#        opt.state = QStyle.State_None
#        opt.direction = self.layoutDirection()
#        opt.rect = self.rect()
#        opt.palette = self.palette()
#        opt.fontMetrics = self.fontMetrics()
#        opt.text = self.__title
#        opt.lineWidth = 1
#        opt.midLineWidth = 0
#        opt.textAlignment = Qt.Alignment(self.__align)
#        opt.activeSubControls |= self.__pressedControl
#        opt.subControls = QStyle.SC_GroupBoxFrame
#        
#        if self.__hover:
#            opt.state |= QStyle.State_MouseOver
#        else:
#            opt.state &= ~QStyle.State_MouseOver
#
#        if self.__flat:
#            opt.features |= QStyleOptionFrameV2.Flat
#        else:
#            opt.features |= 0x00
#
#        if self.__checkable:
#            opt.subControls |= QStyle.SC_GroupBoxCheckBox
#            opt.state |= QStyle.State_On if self.__checked else QStyle.State_Off
#
#            if (self.__pressedControl == QStyle.SC_GroupBoxCheckBox \
#                    or self.__pressedControl == QStyle.SC_GroupBoxLabel) \
#                    and (self.__hover or self.__overCheckBox):
#                opt.state |= QStyle.State_Sunken
#        if not opt.palette.isBrushSet((QPalette.Active if self.isEnabled() else QPalette.Disabled), QPalette.WindowText):
#            opt.textColor = QColor(self.style().styleHint(QStyle.SH_GroupBox_TextLabelColor,
#                                       opt, self));
#
#        if self.__title:
#            opt.subControls |= QStyle.SC_GroupBoxLabel

#    def minimumSizeHint(self) -> QSize:
#        opt = QStyleOptionGroupBox()
#        self.initStyleOption(opt)
#
#        metrics = QFontMetrics(self.fontMetrics())
#        baseWidth = metrics.width(self.__title) + metrics.width(' ')
#        baseHeight = metrics.height()
#        style = self.style()
#        if self.__checkable:
#            baseWidth += style.pixelMetric(QStyle.PM_IndicatorWidth)
#            baseWidth += style.pixelMetric(QStyle.PM_CheckBoxLabelSpacing)
#            baseHeight = (baseHeight\
#                    if style.pixelMetric(QStyle.PM_IndicatorHeight) < baseHeight\
#                    else style.pixelMetric(QStyle.PM_IndicatorHeight))
#
#        size = style.sizeFromContents(QStyle.CT_GroupBox, opt, 
#                                      QSize(baseWidth, baseHeight), self)
#        return size.expandedTo(super().minimumSizeHint())

    #################################################
    # Event Handlers                                #
    #################################################
    def paintEvent(self, ev: QPaintEvent) -> None:
        p = QPainter(self)
        opt = QStyleOptionGroupBox()
        self.initStyleOption(opt)
        proxy = self.style().proxy()
        

        # Draw frame
        textRect = proxy.subControlRect(QStyle.CC_GroupBox, opt, QStyle.SC_GroupBoxLabel, self)
        checkBoxRect = proxy.subControlRect(QStyle.CC_GroupBox, opt, QStyle.SC_GroupBoxCheckBox, self)
        if opt.textAlignment & Qt.AlignBottom:
            textRect.moveBottom(opt.rect.bottom())
            checkBoxRect.moveBottom(opt.rect.bottom())
        
        if opt.subControls & QStyle.SC_GroupBoxFrame:
            frame = QStyleOptionFrameV3()
            frame = opt
            frame.version = QStyleOptionFrameV2.Version
            frame.features = opt.features
            frame.lineWidth = opt.lineWidth
            frame.midLineWidth = opt.midLineWidth
            frame.rect = proxy.subControlRect(QStyle.CC_GroupBox, opt, QStyle.SC_GroupBoxFrame)
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
                region -= region.intersected(finalRect)
            p.setClipRegion(region)
            DrawGroupBoxFrameV2(frame, p)
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

            if opt.state & QStyle.State_HasFocus:
                fropt = QStyleOptionFocusRect()
                fropt = opt
                fropt.rect = textRect
                proxy.drawPrimitive(QStyle.PE_FrameFocusRect, fropt, p, self)

        # Draw checkbox
        if opt.subControls & QStyle.SC_GroupBoxCheckBox:
            box = QStyleOptionButton()
            box = opt
            box.rect = checkBoxRect
            proxy.drawPrimitive(QStyle.PE_IndicatorCheckBox, box, p, self)

    def event(self, ev : QEvent) -> bool:

        box = QStyleOptionGroupBox()
        self.initStyleOption(box)
        
        if ev.type() == QEvent.HoverEnter or ev.type() == QEvent.HoverMove:
            control = self.style().hitTestComplexControl(QStyle.CC_GroupBox, 
                                                         box, ev.pos(), self)
            oldHover = self.__hover;
            self.__hover = self.checkable() and \
                (control == QStyle.SC_GroupBoxLabel or control == QStyle.SC_GroupBoxCheckBox)
            if oldHover != self.__hover:
                rect = self.__subControlRect(QStyle.CC_GroupBox, box, QStyle.SC_GroupBoxCheckBox, self) \
                             | self.__subControlRect(QStyle.CC_GroupBox, box, QStyle.SC_GroupBoxLabel, self)
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
        return super().event(ev)
        
#    def focusInEvent(self, ev : QFocusEvent) -> None:
#        if self.focusPolicy() == Qt.NoFocus:
#            self.__fixFocus(ev.reason())
#        else:
#            super(QWidget, self).focusInEvent(ev)
            
#    def changeEvent(self, ev : QEvent) -> None:
#        if ev.type() == QEvent.EnabledChange and self.__checkable \
#                and self.isEnabled() and not self.__checked:
#            # we are being enabled - disable children
#            self.__setChildrenEnabled(False)
#        elif ev.type() == QEvent.FontChange or ev.type() == QEvent.StyleChange:
#            self.__calculateFrame()
#        super(self, QWidget).changeEvent(ev)

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
        pressed = style.__subControlRect(box, ev.pos(), self)
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
        toggle = self.checkable() and (released == QStyle.SC_GroupBoxLabel \
                                       or released == QStyle.SC_GroupBoxCheckBox)
        
        self.__pressedControl = QStyle.SC_None
        self.__overCheckBox = False
        
        if toggle:
            self.__click()
        elif self.checkable():
            self.update(self.style().subControlRect(QStyle.CC_GroupBox, box, 
                                                    QStyle.SC_GroupBoxCheckBox, self))

    #################################################
    # Getters                                       #
    #################################################

#    def alignment(self) -> Qt.Alignment:
#        return Qt.Alignment(self.__align)
#            
#    def isCheckable(self) -> bool:
#        if self.__checkable: return True
#        return False
#        
#    def isChecked(self) -> bool:
#        if self.__checkable and self.__checked: return True
#        return False
#        
#    def isFlat(self) -> bool:
#        if self.__flat: return True
#        return False
#        
#    def title(self) -> str:
#        return str(self.__title)

    #################################################
    # Setters                                       #
    #################################################

#    def setAlignment(self, align : Qt.Alignment = Qt.AlignLeft):
#        self.__align = align
#        self.updateGeometry()
#        self.update()
#
#    def setFlat(self, b = False) -> None:
#        if self.__flat == b:
#            return
#        self.__flat = b
#        self.updateGeometry()
#        self.update()
#
#    def setCheckable(self, checkable = False) -> None:
#        wasCheckable = self.__checkable
#        self.__checkable = checkable
#
#        if checkable:
#            self.setChecked(True)
#            if not wasCheckable:
#                self.setFocusPolicy(Qt.StrongFocus)
#                self.__setChildrenEnabled(True)
#                self.updateGeometry()
#        else:
#            if wasCheckable:
#                self.setFocusPolicy(Qt.NoFocus)
#                self.__setChildrenEnabled(True);
#                updateGeometry();
#            self.__setChildrenEnabled(True)
#
#        if wasCheckable != checkable:
#            self.__calculateFrame();
#            self.update()
#    
#    @pyqtSlot(bool)
#    def setChecked(self, b = False) -> None:
#        if self.__checkable and b != self.__checked:
#            self.update()
#            self.__checked = b;
#            self.__setChildrenEnabled(b)
#            self.toggled.emit(b)
#        
#    def setTitle(self, title : str = None) -> None:
#        if self.__title == title:
#            return
#        self.__title = title
#        self.releaseShortcut(self.__shortcutId)
#        self.__shortcutId = self.grabShortcut(QKeySequence.mnemonic(title))
#        self.__calculateFrame()
#        self.update()
#        self.updateGeometry()
#        QAccessible.updateAccessibility(self, None, QAccessible.NameChanged)
        
    #################################################
    # Private Methods                               #
    #################################################
#    def __calculateFrame(self) -> None:
#        opt = QStyleOptionGroupopt()
#        self.initStyleOption(opt)
#        contentsRect = self.style().subControlRect(QStyle.CC_GroupBox, opt, 
#                                                   QStyle.SC_GroupBoxContents, self)
#        self.setContentsMargins(contentsRect.left() - opt.rect.left(),
#                                contentsRect.top() - opt.rect.top(),
#                                opt.rect.right() - contentsRect.right(),
#                                opt.rect.bottom() - contentsRect.bottom())
#        self.setLayoutItemMargins(QStyle.SE_GroupBoxLayoutItem, opt)

#    def hitTestComplexControl(self):
#            r = QRect()
#            ctrl = 0
#            for ctrl in range(len(controls)):
#                r = self.subControlRect(QStyle.CC_GroupBox, groupBox, QStyle.SubControl(ctrl), widget);
#                if (r.isValid() and r.contains(pt)) {
#                    sc = QStyle.SubControl(ctrl);
#                    break;
#                }
#                ctrl <<= 1;
#            }
#        }
#        break;
        
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

    def __click(self) -> None:
        self.setChecked(not self.checked())
        self.clicked.emit(self.checked())
            
    def __subControlRect(self, control, opt):
        proxy = self.style().proxy()
        fontMetrics = opt.fontMetrics;
        h = fontMetrics.height()
        tw = fontMetrics.size(Qt.TextShowMnemonic, opt.text + ' ').width()
        margin = 0 if opt.features & QStyleOptionFrameV2.Flat else 8

        rect = opt.rect.adjusted(margin, 0, 0 - margin, 0);
        rect.setHeight(h)

        indicatorWidth = proxy.pixelMetric(QStyle.PM_IndicatorWidth, opt, self)
        indicatorSpace = proxy.pixelMetric(QStyle.PM_CheckBoxLabelSpacing, opt, self) - 1
        hasCheckBox = opt.subControls & QStyle.SC_GroupBoxCheckBox
        checkBoxSize = (indicatorWidth + indicatorSpace) if hasCheckBox else 0

        # Adjusted rect for label + indicatorWidth + indicatorSpace
        totalRect = proxy.alignedRect(opt.direction, opt.textAlignment,
                                      QSize(tw + checkBoxSize, h), rect);

        # Adjust totalRect if checkbox is set
        if hasCheckBox:
            ltr = opt.direction == Qt.LeftToRight
            left = 0
            # Adjust for check box
            if control == SC_GroupBoxCheckBox:
                indicatorHeight = proxy.pixelMetric(PM_IndicatorHeight, opt, widget);
                left = totalRect.left() if ltr else (totalRect.right() - indicatorWidth);
                top = totalRect.top() + (fontMetrics.height() - indicatorHeight) / 2;
                totalRect.setRect(left, top, indicatorWidth, indicatorHeight);
            # Adjust for label
            else:
                left = (totalRect.left() + checkBoxSize - 2) if ltr else totalRect.left()
                totalRect.setRect(left, totalRect.top(),
                                  totalRect.width() - checkBoxSize, totalRect.height());
        rect = totalRect
            
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
        gb.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
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
