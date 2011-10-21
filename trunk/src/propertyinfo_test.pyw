#UTF-8
#propertyinfo_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

from Widgets.propertyinfo import FormattableTypes, FormatQType, CreatePropertyItem
from Widgets.colorbutton import ColorButton
from Widgets.colorpicker import ColorPicker

from template_test import TemplateDialog

ClassPairs = {'QWidget' : QWidget, 
              'QPushButton' : QPushButton, 
              'QToolButton' : QToolButton, 
              'QDialog' : QDialog, 
              'QMenu' : QMenu, 
              'QComboBox' : QComboBox, 
              'QFrame' : QFrame, 
              'QSpinBox' : QSpinBox, 
              'ColorButton' : ColorButton, 
              'ColorPicker' : ColorPicker}

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
        
        self.colorButton = ColorButton(self)
        self.colorButton.hide()
        
        self.colorPicker = ColorPicker(self)
        self.colorPicker.hide()
        
        self.testWidget = None
        
        self.treeWidget = QTreeWidget(self, objectName='treeWidget')
        self.treeWidget.setColumnCount(3)
        self.treeWidget.setHeaderLabels(['Property', 'Value', 'Type'])
        self.treeWidget.setColumnWidth(0, 150)
        self.treeWidget.setColumnWidth(1, 150)
        self.treeWidget.setAlternatingRowColors(True)
        self.layout.insertWidget(0, self.treeWidget)
        
        self.classLabel = QLabel(self.settingsBox)
        self.classLabel.setObjectName('classLabel')
        self.classBox = QComboBox(self.settingsBox)
        self.classBox.setObjectName('classBox')
        self.classBox.addItem('ColorButton', self.colorButton)
        self.classBox.addItem('ColorPicker', self.colorPicker)
        self.classBox.addItem('ComboBox', self.classBox)
        self.classBox.addItem('DebugBox', self.debugBox)
        self.classBox.addItem('Dialog', self)
        self.classBox.addItem('Label', self.classLabel)
        self.classBox.addItem('PushButton', self.closeButton)
        self.classBox.addItem('TreeWidget', self.treeWidget)
        
        self.classLabel.setBuddy(self.classBox)
        self.settingsLayout.addRow(self.classLabel, self.classBox)
        
        self.debugBox.setFixedHeight(100)
        
    def retranslateUi(self):
        super().retranslateUi()
        
        self.setWindowTitle(self.trUtf8('PropertyInfo Test'))
        self.classLabel.setText('Class &List')
        
    def connectSignals(self):
        super().connectSignals()
        self.classBox.currentIndexChanged[int].connect(self.setupClassTree)
        
    def setupClassTree(self, index):
        self.treeWidget.clear()
        self.testWidget = self.classBox.itemData(index)
        mObject = self.testWidget.metaObject()
        propRootItem = QTreeWidgetItem(self.treeWidget, ['Properties'])
        signalRootItem = QTreeWidgetItem(self.treeWidget, ['Signals'])
        slotRootItem = QTreeWidgetItem(self.treeWidget, ['Slots'])
        while mObject.superClass():
            propClassItem = QTreeWidgetItem(None, [mObject.className()])
            signalClassItem = QTreeWidgetItem(None, [mObject.className()])
            slotClassItem = QTreeWidgetItem(None, [mObject.className()])
            self.setupPropertyTree(propClassItem, mObject)
            if propClassItem.childCount() != 0:
                propRootItem.insertChild(0, propClassItem)
                propClassItem.setExpanded(True)
            self.setupSignalSlotTree(signalClassItem, slotClassItem, mObject)
            if signalClassItem.childCount() != 0:
                signalRootItem.insertChild(0, signalClassItem)
                signalClassItem.setExpanded(True)
            if slotClassItem.childCount() != 0:
                slotRootItem.insertChild(0, slotClassItem)
                slotClassItem.setExpanded(True)
            mObject = mObject.superClass()
        
    def setupPropertyTree(self, propItem, mObject):
        for index in range(mObject.propertyOffset(), mObject.propertyCount()):
            prop = mObject.property(index)
            CreatePropertyItem(prop, propItem, self.testWidget)
        propItem.setExpanded(True)
    
    def setupSignalSlotTree(self, signalItem, slotItem, mObject):
        def accessToStr(access):
            if access == QMetaMethod.Public:
                return 'Public'
            elif access == QMetaMethod.Protected:
                return 'Protected'
            else:
                return 'Private'
        for index in range(mObject.methodOffset(), mObject.methodCount()):
            method = mObject.method(index)
            if method.methodType() == QMetaMethod.Signal:
                item = QTreeWidgetItem(signalItem, 
                                       [str(method.signature()), 
                                       '', 
                                       accessToStr(method.access())])
            elif method.methodType() == QMetaMethod.Slot:
                item = QTreeWidgetItem(slotItem, 
                                       [str(method.signature()), 
                                       '',
                                       accessToStr(method.access())])
        signalItem.setExpanded(True)
        slotItem.setExpanded(True)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
