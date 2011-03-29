#UTF-8
#gradient_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from template_test import TemplateDialog
from Experimental.gradient import ToolbarGradient, ToolGroupButton

class Dialog(TemplateDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setObjectName('dialog')
        
        self.setupUi()
        self.connectSignals()
        
    def setupUi(self):
        super().setupUi()
        
        self.testWidget = ToolbarGradient(self)
        self.testWidget.setObjectName('testWidget')
        self.testWidget.setContentsMargins(0, 0, 0, 0)
        self.testWidget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layout.insertWidget(0, self.testWidget)
        
        self.testLayout = QHBoxLayout(self.testWidget)
        self.testLayout.setObjectName('testLayout')
        self.testLayout.setContentsMargins(0, 0, 0, 0)
        
        self.testButton = ToolGroupButton(self.testWidget)
        self.testButton.setObjectName('testButton')
        self.testButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.testLayout.addWidget(self.testButton)

        self.testButton.setText('Test')
        icon = self.style().standardIcon(QStyle.SP_DriveHDIcon).pixmap(self.testButton.iconSize())
        self.testButton.setIcon(QIcon(icon))
    
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
