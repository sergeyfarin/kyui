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

class TabBar(QWidget):
    currentChanged = pyqtSignal(int)
    tabCloseRequested = pyqtSignal(int)
    tabMoved = pyqtSignal((int, int))
    
    def __init__(self, parent : QWidget = None):
        super().__init__(parent)
        self._tabs = []
        self.__currentIndex = -1
        self.setFocusPolicy(Qt.TabFocus)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        
        self.elideMode = Qt.TextElideMode(self.style().styleHint(QStyle.SH_TabBar_ElideMode, 
                                                                 None, None))
        self.usesScrollButtons = not self.style().styleHint(QStyle.SH_TabBar_PreferNoArrows, 
                                                            None, None)
        self.documentMode = False
        self.drawBase = True
        self.expanding = True
        self.movable = False
        self.selectionBehaviorOnRemove = QTabBar.SelectRightTab
        self.shape = QTabBar.RoundedNorth
        self.tabsClosable = False

        self.__pressedIndex = -1
        self.__layoutDirty = False
        self.__scrollOffset = 0
        self.__elideModeSetByUser = False
        self.__useScrollButtonsSetByUser = False
        self.__paintWithOffsets = True
        self.__dragInProgress = False
        
        self.__movingTab = 0

    def __len__(self) -> int:
        return self.count
        
    #==================================================#
    # Property Getters                                 #
    #==================================================#
    def getCount(self):
        return len(self._tabs)
    def getCurrentIndex(self) -> int:
        return self.__currentIndex
    def getDocumentMode(self) -> bool:
        return self.__docMode == True
    def getDrawBase(self) -> bool:
        return self.__drawBase == True
    def getElideMode(self) -> Qt.TextElideMode:
        return self.__elideMode
    def getExpanding(self) -> bool:
        return self.__expanding == True
    def getIconSize(self) -> QSize:
        return super().iconSize()
    def getMovable(self) -> bool:
        return self.__movable == True
    def getSelectionBehaviorOnRemove(self) -> QTabBar.SelectionBehavior:
        return self.__selectionBehavior
    def getShape(self) -> QTabBar.Shape:
        return self.__shape
    def getTabsClosable(self) -> bool:
        return self.__tabsClosable == True
    def getUsesScrollButtons(self) -> bool:
        return self.__useScroll == True
        
    #==================================================#
    # Property Setters                                 #
    #==================================================#
    def setCurrentIndex(self, index : int):
        if index < len(self._tabs):
            self.__currentIndex = index
        self.update()
    def setDocumentMode (self, set : bool):
        self.__docMode = set
    def setDrawBase (self, drawTheBase : bool):
        self.drawBase = (drawTheBase == True)
    def setElideMode (self, mode : Qt.TextElideMode):
        self.__elideMode = mode
    def setExpanding (self, expanding : bool):
        self.__expanding = expanding
    def setIconSize (self, size : QSize):
        super().setIconSize(size)
    def setMovable (self, movable : bool):
        self.__movable = (movable == True)
    def setSelectionBehaviorOnRemove (self, behavior : QTabBar.SelectionBehavior):
        self.__selectionBehavior = behavior
    def setShape (self, shape : QTabBar.Shape):
        self.__shape = shape
    def setTabsClosable(self, closable : bool):
        self.__tabsClosable = (closable == True)
    def setUsesScrollButtons (self, useButtons : bool):
        self.__useScroll = (useButtons == True)

    #==================================================#
    # Property Definitions                             #
    #==================================================#
    count = pyqtProperty(int, fget=getCount)
    currentIndex = pyqtProperty(int, fget=getCurrentIndex, fset=setCurrentIndex)
    documentMode = pyqtProperty(bool, fget=getDocumentMode, fset=setDocumentMode)
    drawBase = pyqtProperty(bool, fget=getDrawBase, fset=setDrawBase)
    elideMode = pyqtProperty(Qt.TextElideMode, fget=getElideMode, fset=setElideMode)
    expanding = pyqtProperty(bool, fget=getExpanding, fset=setExpanding)
    iconSize = pyqtProperty(QSize, fget=getIconSize, fset=setIconSize)
    movable = pyqtProperty(bool, fget=getMovable, fset=setMovable)
    selectionBehaviorOnRemove = pyqtProperty(QTabBar.SelectionBehavior, 
                                             fget=getSelectionBehaviorOnRemove, 
                                             fset=setSelectionBehaviorOnRemove)
    shape = pyqtProperty(QTabBar.Shape, fget=getShape, fset=setShape)
    tabsClosable = pyqtProperty(bool, fget=getTabsClosable, fset=setTabsClosable)
    usesScrollButtons = pyqtProperty(bool, 
                                     fget=getUsesScrollButtons, 
                                     fset=setUsesScrolLButtons)
