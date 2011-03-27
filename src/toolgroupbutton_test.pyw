from PyQt4.QtCore import *
from PyQt4.QtGui import *

from template_test import TemplateDialog

from Widgets.toolgroup import ToolGroupButton

class Dialog(TemplateDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.connectSignals()
    
    def setupUi(self):
        super().setupUi()
        
        self.testWidget = ToolGroupButton(self)
        self.testWidget.setObjectName('testWidget')
        self.layout.insertWidget(0, self.testWidget)
        self.testWidget.setFixedSize(44, 86)
        
        self.testWidget.setText('Test')
        
        self.retranslateUi()
        
    def retranslateUi(self):
        super().retranslateUi()
    
    def connectSignals(self):
        super().connectSignals()
        
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
