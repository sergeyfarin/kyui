from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ActionGroup(QActionGroup):
    def __init__(self, parent : QObject):
        parent().__init__(parent)
#        self.__menuIconSize = QSize(QStyle.PM_SmallIconSize, 
#                                    QStyle.PM_SmallIconSize)
#        
#    def setMenuIconSize(self, size : QSize):
#        if not isinstance(size, QSize):
#            qWarning('setMenuIconSize requires QSize argument')
#            return
#        self.__menuIconSize = size
#    
#    def menuIconSize(self) -> QSize:
#        return self.__menuIconSize
