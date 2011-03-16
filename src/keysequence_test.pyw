#UTF-8
#keysequence_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

from template_test import TemplateDialog

from Widgets.keysequenceeditor import KeySequenceLineEdit

class Dialog(TemplateDialog):
    def __init__(self, parent = None):
        super(QDialog, self).__init__(parent)
        
        self.setupUi()
        self.retranslateUi()
        self.connectSignals()
        
    def setupUi(self):
        super().setupUi()
        
        self.debugBox.hide()
        
        self.testWidget = KeySequenceLineEdit(self)
        self.testWidget.setObjectName('testWidget')
        self.layout.insertWidget(0, self.testWidget)
    
    def retranslateUi(self):
        super().retranslateUi()
    
    def connectSignals(self):
        super().connectSignals()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
