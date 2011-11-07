#UTF-8
#colorslider_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

from Widgets.colorslider2 import ColorSlider

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
        
        self.testWidget = ColorSlider(Qt.Horizontal, 
                                     parent=self, 
                                     objectName='testBox')
        
        self.layout.insertWidget(0, self.testWidget)
        
        self.handleBox = QComboBox(self.settingsBox, 
                                   objectName='handleBox')
        self.settingsLayout.addRow('&Handle Style', self.handleBox)
        
#        self.specLabel = QLabel(self.settingsBox)
#        self.specLabel.setObjectName('specLabel')
#        self.specBox = QComboBox(self.settingsBox)
#        self.specBox.setObjectName('specBox')
#        self.specBox.addItem('RGB', QColor.Rgb)
#        self.specBox.addItem('HSV', QColor.Hsv)
#        self.specBox.addItem('HSL', QColor.Hsl)
#        self.specLabel.setBuddy(self.specBox)
#        self.settingsLayout.addRow(self.specLabel, self.specBox)
#        
        self.orientBox = QCheckBox(self)
        self.orientBox.setObjectName('orientBox')
        self.settingsLayout.addWidget(self.orientBox)
#        
#        self.dynamicBox = QCheckBox(self)
#        self.dynamicBox.setObjectName('dynamicBox')
#        self.dynamicBox.setChecked(True)
#        self.settingsLayout.addWidget(self.dynamicBox)
        
        self.populateComboBoxes()
        
        self.retranslateUi()
        
    def retranslateUi(self):
        super().retranslateUi()
        tr = self.trUtf8
        self.setWindowTitle(self.trUtf8('ColorSlider Test'))
        self.settingsLayout.labelForField(self.handleBox).setText(tr('&Handle Style'))
        
#        self.testBox.setTitle(self.trUtf8('&Test'))
#        self.specLabel.setText(self.trUtf8('&Spec'))
        self.orientBox.setText('&Vertical Sliders')
#        self.dynamicBox.setText('&Dynamic Gradients')

    def populateComboBoxes(self):
        self.handleBox.addItem('Native Style', ColorSlider.NativeStyle)
        self.handleBox.addItem('Photoshop Style', ColorSlider.PhotoshopStyle)
        self.handleBox.addItem('Triangle Style', ColorSlider.TriangleStyle)

    def connectSignals(self):
        super().connectSignals()
        
        
        self.handleBox.currentIndexChanged[int].connect(self.changeHandleStyle)
        self.orientBox.toggled.connect(self.changeOrientation)
#        self.dynamicBox.toggled.connect(self.setDynamic)
#        self.setDynamic(True)
            
    def changeHandleStyle(self, style):
        self.testWidget.sliderStyle = self.handleBox.itemData(style)

    def changeOrientation(self, vertical):
        self.testWidget.setOrientation(Qt.Vertical if vertical else Qt.Horizontal)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
