from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Style.StyleFactory import KyStyleFactory
from Widgets.ExtendedToolBar.ToolButton2 import ToolButton
from Widgets.ExtendedToolBar.ToolGroup2 import ToolGroupBox
from Widgets.Action import KyAction
from Widgets.ExtendedToolBar.Menu import KyMenu

class DebugBox(QPlainTextEdit):
    def __init__(self, parent : QWidget = None, text : str = None):
        super().__init__(parent)
        if text:
            self.setPlainText(text)
        self.setReadOnly(True)
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Sunken)
    
    def postMsg(self, msgType = QtDebugMsg, text : str = None) -> None:
        if msgType == QtDebugMsg:
            self.appendPlainText('Debug: ' + bytes.decode(text))
        elif msgType == QtWarningMsg:
            self.appendPlainText('Warning: ' + bytes.decode(text))
        elif msgType == QtCriticalMsg:
            print('Critical: ' + bytes.decode(text))
        elif msgType == QtFatalMsg:
            print('Fatal: ' + bytes.decode(text))
        else:
            print('Unknown Error: ' + bytes.decode(text))

class GenericDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setObjectName('dialog')
        self.setWindowTitle('Test')
        font = QFont('Segoe Ui', 8)
        self.setFont(font)
        self.__styleName = 'Plastique'
        QApplication.setStyle(KyStyleFactory.create(self.__styleName))
        self.__setupUi()
        
        self.__setupTestItems()
        
    def __setupUi(self):
        self.__layout = QGridLayout(self)
        self.__layout.setSpacing(6)
        
        self.grpBox = ToolGroupBox('Testing Items', self, 
                                   alignment=Qt.AlignHCenter | Qt.AlignBottom)
        self.grpBox.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.grpBox.setMinimumSize(100, 150)
        self.__layout.addWidget(self.grpBox, 0, 0, 1, 0)
        
        self.dbgBox = DebugBox(self)
        self.__layout.addWidget(self.dbgBox, 1, 0, 3, 1)
        qInstallMsgHandler(self.dbgBox.postMsg)
        
        self.styleBox = QComboBox(self)
        self.styleBox.addItems(KyStyleFactory.keys())
        self.styleBox.setCurrentIndex(0)
        self.connect(self.styleBox, SIGNAL('currentIndexChanged(int)'), self.changeStyle)
        self.__layout.addWidget(self.styleBox, 1, 1)
        
        self.raiseBox = QCheckBox('&Autoraise', self)
        self.connect(self.raiseBox, SIGNAL('stateChanged(int)'), self.toggleButtonsRaised)
        self.__layout.addWidget(self.raiseBox, 2, 1)
        
        self.checkableBox = QCheckBox('&Checkable', self)
        self.connect(self.raiseBox, SIGNAL('stateChanged(int)'), self.toggleActionsCheckable)
        self.__layout.addWidget(self.checkableBox, 3, 1)
        
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok,
                                          Qt.Horizontal, self)
        self.__layout.addWidget(self.buttonBox, 4, 1, 1, 1)
        self.buttonBox.accepted.connect(self.accept)
        
    def changeStyle(self, index):
        self.__styleName = self.styleBox.itemText(index)
        style = KyStyleFactory.create(self.__styleName)
        QApplication.setStyle(style)
        
    def toggleButtonsRaised(self, state : int):
        for button in self.buttons:
            button.setAutoRaise(True if state == Qt.Checked else False)
            
    def toggleActionsCheckable(self, state : int):
        for act in self.actions():
            act.setCheckable(True if state == Qt.Checked else False)
            act.setChecked(False)
        for button in self.buttons:
            button.update()
        
    def __setupTestItems(self):
        layout = QHBoxLayout(self.grpBox)
        self.grpBox.setContentsMargins(0, 0, 0, 0)
        
        menu = KyMenu()
        menu.setTearOffEnabled(True)
        saveAsAct = KyAction(parent=menu, 
                       icon=QIcon('./E5Icons/fileSaveAs.png'), 
                       text='Save &As', 
                       shortcut='Ctrl+Shift+S')
        menu.addAction(saveAsAct)
        menu.addAction(QIcon('./E5Icons/fileSaveAll.png'), 'Save A&ll')
        menu.addAction(QIcon('./E5Icons/fileSaveToProject.png'), 'Save &To Project').setDisabled(True)
        checkableAct = KyAction(parent=menu, 
                                text='Checkable Item', 
                                shortcut='Ctrl+Alt+Shift+L', 
                                checkable=True)
        menu.addSeparator().setText('Testing')
        menu.addAction(checkableAct)
        
        submenu = menu.addMenu('SubMenu')
        submenu.addAction('Test1')
        submenu.addAction('Test2')
        submenu.addAction('Test3')
#        subMenuAct = KyAction(parent=menu, 
#                              text='Submenu', 
#                              menu=submenu)
        
        act = QAction(QIcon('./E5Icons/fileSave.png'), 'Save\nButton', self)
        self.addAction(act)
        act2 = QAction(QIcon('./E5Icons/fileSave.png'), 'Instant', self)
        self.addAction(act2)
        act3 = QAction(QIcon('./E5Icons/fileSave.png'), 'Horizontal', self)
        self.addAction(act3)
        
        act.setMenu(menu)
        act2.setMenu(menu)
        act3.setMenu(menu)
        self.buttons = []
        button = ToolButton(parent=self, 
                            style=Qt.ToolButtonTextUnderIcon, 
                            mode=QToolButton.DelayedPopup, 
                            action=act, 
                            size=QSize(32, 32))
        layout.addWidget(button)
        self.buttons.append(button)

        self.button2 = ToolButton(parent=self, 
                             style=Qt.ToolButtonTextUnderIcon, 
                             mode=QToolButton.InstantPopup, 
                             size=QSize(32, 32), 
                             action=act2)
        layout.addWidget(self.button2)
        self.buttons.append(self.button2)
#        self.button2.setStyle(QStyleFactory.create(self.__styleName))
        
        button3 = ToolButton(parent=self, 
                             style=Qt.ToolButtonTextBesideIcon, 
                             mode=QToolButton.MenuButtonPopup, 
                             size=QSize(16, 16), 
                             action=act3)
        layout.addWidget(button3)
        self.buttons.append(button3)
        
        self.grpBox.setLayout(layout)
#        font = QFont('Segoe UI Light', 8)
#        for btn in self.buttons:
#            btn.setFont(font)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = GenericDialog()
    dialog.show()
    sys.exit(app.exec_())
