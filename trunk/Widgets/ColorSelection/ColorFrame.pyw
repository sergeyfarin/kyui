from PyQt4.QtCore import pyqtSignal, pyqtSlot, Qt, QObject
from PyQt4.QtGui import QFrame, QColor, QPalette

class ColorFrame(QFrame):
    colorChanged = pyqtSignal(QColor)
    
    def __init__(self, 
                 color : QColor = None, 
                 shape : QFrame.Shape = None, 
                 shadow : QFrame.Shadow = None, 
                 parent : QObject = None):
        super().__init__(parent)
        if shape:
            self.setFrameShape(shape)
        if shadow:
            self.setFrameShadow(shadow)
        self.__color = QColor(color)
        pal = self.palette()
        pal.setColor(QPalette.Window, color if color else QColor(Qt.black))
        self.setPalette(pal)
        self.setAutoFillBackground(True)
            
    def color(self) -> QColor:
        return QColor(self.__color)
    
#    @pyqtSlot
    def setColor(self, color : QColor) -> None:
        pal = self.palette()
        pal.setColor(QPalette.Window, color)
        self.setPalette(pal)
        self.__color = QColor(color)
        self.colorChanged.emit(color)
        
    def setBlue(self, blue : int) -> None:
        self.__color.setBlue(blue)
    def setGreen(self, green : int) -> None:
        self.__color.setGreen(green)
    def setRed(self, red : int) -> None:
        self.__color.setRed(red)
