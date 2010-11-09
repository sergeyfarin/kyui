from PyQt4.QtCore import *
from PyQt4.QtGui import *

class KyRibbonTabBar(QTabBar):
    def __init__(self, parent : QWidget = None):
        super().__init__(parent)
        
    def minimumSizeHint(self) -> QSize:
        return super().minimumSizeHint()
        
    def sizeHint(self) -> QSize:
        return super().sizeHint()
        
    def tabSizeHint(self, index = 0) -> QSize:
        count = self.count()
        if count * 23 < self.sizeHint().width():
            pass
        else:
            return super().tabSizeHint(index)
