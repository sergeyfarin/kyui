# RibbonActionSet

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class RibbonToolButton(QAction):
    def __init__(self, parent : QWidget = None,
                 text : str = None, 
                 icon : QIcon = None,
                 actionGroup : QActionGroup = None, 
                 checkable : bool = None,
                 checked : bool = None,
                 enabled : bool = None,
                 font : QFont = None,
                 iconText: str = None,
                 iconVisibleInMenu : bool = None,
                 shortcut : QKeySequence = None,
                 shortcuts : list(QKeySequence) = None, 
                 statusTip : str = None,
                 toolTip : str = None,
                 userData : object = None):
        if text:
            if icon:
                super().__init__(icon, text, parent)
            else:
                super().__init__(text, parent)
        if checkable:
            self.setCheckable(checkable)
            if checked:
                self.setChecked(checked)
        if shortcuts:
            self.setShortcuts(shortcut)
        elif shortcut:
            self.setShortcut(shortcut)
        if actionGroup: self.setActionGroup(actionGroup)
        if enabled: self.setEnabled(enabled)
        if font: self.setFont(font)
        if iconText: self.setIconText(iconText)
        if iconVisibleInMenu: self.setIconVisibleInMenu(iconVisibleInMenu)
        if statusTip: self.setStatusTip(statusTip)
        if toolTip: self.setToolTip(toolTip)
        if userData: self.setUserData(userData)
    
class RibbonActionSet(QAction):
    def __init__(self, parent : QWidget = None):
        pass

