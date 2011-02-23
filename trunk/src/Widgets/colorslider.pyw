from PyQt4.QtCore import *
from PyQt4.QtGui import *
           
gradients = {QColor.Rgb : { 0 : ((0.0, 0.0, 0.0), (1.0, 0.0, 0.0)), 
                            1 : ((0.0, 0.0, 0.0), (0.0, 1.0, 0.0)), 
                            2 : ((0.0, 0.0, 0.0), (0.0, 0.0, 1.0))}, 
             QColor.Hsl : { 0 : ((0.0, 0.5, 0.5), (1.0, 0.5, 0.5)), 
                            1 : ((0.5, 0.0, 0.5), (0.5, 1.0, 0.5)), 
                            2 : ((0.5, 1.0, 0.0), (0.5, 1.0, 1.0))}, 
             QColor.Hsv : { 0 : ((0.0, 0.5, 1.0), (1.0, 0.5, 1.0)), 
                            1 : ((0.5, 0.0, 1.0), (0.5, 1.0, 1.0)), 
                            2 : ((0.5, 1.0, 0.0), (0.5, 1.0, 1.0))}}
           
def generateGradient(orientation, spec, channel) -> QLinearGradient:
        gradient = QLinearGradient()
        gradient.setCoordinateMode(QGradient.StretchToDeviceMode)
        if orientation == Qt.Horizontal:
            gradient.setStart(0, 0)
            gradient.setFinalStop(1, 0)
        else:
            gradient.setStart(0, 1)
            gradient.setFinalStop(0, 0)
        if spec == QColor.Rgb:
            stops = [(0, QColor.fromRgbF(*gradients[spec][channel][0])), 
                     (1, QColor.fromRgbF(*gradients[spec][channel][1]))]
            gradient.setStops(stops)
        elif spec == QColor.Hsl:
            if channel == 0:
                stops = []
                for stop in (0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0):
                    stops.append((stop, QColor.fromHslF(stop, 1.0, 0.5)))
            else:
                stops = [(0, QColor.fromHslF(*gradients[spec][channel][0])), 
                         (1, QColor.fromHslF(*gradients[spec][channel][1]))]
            gradient.setStops(stops)
        elif spec == QColor.Hsv:
            if channel == 0:
                stops = []
                for stop in (0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0):
                    stops.append((stop, QColor.fromHsvF(stop, 1.0, 1.0)))
            else:
                stops = [(0, QColor.fromHsvF(*gradients[spec][channel][0])), 
                         (1, QColor.fromHsvF(*gradients[spec][channel][1]))]
            gradient.setStops(stops)
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
        gradient.setStops((0.0, QColor.fromHslF(*gradients[spec][component][0]), 
                           1.0, QColor.fromHslF(*gradients[spec][component][1])))
    elif spec == QColor.Hsv:
        gradient.setStops((0.0, QColor.fromHsvF(*gradients[spec][component][0]), 
                           1.0, QColor.fromHsvF(*gradients[spec][component][1])))
    elif spec == QColor.Rgb:
        gradient.setStops((0.0, QColor.fromRgbF(*gradients[spec][component][0]), 
                           1.0, QColor.fromRgbF(*gradients[spec][component][1])))
    return gradient

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
        
class HueSlider(QSlider):
    def __init__(self, 
                 orientation : Qt.Orientation = Qt.Horizontal, 
                 parent : QWidget = None):
        super().__init__(orientation, parent)
        self._gradient = generateGradient(QColor.Hsv, 0, orientation)

    #==================================================#
    # Event Handling                                   #
    #==================================================#
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
        p.setBrush(QBrush(self._gradient))
        p.drawRect(rect.adjusted(1, 1, -1, -1))
        
        self.style().drawComplexControl(QStyle.CC_Slider, opt, p, None)
        p.end()

    #==================================================#
    # Reimplemented Public Methods                     #
    #==================================================#
    def sizeHint(self):
        return self.minimumSizeHint()
        
    def minimumSizeHint(self):
        if self.orientation() == Qt.Horizontal:
            return QSize(200, 18) 
        else:
            return QSize(18, 200)

    def setOrientation(self, orient):
        super().setOrientation(orient)
        self._gradient = generateGradient(QColor.Hsv, 0, orient)
        self.update()

