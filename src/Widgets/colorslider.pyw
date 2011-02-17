from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ColorSlider(QSlider):
    
    
    def __init__(self, 
                 orientation : Qt.Orientation = Qt.Horizontal, 
                 parent : QWidget = None):
        super().__init__(orientation, parent)
        
        self.gradient = QLinearGradient()
        self.gradient.setCoordinateMode(QGradient.StretchToDeviceMode)
        self.color = QColor(Qt.red)
        self.gradient.setStart(0, 0)
        self.gradient.setFinalStop(1, 0)
        self.gradient.setColorAt(0.0, QColor(0, 0, 0))
        self.gradient.setColorAt(1.0, QColor(255, 0, 0))
        
    def paintEvent(self, pe):
        p = QPainter(self)
        opt = QStyleOptionSlider()
        self.initStyleOption(opt)
        opt.subControls = QStyle.SC_SliderHandle
        
        center = opt.rect.center()
        if self.orientation() == Qt.Horizontal:
            rect = QRect(opt.rect.x(), center.y() - 3, opt.rect.width(), 6)
        else:
            rect = QRect(center.x() - 3, opt.rect.y(), 6, opt.rect.height())
        p.fillRect(rect.adjusted(1, 1, 0, 0), QBrush(self.gradient))
        
        self.style().drawComplexControl(QStyle.CC_Slider, opt, p, None)
        
        p.end()
#        super().paintEvent(pe)

    def setStartColor(self, color):
        self.gradient.setColorAt(0.0, color)
        self.update()
        
    def setEndColor(self, color):
        self.gradient.setColorAt(1.0, color)
        self.update()

    def sizeHint(self):
        return self.minimumSizeHint()
        
    def minimumSizeHint(self):
        return QSize(256, 20)
