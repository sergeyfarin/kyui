from PyQt4.QtCore import *
from PyQt4.QtGui import *

from DebugBox import DebugBox
from IconSet2 import IconSet, E5Icons
from Widgets.RibbonBar import KyRibbonBar
from Widgets.MenuButton import KyMenuButton

from TestItems.ActionTest import ActionTestClass
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
        
#        self.printIconCacheNames(self.iconCache)
        
    def __setupUi(self) -> None:
        self.__setupDebugDock()
        self.__setupActions()
        self.__setupRibbon()
        self.__setupTreeWidget()
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
        menu.addMenu('File')
        menu.addMenu('View')
        menuButton.setMenu(menu)
        
        ribbonBar.setMenuWidget(menuButton)
        self.setMenuWidget(ribbonBar)
        
        toolbar = ribbonBar.addRibbonTab('Testing')
        toolbar2 = ribbonBar.addRibbonTab('Font')
        
        self.menu = menu
        self.menuButton = menuButton
        self.ribbonBar = ribbonBar
        
    def __setupActions(self) -> None:
        atc = ActionTestClass(None)
        self.actionDict = atc.actionDict()
        font = QFont('Segoe UI', 9, QFont.Normal, False)
        for action in self.actionDict:
            self.actionDict[action].setParent(self)
    
    def __setupTreeWidget(self):
        self.treeWidget = QTreeWidget(self)
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setHeaderLabels(['Filename', 'Dimensions'])
        
        reader = QImageReader()
        iconFiles = self.iconCache.iconNames()
        for filename in iconFiles:
            reader.setFileName(self.iconPath + filename)
            size = strFromQSize(reader.size(), 'wxh')
            item = QTreeWidgetItem(self.treeWidget, [filename, size])
    
    def printIconCacheNames(self, cache):
        icons = cache.iconNames()
        iconStr = ''
        for icon in icons:
            iconStr += '\n' + icon
        qDebug('Icons:' + iconStr)
