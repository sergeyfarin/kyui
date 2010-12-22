from PyQt4.QtCore import *
from PyQt4.QtGui import *

from DebugBox import DebugBox
from IconSet2 import IconSet, E5Icons
from Style.StyleFactory import KyStyleFactory
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
        self.setIconSize(QSize(32, 32))
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        
        self.__initActions()
        
        ribbon = KyRibbonBar(self)
        menuButton = KyMenuButton(parent = ribbon, icon = IconSet.Folder(), 
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
        
        self.fileMenu = menu
        
        ribbon.setMenuWidget(menuButton)
        self.setMenuWidget(ribbon)
        
        editTb = ribbon.addRibbonTab('Edit')
        editTb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        editTb.setIconSize(QSize(32, 32))
        editTb.addAction(self.editAddAct)
        editTb.addAction(self.viewPropsAct)
        editTb.addAction(self.styleAct)
        
        styleButton = editTb.widgetForAction(self.styleAct)
        styleButton.setPopupMode(QToolButton.InstantPopup)
        
        self.ribbon = ribbon
        
    def __initActions(self) -> None:
        cache = E5Icons()
        self.fileNewAct = KyAction(parent=self, 
                text='&New', 
                icon=cache.icon('fileNew.png'))
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
        self.editAddAct = KyAction(parent=self, 
                text='&New Item', 
                icon=IconSet.Add(), 
                iconText='New\nItem', 
                trigger=self.addItemDiag, 
                shortcut='Ctrl+N')
        self.viewPropsAct = KyAction(parent=self, 
                text='&Item Properties', 
                icon=cache.icon('zoomTo.png'), 
                iconText='Item\nProperties', 
                shortcut='Ctrl+E', 
                trigger=self.viewProperties)
                
        self.styleMenu = KyMenu('Set Style', self)
        self.styleAct = self.styleMenu.menuAction()
        self.styleAct.setIcon(IconSet.Display())
        self.styleAct.setIconText('Set\nStyle')
        self.styleAct.setShortcut('F3')
        self.styleActGrp = QActionGroup(self)
        self.styleActGrp.setExclusive(True)
        
        for name in KyStyleFactory.keys():
            act = KyAction(parent=self.styleActGrp, 
                           text=KyStyleFactory.formattedKey(name, True), 
                           iconText=KyStyleFactory.formattedKey(name), 
                           checkable=True,
                           trigger=self.styleActTriggered,  
                           userData=name)
            if name == self.style().styleName():
                act.setChecked(True)
            self.styleMenu.addAction(act)
            
#        self.connect(self.styleActGrp, SIGNAL('triggered(QAction)'), self.styleActTriggered)

    def addItemDiag(self):
        pass
    def viewProperties(self):
        pass
    def styleActTriggered(self):
        qDebug('Style Change Triggered')
        name = self.styleActGrp.checkedAction().data()
        if name not in KyStyleFactory.keys():
            qWarning(str.format('{} is not a valid style', name))
            return
        QApplication.setStyle(KyStyleFactory.create(name))
