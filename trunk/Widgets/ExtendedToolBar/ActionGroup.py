from PyQt4.QtCore import QObject, pyqtSignal
from PyQt4.QtGui import QActionGroup

class NamedActionGroup(QActionGroup):
    titleChanged = pyqtSignal(str)
    def __init__(self, 
                 parent : QObject, 
                 title : str  = None, 
                 #Defaults to False
                 enabled : bool = True,
                 #Defaults to false
                 exclusive : bool = False,
                 #Defaults to true
                 visible: bool = True): 
        parent().__init__(parent)
        if title: self.__title = title
        if not enabled: self.setEnabled(False)
        if exclusive: self.setExclusive(True)
        if not visible: self.setVisible(False)
        
    def setTitle(self, title : str = None) -> None:
        if not isinstance(title, str):
            return
        self.__title = title
        self.titleChanged.emit(title)
        
    def title(self) -> str:
        return str(self.__title)
