from PyQt4.QtCore import *
from PyQt4.QtGui import *

from .util import Util

#from CleanLooks
def drawDashedHandle(opt, painter):
    button = opt.palette.button().color()
    dark = QColor.fromHsv(button.hue(),
                min((255, int(button.saturation()*1.9))), 
                min((255, int(button.value()*0.7))))
    
    painter.save()
    
    grooveColor = Util.mergedColors(dark.lighter(110), opt.palette.button().color(), 40)
    #draw grips
    if opt.state & QStyle.State_Horizontal: #horizontal
        for i in range(-20, 20, 2):
            painter.setPen(QPen(grooveColor.darker(110), 1))
            painter.drawLine(
                QPoint(opt.rect.left() + 4, opt.rect.center().y()+ i),
                QPoint(opt.rect.right() - 4, opt.rect.center().y()+ i))
            painter.setPen(QPen(opt.palette.light(), 1))
            painter.drawLine(
                QPoint(opt.rect.left() + 4, opt.rect.center().y() + 1 + i),
                QPoint(opt.rect.right() - 4, opt.rect.center().y() + 1 + i))
    else: #vertical
        for i in range(-20, 20, 2):
            painter.setPen(QPen(grooveColor.darker(110), 1))
            painter.drawLine(
                QPoint(opt.rect.center().x() + i, opt.rect.top() + 4),
                QPoint(opt.rect.center().x() + i, opt.rect.bottom() - 4))
            painter.setPen(QPen(opt.palette.light(), 1))
            painter.drawLine(
                QPoint(opt.rect.center().x() + i + 1, opt.rect.top() + 4),
                QPoint(opt.rect.center().x() + i + 1, opt.rect.bottom() - 4))
    painter.restore()

def drawDashedHandle(opt, painter):
    button = opt.palette.button().color()
    dark = QColor.fromHsv(button.hue(),
                min((255, int(button.saturation()*1.9))), 
                min((255, int(button.value()*0.7))))
    
    painter.save()
    
    grooveColor = Util.mergedColors(dark.lighter(110), opt.palette.button().color(), 40)
    #draw grips
    if opt.state & QStyle.State_Horizontal: #horizontal
        for i in range(-20, 20, 2):
            painter.setPen(QPen(grooveColor.darker(110), 1))
            painter.drawLine(
                QPoint(opt.rect.left() + 4, opt.rect.center().y()+ i),
                QPoint(opt.rect.right() - 4, opt.rect.center().y()+ i))
            painter.setPen(QPen(opt.palette.light(), 1))
            painter.drawLine(
                QPoint(opt.rect.left() + 4, opt.rect.center().y() + 1 + i),
                QPoint(opt.rect.right() - 4, opt.rect.center().y() + 1 + i))
    else: #vertical
        for i in range(-20, 20, 2):
            painter.setPen(QPen(grooveColor.darker(110), 1))
            painter.drawLine(
                QPoint(opt.rect.center().x() + i, opt.rect.top() + 4),
                QPoint(opt.rect.center().x() + i, opt.rect.bottom() - 4))
            painter.setPen(QPen(opt.palette.light(), 1))
            painter.drawLine(
                QPoint(opt.rect.center().x() + i + 1, opt.rect.top() + 4),
                QPoint(opt.rect.center().x() + i + 1, opt.rect.bottom() - 4))
    painter.restore()

def paintBackground(opt, painter):
    painter.save()
    
    # hovered
    if (opt.state & QStyle.State_MouseOver
            and opt.state & QStyle.State_Enabled):
        # set the pen
        if opt.state & QStyle.State_Sunken:
            painter.setPen(opt.palette.highlight().color())
            painter.fillRect(opt.rect, opt.palette.highlight().color().lighter())
        else:
            painter.setPen(opt.palette.highlight().color().lighter())
            
        if opt.state & QStyle.State_Horizontal:
            painter.drawLine(opt.rect.topLeft(), opt.rect.bottomLeft())
            painter.drawLine(opt.rect.topRight(), opt.rect.bottomRight())
        else:
            painter.drawLine(opt.rect.topLeft(), opt.rect.topRight())
            painter.drawLine(opt.rect.bottomLeft(), opt.rect.bottomRight())
    #inactive
    else:
        painter.fillRect(opt.rect, opt.palette.window().color())
    
    painter.restore()

