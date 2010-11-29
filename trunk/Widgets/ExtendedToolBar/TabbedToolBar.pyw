from PyQt4.QtCore import Qt
from PyQt4.QtGui import QTabWidget, QIcon, QToolBar

from .ToolTabBar import ToolTabBar
from .ExtToolBar import ExtendedToolBar

class TabbedToolBar(QTabWidget):
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
        
    def addTab(self, text : str, icon : QIcon = None) -> QToolBar:
        tb = QToolBar(text, self)
        index = self.addTab(tb, text)
        if icon:
            self.setTabIcon(index, icon)
        return tb
            
    def setTabText(self, index : int = 0, text : str = None) -> None:
        super().setTabText(index)
        self.widget(index).setWindowTitle(text)
        
