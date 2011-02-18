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
        
        self.testBox = QGroupBox(self)
        self.testBox.setObjectName('testBox')
        self.testLayout = QBoxLayout(QBoxLayout.TopToBottom, self.testBox)
        self.testLayout.setObjectName('testLayout')
        
        self.testWidget1 = ColorSlider(Qt.Horizontal, self.testBox, 
                                       ColorSlider.Red)
        self.testWidget1.setObjectName('testWidget1')
        self.testWidget1.setRange(0, 255)
        self.testLayout.addWidget(self.testWidget1)
        
        self.testWidget2 = ColorSlider(Qt.Horizontal, self.testBox, 
                                       ColorSlider.Green)
        self.testWidget2.setObjectName('testWidget2')
        self.testWidget2.setRange(0, 255)
        self.testLayout.addWidget(self.testWidget2)
        
        self.testWidget3 = ColorSlider(Qt.Horizontal, self.testBox, 
                                       ColorSlider.Blue)
        self.testWidget3.setObjectName('testWidget3')
        self.testWidget3.setRange(0, 255)
        self.testLayout.addWidget(self.testWidget3)
        
        self.layout.addWidget(self.testBox)
        
        self.settingsBox = QGroupBox(self)
        self.settingsBox.setObjectName('settingsBox')
        self.settingsLayout = QFormLayout(self.settingsBox)
        self.settingsLayout.setObjectName('settingsLayout')
        
        self.specLabel = QLabel(self.settingsBox)
        self.specLabel.setObjectName('specLabel')
        self.specBox = QComboBox(self.settingsBox)
        self.specBox.setObjectName('specBox')
        self.specBox.addItem('RGB', QColor.Rgb)
        self.specBox.addItem('HSV', QColor.Hsv)
        self.specBox.addItem('HSL', QColor.Hsl)
        self.specLabel.setBuddy(self.specBox)
        self.settingsLayout.addRow(self.specLabel, self.specBox)
        
        self.orientBox = QCheckBox(self)
        self.orientBox.setObjectName('orientBox')
        self.settingsLayout.addWidget(self.orientBox)
        
        self.dynamicBox = QCheckBox(self)
        self.dynamicBox.setObjectName('dynamicBox')
        self.dynamicBox.setChecked(True)
        self.settingsLayout.addWidget(self.dynamicBox)
        
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
        self.testBox.setTitle(self.trUtf8('&Test'))
        self.settingsBox.setTitle(self.trUtf8('&Options'))
        self.specLabel.setText(self.trUtf8('&Spec'))
        self.orientBox.setText('&Vertical Sliders')
        self.dynamicBox.setText('&Dynamic Gradients')
        self.closeButton.setText(self.trUtf8('&Close'))
        
    def connectSignals(self):
        self.specBox.currentIndexChanged[int].connect(self.onSpecChanged)
        self.orientBox.toggled.connect(self.onOrientationChanged)
        self.dynamicBox.toggled.connect(self.setDynamic)
        self.closeButton.clicked.connect(self.close)
        self.setDynamic(True)
        
#        self.onSpecChanged(0)
        
    def onSpecChanged(self, index : int):
        if index == 0:
            qDebug('Spec: RGB')
            self.testWidget1.setComponent(ColorSlider.Red)
            self.testWidget2.setComponent(ColorSlider.Green)
            self.testWidget3.setComponent(ColorSlider.Blue)
        elif index == 1:
            qDebug('Spec: HSV')
            self.testWidget1.setComponent(ColorSlider.HsvHue)
            self.testWidget2.setComponent(ColorSlider.HsvSat)
            self.testWidget3.setComponent(ColorSlider.HsvVal)
        elif index == 2:
            qDebug('Spec: HSL')
            self.testWidget1.setComponent(ColorSlider.HslHue)
            self.testWidget2.setComponent(ColorSlider.HslSat)
            self.testWidget3.setComponent(ColorSlider.HslLum)
            
    def onOrientationChanged(self):
        if self.orientBox.isChecked():
            direction = QBoxLayout.LeftToRight
            orient = Qt.Vertical
        else:
            direction = QBoxLayout.TopToBottom
            orient = Qt.Horizontal
        self.testLayout.setDirection(direction)
        self.testWidget1.setOrientation(orient)
        self.testWidget2.setOrientation(orient)
        self.testWidget3.setOrientation(orient)
        
    def setDynamic(self, dynamic):
        if dynamic:
            self.testWidget1.valueChanged.connect(self.onSlider1Changed)
            self.testWidget2.valueChanged.connect(self.onSlider2Changed)
            self.testWidget3.valueChanged.connect(self.onSlider3Changed)
        else:
            self.testWidget1.valueChanged.disconnect(self.onSlider1Changed)
            self.testWidget2.valueChanged.disconnect(self.onSlider2Changed)
            self.testWidget3.valueChanged.disconnect(self.onSlider3Changed)
        
    def onSlider1Changed(self, value):
        component = self.testWidget1.component()
        self.testWidget2.setComponentValue(component, value)
        self.testWidget3.setComponentValue(component, value)

    def onSlider2Changed(self, value):
        component = self.testWidget2.component()
        self.testWidget1.setComponentValue(component, value)
        self.testWidget3.setComponentValue(component, value)

    def onSlider3Changed(self, value):
        component = self.testWidget3.component()
        self.testWidget1.setComponentValue(component, value)
        self.testWidget2.setComponentValue(component, value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
