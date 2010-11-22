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
                 iconSize : QSize = None):
        if title:
            super().__init__(title, parent)
            self.__tb = QToolButton(self)
            self.__tb.setText(title)
            self.__menu = QMenu(title, self.__tb)
        else:
            super().__init__(parent)
            self.__tb = QToolButton(self)
            self.__menu = QMenu(self.__tb)
        if icon:
            self.__tb.setIcon(icon)
        if iconSize:
            self.__tb.setIconSize(iconSize)
            self.__iconSize = QSize(iconSize)
        
        self.__tb.setMenu(self.__menu)
        self.__tb.setPopupMode(QToolButton.InstantPopupMode)
        self.__tb.setAutoRaise(True)
        self.__tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        
        self.setFlat(True)
        self.setAlignment(Qt.AlignHCenter)
        
        self.__layout = QGridLayout(self)
        self.__layout.setSpacing(2)
        
    def addSoloAction(self, act : QAction = None) -> QToolButton:
        if not act:
            return None
        tb = QToolButton(self)
        tb.setDefaultAction(act)
        tb.setText(act.iconText())
        tb.setIcon(act.icon())
        tb.setToolTip(act.toolTip())
        tb.setWhatsThis(act.whatsThis())
