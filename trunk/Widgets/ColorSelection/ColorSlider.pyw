from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ..Style.StyleOption import StyleOptionColorSlider

from collections import namedtuple

#SpecNames = namedtuple('SpecNames', ['Rgb', 'Hsv', 'Hsl', 'Cmyk'])
#
#SpecData = namedtuple('SpecData', 
#                     ['Spec',   # QColor.Spec, specification this is a member of
#                      'Text1'   # str, label for slider
#                      'Unit1'   # str, appended text to spinbox
#                      'Max1',   # Maximum value for the slider
#                      'Text2',  # Repeats for each slider
#                      'Unit2', 
#                      'Max2', 
#                      'Text3', 
#                      'Unit3', 
#                      'Max3',   # Fourth slider is only used for CMYK, so it
#                                # does not need specifying
#                      'Count']) #Number of sliders used, always three or four
#SpecElements = SpecNames(Rgb=SpecData(Spec=QColor.Rgb,
#                                Text1='R', 
#                                Unit1='', 
#                                Max1=255, 
#                                Text2='B',
#                                Unit2='',
#                                Max2=255, 
#                                Text3='G', 
#                                Unit3='', 
#                                Max3=255, 
#                                Count=3), 
#                        Hsv=SpecData(Spec=QColor.Hsv,
#                                Text1='H', 
#                                Unit1='°', 
#                                Max1=360, 
#                                Text2='S', 
#                                Unit2='%', 
#                                Max2=100, 
#                                Text3='V', 
#                                Unit3='%', 
#                                Max3=100,
#                                Count=3), 
#                        Hsl=SpecData(Spec=QColor.Hsl,
#                                Text1='H', 
#                                Unit1='°', 
#                                Max1=360, 
#                                Text2='S', 
#                                Unit2='%', 
#                                Max2=100, 
#                                Text3='L', 
#                                Unit3='%', 
#                                Max3=100,
#                                Count=3), 
#                        Cmyk=SpecData(Spec=QColor.Cmyk,
#                                Text1='C', 
#                                Unit1='%', 
#                                Max1=100, 
#                                Text2='M', 
#                                Unit2='%', 
#                                Max2=100, 
#                                Text3='Y', 
#                                Unit3='%', 
#                                Max3=100, 
#                                Count=4))

class ColorWidget(QWidget):
    colorChanged = pyqtSignal(QColor)
    valueChanged = pyqtSignal(int, int)
    
    def __init__(self, 
                 spec : QColor.Spec = None, 
                 color : QColor = None, 
                 orientation : Qt.Orientation = None, 
                 parent : QObject = None):
        super().__init__(parent)
        layout = QGridLayout(self)
        layout.setSpacing(6)
