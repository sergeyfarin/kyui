from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ColorSlider(QSlider):
    def __init__(self, 
                 orientation : Qt.Orientation = Qt.Horizontal, 
                 parent : QWidget = None):
        super().__init__(orientation, parent)
        
    def paintEvent(self, pe):
        p = QPainter(self)
        opt = QStyleOption()
        opt.initFrom(self)
        opt.rect = self.rect().adjusted(0, 0, -1, -1)
        
        p.setPen(QColor(Qt.black))
        p.drawRect(opt.rect)

        gradient = QLinearGradient()
        gradient.setCoordinateMode(QGradient.StretchToDeviceMode)
        color = QColor(Qt.red)
        gradient.setColorAt(0.0, color.darker())
        gradient.setColorAt(1.0, color.lighter())
        brush = QBrush(gradient)

        p.setBrush(brush)
        p.fillRect(opt.rect.adjusted(1, 1, 0, 0), brush)
        p.end()
#        super().paintEvent(pe)
