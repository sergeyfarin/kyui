#UTF-8
#colorbutton_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

from Widgets.colorbutton import ColorButton
from Widgets.debugbox import DebugBox

from template_test import TemplateDialog

class Dialog(TemplateDialog):
    def __init__(self, parent = None):
        super(QDialog, self).__init__(parent)
        self.setObjectName('dialog')
        
        self.setupUi()
        self.retranslateUi()
        self.connectSignals()
        
    def setupUi(self):
        super().setupUi()
        self.testWidget = ColorButton(color=Qt.white, 
                                      text='Test', 
                                      parent=self)
        self.testWidget.setObjectName('testWidget')
        self.testWidget.setIconSize(QSize(16, 16))
        self.layout.insertWidget(0, self.testWidget)
        
        self.sizeLabel = QLabel(self.settingsBox)
        self.sizeLabel.setObjectName('sizeLabel')
        self.sizeBox = QComboBox(self.settingsBox)
        self.sizeBox.setObjectName('sizeBox')
        self.sizeBox.addItem('16 x 16', QSize(16, 16))
        self.sizeBox.addItem('22 x 22', QSize(22, 22))
        self.sizeBox.addItem('24 x 24', QSize(24, 24))
        self.sizeBox.addItem('32 x 32', QSize(32, 32))
        self.settingsLayout.addRow(self.sizeLabel, self.sizeBox)
        self.sizeLabel.setBuddy(self.sizeBox)
        
        self.colorLabel = QLabel(self.settingsBox)
        self.colorLabel.setObjectName('colorLabel')
        self.colorBox = QComboBox(self.settingsBox)
        self.colorBox.setObjectName('colorBox')
        self.colorBox.addItem('White', QColor(Qt.white))
        self.colorBox.addItem('Black', QColor(Qt.black))
        self.colorBox.addItem('Red', QColor(Qt.red))
        self.colorBox.addItem('Dark Red', QColor(Qt.darkRed))
        self.colorBox.addItem('Green', QColor(Qt.green))
        self.colorBox.addItem('Dark Green', QColor(Qt.darkGreen))
        self.colorBox.addItem('Blue', QColor(Qt.blue))
        self.colorBox.addItem('Dark Blue', QColor(Qt.darkBlue))
        self.colorBox.addItem('Cyan', QColor(Qt.cyan))
        self.colorBox.addItem('Dark Cyan', QColor(Qt.darkCyan))
        self.colorBox.addItem('Magenta', QColor(Qt.magenta))
        self.colorBox.addItem('Dark Magenta', QColor(Qt.darkMagenta))
        self.colorBox.addItem('Yellow', QColor(Qt.yellow))
        self.colorBox.addItem('Dark Yellow', QColor(Qt.darkYellow))
        self.colorBox.addItem('Gray', QColor(Qt.gray))
        self.colorBox.addItem('Dark Gray', QColor(Qt.darkGray))
        self.colorBox.addItem('Light Gray', QColor(Qt.lightGray))
        self.settingsLayout.addRow(self.colorLabel, self.colorBox)
        self.colorLabel.setBuddy(self.colorBox)
        
        self.textStyleLabel = QLabel(self.settingsBox)
        self.textStyleLabel.setObjectName('textStyleLabel')
        self.textStyleBox = QComboBox(self.settingsBox)
        self.textStyleBox.setObjectName('textStyleBox')
        self.textStyleBox.addItem('Icon Only', Qt.ToolButtonIconOnly)
        self.textStyleBox.addItem('Text Beside Icon', Qt.ToolButtonTextBesideIcon)
        self.textStyleBox.addItem('Text Under Icon', Qt.ToolButtonTextUnderIcon)
        self.textStyleBox.setCurrentIndex(1)
        self.settingsLayout.addRow(self.textStyleLabel, self.textStyleBox)
        self.textStyleLabel.setBuddy(self.textStyleBox)
        
    def connectSignals(self):
        super().connectSignals()
        self.sizeBox.currentIndexChanged[int].connect(self.onSizeChanged)
        self.colorBox.currentIndexChanged[int].connect(self.onColorChanged)
        self.textStyleBox.currentIndexChanged[int].connect(self.onStyleChanged)
        self.testWidget.clicked.connect(self.onColorButtonClicked)
        
    def retranslateUi(self):
        super().retranslateUi()
        self.sizeLabel.setText(self.trUtf8('&Icon Size'))
        self.colorLabel.setText(self.trUtf8('C&olor'))
        self.textStyleLabel.setText(self.trUtf8('&Text Style'))
        
        self.sizeBox.setItemText(0, self.trUtf8('16 x 16'))
        self.sizeBox.setItemText(1, self.trUtf8('22 x 22'))
        self.sizeBox.setItemText(2, self.trUtf8('24 x 24'))
        self.sizeBox.setItemText(3, self.trUtf8('32 x 32'))
        
        self.colorBox.setItemText(0, self.trUtf8('White'))
        self.colorBox.setItemText(1, self.trUtf8('Black'))
        self.colorBox.setItemText(2, self.trUtf8('Red'))
        self.colorBox.setItemText(3, self.trUtf8('Dark Red'))
        self.colorBox.setItemText(4, self.trUtf8('Green'))
        self.colorBox.setItemText(5, self.trUtf8('Dark Green'))
        self.colorBox.setItemText(6, self.trUtf8('Blue'))
        self.colorBox.setItemText(7, self.trUtf8('Dark Blue'))
        self.colorBox.setItemText(8, self.trUtf8('Cyan'))
        self.colorBox.setItemText(9, self.trUtf8('Dark Cyan'))
        self.colorBox.setItemText(10, self.trUtf8('Magenta'))
        self.colorBox.setItemText(11, self.trUtf8('Dark Magenta'))
        self.colorBox.setItemText(12, self.trUtf8('Yellow'))
        self.colorBox.setItemText(13, self.trUtf8('Dark Yellow'))
        self.colorBox.setItemText(14, self.trUtf8('Gray'))
        self.colorBox.setItemText(15, self.trUtf8('Dark Gray'))
        self.colorBox.setItemText(16, self.trUtf8('Light Gray'))

    def onSizeChanged(self, index : int):
        self.testWidget.setIconSize(self.sizeBox.itemData(index, Qt.UserRole))

    def onColorChanged(self, index : int):
        self.testWidget.setColor(self.colorBox.itemData(index, Qt.UserRole))
        
    def onStyleChanged(self, index : int):
        self.testWidget.setToolButtonStyle(self.textStyleBox.itemData(index, Qt.UserRole))
    
    def onColorButtonClicked(self):
        color = QColorDialog.getColor(self.testWidget.color, self)
        self.testWidget.setColor(color)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
