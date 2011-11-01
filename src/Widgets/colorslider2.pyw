"""
@module colorslider2
@brief Cleaner implementation of ColorSlider_Old from colorslider.py.
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

def sliderPosition(opt):
    return QStyle.sliderPositionFromValue(
                opt.minimum, 
                opt.maximum, 
                opt.sliderValue, 
                opt.rect.width(), # if opt.orientation == Qt.Horizontal else opt.rect.height() - 12, 
                opt.upsideDown)

class ColorSlider(QSlider):
    """
    @class ColorSlider
    @brief A different implementation of ColorSlider from colorslider.py
    
    This class will replace the ugly, obfuscated junk in the ColorSlider_Old class.
    """
    
    NativeStyle = 0
    PhotoshopStyle = 1
    TriangleStyle = 2
    
    SliderStyles = (NativeStyle, PhotoshopStyle, TriangleStyle)
    
    def __init__(self, *args, **kwargs):
        if len(args) == 2:
            parent = args[1]
            kwargs['orientation'] = args[0]
        elif len(args) == 1:
            parent = args[0]
        else:
            parent = None
        super().__init__(parent, **kwargs)
        self.__style = ColorSlider.NativeStyle

    ### Reimplemented Methods ###
    def sizeHint(self):
        return self.minimumSizeHint()
        
    def minimumSizeHint(self):
        if self.orientation() == Qt.Horizontal:
            return QSize(212, 18) 
        else:
            return QSize(18, 212)

    ### Private Methods ###
    def paintEvent(self, pe):
        p = QPainter(self)
        opt = QStyleOptionSlider()
        self.initStyleOption(opt)
        #don't draw the groove; we'll do that.
        opt.subControls |= ~QStyle.SC_SliderGroove
        
        thickness = self.style().pixelMetric(QStyle.PM_SliderControlThickness, opt, self)
        len = self.style().pixelMetric(QStyle.PM_SliderLength, opt, self)
        grooveRect = self.style().subControlRect(QStyle.CC_Slider, opt, QStyle.SC_SliderGroove, self)
        handleRect = self.style().subControlRect(QStyle.CC_Slider, opt, QStyle.SC_SliderHandle, self)
        
        center = opt.rect.center()
        if opt.orientation == Qt.Horizontal:
            rect = QRect(opt.rect.x() + 6, center.y() - 3, 
                         opt.rect.width() - 12, 6)
        else:
            rect = QRect(center.x() - 3, opt.rect.y() + 6, 
                         6, opt.rect.height() - 12)
        p.setPen(QPen(Qt.black))
#        p.drawRect(rect.adjusted(1, 1, -1, -1))
        p.drawRect(grooveRect)

        if self.sliderStyle == ColorSlider.NativeStyle:
            self.style().drawComplexControl(QStyle.CC_Slider, opt, p, None)
        elif self.sliderStyle == ColorSlider.TriangleStyle:
            if opt.orientation == Qt.Horizontal:
                x = sliderPosition(opt) + 6 + 1
                y = (rect.bottom() + 1) if not opt.upsideDown else (rect.top() - 1)
                p1 = QPoint(x, y)
                p2 = QPoint(x + 3, y + 3)
                p3 = QPoint(x - 3, y + 3)
            else:
                x = (rect.right() + 1) if not opt.upsideDown else (rect.left() - 1)
                y = sliderPosition(opt) + 6 + 1
                p1 = QPoint(x, y)
                p2 = QPoint(x + 3, y + 3)
                p3 = QPoint(x - 3, y + 3)
            p.setPen(opt.palette.windowText().color())
            p.setBrush(opt.palette.windowText())
            p.drawPolygon(p1, p2, p3)
                
        p.end()

    def getSliderStyle(self):
        return self.__style
        
    def setSliderStyle(self, style):
        if style not in ColorSlider.SliderStyles:
            return
        self.__style = int(style)
        self.update()

    sliderStyle = pyqtProperty(int, fget=getSliderStyle, fset=setSliderStyle)
