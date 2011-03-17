from PyQt4.QtCore import *
from PyQt4.QtGui import *
           
gradients = {QColor.Rgb : {0 : ((0.0, 0.0, 0.0), (1.0, 0.0, 0.0)), 
                           1 : ((0.0, 0.0, 0.0), (0.0, 1.0, 0.0)), 
                           2 : ((0.0, 0.0, 0.0), (0.0, 0.0, 1.0))}, 
             QColor.Hsl : {1 : ((0.5, 0.0, 0.5), (0.5, 1.0, 0.5)),
                           2 : ((0.5, 0.0, 0.0), (0.5, 0.0, 1.0))}, 
             QColor.Hsv : {1 : ((0.5, 0.0, 1.0), (0.5, 1.0, 1.0)), 
                           2 : ((0.5, 0.0, 0.0), (0.5, 0.0, 1.0))}, 
             QColor.Cmyk: {}}

def generateGradient(spec : QColor.Spec , 
                     component : int, 
                     orientation : Qt.Orientation = Qt.Horizontal) -> QLinearGradient:
    gradient = QLinearGradient()
    gradient.setCoordinateMode(QGradient.StretchToDeviceMode)
    if orientation == Qt.Horizontal:
        gradient.setStart(0, 0)
        gradient.setFinalStop(1, 0)
    else:
        gradient.setStart(0, 1)
        gradient.setFinalStop(0, 0)
    #Let's check for Hue first, since it's created differently
    if (spec == QColor.Hsv or spec == QColor.Hsl) and component == 0:
        stops = []
        #Hue gradient is static, so it doesn't matter if we use HSL or HSV
        for stop in (0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0):
            stops.append((stop, QColor.fromHsvF(stop, 1.0, 1.0)))
        gradient.setStops(stops)
    elif spec == QColor.Hsl:
        gradient.setStops([(0.0, QColor.fromHslF(*gradients[spec][component][0])), 
                           (1.0, QColor.fromHslF(*gradients[spec][component][1]))])
    elif spec == QColor.Hsv:
        gradient.setStops([(0.0, QColor.fromHsvF(*gradients[spec][component][0])), 
                           (1.0, QColor.fromHsvF(*gradients[spec][component][1]))])
    elif spec == QColor.Rgb:
        gradient.setStops([(0.0, QColor.fromRgbF(*gradients[spec][component][0])), 
                           (1.0, QColor.fromRgbF(*gradients[spec][component][1]))])
    return gradient

class ColorWidget(QFrame):
    currentColorChanged = pyqtSignal(QColor)
    
    def __init__(self, 
                 orientation : Qt.Orientation = Qt.Horizontal, 
                 parent : QWidget = None, 
                 spec : QColor.Spec = QColor.Rgb):
        super().__init__(parent)
        self._orientation = orientation
        self._spec = spec
        gradients = []
        if spec == QColor.Hsv or spec == QColor.Hsl:
            self._hasHue = True
            gradients.append(generateGradient(orientation, spec, 0))
            gradients.append(generateGradient(orientation, spec, 1))
            gradients.append(generateGradient(orientation, spec, 2))
        elif spec == QColor.Rgb:
            self._hasHue = False
            gradients.append(generateGradient(orientation, spec, 0))
            gradients.append(generateGradient(orientation, spec, 1))
            gradients.append(generateGradient(orientation, spec, 2))
        elif spec == QColor.Cmyk:
            qWarning('ColorWidget: Cmyk not supported')


class ColorSliderWidget(QWidget):
    def __init__(self, 
                 parent : QWidget = None, 
                 orientation : Qt.Orientation = Qt.Horizontal, 
                 spec : QColor.Spec = QColor.Rgb):
        super().__init__(parent)
        self._orientation = orientation
        self._spec = spec
        self._layout = QBoxLayout(Qt.TopToBottom if orientation == Qt.Horizontal
                                  else Qt.LeftToRight, self)
        self.sliders = self.__createSliders()
        
    def __createSliders(self) -> list:
        pass
        
class ColorSlider_Old(QSlider):
    def __init__(self, 
                 spec : QColor.Spec = QColor.Rgb, 
                 channel : int = 0, 
                 orientation : Qt.Orientation = Qt.Horizontal, 
                 parent : QWidget = None):
        super().__init__(orientation, parent)
        self.setColorChannel(spec, channel)
        
    #==================================================#
    # Setters                                          #
    #==================================================#
    def setColorChannel(self, spec : QColor.Spec, channel : int):
        self.__spec = QColor.Spec(spec)
        self.__channel = int(channel)
        self.__gradient = generateGradient(spec, channel, self.orientation())
        
        if (spec == QColor.Hsv or self == QColor.Hsl) and channel == 0:
            super().setRange(0, 359)
            super().setPageStep(30)
            self.__static = True
        else:
            super().setRange(0, 255)
            super().setPageStep(10)
            self.__static = False
        self.update()
        
    def setChannelValue(self, channel : int, value : int):
        if channel == self.__channel:
            self.setValue(value)
            return
        if (self.__spec == QColor.Hsv or self.__spec == QColor.Hsl):
            if self.__channel == 0:
                return
            elif self.__channel == 1 and channel == 2:
                return
        ((stop0, color0), (stop1, color1)) = self.__gradient.stops()
        if self.__spec == QColor.Rgb:
            channels = list(color0.getRgb())
            channels[channel] = value
            color0 = QColor.fromRgb(*channels)
            channels = list(color1.getRgb())
            channels[channel] = value
            color1 = QColor.fromRgb(*channels)
        elif self.__spec == QColor.Hsl:
            channels = list(color0.getHsl())
            channels[channel] = value
            color0 = QColor.fromHsl(*channels)
            channels = list(color1.getHsl())
            channels[channel] = value
            color1 = QColor.fromHsl(*channels)
        elif self.__spec == QColor.Hsv:
            channels = list(color0.getHsv())
            channels[channel] = value
            color0 = QColor.fromHsv(*channels)
            channels = list(color1.getHsv())
            channels[channel] = value
            color1 = QColor.fromHsv(*channels)
        self.__gradient.setStops([(stop0, color0), (stop1, color1)])
        self.update()
            
