#UTF-8
#colorbutton.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ColorButton(QToolButton):
    #==================================================#
    # Signals                                          #
    #==================================================#
    colorChanged = pyqtSignal(QColor)
    
    def __init__(self, 
                 color : QColor = None, 
                 text : str = None, 
                 parent : QWidget = None, 
                 style : Qt.ToolButtonStyle = Qt.ToolButtonTextBesideIcon):
        super().__init__(parent)
        self.setText(text)
        self.setToolButtonStyle(style)
        self._color = QColor()
        self.setColor(color if color else QColor(Qt.black))
    
    #==================================================#
    # Setters                                          #
    #==================================================#
    @pyqtSlot(QColor)
    def setColor(self, color : QColor):
        self._color = QColor(color)
        pixmap = QPixmap(self.iconSize())
        rect = pixmap.rect().adjusted(1, 1, -1, -1)
        pixmap.fill(Qt.transparent)
        painter = QPainter()
        painter.begin(pixmap)
        painter.fillRect(rect, self._color)
        painter.setPen(QColor(Qt.black))
        painter.drawRect(rect)
        painter.end()
        super().setIcon(QIcon(pixmap))
        self.colorChanged.emit(self._color)
        
    def setIcon(self, icon):
        qWarning('ColorButton.setIcon: Use setColor(QColor).')
    
    def setIconSize(self, size : QSize):
        super().setIconSize(size)
        self.setColor(self._color)

    #==================================================#
    # Getters                                          #
    #==================================================#
    def color(self) -> QColor:
        return QColor(self._color)
    
    #==================================================#
    # Properties                                       #
    #==================================================#
    color = pyqtProperty(QColor, fget=color, fset=setColor)
