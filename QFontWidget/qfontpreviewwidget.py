# QFontWidget

from PyQt4.QtCore import Qt, pyqtSignal, pyqtSlot, pyqtProperty
from PyQt4.QtGui import QWidget, QScrollArea, QLineEdit
from PyQt4.QtGui import QPalette, QColor
from PyQt4.QtGui import QFont
from PyQt4.QtGui import QSizePolicy

class QFontPreviewWidget(QScrollArea):
    backgroundColorChanged = pyqtSignal('QColor')
    currentFontChanged = pyqtSignal(QFont)
    textChanged = pyqtSignal()
    textColorChanged = pyqtSignal(QColor)
    
    def __init__(self, text = '', font = None, parent = None):
        super().__init__(parent)
        if not font or not isinstance(font, QFont):
            font = self.font()
        else:    
            self.setFont(font)
            
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.setAcceptDrops(False)        
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)    
        self.setWidgetResizable(True)
        self.setAlignment(Qt.AlignCenter)
        
        previewText = QLineEdit()
        previewText.setObjectName('textSample')
        previewText.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        previewText.setReadOnly(True)
        previewText.setAlignment(Qt.AlignCenter)
        previewText.setFrame(False)
        previewText.setText(text)
        
        self.setWidget(previewText)
        
    def backgroundColor(self): return self.widget().palette().color(QPalette.Base)
    def text(self): return self.widget().text()
    def textColor(self): return self.widget().palette().color(QPalette.Text)
    def textFont(self): self.widget().font()    
        
    def setBackgroundColor(self, color) -> None:
        palette = self.widget().palette()
        palette.setColor(QPalette.Base, color)
        self.widget().setPalette(palette)
        self.backgroundColorChanged.emit(color)
        
    def setText(self, text : str) -> None:
        self.widget().setText(text)
        self.textChanged.emit()

    def setTextColor(self, color):
        palette = self.widget().palette()
        palette.setColor(QPalette.Text, color)
        self.textColorChanged.emit(color)
        
    def setTextFont(self, font):
        if not isinstance(font, QFont):
            return
        self.setFont(font)
        self.currentFontChanged.emit(font)

# Simple dialog to demonstrate the widget and how to use it.
if __name__ == '__main__':
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    class GenericDialog(QDialog):
        def __init__(self, parent = None):
            super().__init__(parent)
            self.setObjectName('dialog')
            self.setWindowTitle('QFontPreviewWidget Test')
            self.resize(371, 151)
            self.setFont(QFont('Segoe UI', 9))
            self.__setupUi()
            
            self.buttonBox.accepted.connect(self.accept)
            
        def __setupUi(self):
            self.layout = QVBoxLayout(self)
            self.layout.setObjectName('layout')
            
            font = self.font()
            
            self.previewWidget = QFontPreviewWidget('Sample 123', font, self)
            self.previewWidget.setGeometry(QRect(20, 10, 351, 51))
            self.previewWidget.setFrameShape(QFrame.Panel)
            self.layout.addWidget(self.previewWidget)
            
            self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok, 
                                              Qt.Horizontal, self)
            self.layout.addWidget(self.buttonBox)

    import sys
    app = QApplication(sys.argv)
    dialog = GenericDialog()
    dialog.show()
    sys.exit(app.exec_())
