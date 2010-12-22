from PyQt4.QtCore import *
from PyQt4.QtGui import *

from DebugBox import DebugBox
from IconSet2 import IconSet, E5Icons
from Widgets.RibbonBar import KyRibbonBar
from Widgets.Action import KyAction
from Widgets.MenuButton import KyMenuButton
from Widgets.ExtendedToolBar.Menu import KyMenu

class KyMainWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.resize(1024, 768)
        self.setWindowTitle('KyWindowTest')
        self.setWindowIcon(IconSet.QtLogo())
        self.setFont(QFont('Segoe UI', 9, QFont.Normal, False))
        
        self.setupUi()
        self.installDebugHandler()
        
        qDebug('Setup completed.')

    def installDebugHandler(self):
        self.debugDock = QDockWidget('Debug', self)
        self.debugOutput = DebugBox(self.debugDock)
        self.debugDock.setWidget(self.debugOutput)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.debugDock)
        
        qInstallMsgHandler(self.debugOutput.postMsg)
        
    def setupUi(self) -> None:
        self.__initActions()
        
        ribbonBar = KyRibbonBar(self)
        menuButton = KyMenuButton(parent = ribbonBar, icon = IconSet.Folder(), 
                                  text = 'File')
        
        menu = KyMenu()
        menu.addSeparator().setText('Files')
        menu.addAction(self.fileNewAct)
        menu.addAction(self.fileOpenAct)
        menu.addSeparator().setText('Save')
        menu.addAction(self.fileSaveAct)
        menu.addAction(self.fileSaveAsAct)
        menu.addAction(self.fileSaveAllAct)
        menu.addSeparator()
        menu.addAction(self.fileExitAct)
        menuButton.setMenu(menu)
        
        ribbonBar.setMenuWidget(menuButton)
        self.setMenuWidget(ribbonBar)
        
        editTb = ribbonBar.addRibbonTab('Edit')
        editTb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        
    def __initActions(self) -> None:
        cache = E5Icons()
        self.fileNewAct = KyAction(parent=self, 
                text='&New', 
                icon=cache.icon('fileNew.png'), 
                shortcut='Ctrl+N')
        self.fileOpenAct = KyAction(parent=self, 
                text='&Open', 
                icon=cache.icon('fileOpen.png'), 
                shortcut='Ctrl+O')
        self.fileCloseAct = KyAction(parent=self, 
                text='&Close', 
                icon=cache.icon('fileClose.png'), 
                shortcut='Ctrl+W')
        self.fileSaveAct = KyAction(parent=self, 
                text='&Save', 
                icon=cache.icon('fileSave.png'), 
                shortcut='Ctrl+S')
        self.fileSaveAsAct = KyAction(parent=self, 
                text='Save &As', 
                icon=cache.icon('fileSaveAs.png'), 
                shortcut='Ctrl+Shift+S')
        self.fileSaveAllAct = KyAction(parent=self, 
                text='Save A&ll', 
                icon=cache.icon('fileSaveAll.png'), 
                shortcut='Ctrl+Alt+S')
        self.fileExitAct = KyAction(parent=self,
                text='Exit', 
                icon=cache.icon('fileExit.png'), 
                trigger=self.close, 
                shortcut='Ctrl+Q')
