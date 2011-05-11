#UTF-8
#magslider_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from template_test import TemplateDialog
from Widgets.magslider import MagSlider

class Dialog(TemplateDialog):
    def __init__(self, parent : QWidget = None):
        super().__init__(parent)
        self.setupUi()
        self.connectSignals()
    
    def setupUi(self):
        super().setupUi()
        
        self.testView = QGraphicsView(self, objectName='testView')
        self.testScene = QGraphicsScene(self.testView, objectName='testScene')
        self.testView.setScene(self.testScene)
        self.testItem = self.testScene.addPixmap(QPixmap('./Widgets/resource/test.png'))
        self.testItem.setPos(self.testItem.mapFromScene(QPointF(0, 0)))
        self.layout.insertWidget(0, self.testView)
        
        self.testWidget = MagSlider(Qt.Horizontal, self)
        self.testWidget.setObjectName('testWidget')
        self.layout.insertWidget(1, self.testWidget)
        
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
