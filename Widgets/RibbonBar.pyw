from PyQt4.QtCore import *
from PyQt4.QtGui import *

from .RibbonTabBar import KyRibbonTabBar

class KyRibbonBar(QTabWidget):
    def __init__(self, parent : QWidget = None):
        super().__init__(parent)        
        self.setTabBar(KyRibbonTabBar(self))
        self.setMovable(False)
        self.setDocumentMode(False)
        self.setElideMode(Qt.ElideNone)
        self.setUsesScrollButtons(True)
        
    def menuWidget(self) -> QWidget:
        return self.cornerWidget(Qt.TopLeftCorner)
    
    def setMenuWidget(self, widget : QWidget = None) -> None:
        widget.setParent(self)
        self.setCornerWidget(widget, Qt.TopLeftCorner)
        
    def addRibbonTab(self, text : str, icon : QIcon = None) -> QToolBar:
        index = self.addTab(QToolBar(text, self), text)
        if icon:
            assert isinstance(icon, QIcon)
            self.setTabIcon(index, icon)
            
    def setTabText(self, index : int = 0, text : str = None) -> None:
        assert isinstance(text, str)
        super().setTabText(index)
        self.widget(index).setWindowTitle(text)
        
