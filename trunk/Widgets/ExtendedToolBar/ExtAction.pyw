# RibbonActionSet

from PyQt4.QtCore import *
from PyQt4.QtGui import *

ExtActType = { 'Solo' : 0,      #An action without a menu 
               'Menu' : 1,      #An action that serves solely to trigger a menu
               'Split': 2,      #An action that can be triggered and contains a menu
               'ToolGroup' : 3, #An action for a ToolGroup (menu entry, specifically)
               'ToolWidget' : 4,#An action for a widget embedded in a toolbar
               'ToolBar' : 5}   #Action for either setting a toolbar's visibility
                                    #or switching tabs on a TabbedToolBar

class ExtendedAction(QAction):
    def __init__(self,
                 ###
                 # Set either parent or actionGroup. The parent will be set to 
                 # actionGroup if it is set and parent will be ignored
                 ###
                 parent : QWidget = None,
                 actionGroup : QActionGroup = None,
                 ###
                 # This determines how the action will appear and behave.
                 # It cannot be changed.
                 ###
                 actionType : ExtActType = ExtActType['Solo'], 
                 ###
                 #These values make sense for all actions
                 ###
                 text : str = None, 
                 icon : QIcon = None,
                 iconVisibleInMenu : bool = None,
                 font : QFont = None,
                 enabled : bool = None,
                 iconText: str = None,
                 objectName : str = None, 
                 receiver : pyqtSlot = None, 
                #Note: Only the primary shortcut will appear in a tooltip
                 shortcut : QKeySequence = None,
                 shortcut2 : QKeySequence = None, 
                 statusTip : str = None,
                 toolTip : str = None,
                #Note: If no toolTipTitle is set, the text string is used
                 toolTipTitle : str = None, 
                 userData = None, 
                 whatsThis : str = None, 
                 
                 
                 ###
                 # These are specific to certain action types
                 ###
                 # For 'Menu', 'Split', and 'ToolBar' types:
                 menu : QMenu = None, 
                 # For 'Solo' and possibly 'Split'
                 checkable : bool = None,
                 checked : bool = None):
        if actionGroup:
            parent = actionGroup
            self.setActionGroup(actionGroup)
        if text:
            if icon:
                super().__init__(icon, text, parent)
            else:
                super().__init__(text, parent)
        if shortcut:
            if not shortcut2:
                self.setShortcut(shortcut)
            else:
                self.setShortcuts((shortcut, shortcut2))
        if enabled: self.setEnabled(enabled)
        if font: self.setFont(font)
        if iconText: self.setIconText(iconText)
        if iconVisibleInMenu: self.setIconVisibleInMenu(iconVisibleInMenu)
        if objectName : self.setObjectName(objectName)
        if statusTip: self.setStatusTip(statusTip)
        if receiver:
            self.connect(self, SIGNAL('triggered()'), receiver)
        if userData: self.setUserData(userData)
        if whatsThis: self.setWhatsThis(whatsThis)
        if toolTip:
            self.__tt = toolTip
            if toolTipTitle:
                self.__ttTitle = toolTipTitle
            elif text:
                self.__ttTitle = self.text
            else:
                self.__ttTitle = None
            self.__rebuildToolTip()
        
        self.__actType = actionType
        
        # Don't set this for a solo action or toolwidget action
        if menu:
            self.setMenu(menu)
        # Do not set this for anything but a solo or split action
        if checkable:
            self.setCheckable(checkable)
            if checked:
                self.setChecked(checked)
                
    def actionType(self):
        return self.__actionType
            
    def setShortcut(self, key : QKeySequence = None) -> None:
        shortcuts = self.shortcuts()
        if len(shortcuts) == 2:
            shortcuts[0] = key
            super().setShortcuts(shortcuts)
        else:
            super().setShortcut(key)
        self.__rebuildToolTip()
    
    #The tooltip will NOT reflect the alternate shortcut
    def setAlternateShortcut(self, key : QKeySequence = None) -> None:
        shortcuts = self.shortcuts()
        if len(shortcuts) == 2:
            shortcuts[1] = key
            super().setShortcuts(shortcuts)
        elif len(shortcuts) == 1:
            shortcuts.append(key)
            super().setShortcuts(shortcuts)
            
    def setToolTip(self, toolTip : str = None) -> None:
        if not toolTip:
            return
        self.__tt = toolTip
        self.__rebuildToolTip()
        
    def setToolTipTitle(self, title : str = None) -> None:
        if not title:
            return
        self.__ttTitle = title
        self.__rebuildToolTip()
        
    def setText(self, text):
        super().setText(text)
        if not self.__ttTitle:
            self.__rebuildToolTip
    
    def __rebuildToolTip(self) -> None:
        if self.shortcut():
            tt = str.format('{}\n({})\n\n{}', 
                            self.__ttTitle, 
                            self.shortcut().toString(),
                            self.__tt)
        else:
            tt = str.format('{}\n\n{}',
                            self.__ttTitle, 
                            self.__tt)
        super().setToolTip(tt)
