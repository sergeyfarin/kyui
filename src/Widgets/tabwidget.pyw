from PyQt4.QtCore import *
from PyQt4.QtGui import *

from .closeButton import CloseButton

def isVertical(position : QTabWidget.TabPosition) -> bool:
    return (position == QTabWidget.West
           or shape == QTabWidget.East)

#Given that tab at position oldIndex moved to position newIndex, return the tab's
#(correct) new index
def calculateNewPosition(oldIndex : int, newIndex : int, index : int) -> int:
    if index == oldIndex:
        return newIndex
    start = oldIndex if oldIndex < newIndex else newIndex
    end = oldIndex if oldIndex < newIndex else newIndex
    if (index >= start and index <= end):
        index += - 1 if (oldIndex < newIndex) else 1
    return index

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
        self._tabList = []
        self.__currentIndex = -1
        
        self.setFocusPolicy(Qt.TabFocus)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        
        #Setup scroll buttons
        self._leftB = QToolButton(self)
        self._leftB.setAutoRepeat(True)
        self._leftB.clicked.connect(self._scrollTabs)
        self._leftB.hide()
        
        self._rightB = QToolButton(self)
        self._rightB.setAutoRepeat(True)
        self._rightB.clicked.connect(self._scrollTabs)
        self._rightB.hide()
        
        #Set private data
        self._pressedIndex = -1
        self._movingTab = None
        self._layoutDirty = False
        self._scrollOffset = 0
        self._manualElideMode = False
        self._manualScrollSet = False
        self._paintWithOffsets = True
        self._dragInProgress = False
        
        #Set propeties
        self.__elideMode = Qt.TextElideMode(self.style().styleHint(QStyle.SH_TabBar_ElideMode, 
                                                                 None, None))
        self.__useScroll = not self.style().styleHint(QStyle.SH_TabBar_PreferNoArrows, 
                                                            None, None)
        self.__docMode = False
        self.__drawBase = True
        self.__expanding = True
        self.__movable = False
        self.__position = QTabWidget.North
        self.__vertical = False
        self.__selectionBehavior = QTabBar.SelectRightTab
        self.__shape = QTabWidget.Rounded
        self.__tabsClosable = False
        iconMetric = self.style().pixelMetric(QStyle.PM_TabBarIconSize, None, self)
        self.__iconSize = QSize(iconMetric, iconMetric)

    def __len__(self) -> int:
        return self.count
        
    #==================================================#
    # Property Getters                                 #
    #==================================================#
    def getCount(self):
        return len(self._tabList)
        
    def getCurrentIndex(self) -> int:
        if self.isValidIndex(self.__currentIndex):
            return self.__currentIndex;
        return -1
        
    def getDocumentMode(self) -> bool:
        return self.__docMode
        
    def getDrawBase(self) -> bool:
        return self.__drawBase
        
    def getElideMode(self) -> Qt.TextElideMode:
        return self.__elideMode
        
    def getExpanding(self) -> bool:
        return self.__expanding
        
    def getIconSize(self) -> QSize:
        if self.__iconSize().isValid():
            return self.__iconSize
        size = style().pixelMetric(QStyle.PM_TabBarIconSize, None, self);
        return QSize(size, size)
        
    def getMovable(self) -> bool:
        return self.__movable
        
    def getSelectionBehaviorOnRemove(self) -> QTabBar.SelectionBehavior:
        return self.__selectionBehavior
        
    def getShape(self) -> QTabBar.Shape:
        return self.__shape
        
    def getTabsClosable(self) -> bool:
        return self.__tabsClosable
        
    def getUsesScrollButtons(self) -> bool:
        return self.__useScroll
        
    #==================================================#
    # Property Setters                                 #
    #==================================================#
    def setCurrentIndex(self, index : int):
        if self._dragInProgress and self._pressedIndex != -1:
            return
        if not self.isValidIndex(index) or self.__currentIndex != index:
            return
        oldIndex = int(self.__currentIndex)
        self.__currentIndex = index
        self.update()
        self._makeVisible(index)
        self._tabList[index].lastTab = oldIndex;
        if oldIndex >= 0 and oldIndex < self.count():
            self._layoutTab(oldIndex)
        self._layoutTab(index)
        self.currentChanged.emit(index)
    
    def setDocumentMode (self, set : bool):
        self.__docMode = set
        #self._updateMacBorderMetrics()
    
    def setDrawBase(self, drawBase : bool):
        if self.__drawBase == drawBase:
            return
        self.__drawBase = drawBase
        self.update()
        
    def setElideMode(self, mode: Qt.TextElideMode):
        self.__elideMode = mode
        self._manualElideMode = True
        self._refresh()
        
    def setExpanding(self, enabled : bool):
        if self.__expanding == enabled:
            return
        self.__expanding = enabled;
        self._layoutTabs()

    def setIconSize(self, size : QSize):
        self.__iconSize = size
        self._layoutDirty = True
        self.update()
        self.updateGeometry()

    def setMovable (self, movable : bool):
        self.__movable = (movable == True)
        
    def setSelectionBehaviorOnRemove (self, behavior : QTabBar.SelectionBehavior):
        self.__selectionBehavior = behavior

    def setShape(self, shape : QTabBar.Shape):
        if self.__shape == shape:
            return
        self.__shape = shape
        self._refresh()

    def setTabsClosable(self, closable : bool):
        if self.__tabsClosable == closable:
            return
        self.__tabsClosable = closable
        closeSide = self.style().styleHint(QStyle.SH_TabBar_CloseButtonPosition, None, self)
        if not closable:
            for tab in iter(self._tabList):
                if closeSide == LeftSide and tab.leftWidget:
                    tab.leftWidget.deleteLater()
                    tab.leftWidget = None
                if closeSide == RightSide and tab.rightWidget:
                    tab.rightWidget.deleteLater()
                    tab.rightWidget = None
        else:
            newButtons = False;
            for i in range(self.count):
                if self.tabButton(i, closeSide):
                    continue
                newButtons = True;
                closeButton = CloseButton(self)
                closeButton.clicked.connect(self._closeTab())
                self.setTabButton(i, closeSide, closeButton)
            if newButtons:
                self._layoutTabs()
        self.update()

    def setUsesScrollButtons(self, useButtons : bool):
        self._manualScrollSet = True
        if self.__useScrollButtons == useButtons:
            return
        self.__useScrollButtons = useButtons
        self._refresh()
        
    def setVerticalText(self, vertical : bool = False):
        self.__verticalText = vertical
        self._refresh()

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
    verticalText = pyqtProperty(bool, fget=getVerticalText, fset=setVerticalText)
