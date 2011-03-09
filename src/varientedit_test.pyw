#UTF-8
#varientedit_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

from Widgets.varientedit import *
from template_test import TemplateDialog

class Dialog(TemplateDialog):
    def __init__(self, parent = None):
        super(QWidget, self).__init__(parent)
        self.setObjectName('dialog')
        
        self.setupUi()
        self.retranslateUi()
        self.connectSignals()
        
    def setupUi(self):
        super().setupUi()
        
#        self.testWidget = QDataType.generateEditor(QVariant.Bool, 'Test', self)
        self.testWidget = QComboBox(self, editable=True, frame=False)
        self.testWidget.setObjectName('testWidget')
        self.layout.insertWidget(0, self.testWidget)
        
        self.retranslateUi()
        self.connectSignals()
        
    def retranslateUi(self):
        super().retranslateUi()
        
    def connectSignals(self):
        super().connectSignals()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
