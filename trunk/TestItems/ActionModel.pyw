from PyQt4.QtCore import *
from PyQt4.QtGui import *

actionType = { 'TopLevelItem' : 0, 
               'ActionSet' : 1, 
               'SoloAction' : 10, 
               'MenuAction' : 11, 
               'MenuButton' : 12}

class KyActionModel(QObject):
    def __init__(self, 
                 parent : KyRibbonBar = None):
        super().__init__(parent)
        
    def addTopLevelItem(self, title : str = None, icon : QIcon = None) -> int:
        pass
        
    def addActionSet(self, tabIdx : int = 0, title: str = None) -> KyRibbonGroupBox:
        pass
