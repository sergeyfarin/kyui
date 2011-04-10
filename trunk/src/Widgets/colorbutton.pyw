#UTF-8
#colorbutton.pyw

from PyQt4.QtCore import Qt, pyqtSignal, pyqtSlot, pyqtProperty, qWarning
from PyQt4.QtCore import QSize
from PyQt4.QtGui import QWidget, QToolButton
from PyQt4.QtGui import QColor
from PyQt4.QtGui import QPainter
from PyQt4.QtGui import QPixmap, QIcon

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
        self.setColor(color if color else QColor(Qt.transparent))
    
    #==================================================#
    # Setters                                          #
    #==================================================#
    @pyqtSlot(QColor)
    def setColor(self, color : QColor):
        self.__color = QColor(color)
        pixmap = QPixmap(self.iconSize())
        rect = pixmap.rect().adjusted(2, 2, -2, -2)
        pixmap.fill(Qt.transparent)
        painter = QPainter()
        painter.begin(pixmap)
        painter.fillRect(rect, self.__color)
        painter.setPen(QColor(Qt.black))
        painter.drawRect(rect)
        painter.end()
        super().setIcon(QIcon(pixmap))
        self.colorChanged.emit(self.__color)
        
    def setIcon(self, icon):
        qWarning('ColorButton.setIcon: Use setColor(QColor).')
    
    def setIconSize(self, size : QSize):
        super().setIconSize(size)
        self.setColor(self.color)

    #==================================================#
    # Getters                                          #
    #==================================================#
    def color(self) -> QColor:
        return QColor(self.__color)
    
    #==================================================#
    # Properties                                       #
    #==================================================#
    color = pyqtProperty(QColor, fget=color, fset=setColor)