class ColorSlider(): pass

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
        self.__gradient = generateGradient(self.orientation(), spec, channel)
        
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

    def setMinimum(self, value): qWarning('ColorSlider: Use setColorChannel')
    def setMaximum(self, value): qWarning('ColorSlider: Use setColorChannel')
    def setRange(self, value1, value2): qWarning('ColorSlider: Use setColorChannel')

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

#class OldColorSlider(QSlider):
#    Red = 0
#    Green = 1
#    Blue = 2
#    
#    HslHue = 3
#    HslSat = 4
#    HslLum = 5
#    
#    HsvHue = 6
#    HsvSat = 7
#    HsvVal = 8
#    
#    def __init__(self, 
#                 orientation : Qt.Orientation = Qt.Horizontal, 
#                 parent : QWidget = None, 
#                 channel : int = 0):
#        super().__init__(orientation, parent)
#        self._color0 = QColor()
#        self._color1 = QColor()
#        self._channel = channel
#        
#        self.gradient = QLinearGradient()
#        self.gradient.setCoordinateMode(QGradient.StretchToDeviceMode)
#        if self.orientation() == Qt.Horizontal:
#            self.gradient.setStart(0, 0)
#            self.gradient.setFinalStop(1, 0)
#        else:
#            self.gradient.setStart(0, 1)
#            self.gradient.setFinalStop(0, 0)
#        self.setChannel(channel)
#

#
#    #==================================================#
#    # Setters                                          #
#    #==================================================#
#    def setChannelValue(self, idx, value):
#        v = value / (self.maximum() - self.minimum())
#        if idx == ColorSlider.Red:
#            self._color0.setRedF(v)
#            self._color1.setRedF(v)
#        elif idx == ColorSlider.Green:
#            self._color0.setGreenF(v)
#            self._color1.setGreenF(v)
#        elif idx == ColorSlider.Blue:
#            self._color0.setBlueF(v)
#            self._color1.setBlueF(v)
#        else:
#            if colors[idx][2] == QColor.Hsl:
#                (h0, s0, l0, a0) = self._color0.getHslF()
#                (h1, s1, l1, a1) = self._color1.getHslF()
#            else:
#                (h0, s0, l0, a0) = self._color0.getHsvF()
#                (h1, s1, l1, a1) = self._color1.getHsvF()
#            if idx == ColorSlider.HslHue or idx == ColorSlider.HsvHue:
#                h0 = v
#                h1 = v
#            elif idx == ColorSlider.HslSat or idx == ColorSlider.HsvSat:
#                s0 = v
#                s1 = v
#            elif idx == ColorSlider.HslLum or idx == ColorSlider.HsvVal:
#                l0 = v
#                l1 = v
#            if colors[idx][2] == QColor.Hsl:
#                self._color0.setHslF(h0, s0, l0, a0)
#                self._color1.setHslF(h1, s1, l1, a1)
#            else:
#                self._color0.setHsvF(h0, s0, l0, a0)
#                self._color1.setHsvF(h1, s1, l1, a1)
#        self.__generateGradient()
#        
#    def setChannel(self, channel):
#        spec = colors[channel][2]
#        if spec == QColor.Rgb:
#            self._color0.setRgbF(*colors[channel][0])
#            self._color1.setRgbF(*colors[channel][1])
#        elif spec == QColor.Hsl:
#            self._color0.setHslF(*colors[channel][0])
#            self._color1.setHslF(*colors[channel][1])
#        elif spec == QColor.Hsv:
#            self._color0.setHsvF(*colors[channel][0])
#            self._color1.setHsvF(*colors[channel][1])
#        self._channel = channel
#        self.__generateGradient()
#        
