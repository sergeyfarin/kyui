#UTF-8
#template_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Widgets.debugbox import DebugBox

class TemplateDialog(QDialog):
    def __init__(self, parent = None):
        super(QDialog, self).__init__(parent)
    
    def setupUi(self):
        self.layout = QVBoxLayout(self)
        self.layout.setObjectName('layout')
        
        self.settingsBox = QGroupBox(self)
        self.settingsBox.setObjectName('settingsBox')
        self.settingsLayout = QFormLayout(self.settingsBox)
        self.settingsLayout.setObjectName('settingsLayout')
        
        self.styleLabel = QLabel(self.settingsBox)
        self.styleLabel.setObjectName('styleLabel')
        self.styleBox = QComboBox(self.settingsBox)
        self.styleBox.setObjectName('styleBox')
        
        self.styleBox.addItems(QStyleFactory.keys())
        self.styleLabel.setBuddy(self.styleBox)
        
        self.settingsLayout.addRow(self.styleLabel, self.styleBox)
        
        self.layout.addWidget(self.settingsBox)
        
        self.debugBox = DebugBox(self)
        self.debugBox.setObjectName('debugBox')
        self.layout.addWidget(self.debugBox)
        qInstallMsgHandler(self.debugBox.postMsg)
        
        self.closeButton = QPushButton(self)
        self.closeButton.setObjectName('closeButton')
        self.closeButton.setDefault(True)
        self.layout.addWidget(self.closeButton)
        self.layout.setAlignment(self.closeButton, 
                                 Qt.AlignRight | Qt.AlignBottom)
        
        self.setupStyle()
    
    def setupStyle(self):
        version = QSysInfo.WindowsVersion
        if version & QSysInfo.WV_NT_based:
            if version == QSysInfo.WV_WINDOWS7 or version == QSysInfo.WV_VISTA:
                style = 'WindowsVista'
            elif version == QSysInfo.WV_XP or version == QSysInfo.WV_2003:
                style = 'WindowsXP'
            else:
                style = 'Windows'
        else:
            style = 'Plastique'
        self.styleBox.setCurrentIndex(self.styleBox.findText(style, Qt.MatchFixedString))
    
    def retranslateUi(self):
        self.setWindowTitle(self.trUtf8('Test Dialog'))
        self.settingsBox.setTitle(self.trUtf8('Options'))
        self.styleLabel.setText(self.trUtf8('St&yle'))
        self.closeButton.setText(self.trUtf8('&Close'))
    
    def connectSignals(self):
        self.styleBox.currentIndexChanged[str].connect(self.changeStyle)
        self.closeButton.clicked.connect(self.close)

    def changeStyle(self, style : str):
        qApp.setStyle(QStyleFactory.create(style))

class Dialog(TemplateDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi()
        self.connectSignals()
    
    def setupUi(self):
        super().setupUi()
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
