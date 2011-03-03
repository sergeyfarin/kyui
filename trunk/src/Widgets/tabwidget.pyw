from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Tab():
    __slots__ = ['enabled', 'shortcutId', 'text', 'icon', 'toolTip', 'whatsThis', 
                 'textColor', 'tabData', 'leftWidget', 'rightWidget', 'lastTab', 
                 'dragOffset', 'animation', 'rect', 'minRect', 'maxRect']
    def __init__(self, icon : QIcon, text : str):
        self.enabled = True
        self.shortcutId = 0
        self.text = txt
        self.icon = QIcon(icon)
        self.toolTip = None
        self.whatsThis = None
        self.textColor = QColor(Qt.black)
        self.tabData = None
        
        self.leftWidget = None
        self.rightWidget = None
        self.lastTab = -1
        self.dragOffset = 0
        self.animation = None
        
        self.rect = QRect()
        self.minRect = QRect()
        self.maxRect = QRect()

class TabBar(QTabBar):    
    def __init__(self, parent : QWidget = None):
        super().__init__(parent)
        self._tabList = []
        self.__currentIndex = -1
        
    #==================================================#
    # Properties                                       #
    #==================================================#
    def getCurrentIndex(self) -> int:
        return self.__currentIndex
        
    def setCurrentIndex(self, index : int):
        if index < len(self._tabList):
            self.__currentIndex = index
            
    currentIndex = pyqtProperty(int, fget=getCurrentIndex, fset=setCurrentIndex)



#Types
#    enum ButtonPosition { LeftSide, RightSide }
#    enum SelectionBehavior { SelectLeftTab, SelectRightTab, SelectPreviousTab }
#    enum Shape { RoundedNorth, RoundedSouth, RoundedWest, RoundedEast, ..., TriangularEast }


#Methods
    def minimumSizeHint (self) -> QSize:
        return super().minimumSizeHint()
    def moveTab (self, startpos : int, endpos : int):
        return super().moveTab(startpos, endpos)
    def removeTab (self, index : int):
        return super().removeTab(index)
    def sizeHint (self) -> QSize:
        return super().sizeHint()
    def tabAt (self, pos : QPoint) -> int:
        return super().tabAt(pos)
    def tabRect (self, index : int) -> QRect:
        return super().tabRect(index)

#Properties
    def setCurrentIndex (self, index : int):
        return super().setCurrentIndex(index)
    def setDocumentMode (self, set : bool):
        return super().setDocumentMode(set)
    def setDrawBase (self, drawTheBase : bool):
        return super().setDrawBase(drawTheBase)
    def setElideMode (self, mode : Qt.TextElideMode):
        return super().setElideMode(mode)
    def setExpanding (self, enabled : bool):
        return super().setExpanding(enabled)
    def setIconSize (self, size : QSize):
        return super().setIconSize(size)
    def setMovable (self, movable : bool):
        return super().setMovable(movable)
    def setSelectionBehaviorOnRemove (self, behavior : QTabBar.SelectionBehavior):
        return super().setSelectionBehaviorOnRemove(behavior)
    def setShape (self, shape : QTabBar.Shape):
        return super().setShape(shape)
    def setUsesScrollButtons (self, useButtons : bool):
        return super().setUsesScrollButtons(useButtons)


#Protected Methods
    def initStyleOption (self, opt : QStyleOptionTab, index : int):
        super().initStyleOption(opt, index)
    def tabInserted (self, index : int):
        super().tabInserted(index)
    def tabLayoutChange (self):
        super().tabLayoutChange()
    def tabRemoved (self, index : int):
        super().tabRemoved(index)
    def tabSizeHint (self, index : int) -> QSize:
        return super().tabSizeHint(index)

    def changeEvent (self, ev : QEvent):
        super().changeEvent(ev)
    def event (self, ev : QEvent) -> bool:
        return super().event(ev)
    def hideEvent (self, ev : QHideEvent):
        super().hideEvent(ev)

    def keyPressEvent (self, ev : QKeyEvent):
        super().keyPressEvent(ev)
    def mouseMoveEvent (self, ev : QMouseEvent):
        super().mouseMoveEvent(ev)
    def mousePressEvent (self, ev : QMouseEvent):
        super().mousePressEvent(ev)
    def mouseReleaseEvent (self, ev : QMouseEvent):
        super().mouseReleaseEvent(ev)
    def paintEvent (self, ev : QPaintEvent):
        super().paintEvent(ev)
    def resizeEvent (self, ev : QResizeEvent):
        super().resizeEvent(ev)
    def showEvent (self, ev : QShowEvent):
        super().showEvent(ev)
    def wheelEvent (self, ev : QWheelEvent):
        super().wheelEvent(ev)
