#UTF-8
#colorbutton.pyw

from PyQt4.QtCore import Qt, pyqtSignal, pyqtSlot, pyqtProperty, qWarning
from PyQt4.QtGui import QToolButton
from PyQt4.QtGui import QColor
from PyQt4.QtGui import QPainter, QStyleOptionToolButton, QStyle
from PyQt4.QtGui import QPixmap, QIcon

#TODO: add property for drawing outside rect
class ColorButton(QToolButton):
    #==================================================#
    # Signals                                          #
    #==================================================#
    colorChanged = pyqtSignal(QColor)
    
    def __init__(self, *args, **kwargs):
        """args:"""
        """color : QColor = Qt.transparent, text : str = None, parent : QObject = None"""
        """color : QColor = Qt.transparent, parent : QObject = None"""
        """parent : QObject = None"""
        """color may be any type the QColor constructor accepts"""
        
        if len(args) == 3:
            color = QColor(args[0])
            kwargs['text'] = args[1]
            parent = args[2]
        elif len(args) == 2:
            color = QColor(args[0])
            if 'text' not in kwargs: kwargs['text'] = None
            parent = args[1]
        elif len(args) == 1:
            color = kwargs.pop('color', QColor(Qt.transparent))
            if 'text' not in kwargs: kwargs['text'] = None
            parent = args[0]
        else:
            color = kwargs.pop('color', QColor(Qt.transparent))
            if 'text' not in kwargs: kwargs['text'] = None
            parent = kwargs.pop('parent', None)
        frameColor = kwargs.pop('frameColor', QColor(Qt.black))
        super().__init__(parent, **kwargs)
        
        #when painting, we need to check if the icon size has changed.
        self.__isz = super().iconSize()
        
        self.__frameColor = frameColor
        self.__color = color
        self._regenerateIcon()
    
    #==================================================#
    # Setters                                          #
    #==================================================#
    @pyqtSlot(QColor)
    def setColor(self, color):
        #use QColor(color) to allow QRgb values, Qt.GlobalColor et cetera
        if self.__color == QColor(color):
            return
        self.__color = QColor(color)
        self._regenerateIcon()
        self.colorChanged.emit(self.__color)
        
    @pyqtSlot(QColor)
    def setFrameColor(self, color):
        if self.__frameColor == QColor(color):
            return
        self.__frameColor = QColor(color)
        self._regenerateIcon()
        
    def setIcon(self, icon):
        qWarning('ColorButton.setIcon: Use setColor(QColor).')

    #==================================================#
    # Getters                                          #
    #==================================================#
    def color(self): 
        return QColor(self.__color)
    
    def frameColor(self):
        return QColor(self.__frameColor)
    
    #==================================================#
    # Properties                                       #
    #==================================================#
    color = pyqtProperty(QColor, fget=color, fset=setColor)
    frameColor = pyqtProperty(QColor, fget=frameColor, fset=setFrameColor)
    
    def paintEvent(self, ev):
        #check and see if the icon size has changed
        if self.__isz != self.iconSize():
            self._regenerateIcon()
            return
        
        #using 
        p = QPainter(self)
        opt = QStyleOptionToolButton()
        self.initStyleOption(opt)
        self.style().drawComplexControl(QStyle.CC_ToolButton, opt, p, self)

    def _regenerateIcon(self):
        self.__isz = self.iconSize()
        pixmap = QPixmap(self.iconSize())
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        if self.frameColor.isValid():
            rect = pixmap.rect().adjusted(2, 2, -2, -2)
            painter.fillRect(rect, self.color)
            painter.setPen(self.frameColor)
            painter.drawRect(rect)
        else:
            painter.fillRect(pixmap.rect(), self.color)
        painter.end()
        super().setIcon(QIcon(pixmap))
