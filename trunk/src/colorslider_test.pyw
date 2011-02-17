#UTF-8
#template_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

from Widgets.colorslider import ColorSlider
from Widgets.debugbox import DebugBox

class Dialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setObjectName('dialog')
        
        self._color = QColor(0, 0, 0)
        
        self.setupUi()
        self.connectSignals()
        
    def setupUi(self):
        self.layout = QVBoxLayout(self)
        self.layout.setObjectName('layout')
        
        self.testWidget = ColorSlider(Qt.Horizontal, self)
        self.testWidget.setObjectName('testWidget')
        self.testWidget.setRange(0, 255)
#        self.testWidget.setFixedWidth(256)
        self.layout.addWidget(self.testWidget)
        
        self.settingsBox = QGroupBox(self)
        self.settingsBox.setObjectName('settingsBox')
        self.settingsLayout = QFormLayout(self.settingsBox)
        self.settingsLayout.setObjectName('settingsLayout')
        
        self.specLabel = QLabel(self)
        self.specLabel.setObjectName('specLabel')
        self.specBox = QComboBox(self)
        self.specBox.setObjectName('specBox')
        self.specBox.addItem('RGB', QColor.Rgb)
        self.specBox.addItem('HSV', QColor.Hsv)
        self.specBox.addItem('HSL', QColor.Hsl)
        self.specLabel.setBuddy(self.specBox)
        self.settingsLayout.addRow(self.specLabel, self.specBox)
        
        self.channelLabel = QLabel(self)
        self.channelLabel.setObjectName('channelLabel')
        self.channelBox = QComboBox(self)
        self.channelBox.setObjectName('channelBox')
        self.channelLabel.setBuddy(self.channelBox)
        self.settingsLayout.addRow(self.channelLabel, self.channelBox)
        
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
        
        self.retranslateUi()
        
    def retranslateUi(self):
        self.setWindowTitle(self.trUtf8('Test Dialog'))
        self.settingsBox.setTitle(self.trUtf8('&Options'))
        self.specLabel.setText(self.trUtf8('&Spec'))
        self.channelLabel.setText(self.trUtf8('Cha&nnel'))
        self.closeButton.setText(self.trUtf8('&Close'))
        
    def connectSignals(self):
        self.specBox.currentIndexChanged[int].connect(self.onSpecChanged)
        self.channelBox.currentIndexChanged[int].connect(self.onChannelChanged)
        self.closeButton.clicked.connect(self.close)
        
        self.onSpecChanged(0)
        
    def onSpecChanged(self, index : int):
        if index == 0:
            qDebug('Spec: RGB')
            self.channelBox.clear()
            self.channelBox.addItem('Red')
            self.channelBox.addItem('Green')
            self.channelBox.addItem('Blue')
        elif index == 1:
            qDebug('Spec: HSV')
            self.channelBox.clear()
            self.channelBox.addItem('Hue')
            self.channelBox.addItem('Saturation')
            self.channelBox.addItem('Lightness')
        elif index == 2:
            qDebug('Spec: HSL')
            self.channelBox.clear()
            self.channelBox.addItem('Hue')
            self.channelBox.addItem('Saturation')
            self.channelBox.addItem('Luminosity')

    def onChannelChanged(self, channel : int):
        if self.specBox.currentIndex == 0:
            self.testWidget.setStartColor(QColor(0, 0, 0))
            if channel == 0: #Red
                self.testWidget.setEndColor(QColor(255, 0, 0))
                qDebug('Channel: Red')
            elif channel == 1: #Green
                self.testWidget.setEndColor(QColor(0, 255, 0))
                qDebug('Channel: Green')
            elif channel == 2: #Blue
                self.testWidget.setEndColor(QColor(0, 0, 255))
                qDebug('Channel: Blue')
        elif self.specBox.currentIndex == 1:
            pass
        elif self.specBox.currentIndex == 2:
            pass
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
