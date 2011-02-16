#UTF-8
#template_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

from Widgets.colorslider import ColorSlider

class Dialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setObjectName('dialog')
        
        self.setupUi()
        
    def setupUi(self):
        self.layout = QVBoxLayout(self)
        self.layout.setObjectName('layout')
        
        self.testWidget = ColorSlider(Qt.Horizontal, self)
        self.testWidget.setObjectName('testWidget')
        self.testWidget.setRange(0, 255)
        self.testWidget.setFixedWidth(256)
        self.layout.addWidget(self.testWidget)
        
        self.settingsBox = QGroupBox(self)
        self.settingsBox.setObjectName('settingsBox')
        self.settingsLayout = QFormLayout(self.settingsBox)
        self.settingsLayout.setObjectName('settingsLayout')
        
        self.channelLabel = QLabel(self)
        self.channelLabel.setObjectName('channelLabel')
        self.channelBox = QComboBox(self)
        self.channelBox.setObjectName('channelBox')
        self.channelLabel.setBuddy(self.channelBox)
        self.settingsLayout.addRow(self.channelLabel, self.channelBox)
        
        self.rangeLabel = QLabel(self)
        self.rangeLabel.setObjectName('rangeLabel')
        self.rangeBox = QComboBox(self)
        self.rangeBox.setObjectName('rangeBox')
        self.rangeLabel.setBuddy(self.rangeBox)
        self.settingsLayout.addRow(self.rangeLabel, self.rangeBox)
        
        self.layout.addWidget(self.settingsBox)
        
        self.closeButton = QPushButton(self)
        self.closeButton.setObjectName('closeButton')
        self.closeButton.setDefault(True)
        self.layout.addWidget(self.closeButton)
        self.layout.setAlignment(self.closeButton, 
                                 Qt.AlignRight | Qt.AlignBottom)
        
        self.closeButton.clicked.connect(self.close)
        
        self.retranslateUi()
        
    def retranslateUi(self):
        self.setWindowTitle(self.trUtf8('Test Dialog'))
        self.settingsBox.setTitle(self.trUtf8('&Options'))
        self.channelLabel.setText(self.trUtf8('Cha&nnel'))
        self.rangeLabel.setText(self.trUtf8('&Range'))
        self.closeButton.setText(self.trUtf8('&Close'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
