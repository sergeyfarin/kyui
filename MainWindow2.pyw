from PyQt4.QtCore import *
from PyQt4.QtGui import *

from IconSet2 import IconSet
from DebugBox import DebugBox

from Widgets.ButtonBox2 import *
from TestItems.ActionTest import ActionTestClass

class KyMainWindow(QMainWindow):
    
    def __init__(self, parent = None):
        super().__init__(parent)
        self.resize(1024, 768)
        self.setWindowTitle('KyWindowTest')
        self.setWindowIcon(IconSet.QtLogo())
        self.setFont(QFont('Segoe UI', 9, QFont.Normal, False))
        
        self.setupUi()
        self.installDebugHandler()
        self.setupActions()
        
        self.setupToolButtons()
        
        qDebug('Setup completed.')
        
    def setupUi(self) -> None:
        tabWidget = QTabWidget(self)
        tabWidget.setObjectName('tabWidget')
        tabWidget.setFixedHeight(115)
        self.setMenuWidget(tabWidget)
        
        #Menu setup
        menuButton = QToolButton()
        menuButton.setObjectName('menuButton')
        menuButton.setIcon(IconSet.Folder())
        menuButton.setIconSize(QSize(22, 22))
        menuButton.setText('Menu')
        menuButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        menuButton.setPopupMode(QToolButton.InstantPopup)
        
        menu = QMenu()
        fileMenu = menu.addMenu('File')
        viewMenu = menu.addMenu('View')
        menuButton.setMenu(menu)
        
        menuToolBar = QToolBar()
        menuToolBar.addWidget(menuButton)
        
        #Add tabs
        tabWidget.addTab(QWidget(tabWidget), 'Test')
        tabWidget.addTab(QFrame(tabWidget), 'Test2')
        tabWidget.setIconSize(QSize(22, 22))
        tabWidget.setCornerWidget(menuToolBar, Qt.TopLeftCorner)
        
        self.setCentralWidget(QWidget())
        
        #Save variable names
        self.menuToolBar = menuToolBar
        self.tabWidget = tabWidget
        self.menuButton = menuButton
        
    def installDebugHandler(self):
        self.debugOutput = DebugBox()
        
        debugDock = QDockWidget('Debug')
        debugDock.setWidget(self.debugOutput)
        self.addDockWidget(Qt.LeftDockWidgetArea, debugDock)
        
        qInstallMsgHandler(self.debugOutput.postMsg)
        
    def setupActions(self):
        atc = ActionTestClass(None)
        self.actionDict = atc.actionDict()
        font = QFont('Segoe UI', 9, QFont.Normal, False)
        for action in self.actionDict:
            self.actionDict[action].setParent(self)
            self.actionDict[action].setFont(font)
            
    def setupToolButtons(self):
        actions = self.actionDict
        tab = self.tabWidget.widget(0)
        
        tabLayout = QHBoxLayout()
#        tabLayout.setSizeConstraint(QLayout.SetFixedSize)
        
        viewButtons = ButtonBox(tab)
        viewButtons.setObjectName('viewButtons')
        viewButtons.addAction(actions['ZoomIn'])
        viewButtons.addAction(actions['ZoomOut'])
        viewButtons.addAction(actions['ActualSize'])
        viewButtons.setIconSize(QSize(22, 22))
        
        tab.setLayout(tabLayout)
        

