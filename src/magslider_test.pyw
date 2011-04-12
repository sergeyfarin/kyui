from PyQt4.QtCore import *
from PyQt4.QtGui import *

from template_test import TemplateDialog
from Widgets.magslider import ZoomInButton#, ZoomOutButton

class Dialog(TemplateDialog):
    def __init__(self, parent : QWidget = None):
        super().__init__(parent)
        self.setupUi()
        self.connectSignals()
    
    def setupUi(self):
        super().setupUi()
        
        self.testWidget = ZoomInButton(self)
        self.testWidget.setObjectName('testWidget')
        self.layout.insertWidget(0, self.testWidget)
        
#        self.testWidget2 = ZoomOutButton(self)
#        self.testWidget2.setObjectName('testWidget2')
#        self.layout.insertWidget(0, self.testWidget)
        
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
