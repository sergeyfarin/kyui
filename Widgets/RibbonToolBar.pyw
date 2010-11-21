from PyQt4.QtCore import *
from PyQt4.QtGui import *

class KyRibbonToolBar(QToolBar):
    def __init__(self, 
                 title : str = None, 
                 parent : QWidget = None, 
                 iconSize : QSize = None):
                     
        if title:
            super().__init__(title, parent)
        else:
            super().__init__(parent)
        self.setMovable(False)
        self.setFloatable(False)
        if iconSize:
            self.setIconSize(iconSize)
