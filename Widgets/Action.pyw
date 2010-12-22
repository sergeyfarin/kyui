# RibbonActionSet

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class KyAction(QAction):
    def __init__(self,
                 parent : QWidget = None,
                 text : str = None, 
                 icon : QIcon = None,
                 actionGroup : QActionGroup = None,
                 menu : QMenu = None, 
                 checkable : bool = None,
                 checked : bool = None,
                 enabled : bool = None,
                 font : QFont = None,
                 iconText: str = None,
                 iconVisibleInMenu : bool = None,
                 objectName : str = None, 
                 shortcut : QKeySequence = None,
                 shortcut2 : QKeySequence = None, 
                 statusTip : str = None,
                 trigger : pyqtSignal = None, 
                 toolTip : str = None,
                 userData = None, 
                 whatsThis : str = None):
        if actionGroup:
            parent = actionGroup
        if text:
            if icon:
                super().__init__(icon, text, parent)
            else:
                super().__init__(text, parent)
        if checkable:
            self.setCheckable(checkable)
            if checked:
                self.setChecked(checked)
        if shortcut:
            if not shortcut2:
                self.setShortcut(shortcut)
            else:
                self.setShortcuts((shortcut, shortcut2))
        if actionGroup: self.setActionGroup(actionGroup)
        if enabled: self.setEnabled(enabled)
        if font: self.setFont(font)
        if iconText: self.setIconText(iconText)
        if iconVisibleInMenu: self.setIconVisibleInMenu(iconVisibleInMenu)
        if objectName : self.setObjectName(objectName)
        if statusTip: self.setStatusTip(statusTip)
        if toolTip: self.setToolTip(toolTip)
        if trigger:
            self.connect(self, SIGNAL('triggered()'), trigger)
        if userData: self.setData(userData)
        if whatsThis: self.setWhatsThis(whatsThis)
        
        if menu: menu.addAction(self)