#    def setChannelValueF(self, channel : int, valueF : float):
#        if channel == self.__channel():
#            self.setValueF(valueF)
#            return
#        if self.__spec == QColor.Rgb:
#            channels = list(self.__gradient.colorAt(0.0).getRgbF())
#            channels[channel] = valueF
#            self.__gradient.setColorAt(0.0, QColor.fromRgbF(*channels))
#            channels = list(self.__gradient.colorAt(1.0).getRgbF())
#            channels[channel] = valueF
#            self.__gradient.setColorAt(1.0, QColor.fromRgbF(*channels))
#        elif self.__spec == QColor.Hsl:
#            if self.__channel == 0:
#                return
#            channels = list(self.__gradient.colorAt(0.0).getHslF())
#            channels[channel] = valueF
#            self.__gradient.setColorAt(0.0, QColor.fromHslF(*channels))
#            channels = list(self.__gradient.colorAt(1.0).getHslF())
#            channels[channel] = valueF
#            self.__gradient.setColorAt(1.0, QColor.fromHslF(*channels))
#        elif self.__spec == QColor.Hsv:
#            if self.__channel == 0:
#                return
#            channels = list(self.__gradient.colorAt(0.0).getHsvF())
#            channels[channel] = valueF
#            self.__gradient.setColorAt(0.0, QColor.fromHsvF(*channels))
#            channels = list(self.__gradient.colorAt(1.0).getHsvF())
#            channels[channel] = valueF
#            self.__gradient.setColorAt(1.0, QColor.fromHsvF(*channels))

    def setCurrentColor(self, color : QColor):
        if self.__static:
            return
        if self.__spec == QColor.Rgb:
            channels = list(color.getRgb())
            channels[self.__channel] = 0.0
            color0 = QColor.fromRgb(*channels)
            channels[self.__channel] = 1.0
            color1 = QColor.fromRgb(*channels)
        elif self.__spec == QColor.Hsl:
            channels = list(color.getHsl())
            channels[self.__channel] = 0.0
            color0 = QColor.fromHsl(*channels)
            channels[self.__channel] = 1.0
            color1 = QColor.fromHsl(*channels)
        elif self.__spec == QColor.Hsv:
            channels = list(color.getHsv())
            channels[self.__channel] = 0.0
            color0 = QColor.fromHsv(*channels)
            channels[self.__channel] = 1.0
            color1 = QColor.fromHsv(*channels)
        elif self.__spec == QColor.Cmyk:
            channels = list(color.getCymk())
            channels[self.__channel] = 0.0
            color0 = QColor.fromCmyk(*channels)
            channels[self.__channel] = 1.0
            color1 = QColor.fromCmyk(*channels)
        self.__gradient.setStops([(0.0, color0), (1.0, color1)])
        self.update()
        
    def setOrientation(self, orient):
        super().setOrientation(orient)
        if orient == Qt.Horizontal:
            self.__gradient.setStart(0, 0)
            self.__gradient.setFinalStop(1, 0)
        else:
            self.__gradient.setStart(0, 1)
            self.__gradient.setFinalStop(0, 0)
        
    def setValueF(self, valueF : float = 0.0):
        value = int(valueF * (super().maximum() - super().minimum()))
        self.setValue(value)

    def setMinimum(self, value): qWarning('ColorSlider.setMinimum: Use setColorChannel')
    def setMaximum(self, value): qWarning('ColorSlider.setMaximum: Use setColorChannel')
    def setRange(self, value1, value2): qWarning('ColorSlider.setRange: Use setColorChannel')

    #==================================================#
    # Getters                                          #
    #==================================================#
    def colorChannel(self) -> int:
        return int(self.__channel)
    
    def currentColor(self) -> QColor:
        return QColor(self.__color)
        
    def spec(self) -> QColor.Spec:
        return self.__spec
    
    def valueF(self) -> float:
        return self.value() / (self.maximum() - self.minimum())

    #==================================================#
    # Reimplemented Public Methods                     #
    #==================================================#
    def sizeHint(self):
        return self.minimumSizeHint()
        
    def minimumSizeHint(self):
        if self.orientation() == Qt.Horizontal:
            return QSize(212, 18) 
        else:
            return QSize(18, 212)

    #==================================================#
    # Private Methods                                  #
    #==================================================#
    def paintEvent(self, pe):
        p = QPainter(self)
        opt = QStyleOptionSlider()
        self.initStyleOption(opt)
        opt.subControls |= ~QStyle.SC_SliderGroove
        
        center = opt.rect.center()
        if self.orientation() == Qt.Horizontal:
            rect = QRect(opt.rect.x() + 6, center.y() - 3, 
                         opt.rect.width() - 12, 6)
        else:
            rect = QRect(center.x() - 3, opt.rect.y() + 6, 
                         6, opt.rect.height() - 12)
        p.setPen(QPen(Qt.black))
        p.setBrush(QBrush(self.__gradient))
        p.drawRect(rect.adjusted(1, 1, -1, -1))
        
        self.style().drawComplexControl(QStyle.CC_Slider, opt, p, None)
        p.end()
