from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qsimplefontwidget import KySimpleFontWidget
from qfontpreviewwidget import QFontPreviewWidget

class GenericDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setObjectName('dialog')
        self.setWindowTitle('Font Widgets Test')
        self.setFont(QFont('Segoe UI', 9))
        
        self.__setupUi()
        
        
        
    def __setupUi(self):
        layout = QVBoxLayout(self)
        layout.setObjectName('layout')
        
        fontWidget = KySimpleFontWidget(self.font(), self)
        fontWidget.setBoldButtonVisible(True)
        fontWidget.setItalicButtonVisible(True)
        fontWidget.setUnderlineButtonVisible(True)
        layout.addWidget(fontWidget)
        
        text = 'Sample 123'
        
        previewWidget = QFontPreviewWidget(text, self.font(), self)
        previewWidget.setFrameShape(QFrame.Panel)
        layout.addWidget(previewWidget)
        
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok, 
                                          Qt.Horizontal, self)
        layout.addWidget(buttonBox)
        
        fontWidget.currentFontChanged.connect(previewWidget.setTextFont)
        buttonBox.accepted.connect(self.accept)
        
        self.layout = layout
        self.buttonBox = buttonBox
        self.fontWidget = fontWidget

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = GenericDialog()
    dialog.show()
    sys.exit(app.exec_())
