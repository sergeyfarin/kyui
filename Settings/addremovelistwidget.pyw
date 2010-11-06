#itempickerlist

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from iconset import SettingsIcons

class AddRemoveListWidget(QWidget):
    sourceItemSelected = pyqtSignal()
    def __init__(self, parent = None):
        super().__init__(parent)
        self.__setupUi()
        self.retranslateUi()
        
    def __setupUi(self):
        layout = QGridLayout(self)
        layout.setObjectName('layout')
        
        sourceLabel = QLabel(self)
        sourceLabel.setObjectName('sourceLabel')
        sourceLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        layout.addWidget(sourceLabel, 0, 0)
        
        sourceList = QListWidget(self)
        sourceList.setFrameShape(QFrame.Box)
        sourceList.setObjectName('sourceList')
        layout.addWidget(sourceList, 1, 0)
        
        buttonLayout = QVBoxLayout()
        buttonLayout.setSpacing(1)
        buttonLayout.setObjectName('buttonLayout')
        
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        
        spacerItem = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)
        buttonLayout.addItem(spacerItem)
        
        addButton = QPushButton(self)
        addButton.setSizePolicy(sizePolicy)
        addButton.setIcon(SettingsIcons.AddItem())
        addButton.setObjectName('addButton')
        addButton.setEnabled(False)
        buttonLayout.addWidget(addButton)
        
        removeButton = QPushButton(self)
        removeButton.setSizePolicy(sizePolicy)
        removeButton.setIcon(SettingsIcons.RemoveItem())
        removeButton.setObjectName('removeButton')
        removeButton.setEnabled(False)
        buttonLayout.addWidget(removeButton)
        
        spacerItem = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)
        buttonLayout.addItem(spacerItem)
        
        upButton = QPushButton(self)
        upButton.setSizePolicy(sizePolicy)
        upButton.setIcon(SettingsIcons.MoveUp())
        upButton.setObjectName('upButton')
        upButton.setEnabled(False)
        buttonLayout.addWidget(upButton)
        
        downButton = QPushButton(self)
        downButton.setSizePolicy(sizePolicy)
        downButton.setIcon(SettingsIcons.MoveDown())
        downButton.setObjectName('downButton')
        downButton.setEnabled(False)
        buttonLayout.addWidget(downButton)
        
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        buttonLayout.addItem(spacerItem)
        
        layout.addLayout(buttonLayout, 0, 1, -1, 1)
        destLabel = QLabel(self)
        destLabel.setObjectName('destLabel')
        
        destLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        layout.addWidget(destLabel, 0, 2)
        
        destList = QListWidget(self)
        destList.setFrameShape(QFrame.Box)
        destList.setObjectName('destList')
        layout.addWidget(destList, 1, 2)
        
        sourceLabel.setBuddy(sourceList)
        destLabel.setBuddy(destList)
        
        self.setLayout(layout)
        
        self.__layout = layout
        self.__buttonLayout = buttonLayout
        self.__sourceLabel = sourceLabel
        self.__sourceList = sourceList
        self.__destLabel = destLabel
        self.__destList = destList
        self.__addButton = addButton
        self.__removeButton = removeButton
        self.__upButton = upButton
        self.__downButton = downButton
        
        self.__widgets = {}
        self.__widgets['destLabel'] = destLabel
        self.__widgets['destList'] = destList
        self.__widgets['sourceLabel'] = sourceLabel
        self.__widgets['sourceList'] = sourceList
        self.__widgets['addButton'] = addButton
        self.__widgets['removeButton'] = removeButton
        self.__widgets['upButton'] = upButton
        self.__widgets['downButton'] = downButton
        
    def retranslateUi(self):
        self.__sourceLabel.setText(self.trUtf8('Available Items'))
        self.__destLabel.setText(self.trUtf8('Added Items'))
        self.__addButton.setToolTip(self.trUtf8('Add item'))
        self.__removeButton.setToolTip(self.trUtf8('Remove item'))
        self.__upButton.setToolTip(self.trUtf8('Move item up'))
        self.__downButton.setToolTip(self.trUtf8('Move item down'))
        
    def addItem(self, itemorlabel):
        self.__sourceList.addItem(itemorlabel)
    
    def addItems(self, labels):
        self.__sourceList.addItems(labels)
        
    def clear(self):
        self.__sourceList.clear()
        self.__destList.clear()
    
    def setDestLabelText(self, text = ''):
        self.__destLabel.setText(text)
        
    def setSourceLabelText(self, text = ''):
        self.__sourceLabel.setText(text)
        
    def setToolTip(self, widgetname, text = ''):
        if widgetname in self.__widgets:
            self.__widgets[widgetname].setToolTip(text)
        
    def button(self, buttonName = ''):
        if buttonName == 'add':
            return self.__addButton
        elif buttonName == 'remove':
            return self.__removeButton
        elif buttonName == 'up':
            return self.__upButton
        elif buttonName == 'down':
            return self.__downButton
        else:
            return None    
    
    def destWidget(self):
        return self.__destList
    
    def destLabel(self):
        return self.__destLabel
        
    def layout(self):
        return self.__layout
        
    def sourceWidget(self):
        return self.__sourceList
        
    def sourceLabel(self):
        return self.__sourceLabel
        
    def widget(self, widgetname = ''):
        if widgetname in self__widgets:
            return self.__widgets[widgetname]

class GenericDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setObjectName('dialog')
        
        self.__setupUi()
        
    def __setupUi(self):
        arlw = AddRemoveListWidget(self)
        arlw.setGeometry(QRect(0, 0, 421, 291))
        arlw.setObjectName('AddRemoveListWidget')
        
        self.arlw = arlw

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = GenericDialog()
    dialog.show()
    sys.exit(app.exec_())
