# QFontWidget

from PyQt4.QtCore import *
from PyQt4.QtGui import *

# QFontPreviewWidget uses a QGraphicsView instead of a line edit widget because
# Qt auto-resizes line edit widgets in order to fit the text inside. I suppose
# I could have used a QLineEdit without a frame inside a QScrollArea, but this
# is both simpler and cleaner WRT coding and maintaining.
class QFontPreviewWidget(QScrollArea):
    bgColorChanged = pyqtSignal('QColor')
    # This signal is currentFontChanged instead of textFontChanged to keep with
    # the signals of the other QFontWidget classes
    currentFontChanged = pyqtSignal('QFont')
    textChanged = pyqtSignal()
    textColorChanged = pyqtSignal('QColor')
    
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
        
    def bgColor(self): return self.widget().palette().color(QPalette.Base)
    def text(self): return self.widget().text()
    def textColor(self): return self.widget().palette().color(QPalette.Text)
    def textFont(self): self.widget().font()    
        
    def setBgColor(self, color):
        if not isinstance(color, QColor):
            return
        palette = self.widget().palette()
        palette.setColor(QPalette.Base, color)
        self.widget().setPalette(palette)
        self.bgColorChanged.emit(color)
        
    def setText(self, text = ''):
        self.widget().setText(text)
        self.textChanged.emit()

    def setTextColor(self, color):
        if not isinstance(color, QColor):
            return
        palette = self.widget().palette()
        palette.setColor(QPalette.Text, color)
        self.textColorChanged.emit(color)
        
    def setTextFont(self, font):
        if not isinstance(font, QFont):
            return
        self.setFont(font)
        self.currentFontChanged.emit(font)

# Simple dialog to demonstrate the widget and how to use it.
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
        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = GenericDialog()
    dialog.show()
    sys.exit(app.exec_())
