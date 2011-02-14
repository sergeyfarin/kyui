from PyQt4.QtCore import Qt, pyqtSignal, pyqtSlot, pyqtProperty
from PyQt4.QtGui import QWidget, QSlider, QSpinBox, QLabel
from PyQt4.QtGui import QSizePolicy, QHBoxLayout

class SliderSpinBoxWidget(QWidget):
    #==================================================#
    # Signals                                          #
    #==================================================#
    valueChanged = pyqtSignal(int)
    rangeChanged = pyqtSignal((int, int))
    sliderMoved = pyqtSignal(int)
    
    def __init__(self, 
                 parent : QWidget = None, 
                 adjust : bool = True, 
                 min : int = None, 
                 max : int = None, 
                 name : str = None, 
                 pagestep : int = None,
                 prefix : str = None, 
                 singlestep : int = None, 
                 suffix : str = None, 
                 text : str = None, 
                 tracking : bool = False, 
                 value : int = None):
        super().__init__(parent)
        self._layout = QHBoxLayout(self)
        self._label = QLabel(self)
        self._layout.addWidget(self._label)
        self._slider = QSlider(Qt.Horizontal, self)
        self._layout.addWidget(self._slider)
        self._spinbox = QSpinBox(self)
        self._layout.addWidget(self._spinbox)
        self._layout.setContentsMargins(3, 3, 3, 3)
        self.setAdjustToRange(adjust)
        self.setTracking(tracking)
        
        if text is not None: self._label.setText(text)
        if min is not None: self.setMinimum(min)
        if max is not None: self.setMaximum(max)
        if name is not None: self.setObjectName(name)
        if pagestep is not None: self.setPageStep(pagestep)
        if prefix is not None: self.setPrefix(prefix)
        if singlestep is not None: self.setSingleStep(singlestep)
        if suffix is not None: self.setSuffix(suffix)
        if value is not None: self.setValue(value)
        
        self._spinbox.valueChanged[int].connect(self._onSpinBoxValueChanged)
        self._slider.valueChanged.connect(self._onSliderValueChanged)
        self._slider.rangeChanged.connect(self.rangeChanged.emit)
        self._slider.sliderMoved.connect(self.sliderMoved.emit)
    
    #==================================================#
    # Getters                                          #
    #==================================================#
    def adjustToRange(self)-> bool: return self._adjust
    def labelText(self) -> str:     return self._label.text()
    def minimum(self)-> int:        return self._slider.minimum()
    def maximum(self) -> int:       return self._slider.maximum()
    def pageStep(self) -> int:      return self._slider.pageStep()
    def prefix(self) -> str:        return self._spinbox.prefix()
    def range(self) -> (int, int):  return (self._slider.minimum(), 
                                            self._slider.maximum())
    def singleStep(self) -> int:    return self._slider.singleStep()
    def suffix(self) -> str:        return self._spinbox.suffix()
    def position(self) -> int:      return self._slider.position()
    def tracking(self) -> bool:     return self._slider.hasTracking()
    def value(self) -> int:         return self._slider.value()
    
    #==================================================#
    # Setters                                          #
    #==================================================#
    def setAdjustToRange(self, adjust : bool) -> None:
        self._adjust = adjust
        if adjust:
            self._slider.setSizePolicy(QSizePolicy.Fixed, 
                                       QSizePolicy.Preferred)
            self._slider.setFixedWidth(self.maximum - self.minimum)
        else:
            self._slider.setSizePolicy(QSizePolicy.Expanding, 
                                       QSizePolicy.Preferred)
            self._slider.setFixedWidth(16777215)
    @pyqtSlot(int)
    def setMinimum(self, min : int) -> None:
        self._slider.setMinimum(min)
        self._spinbox.setMinimum(min)
        if self._adjust:
            self._slider.setFixedWidth(self.maximum - self.minimum)
    
    @pyqtSlot(int)
    def setMaximum(self, max : int) -> None:
        self._slider.setMaximum(max)
        self._spinbox.setMaximum(max)
        if self._adjust:
            self._slider.setFixedWidth(self.maximum - self.minimum)
    
    def setPageStep(self, step : int) -> None:
        self._slider.setPageStep(step)
    
    def setPrefix(self, prefix : str) -> None:
        self._spinbox.setPrefix(prefix)
    
    @pyqtSlot(int, int)
    def setRange(self, min : int,  max : int) -> None:
        self._slider.setMinimum(min)
        self._spinbox.setMinimum(min)
        self._slider.setMaximum(max)
        self._spinbox.setMaximum(max)
    
    def setSingleStep(self, step : int) -> None:
        self._slider.setSingleStep(step)
        self._spinbox.setSingleStep(step)
    
    def setSuffix(self, suffix : str) -> None:
        self._spinbox.setSuffix(suffix)
    
    def setLabelText(self, text : str):
        self._label.setText(text)
    
    def setTracking(self, value : bool) -> None:
        self._slider.setTracking(value)
    
    @pyqtSlot(int)
    def setValue(self, value : int) -> None:
        self._slider.setValue(value)
        self._spinbox.setValue(value)
    
    def setObjectName(self, name : str):
        super().setObjectName(name)
        self._layout.setObjectName(name + '_layout')
        self._label.setObjectName(name + '_label')
        self._spinbox.setObjectName(name + '_spinbox')
        self._slider.setObjectName(name + '_slider')
        
    #==================================================#
    # Direct Access Methods                            #
    #==================================================#
    def label(self) -> QLabel:
        return self._label
        
    def slider(self) -> QSlider:
        return self._slider
        
    def spinBox(self) -> QSpinBox:
        return self._spinbox

    #==================================================#
    # Private Methods                                  #
    #==================================================#
    @pyqtSlot(int)
    def _onSliderValueChanged(self, value : int):
        # We have to adjust the value for the slider's issue with single steps
        adjusted = value - value % self._slider.singleStep()
        self._spinbox.blockSignals(True)
        self._spinbox.setValue(adjusted)
        self._spinbox.blockSignals(False)
        self.valueChanged.emit(adjusted)
    
    @pyqtSlot(int)
    def _onSpinBoxValueChanged(self, value : int):
        self._slider.blockSignals(True)
        self._slider.setValue(value)
        self._slider.blockSignals(False)
        self.valueChanged.emit(value)
    
    #==================================================#
    # Properties                                       #
    #==================================================#
    adjustToRange = pyqtProperty(bool, fget=adjustToRange, fset=setAdjustToRange)
    prefix = pyqtProperty(str, fget=prefix, fset=setPrefix)
    suffix = pyqtProperty(str, fget=suffix, fset=setSuffix)
    tracking = pyqtProperty(bool, fget=tracking, fset=setTracking)
    minimum = pyqtProperty(int, fget=minimum, fset=setMinimum)
    maximum = pyqtProperty(int, fget=maximum, fset=setMaximum)
    range = pyqtProperty(tuple, fget=range, fset=setRange)
    pageStep = pyqtProperty(int, fget=pageStep, fset=setPageStep)
    singleStep = pyqtProperty(int, fget=singleStep, fset=setPageStep)
    position = pyqtProperty(int, fget=position)
    labelText = pyqtProperty(str, fget=labelText, fset=setLabelText)
    value = pyqtProperty(int, fget=value, fset=setValue)
