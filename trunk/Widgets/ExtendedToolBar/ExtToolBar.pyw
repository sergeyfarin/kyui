from PyQt4.QtCore import Qt, QSize
from PyQt4.QtGui import QIcon, QToolBar, QToolButton

from ExtAction import ExtendedAction, ExtActType

class ExtendedToolBar(QToolBar):
    def __init__(self, 
                 icon : QIcon = None, 
                 title : str = None, 
                 parent : QWidget = None, 
                 iconSize : QSize = None):
        if title:
            super().__init__(title, parent)
        else:
            super().__init__(parent)
        if icon:
            self.setIcon(icon)
        if iconSize:
            self.setIconSize(iconSize)
        else:
            self.setIconSize(QSize(32, 32))
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
            
    def addToolButton(self, act : ExtendedAction = None ) -> QToolButton:
        if not act:
            return None
        actType = act.actionType()
        if actType == ExtActType['Solo']:
            button = super().addAction(act)
        elif actType == ExtActType['Menu']:
            button = super().addAction(act)
            button.setPopupMode(QToolButton.InstantPopup)
        elif actType == ExtActType['Split']:
            button = super().addAction(act)
            button.setPopupMode(QToolButton.MenuButtonPopup)
        else:
            return None
        
        
    def addToolGroup(self, 
                     act : ExtendedAction = None,
                     tg : ToolGroup = None) -> QToolButton:
        if not act or not tg or act.actionType() != ExtActType['ToolGroup']:
            return None
        pass
        
    def addToolWidget(self, 
                      act : ExtendedAction = None, 
                      tw : QWidget = None) -> QToolButton:
        if not act or not tw or act.actionType() != ExtActType['ToolWidget']:
            return None
        pass
