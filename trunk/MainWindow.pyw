from PyQt4.QtCore import *
from PyQt4.QtGui import *

from DebugBox import DebugBox
from IconSet2 import IconSet
from Widgets.RibbonBar import KyRibbonBar
from Widgets.MenuButton import KyMenuButton

from TestItems.ActionTest import ActionTestClass


class KyMainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setObjectName('MainWindow')
        self.resize(1024, 768)
        self.setWindowTitle('Kyui Test Window')
        self.setWindowIcon(IconSet.QtLogo())
        self.setFont(QFont('Segoe UI', 9, QFont.Normal, False))
        
        self.__setupUi()
        self.__setupDebugDock()
        self.__setupActions()
        self.__setupRibbon()
        
        self.printDebugData()
        
        
    def __setupUi(self) -> None:
        self.setCentralWidget(QWidget())
        
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
            self.actionDict[action].setFont(font)

    def printDebugData(self):
        tabBar = self.ribbonBar.tabBar()
        
        def formatQSize(size):
            return str.format('({}, {})', size.width(), size.height())
        
        printableSize = formatQSize(tabBar.sizeHint())
        qDebug('SizeHint = ' + printableSize)
        
        printableSize = formatQSize(tabBar.minimumSizeHint())
        qDebug('MinimumSizeHint = ' + printableSize)
        
        printableSize = formatQSize(tabBar.tabSizeHint(0))
        qDebug('Tab0 SizeHint = ' + printableSize)
        
        printableSize = formatQSize(tabBar.tabSizeHint(1))
        qDebug('Tab1 SizeHint = ' + printableSize)
