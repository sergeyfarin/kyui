# QFontWidget

from PyQt4.QtCore import Qt, pyqtSignal, pyqtSlot, pyqtProperty
from PyQt4.QtGui import QWidget, QFrame, QScrollArea, QLineEdit
from PyQt4.QtGui import QPalette, QColor
from PyQt4.QtGui import QFont
from PyQt4.QtGui import QSizePolicy

class KyFontPreviewWidget(QScrollArea):
    backgroundColorChanged = pyqtSignal('QColor')
    currentFontChanged = pyqtSignal(QFont)
    textChanged = pyqtSignal()
    textColorChanged = pyqtSignal(QColor)
    
    def __init__(self, text = '', font = None, parent = None):
        super().__init__(parent)
            
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.setAcceptDrops(False)        
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)    
        self.setWidgetResizable(True)
        self.setAlignment(Qt.AlignCenter)
        self.setFrameShape(QFrame.StyledPanel)
        
        previewText = QLineEdit()
        previewText.setObjectName('textSample')
        previewText.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        previewText.setReadOnly(True)
        previewText.setAlignment(Qt.AlignCenter)
        previewText.setFrame(False)
        previewText.setText(text)
        previewText.setFont(font if font else self.font())
        
        self.setWidget(previewText)
        
    def backgroundColor(self) -> QColor:
        return self.widget().palette().color(QPalette.Base)
    def text(self) -> str:
        return self.widget().text()
    def textColor(self) -> QColor:
        return self.widget().palette().color(QPalette.Text)
    def currentFont(self) -> QFont:
        self.widget().font()    
        
    def setBackgroundColor(self, color : QColor) -> None:
        palette = self.widget().palette()
        palette.setColor(QPalette.Base, color)
        self.widget().setPalette(palette)
        self.backgroundColorChanged.emit(color)
        
    def setText(self, text : str) -> None:
        self.widget().setText(text)
        self.textChanged.emit()

    def setTextColor(self, color : QColor) -> None:
        palette = self.widget().palette()
        palette.setColor(QPalette.Text, color)
        self.textColorChanged.emit(color)
    
    @pyqtSlot(QFont)
    def setCurrentFont(self, font : QFont) -> None:
        if not isinstance(font, QFont):
            return
        self.setFont(font)
        self.currentFontChanged.emit(font)
        
    currentFont = pyqtProperty(QFont, fget=currentFont, fset=setCurrentFont)
    text = pyqtProperty(str, fget=text, fset=setText)
    textColor = pyqtProperty(QColor, fget=textColor, fset=setTextColor)
    backgroundColor = pyqtProperty(QColor, 
                                   fget=backgroundColor, 
                                   fset=setBackgroundColor)
