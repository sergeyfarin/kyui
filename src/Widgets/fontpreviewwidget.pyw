from PyQt4.QtCore import Qt, pyqtSlot, pyqtProperty
from PyQt4.QtGui import QFrame, QScrollArea, QLineEdit
from PyQt4.QtGui import QPalette, QColor
from PyQt4.QtGui import QFont
from PyQt4.QtGui import QSizePolicy

class FontPreviewWidget(QScrollArea):
    """
    \brief Preview widget for a QFont.
    This class is emulates the functionality of preview widgets in font
    selection dialogs.
    """
    def __init__(self, text = None, font = None, parent = None, **kwargs):
        """
        Constructor.
        \param text str: Initial value for the text property.
        \param font QFont: Font used to display the text property.
        \param parent QObject: Parent object
        \param kwargs dict: pyqtProperty constructor keyword arguments.
        """
        kwargs['verticalScrollBarPolicy'] = Qt.ScrollBarAlwaysOff
        kwargs['horizontalScrollBarPolicy'] = Qt.ScrollBarAlwaysOff
        kwargs['acceptDrops'] = False
        kwargs['widgetResizable'] = True
        kwargs['alignment'] = Qt.AlignCenter
        if 'frameShape' not in kwargs:
            kwargs['frameShape'] = QFrame.StyledPanel
        super().__init__(parent, **kwargs)
        
        previewText = QLineEdit(sizePolicy= QSizePolicy(QSizePolicy.Expanding, 
                                                        QSizePolicy.Expanding), 
                                readOnly=True, 
                                alignment=Qt.AlignCenter, 
                                frame=False, 
                                text=text, 
                                font=font if font else self.font())
        
        self.setWidget(previewText)
        
    def getBackgroundColor(self):
        """
        Getter for the backgroundColor property.
        \returns QColor
        """
        return self.widget().palette().color(QPalette.Base)
    def getText(self):
        """
        Getter for the text property.
        \returns str
        """
        return self.widget().text()
    def getTextColor(self):
        """
        Getter for the textColor property.
        \returns QColor
        """
        return self.widget().palette().color(QPalette.Text)
        
    def getCurrentFont(self):
        """
        Getter for the currentFont property.
        \returns QFont
        """
        self.widget().font() 
        
    def setBackgroundColor(self, color):
        """
        Setter for the backgroundColor property.
        \param color QColor
        """
        if self.widget().palette().color(QPalette.Base) == color:
            return
        palette = self.widget().palette()
        palette.setColor(QPalette.Base, color)
        self.widget().setPalette(palette)
        
    def setText(self, text):
        """
        Setter for the text property.
        \param text str
        """
        self.widget().setText(text)

    def setTextColor(self, color):
        """
        Setter for the textColor property.
        \param color QColor
        """
        palette = self.widget().palette()
        palette.setColor(QPalette.Text, color)
    
    @pyqtSlot(QFont)
    def setCurrentFont(self, font):
        """
        Setter for the currentFont property.
        \param font QFont
        """
        if not isinstance(font, QFont) or font == self.font():
            return
        self.widget().setFont(font)
    
    ##\name Properties
    ##\{
    
    currentFont = pyqtProperty(QFont, fget=getCurrentFont, fset=setCurrentFont)
    text = pyqtProperty(str, fget=getText, fset=setText)
    textColor = pyqtProperty(QColor, fget=getTextColor, fset=setTextColor)
    backgroundColor = pyqtProperty(QColor, 
                                   fget=getBackgroundColor, 
                                   fset=setBackgroundColor)
    ##\}
