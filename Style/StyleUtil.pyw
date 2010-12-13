from PyQt4.QtCore import Qt, QRect, QSize, QPoint, qDebug, qWarning, QSysInfo
from PyQt4.QtGui import *

TGB_CtrlList = [QStyle.SC_GroupBoxCheckBox, 
                QStyle.SC_GroupBoxLabel, 
                QStyle.SC_GroupBoxContents, 
                QStyle.SC_GroupBoxFrame]

class FormattedPrint():
    @staticmethod
    def rect(rect : QRect):
        return str.format('QRect({}, {}, {}, {})', 
                             rect.left(), rect.top(), 
                             rect.width(), rect.height())
    @staticmethod
    def point(p : QPoint):
        return str.format('QPoint({},{})', p.x(), p.y())
        
    @staticmethod
    def size(sz : QSize):
        return str.format('QSize({}, {})', sz.width(), sz.height())

class StyleHelper():
    ToolGroupBox = 0x00
    CE_ToolButtonIcon = 0x01
    CE_ToolButtonLabel = 0x02
    
    def copyStyleOption(target, source):
        target.direction = source.direction
        target.fontMetrics = source.fontMetrics
        target.palette = source.palette
        target.rect = source.rect
        target.state = source.state
    
    @staticmethod
    def __drawFocusRect(fropt : QStyleOptionFocusRect, p : QPainter):
            ### check for d->alt_down
            if not fropt.state & QStyle.State_KeyboardFocusChange:
                return
            r = fropt.rect
            p.save()
            p.setBackgroundMode(Qt.TransparentMode)
            bg_col = fropt.backgroundColor
            if not bg_col.isValid():
                bg_col = p.background().color();
            # Create an "XOR" color.
            patternCol = QColor((bg_col.red() ^ 0xff) & 0xff,
                                (bg_col.green() ^ 0xff) & 0xff,
                                (bg_col.blue() ^ 0xff) & 0xff)
            p.setBrush(QBrush(patternCol, Qt.Dense4Pattern))
            p.setBrushOrigin(r.topLeft())
            p.setPen(Qt.NoPen)
            p.drawRect(r.left(), r.top(), r.width(), 1)    # Top
            p.drawRect(r.left(), r.bottom(), r.width(), 1) # Bottom
            p.drawRect(r.left(), r.top(), 1, r.height())   # Left
            p.drawRect(r.right(), r.top(), 1, r.height())  # Right
            p.restore()

    @staticmethod
    def __drawGroupBoxFrame(frame : QStyleOptionFrameV2, p : QPainter, alignBottom : bool):
        if frame.features & QStyleOptionFrameV2.Flat:
            fr = frame.rect
            if not alignBottom:
                p1 = QPoint(fr.x(), fr.y() + 1)
                p2 = QPoint(fr.x() + fr.width(), p1.y())
            else:
                p1 = QPoint(fr.x(), fr.bottom() - 1)
                p2 = QPoint(fr.x() + fr.width(), p1.y())
            qDrawShadeLine(p, p1, p2, frame.palette, True,
                           frame.lineWidth, frame.midLineWidth)
        else:
            qDrawShadeRect(p, frame.rect.x(), frame.rect.y(), frame.rect.width(),
                           frame.rect.height(), frame.palette, True,
                           frame.lineWidth, frame.midLineWidth)
    
    def drawPrimitive(self, el : QStyle.PrimitiveElement, opt : QStyleOption, p : QPainter, widget : QWidget = None ) -> None:
#        if el == QStyle.PE_PanelButtonTool:
#            qDrawShadePanel(p, opt.rect, opt.palette,
#                        opt.state & (QStyle.State_Sunken | QStyle.State_On), 1,
#                        opt.palette.brush(QPalette.Button))
#        elif el == QStyle.PE_FrameFocusRect:
#            bg = opt.palette.color(QPalette.Button) #QColor
#            oldPen = p.pen()
#            if bg:
#                hsv = bg.getHsv()
#                if (hsv[2] >= 128): # V
#                    p.setPen(Qt.black)
#                else:
#                    p.setPen(Qt.white)
#            else:
#                p.setPen(opt.palette.foreground().color())
#            focusRect = opt.rect.adjusted(1, 1, -1, -1)
#            p.drawRect(focusRect.adjusted(0, 0, -1, -1)) #draw pen inclusive
#            p.setPen(oldPen)
#        elif el == QStyle.PE_IndicatorButtonDropDown:
#            qDrawShadePanel(p, opt.rect, opt.palette,
#                    opt.state & (QStyle.State_Sunken | QStyle.State_On), 
#                    1, opt.palette.brush(QPalette.Button))
#        elif el == QStyle.PE_IndicatorArrowDown:
#            ...
#        elif el == QStyle.PE_PanelButtonTool:
#            qDrawShadeRect(p, opt.rect, opt.palette,
#                    opt.state & (State_Sunken | State_On), 1, 0)
#        else:
        self.__proxy.drawPrimitive(el, opt, p, widget)

    @staticmethod
    def __generateArrow(palette : QPalette):
            image = QImage(5, 5, QImage.Format_ARGB32)
            image.fill(Qt.transparent)
            imagePainter = QPainter(image)
            imagePainter.setPen(palette.buttonText().color())
            imagePainter.drawLine(0, 0, 4, 0)
            imagePainter.drawLine(1, 1, 3, 1)
            imagePainter.drawPoint(2, 2)
            
            imagePainter.setPen(QColor(255, 255, 255, 127))
            imagePainter.drawPoints(QPoint(0, 1), 
                                     QPoint(1, 2), 
                                     QPoint(2, 3), 
                                     QPoint(3, 2), 
                                     QPoint(4, 1))
            imagePainter.end()
            
            return QPixmap.fromImage(image)
            

