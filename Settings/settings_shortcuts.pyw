from PyQt4.QtCore import *
from PyQt4.QtGui import *
from iconset import IconSet
from actiontest import ActionTestClass
from settings_default import DefaultSettings

from catcher import KeyPressCatcher

import keypresser_rc
    
#class ToolBarSetting(QObject):
#    _iconSize = QSize(22, 22)
#    _font = QFont('Segoe UI', 9)
#    _style = Qt.ToolButtonIconOnly
#    def __init__(self, parent = None, size = None, font = None, style = None):
#        if parent:
#            self.setParent(parent)
#        if size:
#            self.setIconSize(size)
#        if font:
#            self.setFont(font)
#        if style:
#            self.setStyle(style)
#    
#    def font(self):
#        return self._font    
#    def iconSize(self):
#        return self._iconSize
#    def setFont(self, font):
#        self._font = font
#    def setIconSize(self, size):
#        self._iconSize = size
#    def setStyle(self, style):
#        self._style = style
#    def style(self):
#        return self._style   

class ShortcutsDialog(QDialog):
    def __init__(self, actionList, parent = None):
        QDialog.__init__(self, parent, Qt.Dialog | Qt.Window)
        self.setObjectName("shortcutSettingsDialog")
        self.setWindowModality(Qt.ApplicationModal)
        self.resize(450, 546)
        self.setWindowTitle("Shortcut Settings")
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.setWindowIcon(IconSet.SettingsPreferences())
        font = QFont("Segoe UI", 9, 50, False)
        self.setFont(font)
        self.setSizeGripEnabled(False)
        self.layout = QVBoxLayout(self)
        self.layout.setObjectName("layout")
        self.layout.setContentsMargins(10, 10, 10, 10)
        
        self.__setupShortcutTree(actionList)
        self.__setupKeyPresser()
        self.__setupButtons()
        
        self.actionList = actionList
        
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.buttonRestoreDefaults.clicked.connect(self.restoreDefaults)
        self.treeWidget.itemSelectionChanged.connect(self.onItemSelectionChanged)
        
        self.undoButton.clicked.connect(self.undoShortcutKey)
        self.saveButton.clicked.connect(self.saveShortcutKey)
        self.clearButton.clicked.connect(self.catcher.clear)
        
    def __setupShortcutTree(self, actionList):
        self.treeWidget = QTreeWidget(self)
        self.treeWidget.setSizePolicy(QSizePolicy.Expanding, 
                                      QSizePolicy.Expanding)
        self.treeWidget.setFrameStyle(QFrame.Box | QFrame.Sunken)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setIconSize(QSize(22, 22))
        self.treeWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.treeWidget.setRootIsDecorated(False)
        self.treeWidget.setUniformRowHeights(True)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.treeWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.treeWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        self.itemList = []
        self.shortcutList = []
        for action in actionList:
            name = action.objectName()
            if name != 'actionAbout' and name != 'actionAboutQt':
                item = QTreeWidgetItem(self.treeWidget, 0)
                shortcut = action.shortcut().toString()
                self.shortcutList.append(shortcut)
                item.setData(0, Qt.DisplayRole, action.data())
                item.setData(1, Qt.EditRole, shortcut)
                item.setData(2, Qt.UserRole, action)
                item.setIcon(0, action.icon())
                self.itemList.append(item)
        
        self.treeWidget.header().setDefaultSectionSize(200)
        self.treeWidget.header().setMinimumSectionSize(100)
        self.treeWidget.header().setResizeMode(QHeaderView.ResizeToContents)
        self.treeWidget.headerItem().setText(0, "Setting")
        self.treeWidget.headerItem().setText(1, "Shortcut")
        self.treeWidget.setColumnHidden(2, True)
        self.layout.addWidget(self.treeWidget)
        
    def __setupKeyPresser(self):
        self.shortcutBox = QGroupBox('Change Shortcut Key', self)
        self.shortcutBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.shortcutBox.setMinimumSize(QSize(0, 85))
        self.shortcutBox.setObjectName('shortcutBox')
        
        self.shortcutLayout = QGridLayout(self.shortcutBox)
        self.shortcutLayout.setObjectName('shortcutLayout')
        
        self.catcher = KeyPressCatcher(self.shortcutBox)
        self.catcher.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        self.catcher.setObjectName("catcher")
        self.shortcutLayout.addWidget(self.catcher, 0, 0, 1, 1)
        
        self.clearButton = QPushButton('Clear', self.shortcutBox)
        self.clearButton.setObjectName("clearButton")        
        self.clearButton.setIcon(QIcon(QPixmap(":/keypresser/erase.png")))
        self.clearButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.shortcutLayout.addWidget(self.clearButton, 0, 1, 1, 1)
        
        spacerItem = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.shortcutLayout.addItem(spacerItem, 0, 2, 1, 1)
        
        self.undoButton = QPushButton('Undo', self.shortcutBox)
        self.undoButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.undoButton.setIcon(QIcon(QPixmap(":/keypresser/undo.png")))
        self.undoButton.setObjectName("undoButton")
        self.shortcutLayout.addWidget(self.undoButton, 0, 3, 1, 1)
        
        self.saveButton = QPushButton('Save', self.shortcutBox)
        self.saveButton.setIcon(QIcon(QPixmap(":/keypresser/set.png")))
        self.saveButton.setObjectName("saveButton")
        self.shortcutLayout.addWidget(self.saveButton, 1, 3, 1, 1)
        
        self.setKeyPresserEnabled(False)
        
        self.layout.addWidget(self.shortcutBox)        
        
    def __setupButtons(self):
        self.buttonFrame = QFrame(self)
        self.buttonFrame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.buttonFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonFrame.setFrameShadow(QFrame.Raised)
        self.buttonFrame.setObjectName("buttonFrame")
        
        self.buttonLayout = QHBoxLayout(self.buttonFrame)
        self.buttonLayout.setObjectName("buttonLayout")
        
        self.buttonRestoreDefaults = QPushButton(self.buttonFrame)
        font = font = QFont("Segoe UI", 9, 50, False)
        self.buttonRestoreDefaults.setFont(font)
        self.buttonRestoreDefaults.setAutoDefault(False)
        self.buttonRestoreDefaults.setObjectName("buttonRestoreDefaults")
        self.buttonRestoreDefaults.setToolTip("Restore settings on the current tab to their default values")
        self.buttonRestoreDefaults.setText("Restore Defaults")
        self.buttonRestoreDefaults.setShortcut("Alt+D")
        self.buttonLayout.addWidget(self.buttonRestoreDefaults)

        spacerItem = QSpacerItem(88, 18, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.buttonLayout.addItem(spacerItem)
        
        self.buttonBox = QDialogButtonBox(self.buttonFrame)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply | 
                                          QDialogButtonBox.Cancel|
                                          QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.button(QDialogButtonBox.Apply).setEnabled(False)
        self.buttonLayout.addWidget(self.buttonBox)
        self.layout.addWidget(self.buttonFrame)
    
    def onItemSelectionChanged(self):
        item = self.treeWidget.currentItem()
        self.setKeyPresserEnabled(True)
        self.catcher.setText(item.data(1, Qt.EditRole))
        
    def restoreDefaults(self):
        settings = DefaultSettings()
        settings.setupDefaults()
        settings.beginGroup('shortcuts')
        for item in self.itemList:
            action = item.data(2, Qt.UserRole)
            shortcut = settings.value(action.objectName())
            item.setData(1, Qt.EditRole, shortcut)
        settings.endGroup()
        
    def undoShortcutKey(self):
        item = self.treeWidget.currentItem()
        shortcut = item.data(2, Qt.UserRole).shortcut().toString()
        self.catcher.setText(shortcut)
        
    def saveShortcutKey(self):
        item = self.treeWidget.currentItem()
        item.setData(1, Qt.EditRole, self.catcher.text())
        self.catcher.clear()
        self.setKeyPresserEnabled(False)
        
    def setKeyPresserEnabled(self, state = True):
        self.shortcutBox.setEnabled(state)
        self.shortcutBox.changeEvent(QEvent(QEvent.EnabledChange))
        
    def accept(self):
        for item in self.itemList:
            shortcut = item.data(1, Qt.EditRole)
            action = item.data(2, Qt.UserRole)
            action.setShortcut(shortcut)
        super().accept()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    actionClass = ActionTestClass()
    ui = ShortcutsDialog(actionClass.getActionList())
    ui.show()
    sys.exit(app.exec_())