#        self.setContentsMargins(0, 0, 0, 0)
        
        #First slider
        self.label1 = QLabel(self)
        self.slider1 = ColorSlider(QColor.Rgb, ColorSlider.Red, 
                                   orientation, self)
        self.spinbox1 = QSpinBox(self)
        self.spinbox1.setReadOnly(True)
        self.connect(self.slider1, SIGNAL('valueChanged(int)'), self.spinbox1.setValue)
        
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.slider1, 0, 1)
        layout.addWidget(self.spinbox1, 0, 2) 
        
        #Second slider
        self.label2 = QLabel(self)
        self.slider2 = ColorSlider(QColor.Rgb, ColorSlider.Green, 
                                   orientation, self)
        self.spinbox2 = QSpinBox(self)
        self.spinbox2.setReadOnly(True)
        self.connect(self.slider2, SIGNAL('valueChanged(int)'), self.spinbox2.setValue)

        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.slider2, 1, 1)
        layout.addWidget(self.spinbox2, 1, 2)
        
        #Third slider
        self.label3 = QLabel(self)
        self.slider3 = ColorSlider(QColor.Rgb, ColorSlider.Blue, 
                                   orientation, self)
        self.spinbox3 = QSpinBox(self)
        self.spinbox3.setReadOnly(True)
        self.connect(self.slider3, SIGNAL('valueChanged(int)'), self.spinbox3.setValue)
        
        layout.addWidget(self.label3, 2, 0)
        layout.addWidget(self.slider3, 2, 1)
        layout.addWidget(self.spinbox3, 2, 2)
        
        #Fourth slider
        self.label4 = QLabel('K', self)
        self.slider4 = ColorSlider(QColor.Cmyk, ColorSlider.Black, 
                                   orientation, None)
        self.slider4.setMaximum(100)
        self.spinbox4 = QSpinBox(self)
        self.spinbox4.setReadOnly(True)
        self.spinbox4.setSuffix('%')
        self.connect(self.slider4, SIGNAL('valueChanged(int)'), self.spinbox4.setValue)
        
        layout.addWidget(self.label4, 3, 0)
        layout.addWidget(self.slider4, 3, 1)
        layout.addWidget(self.spinbox4, 3, 2)
        
        # Hide the fourth set unless we're using CMYK
        self.label4.setVisible(False)
        self.slider4.setVisible(False)
        self.spinbox4.setVisible(False)
        
        self.setColorSpec(spec)
        
        self.__layout = layout
        self.__spec = spec
        
    def __changeSlider1(self, value : int):
        pass

    def setColorSpec(self, spec : QColor.Spec):
        if spec == QColor.Rgb:
            self.label1.setText('R')
            self.label2.setText('G')
            self.label3.setText('B')
            
            self.slider1.setSpec(spec, ColorSlider.Red)
            self.slider2.setSpec(spec, ColorSlider.Green)
            self.slider3.setSpec(spec, ColorSlider.Blue)
            
            self.slider1.setRange(0, 255)
            self.slider2.setRange(0, 255)
            self.slider3.setRange(0, 255)
            
            self.spinbox1.setSuffix('')
            self.spinbox2.setSuffix('')
            self.spinbox3.setSuffix('')
            
            self.label4.setVisible(False)
            self.slider4.setVisible(False)
            self.spinbox4.setVisible(False)
        elif spec == QColor.Hsv:
            self.label1.setText('H')
            self.label2.setText('S')
            self.label3.setText('V')
            self.slider1.setSpec(spec, ColorSlider.Hue)
            self.slider2.setSpec(spec, ColorSlider.Saturation)
            self.slider3.setSpec(spec, ColorSlider.Value)
            
            self.slider1.setRange(0, 360)
            self.slider2.setRange(0, 100)
            self.slider3.setRange(0, 100)
            
            self.spinbox1.setSuffix('°')
            self.spinbox2.setSuffix('%')
            self.spinbox3.setSuffix('%')
            
            self.label4.setVisible(False)
            self.slider4.setVisible(False)
            self.spinbox4.setVisible(False)
        elif spec == QColor.Hsl:
            self.label1.setText('H')
            self.label2.setText('S')
            self.label3.setText('L')
            self.slider1.setSpec(spec, ColorSlider.Hue)
            self.slider2.setSpec(spec, ColorSlider.Saturation)
            self.slider3.setSpec(spec, ColorSlider.Luminosity)
            
            self.slider1.setRange(0, 360)
            self.slider2.setRange(0, 100)
            self.slider3.setRange(0, 100)
            
            self.spinbox1.setSuffix('°')
            self.spinbox2.setSuffix('%')
            self.spinbox3.setSuffix('%')
            
            self.label4.setVisible(False)
            self.slider4.setVisible(False)
            self.spinbox4.setVisible(False)
        elif spec == QColor.Cmyk:
            self.label1.setText('C')
            self.label2.setText('M')
            self.label3.setText('Y')
            self.slider1.setSpec(spec, ColorSlider.Cyan)
            self.slider2.setSpec(spec, ColorSlider.Magenta)
            self.slider3.setSpec(spec, ColorSlider.Yellow)
            self.slider4.setSpec(spec, ColorSlider.Black)
            
            self.slider1.setRange(0, 100)
            self.slider2.setRange(0, 100)
            self.slider3.setRange(0, 100)
            
            self.spinbox1.setSuffix('%')
            self.spinbox2.setSuffix('%')
            self.spinbox3.setSuffix('%')
            
            self.label4.setVisible(True)
            self.slider4.setVisible(True)
            self.spinbox4.setVisible(True)

class ColorSlider(QSlider):
    Red = 0
    Green = 1
    Blue = 2
    Hue = 3
    Saturation = 4
    Value = 5
    Luminosity = 6
    Cyan = 7
    Magenta = 8
    Yellow = 9
    Black = 10
#    Alpha = 11

    def __init__(self, 
                 spec : QColor.Spec = None, 
                 val : int = None, 
                 orientation : Qt.Orientation = None, 
                 parent : QObject = None):
        super().__init__(parent)
        self.__spec = spec if spec else QColor.Rgb
        if val:
            if val not in ColorSlider.specElements(self.__spec):
                qWarning('ColorSlider: Invalid color element, assigning default value')
                self.__value = ColorSlider.specElements(self.__spec)[0]
            else:
                self.__value = val
        self.setOrientation(orientation if orientation else Qt.Horizontal)
        
    @staticmethod
    def specElements(spec : QColor.Spec) -> tuple:
        if spec == QColor.Rgb:
            return (ColorSlider.Red, ColorSlider.Blue, ColorSlider.Green)
        elif spec == QColor.Hsv:
            return (ColorSlider.Hue, ColorSlider.Saturation, ColorSlider.Value)
        elif spec == QColor.Hsl:
            return (ColorSlider.Hue, ColorSlider.Saturation, ColorSlider.Luminosity)
        elif spec == QColor.Cmyk:
            return (ColorSlider.Cyan, ColorSlider.Magenta, ColorSlider.Yellow, ColorSlider.Black)
            
    def spec(self):
        return self.__spec
        
    def colorValue(self) -> int:
        return int(self.__value)
        
    def setSpec(self, spec : QColor.Spec, val : int) -> None:
        if not isinstance(spec, QColor.Spec):
            return
        self.__spec = spec
        if val not in ColorSlider.specElements(spec):
            qWarning('ColorSlider: Invalid color element, assigning default value')
            self.__value = ColorSlider.specElements(spec)[0]
        else:
            self.__value = val
        self.update()

    def initStyleOption(self, opt : QStyleOptionSlider) -> None:
        super().initStyleOption(opt)
        opt.spec = self.__spec
        opt.element = self.__value
        
    def paintEvent(self, ev):
        super().paintEvent(ev)