def drawLongLineHandle(opt, painter):
    painter.save()
    if not opt.state & QStyle.State_Horizontal:
        x1 = opt.rect.left() + 4
        x2 = opt.rect.right() - 4
        y1 = opt.rect.center().y()
        y2 = int(y1)
    else:
        x1 = opt.rect.center().x()
        x2 = int(x1)
        y1 = opt.rect.top() + 4
        y2 = opt.rect.bottom() - 4
    
    painter.setPen(opt.palette.text().color())
    painter.drawLine(x1, y1, x2, y2)
    
    painter.restore()

class Splitter(QSplitter):
    #handle styles
    Plain = 0
    
    ParallelLine = 1
    ParallelGroovedLine = 2
    ParallelDotted = 3
    
    CenteredDashes = 4
    CenteredDotted = 5
    HandleStyles = (Plain, ParallelLine, ParallelGroovedLine, ParallelDotted, 
                    CenteredDashes, CenteredDotted)
    
    #hover styles
    NoHoverHint = 0x00
    HoverHighlight = 0x02
    HoverRaised = 0x04
    
    LocalHover = 0x20
    FullHover = 0x40
    HoverStyles = (NoHoverHint, HoverHighlight, HoverRaised, LocalHover, FullHover)
    
    def __init__(self, *args, **kwargs):
        if 'handleStyle' in kwargs:
            h_style = int(kwargs.pop('handleStyle'))
        else:
            h_style = int(Splitter.Plain)
        super().__init__(*args, **kwargs)
        self.handleStyle = h_style
        
    def createHandle(self) -> QSplitterHandle:
        return SplitterHandle(self.orientation(), self)
        
    def handles(self):
        l = []
        if self.count() < 1:
            return l
        for i in range(self.count()):
            h = self.handle(i)
            if h:
                l.append(h)
        return l
    
    def getHandleStyle(self):
        return int(self.__handleStyle)
    
    def setHandleStyle(self, style):
        assert(isinstance(style, int) and style in Splitter.HandleStyles)
        self.__handleStyle = int(style)
        for h in self.handles():
            h.setHandleStyle(self.__handleStyle)
        self.update()
    
    handleStyle = pyqtProperty(int, fget=getHandleStyle, fset=setHandleStyle)

class SplitterHandle(QSplitterHandle):
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__pressed = False
        self.__hovered = False
        self.__handleStyle = Splitter.Plain
        
    def handleStyle(self):
        return self.__handleStyle
        
    def setHandleStyle(self, style):
        assert(isinstance(style, int))
        self.__handleStyle = int(style)
        self.update()
        
    def initStyleOption(self, opt):
        opt.palette = self.palette()
        opt.rect = self.contentsRect()
        if self.orientation() == Qt.Horizontal:
            opt.state = QStyle.State_Horizontal
        else:
            opt.state = QStyle.State_None
        if self.hovered():
            opt.state |= QStyle.State_MouseOver
        if self.pressed():
            opt.state |= QStyle.State_Sunken
        if self.isEnabled():
            opt.state |= QStyle.State_Enabled
    
    def paintEvent(self, ev):
        p = QPainter(self)
        opt = QStyleOption()
#        opt.initFrom(self)
        
        self.initStyleOption(opt)
        paintBackground(opt, p)
        if self.__handleStyle == Splitter.ParallelLine:
            drawLongLineHandle(opt, p)
        elif self.__handleStyle == Splitter.CenteredDashes:
            drawDashedHandle(opt, p)
    
    def enterEvent(self, ev):
        self.__hovered = True
        super().enterEvent(ev)
        self.update()
        
    def leaveEvent(self, ev):
        self.__hovered = False
        super().leaveEvent(ev)
        self.update()
    
    def mousePressEvent(self, ev):
        if ev.button() == Qt.LeftButton:
            self.__pressed = True
        super().mousePressEvent(ev)
        self.update()
        
    def mouseReleaseEvent(self, ev):
        if ev.button() == Qt.LeftButton:
            self.__pressed = False
        super().mouseReleaseEvent(ev)
        self.update()
        
    def hovered(self):
        return self.__hovered
    def pressed(self):
        return self.__pressed
