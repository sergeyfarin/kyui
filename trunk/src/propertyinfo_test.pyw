#UTF-8
#propertyinfo_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

from Widgets.propertyinfo import ClassPairs, FormattableTypes, FormatQType
from template_test import TemplateDialog

class Dialog(TemplateDialog):
    def __init__(self, parent = None):
        super(QWidget, self).__init__(parent)
        self.setObjectName('dialog')
        self.resize(640, 600)
        
        self.setupUi()
        self.retranslateUi()
        self.connectSignals()
        self.setupClassTree(0)
        
    def setupUi(self):
        super().setupUi()
        
        self.testWidget = None
        
        self.treeWidget = QTreeWidget(self)
        self.treeWidget.setObjectName('treeWidget')
        self.treeWidget.setColumnCount(3)
        self.treeWidget.setColumnWidth(0, 150)
        self.treeWidget.setColumnWidth(1, 150)
        self.treeWidget.setHeaderLabels(['Property', 'Value', 'Type'])
        self.treeWidget.setAlternatingRowColors(True)
        self.layout.insertWidget(0, self.treeWidget)
        
        self.classLabel = QLabel(self.settingsBox)
        self.classLabel.setObjectName('classLabel')
        self.classBox = QComboBox(self.settingsBox)
        self.classBox.setObjectName('classBox')
        for key in ClassPairs.keys():
            self.classBox.addItem(key, ClassPairs[key])
        self.classLabel.setBuddy(self.classBox)
        self.settingsLayout.addRow(self.classLabel, self.classBox)
        
        self.debugBox.setFixedHeight(100)
        
        self.retranslateUi()
        self.connectSignals()
        
    def retranslateUi(self):
        super().retranslateUi()
        self.classLabel.setText('Class &List')
        
    def connectSignals(self):
        super().connectSignals()
        self.classBox.currentIndexChanged[int].connect(self.setupClassTree)
        
    def setupClassTree(self, index):
        self.treeWidget.clear()
        if self.testWidget:
            self.testWidget.setParent(None)
        self.testWidget = self.classBox.itemData(index)(self)
        self.testWidget.hide()
        mObject = self.testWidget.metaObject()
        item = QTreeWidgetItem(self.treeWidget, [mObject.className()])
        self.setupPropertyTree(item, mObject)
        item.setExpanded(True)
        while mObject.superClass():
            mObject = mObject.superClass()
            item = QTreeWidgetItem(None, [mObject.className()])
            self.setupPropertyTree(item, mObject)
            self.treeWidget.insertTopLevelItem(0, item)
            item.setExpanded(True)
        
    def setupPropertyTree(self, rootItem, mObject):
        propItem = QTreeWidgetItem(rootItem, ['Properties'])
        for index in range(mObject.propertyOffset(), mObject.propertyCount()):
            prop = mObject.property(index)
            if (prop.isValid() and prop.isReadable() and prop.isDesignable()
                    and prop.isWritable()):
                value = prop.read(self.testWidget)
                propType = prop.typeName()
                if value == None or isinstance(value, QPyNullVariant):
                    value = ''
                elif prop.isEnumType():
                    enum = prop.enumerator()
                    propType = enum.name()
                    if enum.isFlag():
                        value = enum.valueToKeys(int(value)).data().decode()
                    else:
                        value = enum.valueToKey(int(value))
                elif propType in FormattableTypes:
                    value = FormatQType(value, propType)
                else:
                    value = str(value)
                item = QTreeWidgetItem(propItem, [prop.name(), str(value), propType])
                item.setToolTip(0, self.generatePropToolTip(prop))
        propItem.setExpanded(True)
            
#    def setupEnumList(self, rootItem):
#        enumRootItem = QTreeWidgetItem('Enumerators', rootItem)
#        for index in range(self.mObject.enumeratorOffset(), self.mObject.enumeratorCount()):
#            mEnum = self.mObject.enumerator(index)
#            enumItem = QTreeWidgetItem(mEnum.name(), enumRootItem)

    def formatQType(self, value, propType):
        return value
    
    def generatePropToolTip(self, prop : QMetaProperty) -> str:
        tt = '<b>{}</b><br><br>'.format(prop.name())
        tt += 'Constant:   {}<br>'.format(prop.isConstant())
        tt += 'Designable:   {}<br>'.format(prop.isDesignable(self.testWidget))
        tt += 'Enum:      {}<br>'.format(prop.isEnumType())
        tt += 'Final:      {}<br>'.format(prop.isFinal())
        tt += 'Flag:      {}<br>'.format(prop.isFlagType())
        tt += 'Readable:   {}<br>'.format(prop.isReadable())
        tt += 'Resettable:   {}<br>'.format(prop.isResettable())
        tt += 'Scriptable:   {}<br>'.format(prop.isScriptable(self.testWidget))
        tt += 'Stored:      {}<br>'.format(prop.isStored(self.testWidget))
        tt += 'User:      {}<br>'.format(prop.isUser(self.testWidget))
        tt += 'Valid:      {}<br>'.format(prop.isValid())
        tt += 'Writable:   {}<br>'.format(prop.isWritable())
        return tt
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
