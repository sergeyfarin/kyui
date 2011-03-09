#UTF-8
#varientedit_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

from Widgets.varientedit import *
from template_test import TemplateDialog

class Dialog(TemplateDialog):
    def __init__(self, parent = None):
        super(QWidget, self).__init__(parent)
        self.setObjectName('dialog')
        
        self.setupUi()
        self.retranslateUi()
        self.connectSignals()
        self.setupClassList()
        
    def setupUi(self):
        super().setupUi()
                
        self.treeWidget = QTreeWidget(self)
        self.treeWidget.setObjectName('treeWidget')
        self.layout.insertWidget(0, self.treeWidget)
        
        self.classLabel = QLabel(self.settingsBox)
        self.classLabel.setObjectName('classLabel')
        self.classBox = QComboBox(self.settingsBox)
        self.classBox.setObjectName('classBox')
        self.settingsLayout.addRow(self.classLabel, self.classBox)

        
        self.enumLabel = QLabel(self)
        self.enumLabel.setObjectName('enumLabel')
        self.enumBox = QComboBox(self.settingsBox)
        self.enumBox.setObjectName('enumBox')
        self.enumLabel.setBuddy(self.enumBox)
        self.settingsLayout.addRow(self.enumLabel, self.enumBox)
        
        self.propertyLabel = QLabel(self.settingsBox)
        self.propertyLabel.setObjectName('propertyLable')
        self.propertyBox = QComboBox(self.settingsBox)
        self.propertyBox.setObjectName('propertyBox')
        self.propertyLabel.setBuddy(self.propertyBox)
        self.settingsLayout.addRow(self.propertyLabel, self.propertyBox)
        
        self.retranslateUi()
        self.connectSignals()
        
    def retranslateUi(self):
        super().retranslateUi()
        self.classLabel.setText('Class &List')
        self.enumLabel.setText('&Enums')
        self.propertyLabel.setText('&Properties')
        
    def connectSignals(self):
        super().connectSignals()
        
    def setupClassList(self):
        for key in ClassPairs.keys():
            self.classBox.addItem(key, ClassPairs[key])
        self.mObject = self.classBox.itemData(self.classBox.currentIndex())(None).metaObject()
        item = QTreeWidgetItem(self.mObject.className(), self.treeWidget)
        self.setupEnumList(item)
            
    def setupEnumList(self, rootItem):
        enumRootItem = QTreeWidgetItem('Enumerators', rootItem)
        for index in range(self.mObject.enumeratorOffset(), self.mObject.enumeratorCount()):
            mEnum = self.mObject.enumerator(index)
            enumItem = QTreeWidgetItem(mEnum.name(), enumRootItem)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
