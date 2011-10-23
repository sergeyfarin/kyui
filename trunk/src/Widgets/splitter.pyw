from PyQt4.QtCore import *
from PyQt4.QtGui import *

from .util import Util

def drawCenteredDashedHandle(opt, painter):
    mid = opt.palette.mid().color()
    dark = opt.palette.shadow().color()
    midlight = opt.palette.midlight().color()
    
    painter.save()
    
    #horizontal
    if opt.state & QStyle.State_Horizontal:
        if opt.rect.width() < 4:
            padding = 0
        elif opt.rect.width() < 8:
            padding = 1
        elif opt.rect.width() < 12:
            padding = 2
        else:
            padding = 3
        for i in range(-20, 20, 2):
            painter.setPen(dark)
            painter.drawLine(
                QPoint(opt.rect.left() + padding, opt.rect.center().y()+ i),
                QPoint(opt.rect.right() - padding, opt.rect.center().y()+ i))
            painter.setPen(midlight)
            painter.drawLine(
                QPoint(opt.rect.left() + padding, opt.rect.center().y() + 1 + i),
                QPoint(opt.rect.right() - padding, opt.rect.center().y() + 1 + i))
    #vertical
    else:
        if opt.rect.height() < 4:
            padding = 0
        elif opt.rect.height() < 8:
            padding = 1
        elif opt.rect.height() < 12:
            padding = 2
        else:
            padding = 3
        for i in range(-20, 20, 2):
            painter.setPen(dark)
            painter.drawLine(
                QPoint(opt.rect.center().x() + i, opt.rect.top() + padding),
                QPoint(opt.rect.center().x() + i, opt.rect.bottom() - padding))
            painter.setPen(midlight)
            painter.drawLine(
                QPoint(opt.rect.center().x() + i + 1, opt.rect.top() + padding),
                QPoint(opt.rect.center().x() + i + 1, opt.rect.bottom() - padding))
    painter.restore()
    
def drawCenteredDottedHandle(opt, p):
    p.save()
    
    #horizontal
    if opt.state & QStyle.State_Horizontal:
        if opt.rect.height() < 44:
            y = opt.rect.top() + 2
            y2 = opt.rect.bottom() - 2
            #pad a pixel if the height is not an even value
            if opt.rect.height() % 2:
                y1 += 1
        else:
            y1 = opt.rect.center().y() - 20
            y2 = opt.rect.center().y() + 20
        
        #draw one line of dots for thin panels
        if opt.rect.width() < 4:
            x = opt.rect.center().x()
            #pad a pixel if the width is not an even value
            if opt.rect.width() % 2:
                x += 1
            #draw each color individually to avoid setting the pen over and over
            p.setPen(opt.palette.light().color())
            for y in range(y1, y2, 2):
                p.drawPoint(x, y)
            
            p.setPen(opt.palette.shadow().color())
            for y in range(y1, y2, 2):
                p.drawPoint(x + 1, y + 1)
            
            p.setPen(opt.palette.midlight().color())
            for y in range(y1, y2, 2):
                p.drawPoint(x + 1, y)
#            p.setPen(opt.palette.midlight().color())
#            for y in range(y1, y2, 2):
#                p.drawPoint(x, y + 1)
        else:
            x = opt.rect.center().x() - 2
            if opt.rect.width() % 2:
                x += 1
            p.setPen(opt.palette.light().color())
            left = True
            for y in range(y1, y2, 2):
                p.drawPoint(x, y) if left else p.drawPoint(x + 2, y)
                left = not left
            
            p.setPen(opt.palette.shadow().color())
            left = True
            for y in range(y1, y2, 2):
                p.drawPoint(x + 1, y + 1) if left else p.drawPoint(x + 3, y + 1)
                left = not left
            
            p.setPen(opt.palette.mid().color())
            left = True
            for y in range(y1, y2, 2):
                p.drawPoint(x + 1, y) if left else p.drawPoint(x + 3, y)
            
            p.setPen(opt.palette.midlight().color())
            left = True
            for y in range(y1, y2, 2):
                p.drawPoint(x, y + 1) if left else p.drawPoint(x + 2, y + 1)
    else:
        pass
    
    p.restore()
    
def drawParalellLineHandle(opt, painter):
    painter.save()
    if opt.state & QStyle.State_Horizontal:
        x1 = opt.rect.center().x()
        x2 = int(x1)
        y1 = opt.rect.top() + 4
        y2 = opt.rect.bottom() - 4
    else:
        x1 = opt.rect.left() + 4
        x2 = opt.rect.right() - 4
        y1 = opt.rect.center().y()
        y2 = int(y1)
    painter.setPen(opt.palette.dark().color())
    painter.drawLine(x1, y1, x2, y2)
    
    painter.restore()

