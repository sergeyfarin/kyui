from PyQt4.QtCore import *
from PyQt4.QtGui import *

from DebugBox import DebugBox
from Style.StyleFactory import KyStyleFactory
from Widgets.ExtendedToolBar.ToolButton2 import ToolButton
from Widgets.ExtendedToolBar.ToolGroup2 import ToolGroupBox

#class DebugBox(QPlainTextEdit):
#    def __init__(self, parent : QWidget = None, text : str = None):
#        super().__init__(parent)
#        if text:
#            self.setPlainText(text)
#        self.setReadOnly(True)
#        self.setFrameShape(QFrame.StyledPanel)
#        self.setFrameShadow(QFrame.Sunken)
#    
#    def postMsg(self, msgType = QtDebugMsg, text : str = None) -> None:
#        if msgType == QtDebugMsg:
#            self.appendPlainText('Debug: ' + bytes.decode(text))
#        elif msgType == QtWarningMsg:
#            self.appendPlainText('Warning: ' + bytes.decode(text))
#        elif msgType == QtCriticalMsg:
#            print('Critical: ' + bytes.decode(text))
#        elif msgType == QtFatalMsg:
#            print('Fatal: ' + bytes.decode(text))
#        else:
#            print('Unknown Error: ' + bytes.decode(text))

class GenericDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setObjectName('dialog')
        self.setWindowTitle('Test')
        font = QFont('Segoe Ui', 8)
        self.setFont(font)
        QApplication.setStyle(KyStyleFactory.create('Plastique'))
        self.__setupUi()
        
        self.__setupTestItems()
        
    def __setupUi(self):
        self.__layout = QGridLayout(self)
        self.__layout.setSpacing(6)
        
        self.grpBox = ToolGroupBox('Testing Items', self, 
                                   alignment=Qt.AlignHCenter | Qt.AlignTop)
        self.grpBox.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.grpBox.setMinimumSize(100, 100)
        self.__layout.addWidget(self.grpBox, 0, 0, 1, 0)
        
        self.dbgBox = DebugBox(self)
        self.__layout.addWidget(self.dbgBox, 1, 0, 3, 1)
        qInstallMsgHandler(self.dbgBox.postMsg)
        
        self.styleBox = QComboBox(self)
        self.styleBox.addItems(KyStyleFactory.keys())
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
        style = KyStyleFactory.create(self.styleBox.itemText(index))
        QApplication.setStyle(style)
        
    def toggleButtonsRaised(self, state : int):
        for button in self.buttons:
            button.setAutoRaise(True if state == Qt.Checked else False)
            
    def toggleActionsCheckable(self, state : int):
        for act in self.__actions:
            act.setCheckable(True if state == Qt.Checked else False)
            act.setChecked(False)
        
    def __setupTestItems(self):
        layout = QHBoxLayout(self.grpBox)
        
        menu = QMenu()
        menu.addAction('Item1')
        menu.addAction('Item2')
        menu.addAction('Item3')
        
        self.__actions = []
        act = QAction(QIcon('./E5Icons/editPaste.png'), 'Paste', self)
        self.__actions.append(act)
        act2 = QAction(QIcon('./E5Icons/editPaste.png'), 'Test\nButton', self)
        self.__actions.append(act2)
        act3 = QAction(QIcon('./E5Icons/editPaste.png'), 'Test Button', self)
        self.__actions.append(act3)
        
        act.setMenu(menu)
        act3.setMenu(menu)
        
        self.buttons = []
        button = ToolButton(parent=self, 
                            style=Qt.ToolButtonTextUnderIcon, 
                            mode=QToolButton.MenuButtonPopup, 
                            action=act, 
                            size=QSize(32, 32))
        layout.addWidget(button)
        self.buttons.append(button)

        button2 = ToolButton(parent=self, 
                             style=Qt.ToolButtonTextUnderIcon, 
                             size=QSize(32, 32), 
                             action=act2)
        layout.addWidget(button2)
        self.buttons.append(button2)
        
        button3 = ToolButton(parent=self, 
                             style=Qt.ToolButtonTextBesideIcon, 
                             mode=QToolButton.MenuButtonPopup, 
                             size=QSize(16, 16), 
                             action=act3)
        layout.addWidget(button3)
        self.buttons.append(button3)
        
        self.grpBox.setLayout(layout)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = GenericDialog()
    dialog.show()
    sys.exit(app.exec_())
