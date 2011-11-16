#UTF-8
#colorbutton.pyw

from PyQt4.QtCore import Qt, pyqtSignal, pyqtSlot, pyqtProperty, qWarning
from PyQt4.QtGui import QToolButton
from PyQt4.QtGui import QColor
from PyQt4.QtGui import QPainter, QStyleOptionToolButton, QStyle
from PyQt4.QtGui import QPixmap, QIcon

class ColorButton(QToolButton):
    """
    \brief QToolButton that displays a color selection.
    
    This class is specifically meant for use in settings dialogs and toolbars
    for setting and displaying a color selection (e.g., window background
    color or text color). Refer to the test file for an example of its usage.
    
    \see ColorFrame
    \see ColorWidget
    """
    
    ##\name Signals
    ##\{
    colorChanged = pyqtSignal(QColor)
    ##\}
    
    def __init__(self, *args, **kwargs):
        """
        Initializer.
        \param args \c tuple: See valid signatures below.
        \param kwargs \c dict: Property keyword arguments.
        
        \sigs
        \li ColorButton(color : QColor, text : str, parent : QWidget, **kwargs)
        \li ColorButton(color : QColor, parent : QWidget, **kwargs)
        \li ColorButton(parent : QWidget, **kwargs)
        """

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
    
    @pyqtSlot(QColor)
    def setColor(self, color):
        """
        Setter for the Color property.
        \note Accepts any value the QColor constructor will accept.
        \param color QColor
        """
        #use QColor(color) to allow QRgb values, Qt.GlobalColor et cetera
        if self.__color == QColor(color):
            return
        self.__color = QColor(color)
        self._regenerateIcon()
        self.colorChanged.emit(self.__color)
        
    def setFrameColor(self, color):
        """
        \brief Setter for the FrameColor property.
        Accepts any value the QColor constructor will accept.
        \param color QColor
        """
        if self.__frameColor == QColor(color):
            return
        self.__frameColor = QColor(color)
        self._regenerateIcon()
        
    def setIcon(self, icon):
        qWarning('ColorButton.setIcon: Use setColor(QColor).')

    def getColor(self): 
        """
        \brief Getter for Color property.
        \returns QColor
        """
        return QColor(self.__color)
    
    def getFrameColor(self):
        """
        \brief Getter for the FrameColor property.
        \returns QColor
        """
        return QColor(self.__frameColor)
    
    def paintEvent(self, ev):
        """
        \brief Reimplemented from parent class.
        \param ev QPaintEvent
        """
        if self.__isz != self.iconSize():
            self._regenerateIcon()
            return
        p = QPainter(self)
        opt = QStyleOptionToolButton()
        self.initStyleOption(opt)
        self.style().drawComplexControl(QStyle.CC_ToolButton, opt, p, self)

    def _regenerateIcon(self):
        """
        \brief Creates a new icon when the color property or icon size changes.
        """
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

    ##\name Properties
    ##\{
    
    color = pyqtProperty(QColor, fget=getColor, fset=setColor)
    frameColor = pyqtProperty(QColor, fget=getFrameColor, fset=setFrameColor)
    ##\}
