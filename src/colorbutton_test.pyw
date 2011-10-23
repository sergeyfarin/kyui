#UTF-8
#colorbutton_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Widgets.colorbutton import ColorButton
from template_test import TemplateDialog

colorPairs = (('White', QColor(Qt.white)),
            ('Black', QColor(Qt.black)),
            ('Red', QColor(Qt.red)),
            ('Dark Red', QColor(Qt.darkRed)),
            ('Green', QColor(Qt.green)),
            ('Dark Green', QColor(Qt.darkGreen)),
            ('Blue', QColor(Qt.blue)),
            ('Dark Blue', QColor(Qt.darkBlue)),
            ('Cyan', QColor(Qt.cyan)),
            ('Dark Cyan', QColor(Qt.darkCyan)),
            ('Magenta', QColor(Qt.magenta)),
            ('Dark Magenta', QColor(Qt.darkMagenta)),
            ('Yellow', QColor(Qt.yellow)),
            ('Dark Yellow', QColor(Qt.darkYellow)),
            ('Gray', QColor(Qt.gray)),
            ('Dark Gray', QColor(Qt.darkGray)),
            ('Light Gray', QColor(Qt.lightGray)))

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
                                      parent=self, 
                                      toolButtonStyle=Qt.ToolButtonTextBesideIcon, 
                                      objectName='testWidget', 
                                      iconSize=QSize(16, 16))
        self.layout.insertWidget(0, self.testWidget)
        
        self.sizeBox = QComboBox(self.settingsBox, 
                                 objectName='sizeBox')
        self.settingsLayout.addRow('&Icon Size', self.sizeBox)
        
        self.colorBox = QComboBox(self.settingsBox, 
                                  objectName='colorBox')
        self.settingsLayout.addRow('C&olor', self.colorBox)
        
        self.frameColorBox = QComboBox(self.settingsBox, 
                                       objectName='frameColorBox')
        self.settingsLayout.addRow('&Frame Color', self.frameColorBox)
        
        self.textStyleBox = QComboBox(self.settingsBox, 
                                      objectName = 'textStyleBox')
        self.settingsLayout.addRow('&Text Style', self.textStyleBox)
        
        self.populateComboBoxes()
        self.textStyleBox.setCurrentIndex(1)
        
    def populateComboBoxes(self):
        self.sizeBox.addItem('16 x 16', QSize(16, 16))
        self.sizeBox.addItem('22 x 22', QSize(22, 22))
        self.sizeBox.addItem('24 x 24', QSize(24, 24))
        self.sizeBox.addItem('32 x 32', QSize(32, 32))
        
        self.textStyleBox.addItem('Icon Only', Qt.ToolButtonIconOnly)
        self.textStyleBox.addItem('Text Beside Icon', Qt.ToolButtonTextBesideIcon)
        self.textStyleBox.addItem('Text Under Icon', Qt.ToolButtonTextUnderIcon)
        self.textStyleBox.setCurrentIndex(1)
        
        for name, color in colorPairs:
            self.colorBox.addItem(name, color)
            self.frameColorBox.addItem(name, color)
        self.frameColorBox.setCurrentIndex(1)
        
    def retranslateUi(self):
        super().retranslateUi()
        tr = self.trUtf8
        self.setWindowTitle(tr('ColorButton Test'))
        self.settingsLayout.labelForField(self.sizeBox).setText(tr('&Icon Size'))
        self.settingsLayout.labelForField(self.colorBox).setText(tr('C&olor'))
        self.settingsLayout.labelForField(self.frameColorBox).setText(tr('&Frame Color'))
        self.settingsLayout.labelForField(self.textStyleBox).setText(tr('&Text Style'))
        
        self.sizeBox.setItemText(0, tr('16 x 16'))
        self.sizeBox.setItemText(1, tr('22 x 22'))
        self.sizeBox.setItemText(2, tr('24 x 24'))
        self.sizeBox.setItemText(3, tr('32 x 32'))
        
        self.textStyleBox.setItemText(0, tr('Icon Only'))
        self.textStyleBox.setItemText(1, tr('Text Beside Icon'))
        self.textStyleBox.setItemText(2, tr('Text Under Icon'))
        
        for idx in range(len(colorPairs)):
            self.colorBox.setItemText(idx, tr(colorPairs[idx][0]))
            self.frameColorBox.setItemText(idx, tr(colorPairs[idx][0]))

    def connectSignals(self):
        super().connectSignals()
        self.sizeBox.currentIndexChanged[int].connect(self.onSizeChanged)
        self.colorBox.currentIndexChanged[int].connect(self.onColorChanged)
        self.frameColorBox.currentIndexChanged[int].connect(self.onFrameColorChanged)
        self.textStyleBox.currentIndexChanged[int].connect(self.onStyleChanged)
        self.testWidget.clicked.connect(self.onColorButtonClicked)

    def onSizeChanged(self, idx : int):
        self.testWidget.setIconSize(self.sizeBox.itemData(idx, Qt.UserRole))

    def onColorChanged(self, idx : int):
        self.testWidget.setColor(self.colorBox.itemData(idx, Qt.UserRole))
        
    def onFrameColorChanged(self, idx : int):
        self.testWidget.setFrameColor(self.frameColorBox.itemData(idx, Qt.UserRole))
        
    def onStyleChanged(self, idx : int):
        self.testWidget.setToolButtonStyle(self.textStyleBox.itemData(idx, Qt.UserRole))
    
    def onColorButtonClicked(self):
        color = QColorDialog.getColor(self.testWidget.color, self)
        self.testWidget.setColor(color)
        idx = self.colorBox.findData(color)
        self.colorBox.blockSignals(True)
        self.colorBox.setCurrentIndex(idx)
        self.colorBox.blockSignals(False)
        
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