#Types
#    enum ButtonPosition { LeftSide, RightSide }
#    enum SelectionBehavior { SelectLeftTab, SelectRightTab, SelectPreviousTab }
#    enum Shape { RoundedNorth, RoundedSouth, RoundedWest, RoundedEast, ..., TriangularEast }


    #==================================================#
    # Public Methods                                   #
    #==================================================#
    def addTab(self, **kwargs):
        text = kwargs['text'] if 'text' in kwargs else ''
        icon = kwargs['icon'] if 'icon' in kwargs else QIcon()
        self.insertTab(self.count + 1, icon, text)
        
    def insertTab(self, **kwargs):
        index = kwargs['index'] if 'index' in kwargs else 0
        text = kwargs['text'] if 'text' in kwargs else ''
        icon = kwargs['icon'] if 'icon' in kwargs else QIcon()
        self._tabs.insert(index, Tab(icon, text))
        self.tabInserted(index)
        
    def minimumSizeHint (self) -> QSize:
        return super().minimumSizeHint()
    
    def moveTab (self, startpos : int, endpos : int):
        pass
        self.tabLayoutChange()
    
    def removeTab (self, index : int):
        pass
        self.tabRemoved(index)
        
    def sizeHint (self) -> QSize:
        return super().sizeHint()
        
    def tabAt (self, pos : QPoint) -> int:
        return -1
        
    def tabRect (self, index : int) -> QRect:
        return QRect()
        
    def setTabButton(self, index : int, 
                     position : QTabBar.ButtonPosition, 
                     widget : QWidget):
        if index < self.count and index >= 0:
            if position == QTabBar.LeftSide:
                self._tabs[index].leftWidget = widget
            else:
                self._tabs[index].rightWidget = widget
            self.updateGeometry()
            self.update()
        else:
            qWarning('TabBar: invalid index {}'.format(index))

    def setTabData(self, index : int, data : QVariant):
        if index < self.count and index >= 0:
            self._tabs[index].data = data
        else:
            qWarning('TabBar: invalid index {}'.format(index))

    def setTabEnabled(self, index : int, enabled : bool):
        if index < self.count and index >= 0:
            self._tabs[index].enabled = enabled
            self.update()
        else:
            qWarning('TabBar: invalid index {}'.format(index))
        
    def setTabIcon(self, index : int, icon : QIcon):
        if index < self.count and index >= 0:
            self._tabs[index].icon = icon
            self.update()
        else:
            qWarning('TabBar: invalid index {}'.format(index))

    def setTabText(self, index : int, text : str ):
        if index < self.count and index >= 0:
            self._tabs[index].text = text
            self.updateGeometry()
            self.update()
        else:
            qWarning('TabBar: invalid index {}'.format(index))

    def setTabTextColor(self, index : int, color : QColor):
        if index < self.count and index >= 0:
            self._tabs[index].textColor = color
            self.update()
        else:
            qWarning('TabBar: invalid index {}'.format(index))

    def setTabToolTip(self, index : int, text : str):
        if index < self.count and index >= 0:
            self._tabs[index].toolTip = text
        else:
            qWarning('TabBar: invalid index {}'.format(index))

    def setTabWhatsThis(self, index : int, text : str):
        if index < self.count and index >= 0:
            self._tabs[index].whatsThis = text
        else:
            qWarning('TabBar: invalid index {}'.format(index))

    #==================================================#
    # Protected Methods                                #
    #==================================================#
    def initStyleOption (self, opt : QStyleOptionTab, index : int):
        super().initStyleOption(opt, index)
        
    def tabInserted (self, index : int):
        pass
        
    def tabLayoutChange(self):
        pass
        
    def tabRemoved (self, index : int):
        pass
        
    def tabSizeHint (self, index : int) -> QSize:
        return QSize()

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
