#UTF-8
#template_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

from Widgets.colorslider import ColorSlider_Old

from template_test import TemplateDialog

class Dialog(TemplateDialog):
    def __init__(self, parent = None):
        super(QDialog, self).__init__(parent)
        self.setObjectName('dialog')
        
        self._color = QColor(0, 0, 0)
        
        self.setupUi()
        self.connectSignals()
        
    def setupUi(self):
        super().setupUi()
        
        self.debugBox.hide()
        
        self.testBox = QGroupBox(self)
        self.testBox.setObjectName('testBox')
        self.testLayout = QBoxLayout(QBoxLayout.TopToBottom, self.testBox)
        self.testLayout.setObjectName('testLayout')
        
        self.testWidget1 = ColorSlider_Old(QColor.Rgb, 0, 
                                           Qt.Horizontal, self.testBox)
        self.testWidget1.setObjectName('testWidget1')
        self.testLayout.addWidget(self.testWidget1)
        
        self.testWidget2 = ColorSlider_Old(QColor.Rgb, 1, 
                                           Qt.Horizontal, self.testBox)
        self.testWidget2.setObjectName('testWidget2')
        self.testLayout.addWidget(self.testWidget2)
        
        self.testWidget3 = ColorSlider_Old(QColor.Rgb, 2, 
                                           Qt.Horizontal, self.testBox)
        self.testWidget3.setObjectName('testWidget3')
        self.testLayout.addWidget(self.testWidget3)
        
        self.layout.insertWidget(0, self.testBox)
        
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
        
        self.retranslateUi()
        
    def retranslateUi(self):
        super().retranslateUi()
        self.testBox.setTitle(self.trUtf8('&Test'))
        self.specLabel.setText(self.trUtf8('&Spec'))
        self.orientBox.setText('&Vertical Sliders')
        self.dynamicBox.setText('&Dynamic Gradients')
        
    def connectSignals(self):
        super().connectSignals()
        self.specBox.currentIndexChanged[int].connect(self.onSpecChanged)
        self.orientBox.toggled.connect(self.onOrientationChanged)
        self.dynamicBox.toggled.connect(self.setDynamic)
        self.setDynamic(True)
        
    def onSpecChanged(self, index : int):
        if index == 0:
            qDebug('Spec: RGB')
            self.testWidget1.setColorChannel(QColor.Rgb, 0)
            self.testWidget2.setColorChannel(QColor.Rgb, 1)
            self.testWidget3.setColorChannel(QColor.Rgb, 2)
        elif index == 1:
            self.testWidget1.setColorChannel(QColor.Hsv, 0)
            self.testWidget2.setColorChannel(QColor.Hsv, 1)
            self.testWidget3.setColorChannel(QColor.Hsv, 2)
        elif index == 2:
            self.testWidget1.setColorChannel(QColor.Hsl, 0)
            self.testWidget2.setColorChannel(QColor.Hsl, 1)
            self.testWidget3.setColorChannel(QColor.Hsl, 2)
            
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
        channel = self.testWidget1.colorChannel()
        self.testWidget2.setChannelValue(channel, value)
        self.testWidget3.setChannelValue(channel, value)

    def onSlider2Changed(self, value):
        channel = self.testWidget2.colorChannel()
        self.testWidget1.setChannelValue(channel, value)
        self.testWidget3.setChannelValue(channel, value)

    def onSlider3Changed(self, value):
        channel = self.testWidget3.colorChannel()
        self.testWidget1.setChannelValue(channel, value)
        self.testWidget2.setChannelValue(channel, value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
