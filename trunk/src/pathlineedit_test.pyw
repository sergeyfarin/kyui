#UTF-8
#colorbutton_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Widgets.pathlineedit import PathLineEdit
from template_test import TemplateDialog

import test_resource_rc

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
        
        self.testWidget = PathLineEdit(parent=self)
        self.layout.insertWidget(0, self.testWidget)
        
        self.pathBox = QComboBox(self.settingsBox, 
                                 objectName='pathBox')
        self.settingsLayout.addRow('&Path', self.pathBox)
        
        self.iconBox = QComboBox(self.settingsBox, 
                                  objectName='iconBox')
        self.settingsLayout.addRow('Button &Icon', self.iconBox)
        
        self.textBox = QComboBox(self.settingsBox, 
                                       objectName='textBox')
        self.settingsLayout.addRow('Button &Text', self.textBox)
        
        self.buttonStyleBox = QComboBox(self.settingsBox, 
                                      objectName = 'buttonStyleBox')
        self.settingsLayout.addRow('&ToolButtonStyle', self.buttonStyleBox)
        
        self.populateComboBoxes()
        
    def populateComboBoxes(self):
        self.pathBox.addItem(QDir.toNativeSeparators(QDir.homePath()))
        self.pathBox.addItem(QDir.toNativeSeparators(QDir.rootPath()))
        self.pathBox.addItem(QDir.toNativeSeparators(QDir.currentPath()))
        self.pathBox.addItem(QDir.toNativeSeparators(QDir.tempPath()))
        self.onPathChanged(0)
        
        self.buttonStyleBox.addItem('Qt::ToolButtonIconOnly', Qt.ToolButtonIconOnly)
        self.buttonStyleBox.addItem('Qt::ToolButtonTextOnly', Qt.ToolButtonTextOnly)
        self.buttonStyleBox.addItem('Qt::ToolButtonTextBesideIcon', Qt.ToolButtonTextBesideIcon)
        self.buttonStyleBox.addItem('Qt::ToolButtonTextUnderIcon', Qt.ToolButtonTextUnderIcon)
        self.buttonStyleBox.addItem('Qt::ToolButtonFollowStyle', Qt.ToolButtonFollowStyle)
        self.buttonStyleBox.setCurrentIndex(4)
        
        self.iconBox.addItem('(None)', QIcon())
        self.iconBox.addItem('find.png', QIcon(':/test/find.png'))
        self.iconBox.addItem('folder.png', QIcon(':/test/folder.png'))
        self.iconBox.addItem('qtlogo.png', QIcon(':/test/qtlogo.png'))
        
        self.textBox.addItem('(None)', '')
        self.textBox.addItem('Browse', 'Browse')
        self.textBox.addItem('...', '...')
        self.textBox.setCurrentIndex(2)
        
    def retranslateUi(self):
        super().retranslateUi()
        tr = self.trUtf8
        self.setWindowTitle(tr('ColorButton Test'))
        self.settingsLayout.labelForField(self.pathBox).setText(tr('&Path'))
        self.settingsLayout.labelForField(self.iconBox).setText(tr('Button &Icon'))
        self.settingsLayout.labelForField(self.textBox).setText(tr('Button &Text'))
        self.settingsLayout.labelForField(self.buttonStyleBox).setText(tr('&ToolButtonStyle'))
        
        self.buttonStyleBox.setItemText(0, 'Qt::ToolButtonIconOnly')
        self.buttonStyleBox.setItemText(1, 'Qt::ToolButtonTextOnly')
        self.buttonStyleBox.setItemText(2, 'Qt::ToolButtonTextBesideIcon')
        self.buttonStyleBox.setItemText(3, 'Qt::ToolButtonTextUnderIcon')
        self.buttonStyleBox.setItemText(4, 'Qt::ToolButtonFollowStyle')
        
        self.iconBox.setItemText(0, '(None)')
        self.iconBox.setItemText(1, 'find.png')
        self.iconBox.setItemText(2, 'folder.png')
        self.iconBox.setItemText(3, 'qtlogo.png')
        
        self.textBox.setItemText(0, '(None)')
        self.textBox.setItemText(1, 'Browse')
        self.textBox.setItemText(2, '...')

    def connectSignals(self):
        super().connectSignals()
        self.pathBox.currentIndexChanged[int].connect(self.onPathChanged)
        self.iconBox.currentIndexChanged[int].connect(self.onIconChanged)
        self.textBox.currentIndexChanged[int].connect(self.onTextChanged)
        self.buttonStyleBox.currentIndexChanged[int].connect(self.onStyleChanged)
#        self.testWidget.clicked.connect(self.onColorButtonClicked)

    def onPathChanged(self, idx : int):
        self.testWidget.setCurrentPath(self.pathBox.itemText(idx))

    def onIconChanged(self, idx : int):
        self.testWidget.setButtonIcon(self.iconBox.itemData(idx, Qt.UserRole))
        
    def onTextChanged(self, idx : int):
        self.testWidget.setButtonText(self.textBox.itemData(idx, Qt.UserRole))
        
    def onStyleChanged(self, idx : int):
        self.testWidget.setToolButtonStyle(self.buttonStyleBox.itemData(idx, Qt.UserRole))
    
#    def onColorButtonClicked(self):
#        color = QColorDialog.getColor(self.testWidget.color, self)
#        self.testWidget.setColor(color)
#        idx = self.iconBox.findData(color)
#        self.iconBox.blockSignals(True)
#        self.iconBox.setCurrentIndex(idx)
#        self.iconBox.blockSignals(False)
        
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
