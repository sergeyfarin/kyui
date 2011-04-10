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
        self.testWidget.setFixedSize(48, 86)
        self.testWidget.setText('Test')
        icon = self.style().standardIcon(QStyle.SP_DriveHDIcon).pixmap(self.testWidget.iconSize())
        self.testWidget.setIcon(QIcon(icon))
        self.layout.insertWidget(0, self.testWidget)
        
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