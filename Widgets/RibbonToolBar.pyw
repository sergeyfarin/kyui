from PyQt4.QtCore import *
from PyQt4.QtGui import *

class KyRibbonToolBar(QToolbar):
    def __init__(self, 
                 parent : QWidget = None, 
                 title : str = None, 
                 lgIconSize : QSize = None, 
                 smIconSize : QSize = None):
        super().__init__(parent)
        if title:
            self.setTitle(title)
        if lgIconSize:
            self.__lgIconSize = lgIconSize
            self.setIconSize(iconSize)
        else:
            self.__lgIconSize = QSize(32, 32)
            self.setIconSize(self.__lgIconSize)
        if smIconSize:
            self.__smIconSize = smIconSize
        
        self.setOrientation(orientation)
        
    def sizeHint(self) -> QSize:
        return super().sizeHint()

    def setOrientation(self, orientation = Qt.Horizontal) -> None:
        self.__orient = orientation
        if orientation == Qt.Horizontal:
            self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        else:
            self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.update()
