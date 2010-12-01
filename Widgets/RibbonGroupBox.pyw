from PyQt4.QtCore import *
from PyQt4.QtGui import *

ActionTypeDict = { \
    'SoloAction' : 10, 
    'MenuAction' : 11, 
    'MenuButton' : 12}

class KyRibbonGroupBox(QGroupBox):
    def __init__(self, 
                 parent : QWidget = None, 
                 title : str = None, 
                 icon : QIcon = None, 
                 lgIconSize : QSize = None, 
                 smIconSize : QSize = None):
        if title:
            super().__init__(title, parent)
            self.__button = QToolButton(self)
            self.__button.setText(title)
            self.__menu = QMenu(title, self.__button)
        else:
            super().__init__(parent)
            self.__button = QToolButton(self)
            self.__menu = QMenu(self.__button)
        if icon:
            self.__button.setIcon(icon)
        if lgIconSize:
            self.__lgIconSize = lgIconSize
            self.__button.setIconSize(lgIconSize)
        else:
            self.__lgIconSize = QSize(32, 32)
            self.__button.setIconSize(self.__lgIconSize)
        
        self.__button.setMenu(self.__menu)
        self.__button.setPopupMode(QToolButton.InstantPopupMode)
        self.__button.setAutoRaise(True)
        self.__button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        
        self.setFlat(True)
        self.setAlignment(Qt.AlignHCenter)
        
        self.__layout = RibbonGroupBoxLayout(self)
        
    def addSoloAction(self, act : QAction = None) -> QToolButton:
        if not act:
            return None
        button = QToolButton(self)
        button.setDefaultAction(act)