#Types
#    enum ButtonPosition { LeftSide, RightSide }
#    enum SelectionBehavior { SelectLeftTab, SelectRightTab, SelectPreviousTab }
#    enum Shape { RoundedNorth, RoundedSouth, RoundedWest, RoundedEast, ..., TriangularEast }


    #==================================================#
    # Public Methods                                   #
    #==================================================#
    def addTab(self, **kwargs) -> int:
        text = kwargs['text'] if 'text' in kwargs else ''
        icon = kwargs['icon'] if 'icon' in kwargs else QIcon()
        return self.insertTab(-1, icon, text)
        
    def insertTab(self, **kwargs) -> int:
        index = kwargs['index'] if 'index' in kwargs else -1
        text = kwargs['text'] if 'text' in kwargs else ''
        icon = kwargs['icon'] if 'icon' in kwargs else QIcon()
        
        if (not self.isValidIndex(index)):
            index = self.count
            self._tabList.append(Tab(icon, text))
        else:
            self._tabList.insert(index, Tab(icon, text))

        self._tabList[index].shortcutId = self.grabShortcut(QKeySequence.mnemonic(text))

        self._refresh()
        if self.count == 1:
            self.currentIndex = index
        elif index <= self.currentIndex:
            self.currentIndex += 1

        if self.tabsClosable:
            opt = QStyleOptionTabV3()
            self.initStyleOption(opt, index)
            closeSide = self.style().styleHint(QStyle.SH_TabBar_CloseButtonPosition, None, self)
            closeButton = CloseButton(self)
            closeButton.clicked.connect(self_closeTab())
            self.setTabButton(index, closeSide, closeButton)

        for i in range(self.count):
            if self._tabList[i].lastTab >= index:
                self._tabList[i].lastTab += 1

        self.tabInserted(index)
        return index

    def isTabEnabled(self, index : int) -> bool:
        if self.isValidIndex(index):
            return self._tabList[index].enabled
        return False
    
    def isValidIndex(self, index : int) -> bool:
        return (index < self.count and index >= 0)
        
    def minimumSizeHint(self) -> QSize:
        if not self.useScrollButtons:
            rect = QRect()
            for tab in iter(self._tabList):
                rect = rect.united(tab.minRect)
            sz = rect.size().expandedTo(QApplication.globalStrut())
        elif self.vertical:
            sz = QSize(self.sizeHint().width(), 
                       self._rightB.sizeHint().height() * 2 + 75)
        else:
            sz = QSize(self._rightB.sizeHint().width() * 2 + 75, 
                       self.sizeHint().height())
        return sz
    
    def moveTab(self, start : int, end : int):
        if (start == end
            or not self.isValidIndex(start)
            or not self.isValidIndex(end)):
            return

        vertical = self.vertical
        oldPressedPos = 0
        if (self._pressedIndex != -1):
            # Record the position of the pressed tab before reordering the tabs.
            oldPressedPos = (self._tabList[self._pressedIndex].rect.y() 
                             if vertical else 
                             self._tabList[self._pressedIndex].rect.x())

        # Update the locations of the tabs first
        start = min((start, end))
        end = max((start, end))
        width = self._tabList[start].rect.height() if vertical else self._tabList[start].rect.width()
        if start < end:
            width *= -1;
        rtl = isRightToLeft()
        for tab in iter(self._tabList[start:end]):
            if i == start:
                continue
            if vertical:
                tab.rect.moveTop(tab.rect.y() + width)
            else:
                tab.rect.moveLeft(tab.rect.x() + width)
            direction = -1
            if rtl and not vertical:
                direction *= -1
            if tab.dragOffset != 0:
                tab.dragOffset += (direction * width)

        if vertical:
            if start < end:
                self._tabList[start].rect.moveTop(self._tabList[end].rect.bottom() + 1)
            else:
                self._tabList[start].rect.moveTop(self._tabList[end].rect.top() - width)
        else:
            if start < end:
                self._tabList[start].rect.moveLeft(self._tabList[end].rect.right() + 1)
            else:
                self._tabList[start].rect.moveLeft(self._tabList[end].rect.left() - width)

        # Move the actual data structures
        tab1 = self._tabList[start]
        tab2 = self._tabList[end]
        self._tabList[start] = tab2
        self._tabList[end] = tab1

        # update lastTab locations
        for i in range(self.count):
            self._tabList[i].lastTab = calculateNewPosition(start, end, self._tabList[i].lastTab);

        # update external variables
        self.currentIndex = calculateNewPosition(start, end, self.currentIndex)

        # If we are in the middle of a drag update the dragStartPosition
        if self._pressedIndex != -1:
            self._pressedIndex = calculateNewPosition(start, end, self._pressedIndex)
            if vertical:
                newPressedPos = self._tabList[self._pressedIndex].rect.top()
            else:
                newPressedPos = self._tabList[self._pressedIndex].rect.left()
            diff = oldPressedPos - newPressedPos
            if self.isRightToLeft() and not vertical:
                diff *= -1
            if vertical:
                self._dragStartPosition.setY(self._dragStartPosition.y() - diff)
            else:
                self._dragStartPosition.setX(self._dragStartPosition.x() - diff)

        self._layoutWidgets(start)
        self.update()
        self.tabMoved.emit((start, end))
        self.tabLayoutChange.emit()

    
    def removeTab(self, index : int):
        if not self.isValidIndex(index):
            return
        tab = self._tabList[index]
        self.releaseShortcut(tab.shortcutId)
        if tab.leftWidget:
            stab.leftWidget.hide()
            tab.leftWidget.deleteLater()
            tab.leftWidget = None
        if tab.rightWidget:
            tab.rightWidget.hide()
            tab.rightWidget.deleteLater()
            tab.rightWidget = None

        newIndex = tab.lastTab
        self._tabList.remove(index)
        for tab in iter(self._tabList):
            if tab.lastTab == index:
                tab.lastTab = -1
            if tab.lastTab > index:
                tab.lastTab -= 1
        if index == self.currentIndex:
            # The current tab is going away, in order to make sure
            # we emit that "current has changed", we need to reset this
            # around.
            self.currentIndex = -1
            if (self.count > 0):
                if self.selectionBehaviorOnRemove == QTabBar.SelectPreviousTab:
                    if newIndex > index:
                        newIndex -= 1
                if (not self.isValidIndex(newIndex) 
                        or self.selectionBehaviorOnRemove == QTabBar.SelectRightTab):
                    newIndex = int(index)
                    if newIndex >= self.count:
                        newIndex = self.count - 1
                elif self.selectionBehaviorOnRemove == QTabBar.SelectLeftTab:
                    newIndex = index - 1
                    if newIndex < 0:
                        newIndex = 0

                if self.isValidIndex(newIndex):
                    # don't lose newIndex's old through setCurrentIndex
                    bump = int(self._tabList[newIndex].lastTab)
                    self.currentIndex = newIndex
                    self._tabList[newIndex].lastTab = bump
            else:
                self.currentChanged.emit(-1)
        elif index < self.currentIndex:
            self.currentIndex -= 1
        self._refresh()
        self.tabRemoved(index)
        
    def sizeHint(self) -> QSize:
        if self._layoutDirty:
           self._layoutTabs()
        rect = QRect()
        for tab in iter(self._tabList):
            rect = rect.united(tab.maxRect)
        return rect.size().expandedTo(QApplication.globalStrut())

    def setTabButton(self, 
                     index : int, 
                     position : QTabBar.ButtonPosition, 
                     widget : QWidget):
        if not self.isValidIndex(index):
            return
        if widget:
            widget.setParent(self);
            # make sure our left and right widgets stay on top
            widget.lower()
            widget.show()
        if position == QTabBar.LeftSide:
            if self._tabList[index].leftWidget:
                self._tabList[index].leftWidget.hide()
            self._tabList[index].leftWidget = widget
        else:
            if self._tabList[index].rightWidget:
                self._tabList[index].rightWidget.hide()
            self._tabList[index].rightWidget = widget
        self._layoutTabs()
        self._refresh()
        self.update()

    def setTabData(self, index : int, data : QVariant):
        if self.isValidIndex(index):
            self._tabList[index].data = data

    def setTabEnabled(self, index : int, enabled : bool):
        if not self.isValidIndex(index):
            return 
        tab = self._tabList[index]
        self.setShortcutEnabled(tab.shortcutId, tab.enabled)
        self.update()
        if not tab.enabled and index == self.currentIndex:
            self._setNextEnabledIndex(1 if self.isValidIndex(index + 1) else 0)
        elif tab.enabled and not self.isValidIndex(self.currentIndex):
            self.currentIndex = index
        
    def setTabIcon(self, index : int, icon : QIcon):
        if self.isValidIndex(index):
            tabIcon = self._tabList[index].icon
            updateTabOnly = (not icon.isNull() and not tabIcon.isNull())
            tabIcon = icon
            if updateTabOnly:
                self.update(self.tabRect(index))
            else:
                self._refresh()

    def setTabText(index : int, text : str):
        if self.isValidIndex(index):
            tab = self._tabList[index]
            tab.text = text
            self.releaseShortcut(tab.shortcutId)
            tab.shortcutId = self.grabShortcut(QKeySequence.mnemonic(text))
            self.setShortcutEnabled(tab.shortcutId, tab.enabled)
            self._refresh()

    def setTabTextColor(self, index : int, color : QColor):
        if self.isValidIndex(index):
            self._tabList[index].textColor = color
            self.update(self.tabRect(index))

    def setTabToolTip(self, index : int, text : str):
        if self.isValidIndex(index):
            self._tabList[index].toolTip = text

    def setTabWhatsThis(self, index : int, text : str):
        if self.isValidIndex(index):
            self._tabList[index].whatsThis = text

    def tabAt(self, position : QPoint) -> int:
        if (self.isValidIndex(self.currentIndex)
                and tabRect(self.currentIndex).contains(position)):
            return self.currentIndex

        for i in range(self.count):
            if self.tabRect(i).contains(position):
                return i
        return -1
        
    def tabButton(self, index : int, 
                  position : QTabBar.ButtonPosition) -> QWidget:
        if not self.isValidIndex(index):
            return None
        if position == QTabBar.LeftSide:
            return self._tabList[index].leftWidget
        else:
            return self._tabList[index].rightWidget
            
    def tabData(self, index : int):
        if self.isValidIndex(index):
            return self._tabList[index].data
        return None

    def tabIcon(self, index : int) -> QIcon:
        if self.isValidIndex(index):
            return self._tabList[index].icon
        return QIcon()

    def tabRect(self, index : int) -> QRect:
        if self.isValidIndex(index):
            if self._layoutDirty:
               self._layoutTabs()
            if self.vertical:
                tab.rect.translate(0, -self._scrollOffset)
            else:
                tab.rect.translate(-self._scrollOffset, 0)
                tab.rect = QStyle.visualRect(self.layoutDirection(), 
                                             self.rect(), tab.rect)
            return tab.rect
        return QRect()

    def tabText(self, index : int) -> str:
        if self.isValidIndex(index):
            return self._tabList[index].text
        return None

    def tabTextColor(self, index : int) -> QColor:
        if self.isValidIndex(index):
            return self._tabList[index].textColor
        return QColor()
    
    def tabToolTip(self, index : int) -> str:
        if self.isValidIndex(index):
            return self._tabList[index].toolTip
        return None

    def tabWhatsThis(self, index : int) -> str:
        if self.isValidIndex(index):
            return self._tabList[index].whatsThis
        return None

    #==================================================#
    # Protected Methods                                #
    #==================================================#
    def _computeElidedText(self, mode : Qt.TextElideMode, text : str) -> str:
        if len(text) < 8 or self.mode == Qt.ElideNone:
            return text

        Ellipses = '...'
        if self.mode == Qt.ElideRight:
            ret = text[0:3] + Ellipses
        elif self.mode == Qt.ElideMiddle:
            ret = text[0:1] + Ellipses + text[-2:-1]
        elif self.mode == Qt.ElideLeft:
            ret = Ellipses + text[-4:-1]
        return ret
    
    def initStyleOption(self, opt : QStyleOptionTab, tabIndex : int):
        totalTabs = self.count;

        if (not option or (tabIndex < 0 or tabIndex >= totalTabs)):
            return

        tab = self._tabList[tabIndex]
        opt.initFrom(self)
        opt.state &= ~(QStyle.State_HasFocus | QStyle.State_MouseOver);
        opt.rect = self.tabRect(tabIndex)
        isCurrent = tabIndex == self.currentIndex
        opt.row = 0
        if tabIndex == self._pressedIndex:
            opt.state |= QStyle.State_Sunken
        if isCurrent:
            opt.state |= QStyle.State_Selected
            if self.hasFocus():
                opt.state |= QStyle.State_HasFocus
        if not tab.enabled:
            opt.state &= ~QStyle.State_Enabled
        if self.isActiveWindow():
            opt.state |= QStyle.State_Active
        if not self._dragInProgress and opt.rect == self._hoverRect:
            opt.state |= QStyle.State_MouseOver
        opt.shape = self.shape
        opt.text = tab.text

        if tab.textColor.isValid():
            opt.palette.setColor(self.foregroundRole(), tab.textColor)

        opt.icon = tab.icon
        opt.iconSize = self.iconSize

        opt.leftButtonSize = tab.leftWidget.size() if tab.leftWidget else QSize()
        opt.rightButtonSize = tab.rightWidget.size() if tab.rightWidget else QSize()
        opt.documentMode = self.documentMode


        if tabIndex > 0 and (tabIndex - 1 == self.currentIndex):
            opt.selectedPosition = QStyleOptionTab.PreviousIsSelected
        elif (tabIndex < totalTabs - 1) and (tabIndex + 1 == self.currentIndex):
            opt.selectedPosition = QStyleOptionTab.NextIsSelected
        else:
            opt.selectedPosition = QStyleOptionTab.NotAdjacent

        paintBeginning = ((tabIndex == 0) 
                          or (self._dragInProgress and tabIndex == self._pressedIndex + 1))
        paintEnd = ((tabIndex == totalTabs - 1) 
                    or (self._dragInProgress and tabIndex == self._pressedIndex - 1))
        if paintBeginning:
            if paintEnd:
                opt.position = QStyleOptionTab.OnlyOneTab
            else:
                opt.position = QStyleOptionTab.Beginning
        elif paintEnd:
            opt.position = QStyleOptionTab.End
        else:
            opt.position = QStyleOptionTab.Middle
    ###
    # Fix this later to work with TabWidget
    ###
    #    if (QTabWidget *tw = qobject_cast<QTabWidget *>(parentWidget())):
    #        if (tw.cornerWidget(Qt.TopLeftCorner) or tw.cornerWidget(Qt.BottomLeftCorner))
    #            opt.cornerWidgets |= QStyleOptionTab.LeftCornerWidget;
    #        if (tw.cornerWidget(Qt.TopRightCorner) or tw.cornerWidget(Qt.BottomRightCorner))
    #            opt.cornerWidgets |= QStyleOptionTab.RightCornerWidget;

        textRect = style().subElementRect(QStyle.SE_TabBarTabText, opt, self)
        opt.text = fontMetrics().elidedText(opt.text, 
                                            self.elideMode, 
                                            textRect.width(),
                                            Qt.TextShowMnemonic)

    def initStyleBaseOption(self, optBase : QStyleOptionTabBarBaseV2, tabBar : QTabBar, sz : QSize):
        tabOverlap = QStyleOptionTab()
        tabOverlap.shape = tabBar.shape()
        overlap = tabBar.style().pixelMetric(QStyle.PM_TabBarBaseOverlap, tabOverlap, tabBar)
        widget = tabBar.parentWidget()
        optBase.init(tabBar)
        optBase.shape = tabBar.shape()
        optBase.documentMode = tabBar.documentMode()
        if widget and overlap > 0:
            rect = QRect()
            if (tabOverlap.shape == QTabBar.RoundedNorth
                or tabOverlap.shape == QTabBar.TriangularNorth):
                rect.setRect(0, sz.height()-overlap, sz.width(), overlap);
            elif (tabOverlap.shape == QTabBar.RoundedSouth
                  or tabOverlap.shape == QTabBar.TriangularSouth):
                rect.setRect(0, 0, sz.width(), overlap)
            elif (tabOverlap.shape == QTabBar.RoundedEast 
                  or tabOverlap.shape == QTabBar.TriangularEast):
                rect.setRect(0, 0, overlap, sz.height())
            elif (tabOverlap.shape ==  QTabBar.RoundedWest 
                  or tabOverlap.shape == QTabBar.TriangularWest):
                rect.setRect(sz.width() - overlap, 0, overlap, sz.height())

    def tabInserted (self, index : int):    pass
    def tabLayoutChange(self):              pass
    def tabRemoved (self, index : int):     pass

    def changeEvent(self, ev : QEvent):
        if ev.type() == QEvent.StyleChange:
            if not self._manualElideMode:
                self.elideMode = Qt.TextElideMode(style().styleHint(QStyle.SH_TabBar_ElideMode, 
                                                                    None, self))
            if not self._manualScrollSet:
                self.useScrollButtons =  not style().styleHint(QStyle.SH_TabBar_PreferNoArrows, 
                                                               None, self)
            self._refresh()
        elif (ev.type() == QEvent.FontChange):
            self._refresh()
        super(QWidget, self).changeEvent(ev)
    
    def event(self, ev : QEvent) -> bool:
        if (ev.type() == QEvent.ToolTip):
            tab = self.tabAt(ev.pos())
            if tab and tab.toolTip:
                QToolTip.showText(ev.globalPos(), tab.toolTip, self)
                return True
        elif (ev.type() == QEvent.QueryWhatsThis):
            tab = self.tabAt(ev.pos())
            if not tab or not tab.whatsThis:
                ev.ignore()
            return True
        elif (ev.type() == QEvent.WhatsThis):
            tab = self.tabAt(ev.pos())
            if tab and tab.whatsThis:
                QWhatsThis.showText(ev.globalPos(), tab.whatsThis, self)
                return True
        elif (ev.type() == QEvent.Shortcut):
            for tab in iter(self._tabList):
                if tab.shortcutId == ev.shortcutId():
                    self.currentIndex = self._tabList.index(tab)
                    return True
        return super(QWidget, self).event(ev)

    def hoverEvent(self, ev : QHoverEvent):
        if (event.type() == QEvent.HoverMove or event.type() == QEvent.HoverEnter):
            if self._hoverRect.contains(ev.pos()):
                oldHoverRect = self._hoverRect
                for i in range(self.count):
                    area = self.tabRect(i)
                    if area.contains(ev.pos()):
                        self._hoverRect = area
                        break
                if ev.oldPos() != QPoint(-1, -1):
                    self.update(oldHoverRect);
                self.update(self._hoverRect);
            return True
        elif event.type() == QEvent.HoverLeave:
            oldHoverRect = self._hoverRect;
            self._hoverRect = QRect();
            self.update(oldHoverRect)
            return True

    def keyPressEvent(self, ev : QKeyEvent):
        if (ev.key() != Qt.Key_Left and ev.key() != Qt.Key_Right):
            ev.ignore()
            return
        rtl = self.isRightToLeft()
        if ev.key() == Qt.Key_Right:
            offset = 1 if rtl else -1
        else:
            offset = -1 if rtl else 1
        self._setNextEnabledIndex(offset)

    def mouseMoveEvent(self, ev : QMouseEvent):
        if self.movable:
            # Be safe!
            if (self._pressedIndex != -1
                    and ev.buttons() == Qt.NoButton):
                self._moveTabFinished(self._pressedIndex)
            
            # Start drag
            offset = (ev.pos() - self._dragStartPosition).manhattanLength()
            if (not self._dragInProgress and self._pressedIndex != -1):
                if (offset > QApplication.startDragDistance()):
                    self._dragInProgress = True
                    self._setupMovableTab()
            
            if (ev.buttons() == Qt.LeftButton
                    and offset > QApplication.startDragDistance()
                    and self.isValidIndex(self._pressedIndex)):
                vertical = self.vertical
                startingRect = self.tabRect(self._pressedIndex)
                if vertical:
                    dragDistance = (ev.pos().y() - self._dragStartPosition.y())
                    startingRect.moveTop(startingRect.y() + dragDistance)
                else:
                    dragDistance = (ev.pos().x() - self._dragStartPosition.x())
                    startingRect.moveLeft(startingRect.x() + dragDistance)
                self._tabList[self._pressedIndex].dragOffset = dragDistance

                if dragDistance < 0:
                    overIndex = self.tabAt(startingRect.topLeft())
                else:
                    overIndex = self.tabAt(startingRect.topRight())

                if overIndex != self._pressedIndex and overIndex != -1:
                    offset = 1
                    if self.isRightToLeft() and not vertical:
                        offset *= -1
                    if dragDistance < 0:
                        dragDistance *= -1
                        offset *= -1
                    i = int(self._pressedIndex)
                    while i < overIndex if offset > 0 else i > overIndex:
                        overIndexRect = self.tabRect(overIndex)
                        needsToBeOver = (overIndexRect.height() if vertical else overIndexRect.width()) / 2
                        if dragDistance > needsToBeOver:
                            self._slide(i + offset, self._pressedIndex)
                        i += offset

                # Buttons needs to follow the dragged tab
                self._layoutTab(self._pressedIndex)
                self.update()
    #ifdef Q_WS_MAC
    #    elif (!self.documentMode and ev.buttons() == Qt.LeftButton and d.previousPressedIndex != -1):
    #        int newPressedIndex = self.tabAt(ev.pos());
    #        if (self._pressedIndex == -1 and d.previousPressedIndex == newPressedIndex):
    #            self._pressedIndex = d.previousPressedIndex;
    #            update(tabRect(self._pressedIndex));
    #        elif(self._pressedIndex != newPressedIndex):
    #            self._pressedIndex = -1;
    #            update(tabRect(d.previousPressedIndex));
    #        }
    #endif
        if (ev.buttons() != Qt.LeftButton):
            ev.ignore()
            return
        optBase = QStyleOptionTabBarBaseV2()
        optBase.init(self)
        optBase.documentMode = self.documentMode

        # Re-arrange widget order to avoid overlaps
        if tabList[pressedIndex].leftWidget:
            tabList[pressedIndex].leftWidget.raise_()
        if tabList[pressedIndex].rightWidget:
            tabList[pressedIndex].rightWidget.raise_()
        if leftB:
            leftB.raise_()
        if self._rightB:
            self._rightB.raise_()
        self._movingTab.setVisible(True)

    def mousePressEvent(self, ev : QMouseEvent):
        if ev.button() != Qt.LeftButton:
            ev.ignore()
            return

        # Be safe!
        if (self._pressedIndex != -1 and self.movable):
            self._moveTabFinished(self._pressedIndex)

        self._pressedIndex = self.tabAt(ev.pos())
    #ifdef Q_WS_MAC
    #    d.previousPressedIndex = self._pressedIndex;
    #endif
        if self.isValidIndex(self._pressedIndex):
            optBase = QStyleOptionTabBarBaseV2()
            optBase.init(self)
            optBase.documentMode = self.documentMode;
            if ev.type() == style().styleHint(QStyle.SH_TabBar_SelectMouseType, optBase, self):
                self.currentIndex = self._pressedIndex
            else:
                self.repaint(tabRect(self._pressedIndex));
            if self.movable:
                self._dragStartPosition = ev.pos()
    
    def mouseReleaseEvent(self, ev : QMouseEvent):
        if (ev.button() != Qt.LeftButton):
            ev.ignore()
            return
        #ifdef Q_WS_MAC
        #self._previousPressedIndex = -1;
        #endif
        if (self.movable and self._dragInProgress 
                and self.isValidIndex(self._pressedIndex)):
            length = self._tabList[self._pressedIndex].dragOffset
            width = (tabRect(self._pressedIndex).height() 
                     if self.vertical 
                     else tabRect(self._pressedIndex).width())
            duration = min((250, (abs(length) * 250) / width))
            self._tabList[self._pressedIndex].startAnimation(self, duration)
            self._dragInProgress = False;
            self._movingTab.setVisible(False);
            self._dragStartPosition = QPoint();
        if self.tabAt(ev.pos()) == self._pressedIndex:
            i = self._pressedIndex
        else:
            i = -1
        self._pressedIndex = -1
        baseOpt = QStyleOptionTabBarBaseV2()
        baseOpt.initFrom(self)
        baseOpt.documentMode = self.documentMode
        if (self.style().styleHint(QStyle.SH_TabBar_SelectMouseType, baseOpt, self) 
            == QEvent.MouseButtonRelease):
            self.currentIndex = i
        
    def paintEvent(self, ev : QPaintEvent):
        #Draw the base
        optBase = QStyleOptionTabBarBaseV2()
        self.initStyleBaseOption(optBase, self, self.size())

        p = QStylePainter(self)
        
        #Tab being moved
        cut = -1
        rtl = optBase.direction == Qt.RightToLeft
        vertical = self.vertical
        
        cutTab = QStyleOptionTab()
        
        #Currently selected tab
        if self._dragInProgress:
            selected = self._pressedIndex
        else:
            selected = self.currentIndex
        
        #Add together all the tab rects
        for i in range(self.count):
            optBase.tabBarRect |= self.tabRect(i)
        
        #Set the rect for the currentIndex
        optBase.selectedTabRect = self.tabRect(selected)
        
        #Draw the tab base
        #Why do we need to do the above if this is only used when the base is drawn?
        if self.drawBase:
            p.drawPrimitive(QStyle.PE_FrameTabBarBase, optBase)

        for i in range(self.count):
            optTab = QStyleOptionTabV3()
            self.initStyleOption(optTab, i)
            if self._paintWithOffsets and self._tabList[i].dragOffset != 0:
                if vertical:
                    optTab.rect.moveTop(optTab.rect.y() + self._tabList[i].dragOffset)
                else:
                    optTab.rect.moveLeft(optTab.rect.x() + self._tabList[i].dragOffset)
            if not (optTab.state & QStyle.State_Enabled):
                optTab.palette.setCurrentColorGroup(QPalette.Disabled)

            # If this tab is partially obscured, make a note of it so that we can pass the information
            # along when we draw the tear.
            if (((not vertical and not rtl and optTab.rect.left() < 0)
                    or (rtl and optTab.rect.right() > width()))
                    or (vertical and optTab.rect.top() < 0)):
                cut = i
                cutTab = optTab

            # Don't bother drawing a tab if the entire tab is outside of the visible tab bar.
            if ((not vertical and (optTab.rect.right() < 0 or optTab.rect.left() > width()))
                or (vertical and (optTab.rect.bottom() < 0 or optTab.rect.top() > height()))):
                continue

            optBase.tabBarRect |= tab.rect
            if i == selected:
                continue
            
            p.drawControl(QStyle.CE_TabBarTab, optTab)

        # Draw the selected tab last to get it "on top"
        if selected >= 0:
            optTab = QStyleOptionTabV3()
            self.initStyleOption(optTab, selected)
            if self._paintWithOffsets and self._tabList[selected].dragOffset != 0:
                if vertical:
                    optTab.rect.moveTop(optTab.rect.y() + self._tabList[selected].dragOffset)
                else:
                    optTab.rect.moveLeft(optTab.rect.x() + self._tabList[selected].dragOffset)
            if not self._dragInProgress:
                p.drawControl(QStyle.CE_TabBarTab, optTab)
            else:
                overlap = style().pixelMetric(QStyle.PM_TabBarTabOverlap, None, self)
                self._movingTab.setGeometry(tab.rect.adjusted(-overlap, 0, overlap, 0));

        # Only draw the tear indicator if necessary. Most of the time we don't need to.
        if (self._leftB.isVisible() and cut >= 0):
            cutTab.rect = style().subElementRect(QStyle.SE_TabBarTearIndicator, cutTab, self)
            p.drawPrimitive(QStyle.PE_IndicatorTabTear, cutTab)
    
    def resizeEvent(self, ev : QResizeEvent):
        if self._layoutDirty:
            self.updateGeometry()
        self._layoutTabs()
        self._makeVisible(self.currentIndex)
    
    def wheelEvent(self, ev : QWheelEvent):
        offset = -1 if (ev.delta() > 0) else 1
        self._setNextEnabledIndex(offset)
        super(QWidget, self).wheelEvent(ev)
    
    def showEvent(self, ev : QShowEvent):
        if self._layoutDirty:
            self._refresh()
        if not self.isValidIndex(self.currentIndex):
            self.currentIndex = 0
    #    self._updateMacBorderMetrics()

    def hideEvent(self, ev : QHideEvent):
    #    d.updateMacBorderMetrics();
        pass

    def _setNextEnabledIndex(self, offset : int):
        index = self.currentIndex + offset
        while self._isValidIndex(index):
            if self._tabList[index].enabled:
                self.currentIndex = index
                return
            index += offset
        
    def _makeVisible(self, index : int):
        if not self.isValidIndex(index) or self.leftB.isHidden():
            return

        tabRect = self._tabList[index].rect
        oldScrollOffset = self._scrollOffset
        horiz = not self.vertical
        available = (self.width() if horiz else self.height()) - extraWidth()
        start = tabRect.left() if horiz else tabRect.top()
        end = tabRect.right() if horiz else tabRect.bottom()
        if (start < self._scrollOffset): # too far left
            self._scrollOffset = start - (8 if index else 0)
        elif (end > self._scrollOffset + available): # too far right
            self._scrollOffset = end - available + 1

        self.leftB.setEnabled(self._scrollOffset > 0)
        last = self._tabList[-1].rect.right() if horiz else self._tabList[-1].rect.bottom()
        self.rightB.setEnabled(last - self._scrollOffset >= available)
        if (oldScrollOffset != self._scrollOffset):
            self.update()
            self._layoutWidgets()

    def _layoutTab(self, index : int):
        if not self.isValidIndex(index):
            return

        tab = self._tabList[index]
        if not (tab.leftWidget or tab.rightWidget):
            return

        opt = QStyleOptionTabV3()
        self.initStyleOption(opt, index)
        if (tab.leftWidget):
            rect = self.style().subElementRect(QStyle.SE_TabBarTabLeftButton, opt, self)
            p = rect.topLeft()
            if (index == self._pressedIndex) or self._paintWithOffsets:
                if self.vertical:
                    p.setY(p.y() + tab.dragOffset)
                else:
                    p.setX(p.x() + tab.dragOffset)
            tab.leftWidget.move(p)
        if tab.rightWidget:
            rect = self.style().subElementRect(QStyle.SE_TabBarTabRightButton, opt, self)
            p = rect.topLeft()
            if (index == self._pressedIndex) or self._paintWithOffsets:
                if self.vertical:
                    p.setY(p.y() + tab.dragOffset)
                else:
                    p.setX(p.x() + tab.dragOffset)
            tab.rightWidget.move(p)

    def _closeTab(self):
        sender = self.sender()
        tabToClose = -1
        closeSide = self.style().styleHint(QStyle.SH_TabBar_CloseButtonPosition, None, self)
        if closeSide == QTabBar.LeftSide:
            for i in range(self.count):
                if self._tabList[i].leftWidget == sender:
                    tabToClose = i
                    break
        else:
            for i in range(self.count):
                if self._tabList[i].rightWidget == sender:
                    tabToClose = i
                    break
        if tabToClose != -1:
            self.tabCloseRequested.emit(tabToClose)

    def _layoutWidgets(start : int):
        for i in range(self.count):
            self._layoutTab(i)
            
    def _setupMovableTab(self):
        if not self._movingTab:
            self._movingTab = QWidget(self)

        overlap = self.style().pixelMetric(QStyle.PM_TabBarTabOverlap, None, self)
        grabRect = self.tabRect(self._pressedIndex);
        grabRect.adjust(0 - overlap, 0, overlap, 0)

        grabImage = QPixmap(grabRect.size());
        grabImage.fill(Qt.transparent)
        p = QStylePainter(grabImage, self)
        p.initFrom(self)

        opt = QStyleOptionTabV3()
        self.initStyleOption(opt, self._pressedIndex);
        opt.rect.moveTopLeft(QPoint(overlap, 0));
        p.drawControl(QStyle.CE_TabBarTab, opt);
        p.end()

        pal = QPalette()
        pal.setBrush(QPalette.All, QPalette.Window, grabImage);
        movingTab.setPalette(pal);
        movingTab.setGeometry(grabRect);
        movingTab.setAutoFillBackground(True);
        movingTab.raise_()
    
    def _refresh(self):
        # be safe in case a subclass is also handling move with the tabs
        if (self._pressedIndex != -1
                and self.movable
                and QApplication.mouseButtons() == Qt.NoButton):
            self._moveTabFinished(self._pressedIndex)
            if not self.isValidIndex(self._pressedIndex):
                self._pressedIndex = -1

        if not self.isVisible():
            self._layoutDirty = True
        else:
            self._layoutTabs()
            self._makeVisible(self._currentIndex)
            self.update()
            self.updateGeometry()
            
    def _scrollTabs(self):
        sender = self.sender()
        if not self.vertical:
            if sender == self._leftB:
                for i in range(self.count - 1, 0, -1):
                    if (self._tabList[i].rect.left()) - self._scrollOffset < 0:
                        self._makeVisible(i)
                        return
            elif sender == self._rightB:
                availableWidth = self.width() - self._extraWidth()
                for i in range(self.count):
                    if (self._tabList[i].rect.right() - scrollOffset) > availableWidth:
                        self._makeVisible(i)
                        return
        else: # vertical
            if sender == self._leftB:
                for i in range(self.count - 1, 0, -1):
                    if (self._tabList[i].rect.top() - scrollOffset < 0):
                        self._makeVisible(i)
                        return
            elif sender == self._rightB:
                availableWidth = self.height() - extraWidth()
                for i in range(self.count):
                    if (self._tabList[i].rect.bottom() - scrollOffset > availableWidth):
                        self._makeVisible(i)
                        return
    def _extraWidth(self) -> int:
        return 2 * max((QApplication.globalStrut().width(), 
                        self.style().pixelMetric(QStyle.PM_TabBarScrollButtonWidth, None, self)))

    def _minimumTabSizeHint(self, index : int) -> QSize:
        tab = tabList[index]
        oldText = str(tab.text)
        tab.text = self._computeElidedText(elideMode, oldText)
        size = self.tabSizeHint(index)
        tab.text = oldText
        return size
        
    def tabSizeHint(index : int) -> QSize:
        #Note: this must match with the computations in QCommonStylePrivate.tabLayout
        if not self.isValidIndex(index):
            return QSize()
        tab = self._tabList[index]
        opt = QStyleOptionTabV3()
        self.initStyleOption(opt, index)
        opt.text = tab.text
        iconSize = QSize(0, 0) if tab.icon.isNull() else opt.iconSize
        hframe = style().pixelMetric(QStyle.PM_TabBarTabHSpace, opt, self)
        vframe = style().pixelMetric(QStyle.PM_TabBarTabVSpace, opt, self)
        fm = self.fontMetrics()

        maxWidgetHeight = max((opt.leftButtonSize.height(), opt.rightButtonSize.height()))
        maxWidgetWidth = min((opt.leftButtonSize.width(), opt.rightButtonSize.width()))

        widgetWidth = 0
        widgetHeight = 0
        padding = 0
        if not opt.leftButtonSize.isEmpty():
            padding += 4
            widgetWidth += opt.leftButtonSize.width()
            widgetHeight += opt.leftButtonSize.height()
        
        if not opt.rightButtonSize.isEmpty():
            padding += 4
            widgetWidth += opt.rightButtonSize.width()
            widgetHeight += opt.rightButtonSize.height()
        
        if not opt.icon.isNull():
            padding += 4
        
        if self.vertical:
            w = max((maxWidgetWidth, fm.height(), iconSize.height())) + vframe
            w += fm.size(Qt.TextShowMnemonic, tab.text).width()
            h = iconSize.width() + hframe + widgetHeight + padding
        else:
            w = fm.size(Qt.TextShowMnemonic, tab.text).width()
            w += iconSize.width() + hframe + widgetWidth + padding
            h = max((maxWidgetHeight, fm.height(), iconSize.height())) + vframe

        return style().sizeFromContents(QStyle.CT_TabBarTab, opt, QSize(w, h), self)

    def _slide(self, start : int, end : int):
        if (start == end
                or not self.isValidIndex(start)
                or not self.isValidIndex(end)):
            return
        vertical = verticalTabs(shape)
        preLocation = self.tabRect(start).y() if vertical else self.tabRect(start).x()
        self.setUpdatesEnabled(False)
        self.moveTab(start, end)
        self.setUpdatesEnabled(True)
        postLocation = self.tabRect(end).y() if vertical else self.tabRect(end).x();
        length = postLocation - preLocation
        tabList[end].dragOffset -= length
        tabList[end].startAnimation(self, 250)

    def _moveTabFinished(self, index : int):
        cleanup = (pressedIndex == index 
                   or pressedIndex == -1 
                   or not self.isValidIndex(index))
        allAnimationsFinished = True;
        for tab in iter(self._tabList):
            if tab.animation and tab.animation.state() == QAbstractAnimation.Running:
                allAnimationsFinished = False
                break
        if (allAnimationsFinished and cleanup):
            if self._movingTab:
                self._movingTab.setVisible(False) # We might not get a mouse release
            for tab in iter(self._tabList):
                tab.dragOffset = 0
            if self._pressedIndex != -1 and self.movable:
                self._pressedIndex = -1;
                self._dragInProgress = False;
                self._dragStartPosition = QPoint()
            self._layoutWidgets()
        else:
            if not self.isValidIndex(index):
                return
            self._tabList[index].dragOffset = 0
        self.update()
