#UTF-8
#template_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from template_test import TemplateDialog

from Property.model import PropertyView

class Dialog(TemplateDialog):
    def __init__(self, parent : QWidget = None):
        super().__init__(parent)
        self.setupUi()
        self.connectSignals()
    
    def setupUi(self):
        super().setupUi()
        self.resize(QSize(800, 800))
        
        self.testWidget = QTreeWidget(self, objectName='testWidget')
        self.testWidget.setVisible(False)
        
        self.propview = PropertyView(self.testWidget, 
                                     parent=self, 
                                     uniformRowHeights=True, 
                                     alternatingRowColors=True)
        self.layout.insertWidget(1, self.propview)
        
        self.layout.setStretch(1, 2)
        self.layout.setStretch(2, 1)
        
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
