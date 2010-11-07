from PyQt4.QtCore import *
from PyQt4.QtGui import *

from DebugBox import DebugBox
from IconSet import IconSet
from Widgets.RibbonBar import KyRibbonBar
from Widgets.MenuButton import KyMenuButton

class KyMainWindow(QMainWindow):
    def __init__(self, settings):
        QMainWindow.__init__(self)
        self.setObjectName('MainWindow')
        self.resize(1024, 768)
        self.setWindowTitle('Kyui Test Window')
        self.setWindowIcon(IconSet.MiscQtLogo())
        
        self.__setupUi()
        self.__setupRibbon()
        
    def __setupUi(self) -> None:
        debugDock = QDockWidget('Debug Output', self)
        
        debugOutput = DebugBox()
        debugDock.setWidget(debugOutput)
        
        qInstallMsgHandler(debugOutput.postMsg)
        
        self.addDockWidget(Qt.LeftDockWidgetArea, debugDock)
        
        self.setCentralWidget(QWidget())
        
    def __setupRibbon(self):
        ribbonBar = KyRibbonBar(self)
        menuWidget = KyMenuButton(parent=self, text='Menu')
        ribbonBar.setCornerWidget(menuWidget, Qt.TopLeftCorner)
        self.setMenuWidget(ribbonBar)
