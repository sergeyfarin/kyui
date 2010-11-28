# RibbonActionSet

from PyQt4 import QtCore
from PyQt4.QtGui import QAction

class PyAction(QAction):
    def __init__(self,
                 ###
                 # Set either parent or actionGroup. The parent will be set to 
                 # actionGroup if one is provided and parent will be ignored
                 ###
                 parent : QWidget = None,
                 actionGroup : QActionGroup = None,
                 
                 ###
                 # Standard __init__ args
                 ###
                 text : str = None, 
                 icon : QIcon = None,
                 
                 ###
                 # All of these keyword arguments are syntactic sugar
                 ###
                 # Checked will be ignored if checkable is not set
                 checkable : bool = None,
                 checked : bool = None, 
                 iconVisibleInMenu : bool = None,
                 font : QFont = None,
                 enabled : bool = None,
                 iconText: str = None,
                 menu : QMenu = None, 
                 objectName : str = None, 
                 receiver : pyqtSlot = None, 
                 # shortcut2 will be ignored if shortcut is not set
                 shortcut : QKeySequence = None,
                 shortcut2 : QKeySequence = None,
                 statusTip : str = None,
                 toolTip : str = None,
                 userData = None, 
                 whatsThis : str = None):
        if actionGroup:
            parent = actionGroup
            self.setActionGroup(actionGroup)
        if text:
            if icon:
                super().__init__(icon, text, parent)
            else:
                super().__init__(text, parent)
        if shortcut:
            if not shortcut2: # Check if there is more than one shortcutkey
                self.setShortcut(shortcut)
            else:
                self.setShortcuts((shortcut, shortcut2))
        
        if menu:
            self.setMenu(menu)
        
        if checkable:
            self.setCheckable(checkable)
            if checked:
                self.setChecked(checked)
        if enabled: self.setEnabled(enabled)
        if font: self.setFont(font)
        if iconText: self.setIconText(iconText)
        if iconVisibleInMenu: self.setIconVisibleInMenu(iconVisibleInMenu)
        if objectName : self.setObjectName(objectName)
        if receiver: self.connect(self, QtCore.SIGNAL('triggered()'), receiver)
        if statusTip: self.setStatusTip(statusTip)
        if toolTip: self.setToolTip(toolTip)
        if userData: self.setUserData(userData)
        
        if whatsThis: self.setWhatsThis(whatsThis)
        
        
        
            
    def setShortcut(self, key : QKeySequence = None) -> None:
        shortcuts = self.shortcuts()
        if len(shortcuts) == 2:
            shortcuts[0] = key
            super().setShortcuts(shortcuts)
        else:
            super().setShortcut(key)
    
    #The tooltip will NOT reflect the alternate shortcut
    def setAlternateShortcut(self, key : QKeySequence = None) -> None:
        shortcuts = self.shortcuts()
        if len(shortcuts) > 1:
            shortcuts[1] = key
            super().setShortcuts(shortcuts)
        elif len(shortcuts) == 1:
            shortcuts.append(key)
            super().setShortcuts(shortcuts)
        else:
            QtCore.qWarning('Use setShortcut to set a single shortcut key')
