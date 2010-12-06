from PyQt4.QtCore import *
from PyQt4.QtGui import *



def DrawGroupBoxFrameV2(frame, p, widget = None):
    if frame.version == QStyleOptionFrameV2.Version:
        if frame.features & QStyleOptionFrameV2.Flat:
            fr = frame.rect
            p1 = QPoint(fr.x(), fr.y() + 1)
            p2 = QPoint(fr.x() + fr.width(), p1.y())
            qDrawShadeLine(p, p1, p2, frame.palette, True,
                           frame.lineWidth, frame.midLineWidth)
        else:
            qDrawShadeRect(p, frame.rect.x(), frame.rect.y(), frame.rect.width(),
                           frame.rect.height(), frame.palette, True,
                           frame.lineWidth, frame.midLineWidth)

def DrawGroupBoxFrameV3(frame, p, widget = None):
    if frame.version == QStyleOptionFrameV3.Version:    
        shape  = frame.frameShape
        if frame.state & QStyle.State_Sunken:
            shadow = QFrame.Sunken
        elif frame.state & QStyle.State_Raised:
            shadow = QFrame.Raised
        else:
            shadow = QFrame.Plain
        
        lw = frame.lineWidth
        mlw = frame.midLineWidth
        
        fgRole = widget.foregroundRole() if widget else QPalette.WindowText

        if shape == QFrame.Box:
            if (shadow == QFrame.Plain):
                qDrawPlainRect(p, frame.rect, frame.palette.color(fgRole), lw)
            else:
                qDrawShadeRect(p, frame.rect, frame.palette, shadow == QFrame.Sunken, lw, mlw)
        elif shape == QFrame.StyledPanel:
            if (shadow == QStyle.State_Sunken) or (shadow == QStyle.State_Raised):
                qDrawShadePanel(p, frame.rect, frame.palette, 
                                shadow == QStyle.State_Sunken, 
                                frame.lineWidth);
            else:
                qDrawPlainRect(p, frame.rect, frame.palette.foreground().color(), frame.lineWidth)
        elif shape == QFrame.Panel:
            if shadow == QFrame.Plain:
                qDrawPlainRect(p, frame.rect, frame.palette.color(fgRole), lw)
            else:
                qDrawShadePanel(p, frame.rect, frame.palette, shadow == QFrame.Sunken, lw)
        elif shape == QFrame.WinPanel:
            if (shadow == QFrame.Plain):
                qDrawPlainRect(p, frame.rect, frame.palette.color(fgRole), lw)
            else:
                qDrawWinPanel(p, frame.rect, frame.palette, shadow == QFrame.Sunken)
        elif shape == QFrame.HLine or shape == QFrame.VLine:
            p1, p2 = QPoint(), QPoint()
            if (shape == QFrame.HLine):
                p1 = QPoint(frame.rect.x(), frame.rect.height() / 2)
                p2 = QPoint(frame.rect.x() + frame.rect.width(), p1.y())
            else:
                p1 = QPoint(frame.rect.x()+frame.rect.width() / 2, 0)
                p2 = QPoint(p1.x(), frame.rect.height())
            if shadow == QFrame.Plain:
                oldPen = p.pen()
                p.setPen(QPen(frame.palette.brush(fgRole), lw))
                p.drawLine(p1, p2)
                p.setPen(oldPen)
            else:
                qDrawShadeLine(p, p1, p2, frame.palette, shadow == QFrame.Sunken, lw, mlw)


class ToolGroupBox(QGroupBox):
#    clicked = pyqtSignal(bool)
#    toggled = pyqtSignal(bool)
    
    def __init__(self, 
                 title : str = None, 
                 parent : QWidget = None, 
#                 action : ExtendedAction = None, 
                 alignment : Qt.Alignment = Qt.AlignHCenter | Qt.AlignBottom, 
                 checkable : bool = False, 
                 shape : QFrame.Shape = None, 
                 shadow : QFrame.Shadow = None):
        if title:
            super().__init__(title, parent)
        else:
            super().__init__(parent)
            
        self.setAlignment(alignment)
        self.setCheckable(checkable)

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

    def __subControlRect(control, self, opt):
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

class DebugBox(QPlainTextEdit):
    def __init__(self, parent : QWidget = None, text : str = None):
        super().__init__(parent)
        if text:
            self.setPlainText(text)
        self.setReadOnly(True)
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Sunken)
    
    def postMsg(self, msgType = QtDebugMsg, text : str = None) -> None:
        if msgType == QtDebugMsg:
            self.appendPlainText('Debug: ' + bytes.decode(text))
        elif msgType == QtWarningMsg:
            self.appendPlainText('Warning: ' + bytes.decode(text))
        elif msgType == QtCriticalMsg:
            print('Critical: ' + bytes.decode(text))
        elif msgType == QtFatalMsg:
            print('Fatal: ' + bytes.decode(text))
        else:
            print('Unknown Error: ' + bytes.decode(text))
        
class GenericDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setObjectName('dialog')
        self.setWindowTitle('Test Dialog')
        self.setFont(QFont('Segoe Ui', 9))
        
        self.__setupUi()
        
        self.buttonBox.accepted.connect(self.accept)
        
    def __setupUi(self):
        self.layout = QVBoxLayout(self)
        self.layout.setObjectName('layout')
        
        toolGroupBox = ToolGroupBox(title = '&Test2', parent = self,
                                    checkable=True, alignment = Qt.AlignLeft | Qt.AlignBottom)
        toolGroupBox.setFixedSize(200, 50)
#        toolGroupBox.setFrameShape(QFrame.Box)
#        toolGroupBox.setFrameShadow(QFrame.Raised)
        self.layout.addWidget(toolGroupBox)
        
        grpBox = QGroupBox('&Test2', self)
        grpBox.setAlignment(Qt.AlignLeft)
        grpBox.setFixedSize(200, 50)
        grpBox.setCheckable(True)
        grpBox.setFlat(False)
        self.layout.addWidget(grpBox)
        
        dbgBox = DebugBox(self)
        self.layout.addWidget(dbgBox)
        qInstallMsgHandler(dbgBox.postMsg)
        
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok, 
                                          Qt.Horizontal, self)
        self.layout.addWidget(self.buttonBox)
        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = GenericDialog()
    dialog.show()
    sys.exit(app.exec_())
