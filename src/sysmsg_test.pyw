#UTF-8
#magslider_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from template_test import TemplateDialog
from Widgets.sysmsg import SystrayPopup

class Dialog(TemplateDialog):
    def __init__(self, parent : QWidget = None):
        super().__init__(parent)
        self.setupUi()
        self.connectSignals()
        qDebug(('Primary Screen: {}\nGeometry: {}\nAvailable: {}\nCorner: {}\nPos: {}'.format(
               self.testWidget.primary, self.testWidget.geom,
               self.testWidget.availGeom, self.testWidget.corner, 
               self.testWidget.cornerPos)))
    
    def setupUi(self):
        super().setupUi()
        
        self.testWidget = SystrayPopup(self)
        self.testWidget.setObjectName('testWidget')
        
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
