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
        self.gradient.setColorAt(0.0, QColor(255, 255, 255))
        self.gradient.setColorAt(1.0, QColor(255, 0, 0))
        self.brush = QBrush(self.gradient)

        
    def paintEvent(self, pe):
        p = QPainter(self)
        opt = QStyleOption()
        opt.initFrom(self)

        rect = QRect(opt.rect).adjusted(0, 0, -1, -1)
        rect.setHeight(8)
        
        p.setPen(QColor(Qt.black))
        p.drawRect(rect)
        p.setBrush(self.brush)
        p.fillRect(rect.adjusted(1, 1, 0, 0), self.brush)
        
        p.end()
#        super().paintEvent(pe)

    def sizeHint(self):
        return self.minimumSizeHint()
        
    def minimumSizeHint(self):
        return QSize(256, 20)
