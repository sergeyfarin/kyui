"""
@module colorslider2
@brief Cleaner implementation of ColorSlider_Old from colorslider.py.
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from .util import QTypeToString

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
    Win7Style = 3
    
    SliderStyles = (NativeStyle, PhotoshopStyle, TriangleStyle, Win7Style)
    
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

    def sizeHint(self):
        """
        Reimplemented from parent class. Returns value from minimumSizeHint.
        @returns QSize
        """
        return self.minimumSizeHint()
        
    def minimumSizeHint(self):
        """
        Reimplemented from parent class.
        @returns QSize
        """
        if self.orientation() == Qt.Horizontal:
            return QSize(212, 19) 
        else:
            return QSize(19, 212)



    def paintEvent(self, pe):
        """
        Reimplemented from parent class.
        """
        style = self.style()
        p = QPainter(self)
        opt = QStyleOptionSlider()
        self.initStyleOption(opt)
        
        gRect = style.subControlRect(QStyle.CC_Slider, opt, QStyle.SC_SliderGroove, self)
        hRect = style.subControlRect(QStyle.CC_Slider, opt, QStyle.SC_SliderHandle, self)
        len = style.pixelMetric(QStyle.PM_SliderLength, opt, self)
        offset = style.pixelMetric(QStyle.PM_SliderTickmarkOffset, opt, self)
        thickness = style.pixelMetric(QStyle.PM_SliderControlThickness, opt, self)
#        mid = int(thickness / 2)
        
        if opt.orientation == Qt.Horizontal:
            sliderPos = style.sliderPositionFromValue(opt.minimum, 
                                                      opt.maximum,
                                                      opt.sliderPosition,
                                                      opt.rect.width() - len, 
                                                      opt.upsideDown)
            hRect = QRect(opt.rect.x() + sliderPos, 
                          opt.rect.y() + offset, 
                          len, thickness)
#            gRect.setY(gRect.y() + mid)
#            gRect.setHeight(thickness)
            gRect.adjust(0, 4, -1, -5)
        else:
            sliderPos = style.sliderPositionFromValue(opt.minimum, 
                                                      opt.maximum,
                                                      opt.sliderPosition,
                                                      opt.rect.height() - len, 
                                                      opt.upsideDown)
            hRect = QRect(opt.rect.x() + offset, 
                          opt.rect.y() + sliderPos, 
                          thickness, len)
            gRect.adjust(4, 0, -5, -1)

#        center = opt.rect.center()
#        if opt.orientation == Qt.Horizontal:
#            rect = QRect(opt.rect.x() + 6, center.y() - 3, 
#                         opt.rect.width() - 12, 6)
#        else:
#            rect = QRect(center.x() - 3, opt.rect.y() + 6, 
#                         6, opt.rect.height() - 12)
        p.setPen(QPen(Qt.black))
        p.drawRect(gRect)

        if self.sliderStyle == ColorSlider.NativeStyle:
            #just draw the handle
            opt.subControls = QStyle.SC_SliderHandle
            style.drawComplexControl(QStyle.CC_Slider, opt, p, None)
        elif self.sliderStyle == ColorSlider.TriangleStyle:
            if opt.orientation == Qt.Horizontal:
                x = hRect.center().x()
                y = gRect.bottom() + 2
                tr1 = (QPoint(x, y), 
                       QPoint(x - 3, y + 3), 
                       QPoint(x + 3, y + 3))
                y = gRect.top() - 1
                tr2 = (QPoint(x, y), 
                       QPoint(x - 3, y - 3), 
                       QPoint(x + 3, y - 3))
            else:
                y = hRect.center().y()
                x = hRect.right() + 2
                tr1 = (QPoint(x, y), 
                      QPoint(x + 3, y + 3), 
                      QPoint(x + 3, y - 3))
                x = hRect.left() - 1
                tr2 = (QPoint(x, y), 
                      QPoint(x - 3, y + 3), 
                      QPoint(x - 3, y - 3))
            p.setPen(opt.palette.windowText().color())
            p.setBrush(opt.palette.windowText())
            p.drawPolygon(*tr1)
            p.drawPolygon(*tr2)

    def getSliderStyle(self):
        """
        Getter for sliderStyle QProperty.
        @returns int The current slider style, from ColorSlider.SliderStyles
        """
        return self.__style
        
    def setSliderStyle(self, style):
        """
        Setter for the sliderStyle QProperty.
        @param style int: Must be one of the values in ColorSlider.SliderStyles
        @see SliderStyles
        """
        if style not in ColorSlider.SliderStyles:
            return
        self.__style = int(style)
        self.update()

    sliderStyle = pyqtProperty(int, fget=getSliderStyle, fset=setSliderStyle)