def drawParallelGroovedLineHandle(opt, painter):
    if opt.state & QStyle.State_Horizontal:
        if opt.rect.width() < 5:
            drawParalellLineHandle(opt, painter)
            return
        else:
            x = opt.rect.center().x() - 1
            width = 3 if opt.rect.width() % 2 else 4
            y = opt.rect.top() + 4
            height = opt.rect.height() - y - 4
    else:
        if opt.rect.height() < 6:
            drawParalellLineHandle(opt, painter)
            return
        else:
            x = opt.rect.left() + 4
            width = opt.rect.width() - x - 4
            y = opt.rect.center().y() - 1
            height = 3 if opt.rect.height() % 2 else 4
    painter.save()
    qDrawWinPanel(painter, x, y, width, height, opt.palette, False, None)
    painter.restore()

class Splitter(QSplitter):
    def __init__(self, *args, **kwargs):
        if 'gripPainter' in kwargs:
            p_func = kwargs.pop('gripPainter')
        else:
            p_func = None
        if 'hoverHint' in kwargs:
            h_hint = True if kwargs.pop('hoverHint') else False
        else:
            h_hint = False
        super().__init__(*args, **kwargs)
        self.__gripfunc = p_func
        self.__highlight = h_hint
        
    def createHandle(self):
        h = SplitterHandle(self.orientation(), self)
        h.setGripPainter(self.__gripfunc)
        h.hoverHint = self.hoverHint
        return h
        
    def handles(self):
        l = []
        for i in range(self.count()):
            h = self.handle(i)
            if h:
                l.append(h)
        return l
        
    def widgets(self):
        l = []
        for i in range(self.count()):
            w = self.widget(i)
            if w:
                l.append(w)
        return l
    
    def setGripPainter(self, func):
        if func == self.__gripfunc:
            return
        self.__gripfunc = func
        for h in self.handles():
            h.setGripPainter(func)
        
    def getHoverHint(self):
        return True if self.__highlight else False
        
    def setHoverHint(self, hint):
        assert(isinstance(hint, bool))
        if hint == self.__highlight:
            return
        self.__highlight = True if hint else False
        for h in self.handles():
            h.hoverHint = hint
        
    hoverHint = pyqtProperty(bool, fget=getHoverHint, fset=setHoverHint)

class SplitterHandle(QSplitterHandle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__pressed = False
        self.__hovered = False
        self.__gripfunc = None
        self.__highlight = False
        
    def initStyleOption(self, opt):
        opt.palette = self.palette()
        opt.rect = self.contentsRect()
        
        if self.isEnabled():
            opt.state = QStyle.State_Enabled
        else:
            opt.state = QStyle.State_None
        if self.orientation() == Qt.Horizontal:
            opt.state |= QStyle.State_Horizontal
        #only set these flags if the HoverHint property is set to true
        if self.hoverHint:
            if self.hovered():
                opt.state |= QStyle.State_MouseOver
            if self.pressed():
                opt.state |= QStyle.State_Sunken
        
    
    def paintEvent(self, ev):
        p = QPainter(self)
        opt = QStyleOption()
        
        self.initStyleOption(opt)
        p.save()
        
        #hovered
        if (opt.state & QStyle.State_MouseOver
                and opt.state & QStyle.State_Enabled):
            #pad a pixel on the end to accomodate weird frame style issues
            if opt.state & QStyle.State_Horizontal:
                rect = opt.rect.adjusted(0, 1, 0, -1)
            else:
                rect = opt.rect.adjusted(1, 0, -1, 0)
                
            # set the pen and fill with highlight if mouse is down
            if opt.state & QStyle.State_Sunken:
                p.setPen(opt.palette.highlight().color())
                p.fillRect(rect, opt.palette.highlight().color().lighter())
            else:
                p.setPen(opt.palette.highlight().color().lighter())
            
            #draw the edge highlights
            if opt.state & QStyle.State_Horizontal:
                p.drawLine(rect.topLeft(), rect.bottomLeft())
                p.drawLine(rect.topRight(), rect.bottomRight())
            else:
                p.drawLine(rect.topLeft(), rect.topRight())
                p.drawLine(rect.bottomLeft(), rect.bottomRight())
        #inactive
        else:
            p.fillRect(opt.rect, opt.palette.window().color())
        p.restore()
        
        #call the grip paint function/method if it has been set
        if self.__gripfunc:
            self.__gripfunc(opt, p)
    
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
        
    def getGripPainter(self):
        return self.__gripfunc
        
    def setGripPainter(self, func):
        if self.__gripfunc == func:
            return
        self.__gripfunc = func
        self.update()

    def getHoverHint(self):
        return True if self.__highlight else False
        
    def setHoverHint(self, hint):
        if hint == self.__highlight:
            return
        self.__highlight = True if hint else False
        self.update()
        
    hoverHint = pyqtProperty(bool, fget=getHoverHint, fset=setHoverHint)
