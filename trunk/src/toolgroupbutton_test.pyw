from PyQt4.QtCore import *
from PyQt4.QtGui import *

from template_test import TemplateDialog

from Widgets.toolgroup2 import ToolGroupButton, ToolGroupBox

class Dialog(TemplateDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.connectSignals()
    
    def setupUi(self):
        super().setupUi()
        
        self.toolBar = QToolBar(self)
        self.toolBar.setObjectName('toolBar')
        self.layout.insertWidget(0, self.toolBar)
        
        icon = QIcon(self.style().standardIcon(QStyle.SP_DriveHDIcon).pixmap(QSize(22, 22)))
        self.toolGroupBox = ToolGroupBox(self.toolBar, None, 'Test', icon)
        self.toolGroupBox.setObjectName('toolGroupBox')
        self.toolGroupBox.hide()
        
        self.testWidget = ToolGroupButton(self.toolBar, self.toolGroupBox)
        self.testWidget.setObjectName('testWidget')
        self.testWidget.setFixedSize(48, 86)
        self.toolBar.addWidget(self.testWidget)
        
        
        
        self.fadeAnim = QPropertyAnimation(self, 'windowOpacity')
        self.fadeAnim.setDuration(300)
        self.fadeAnim.setStartValue(1.0)
        self.fadeAnim.setKeyValueAt(0.5, 0.0)
        self.fadeAnim.setEndValue(1.0)
        
        self.fadeButton = QPushButton(self.settingsBox)
        self.fadeButton.setObjectName('fadeButton')
        self.settingsLayout.addWidget(self.fadeButton)
        
        self.retranslateUi()
        
    def retranslateUi(self):
        super().retranslateUi()
        self.fadeButton.setText(self.trUtf8('&Fade Effect'))
    
    def connectSignals(self):
        super().connectSignals()
        self.fadeButton.clicked.connect(self.fadeButtonClicked)
#        self.fadeAnim.finished.connect(self.fadeFinished)
        
    def fadeButtonClicked(self):
        qDebug('Animation started')
        self.fadeAnim.start()
        
    def fadeFinished(self):
        self.setWindowOpacity(1.0)
        
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
