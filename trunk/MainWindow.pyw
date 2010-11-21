from PyQt4.QtCore import *
from PyQt4.QtGui import *

from DebugBox import DebugBox
from IconSet2 import IconSet, E5Icons
from Widgets.RibbonBar import KyRibbonBar
from Widgets.MenuButton import KyMenuButton

from TestItems.E5InitActions import E5ActionCreator
from Utilities.utilities import strFromQSize


class KyMainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setObjectName('MainWindow')
        self.resize(1024, 768)
        self.setWindowTitle('Kyui Test Window')
        self.setWindowIcon(IconSet.QtLogo())
        self.setFont(QFont('Segoe UI', 9, QFont.Normal, False))
        
        self.iconPath = './E5Icons/'
        self.iconCache = E5Icons(self.iconPath)
        
        self.__setupUi()
        
        self.displayActions()
        
        self.connect(self.fileExitAct, SIGNAL('triggered()'), self.close)
        
    def __setupUi(self) -> None:
        self.__setupDebugDock()
        self.__setupActions()
        self.__setupRibbon()
        
        self.treeWidget = QTreeWidget(self)
        self.treeWidget.setIconSize(QSize(22, 22))
        self.setCentralWidget(self.treeWidget)
        
    def __setupDebugDock(self) -> None:
        debugDock = QDockWidget('Debug Output', self)
        debugOutput = DebugBox(debugDock)
        debugDock.setWidget(debugOutput)
        self.addDockWidget(Qt.LeftDockWidgetArea, debugDock)
        
        qInstallMsgHandler(debugOutput.postMsg)
        
    def __setupRibbon(self) -> None:
        ribbonBar = KyRibbonBar(self)
        menuButton = KyMenuButton(parent = ribbonBar, icon = IconSet.Folder())
        
        menu = QMenu()
        menu.addAction(self.newAct)
        menu.addAction(self.openAct)
        menu.addAction(self.saveAct)
        menu.addAction(self.saveAsAct)
        menu.addAction(self.saveAllAct)
        menu.addAction(self.fileExitAct)
        menuButton.setMenu(menu)
        
        ribbonBar.setMenuWidget(menuButton)
        self.setMenuWidget(ribbonBar)
        
        editTb = ribbonBar.addRibbonTab('Edit')
        editTb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        
        for act in self.clipActGrp.actions():
            editTb.addAction(act)
        for act in self.indentActGrp.actions():
            editTb.addAction(act)
        
        editTb.addAction(self.autoCompleteAct)
        autoButton = editTb.widgetForAction(self.autoCompleteAct)
        autoButton.setPopupMode(QToolButton.MenuButtonPopup)
        
        menu = QMenu(autoButton)
        menu.addAction(self.autoCompleteFromDocAct)
        menu.addAction(self.autoCompleteFromAPIsAct)
        menu.addAction(self.autoCompleteFromAllAct)
        menu.addAction(self.calltipsAct)
        autoButton.setMenu(menu)
        
        bmTb = ribbonBar.addRibbonTab('Bookmarks')
        projTb = ribbonBar.addRibbonTab('Project')
        runTb = ribbonBar.addRibbonTab('Run')
        
        self.menu = menu
        self.menuButton = menuButton
        self.ribbonBar = ribbonBar
        
    def __setupActions(self) -> None:
        E5ActionCreator.initActions(self)
    
    def displayIconCache(self):
        self.treeWidget.clear()
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setHeaderLabels(['Filename', 'Dimensions'])
        self.treeWidget.setColumnWidth(0, 200)
        
        reader = QImageReader()
        iconFiles = self.iconCache.iconNames()
        for filename in iconFiles:
            reader.setFileName(self.iconPath + filename)
            size = strFromQSize(reader.size(), 'wxh')
            item = QTreeWidgetItem(self.treeWidget, [filename, size])
            
    def displayActions(self):
        self.treeWidget.clear()
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setHeaderLabels(['Action', 'IconText'])
        self.treeWidget.setColumnWidth(0, 200)
        for key in self.actionSets:
            keyItem = QTreeWidgetItem(self.treeWidget, [key, ])
            for act in self.actionSets[key]:
                item = QTreeWidgetItem(keyItem, 
                                    [act.objectName(), act.iconText()])
                item.setIcon(0, act.icon())
    
    def printIconCacheNames(self, cache) -> None:
        icons = cache.iconNames()
        iconStr = ''
        for icon in icons:
            iconStr += '\n' + icon
        qDebug('Icons:' + iconStr)
