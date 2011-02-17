from PyQt4.QtCore import *
from PyQt4.QtGui import *

colors = { 0 : ((0.0, 0.0, 0.0), (1.0, 0.0, 0.0), QColor.Rgb), 
               1 : ((0.0, 0.0, 0.0), (0.0, 1.0, 0.0), QColor.Rgb), 
               2 : ((0.0, 0.0, 0.0), (0.0, 0.0, 1.0), QColor.Rgb), 
               3 : ((0.0, 0.5, 0.5), (0.9, 0.5, 0.5), QColor.Hsl),  
               4 : ((0.5, 0.0, 0.5), (0.5, 1.0, 0.5), QColor.Hsl), 
               5 : ((0.5, 0.0, 0.0), (0.5, 0.0, 1.0), QColor.Hsl), 
               6 : ((0.0, 0.5, 1.0), (1.0, 0.5, 1.0), QColor.Hsv), 
               7 : ((0.5, 0.0, 1.0), (0.5, 1.0, 1.0), QColor.Hsv), 
               8 : ((0.5, 0.0, 0.0), (0.5, 0.0, 1.0), QColor.Hsv)}

class ColorSlider(QSlider):
    Red = 0
    Green = 1
    Blue = 2
    
    HslHue = 3
    HslSat = 4
    HslLum = 5
    
    HsvHue = 6
    HsvSat = 7
    HslLum = 8
    
    
    def __init__(self, 
                 orientation : Qt.Orientation = Qt.Horizontal, 
                 parent : QWidget = None, 
                 component : int = ColorSlider.Red):
        super().__init__(orientation, parent)
        self._color0 = QColor()
        self._color1 = QColor()
        self._component = component
        spec = colors[component]
        if spec == QColor.Rgb:
            self._color0.setRgbF(*colors[component][0])
            self._color1.setRgbF(*colors[component][1])
        elif spec == QColor.Hsl:
            self._color0.setHslF(*colors[component][0])
            self._color1.setHslF(*colors[component][1])
        elif spec == QColor.Hsv:
            self._color0.setHsvF(*colors[component][0])
            self._color1.setHsvF(*colors[component][1])
        self.generateGradient()
    
    def generateGradient(self):
        self.gradient = QLinearGradient()
        self.gradient.setCoordinateMode(QGradient.StretchToDeviceMode)
        if self.orientation() == Qt.Horizontal:
            self.gradient.setStart(0, 0)
            self.gradient.setFinalStop(1, 0)
        else:
            self.gradient.setStart(0, 1)
            self.gradient.setFinalStop(0, 0)
        self.gradient.setStops([(0.0, self._color0),
                                (1.0, self._color1)])
        
    def paintEvent(self, pe):
        p = QPainter(self)
        opt = QStyleOptionSlider()
        self.initStyleOption(opt)
        opt.subControls |= ~QStyle.SC_SliderGroove
        
        center = opt.rect.center()
        if self.orientation() == Qt.Horizontal:
            rect = QRect(opt.rect.x() + 7, center.y() - 3, 
                         opt.rect.width() - 14, 6)
        else:
            rect = QRect(center.x() - 3, opt.rect.y() + 7, 
                         6, opt.rect.height() - 14)
        p.setPen(QPen(Qt.black))
        p.setBrush(QBrush(self.gradient))
        p.drawRect(rect.adjusted(1, 1, -1, -1))
        
        self.style().drawComplexControl(QStyle.CC_Slider, opt, p, None)
        p.end()
        
    def setComponentValue(self, idx, value):
        spec = colors[self._component][2]
        if spec == QColor.Rgb:
            self._color0.setRed

    def setStartColor(self, color):
        self._color0 = color
        self.gradient.setColorAt(0.0, color)
        self.update()
        
    def setEndColor(self, color):
        self._color1 = color
        self.gradient.setColorAt(1.0, color)
        self.update()
        
    def endColor(self):
        return self._color1
        
    def startColor(self):
        return self._color0

    def sizeHint(self):
        return self.minimumSizeHint()
        
    def minimumSizeHint(self):
        if self.orientation() == Qt.Horizontal:
            return QSize(272, 20) 
        else:
            return QSize(20, 272)

    def setOrientation(self, orient):
        super().setOrientation(orient)
        self.generateGradient()
        
class HueSlider(ColorSlider):
    def generateGradient(self):
        self.gradient = QRadialGradient(0.5, 0.5, 1.0)
        self.gradient.setCoordinateMode(QGradient.StretchToDeviceMode)
        self.gradient.setColorAt(0.5, self._color0)
        self.gradient.setSpread(QGradient.PadSpread)
