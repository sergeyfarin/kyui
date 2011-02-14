#UTF-8
#template_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class Dialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setObjectName('dialog')
        
        self.setupUi()
        
    def setupUi(self):
        self.layout = QVBoxLayout(self)
        self.layout.setObjectName('layout')
        
        self.testWidget = QWidget(self)
        self.testWidget.setObjectName('testWidget')
        self.layout.addWidget(self.testWidget)
        
        self.closeButton = QPushButton(self)
        self.closeButton.setObjectName('closeButton')
        self.closeButton.setDefault(True)
        self.layout.addWidget(self.closeButton)
        self.layout.setAlignment(self.closeButton, 
                                 Qt.AlignRight | Qt.AlignBottom)
        
        self.closeButton.clicked.connect(self.close)
        
        self.retranslateUi()
        
    def retranslateUi(self):
        self.setWindowTitle(self.trUtf8('Test Dialog'))
        self.closeButton.setText(self.trUtf8('&Close'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
