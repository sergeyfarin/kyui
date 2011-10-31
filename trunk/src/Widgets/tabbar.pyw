from PyQt4.QtCore import *
from PyQt4.QtGui import *
    
from .closebutton import CloseButton

def isVertical(position : QTabWidget.TabPosition):
    return (position == QTabWidget.West or position == QTabWidget.East)
    
def convertTabWidgetShape(position, shape):
    ret = int(position)
    if shape != QTabWidget.Rounded:
         ret += 4
    return QTabBar.Shape(position)

def computeElidedText(mode : Qt.TextElideMode, text : str) -> str:
        if len(text) < 8 or self.mode == Qt.ElideNone:
            return text
        text = text[:]
        ellipses = '...'
        if self.mode == Qt.ElideRight:
            return text[0:3] + ellipses
        elif self.mode == Qt.ElideMiddle:
            return text[0:1] + ellipses + text[-2:-1]
        elif self.mode == Qt.ElideLeft:
            return ellipses + text[-4:-1]
        return ellipses

class Tab():
    __slots__ = ['enabled', 'shortcutId', 'text', 'icon', 'toolTip', 'whatsThis', 
                 'textColor', 'tabData', 'leftWidget', 'rightWidget', 'lastTab', 
                 'dragOffset', 'animation', 'rect', 'minRect', 'maxRect']
    def __init__(self, icon : QIcon, text : str):
        self.enabled = True
        self.shortcutId = 0
        self.text = text
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
        
        self._refresh()
        
    def __len__(self) -> int:
        return self.count
        
    #==================================================#
    # Property Getters                                 #
    #==================================================#
    def getCount(self):
        return len(self._tabList)
        
    def getCurrentIndex(self) -> int:
        if self.isValidIndex(self.__currentIndex):
            return self.__currentIndex
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
        if self.__iconSize.isValid():
            return self.__iconSize
        size = style().pixelMetric(QStyle.PM_TabBarIconSize, None, self)
        return QSize(size, size)
        
    def getMovable(self) -> bool:
        return self.__movable
    
    def getPosition(self) -> QTabWidget.TabPosition:
        return self.__position
        
    def getSelectionBehaviorOnRemove(self) -> QTabBar.SelectionBehavior:
        return self.__selectionBehavior
        
    def getShape(self) -> QTabWidget.TabShape:
        return self.__shape
        
    def getTabsClosable(self) -> bool:
        return self.__tabsClosable
        
    def getUsesScrollButtons(self) -> bool:
        return self.__useScroll
        
    def getVertical(self) -> bool:
        return self.__vertical
    #==================================================#
    # Property Setters                                 #
    #==================================================#
    def setCurrentIndex(self, index : int):
        if self._dragInProgress and self._pressedIndex != -1:
            return
        if not self.isValidIndex(index) or self.__currentIndex == index:
            return
#        oldIndex = int(self.__currentIndex)
        self.__currentIndex = index
        self.update()
#        self._makeVisible(index)
#        self._tabList[index].lastTab = oldIndex
#        if oldIndex >= 0 and oldIndex < self.count()
#            self._layoutTab(oldIndex)
#        self._layoutTab(index)
        self.currentChanged.emit(index)
    
    def setDocumentMode (self, mode : bool):
        if self.__docMode == mode:
            return
        self.__docMode = mode
        #self._updateMacBorderMetrics()
    
    def setDrawBase(self, drawBase : bool):
        if self.__drawBase == drawBase:
            return
        self.__drawBase = drawBase
        self.update()
        
    def setElideMode(self, mode: Qt.TextElideMode):
        self._manualElideMode = True
        if self.__elideMode == mode:
            return
        self.__elideMode = mode
        self._refresh()
        
    def setExpanding(self, enabled : bool):
        if self.__expanding == enabled:
            return
        self.__expanding = enabled
        self._layoutTabs()

    def setIconSize(self, size : QSize):
        self.__iconSize = size
        self._layoutDirty = True
        self.update()
        self.updateGeometry()

    def setMovable(self, movable : bool):
        self.__movable = movable
        
    def setPosition(self, position : QTabWidget.TabPosition):
        if self.__position == position:
            return
        self.__position = position
        self.__vertical = isVertical(position)
        self._refresh()
        
    def setSelectionBehaviorOnRemove (self, behavior : QTabBar.SelectionBehavior):
        self.__selectionBehavior = behavior

    def setShape(self, shape : QTabWidget.TabShape):
        if self.__shape == shape:
            return
        self.__shape = shape
        self._refresh()

    def setTabButton(self, 
                     index : int, 
                     position : QTabBar.ButtonPosition, 
                     widget : QWidget):
        if not self.isValidIndex(index):
            return
        if widget:
            widget.setParent(self)
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

    def setTabsClosable(self, closable : bool):
        if self.__tabsClosable == closable:
            return
        self.__tabsClosable = closable
        closeSide = self.style().styleHint(QStyle.SH_TabBar_CloseButtonPosition, 
                                           None, self)
        if not closable:
            for tab in iter(self._tabList):
                if closeSide == QTabBar.LeftSide and tab.leftWidget:
                    tab.leftWidget.deleteLater()
                    tab.leftWidget = None
                if closeSide == QTabBar.RightSide and tab.rightWidget:
                    tab.rightWidget.deleteLater()
                    tab.rightWidget = None
        else:
            newButtons = False
            for i in range(self.count):
                if self.tabButton(i, closeSide):
                    continue
                newButtons = True
                closeButton = CloseButton(self)
                closeButton.clicked.connect(self._closeTab)
                self.setTabButton(i, closeSide, closeButton)
            if newButtons:
                self._layoutTabs()
        self.update()

    def setUsesScrollButtons(self, useButtons : bool):
        self._manualScrollSet = True
        if self.__useScroll == useButtons:
            return
        self.__useScroll = useButtons
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
    position = pyqtProperty(QTabWidget.TabPosition, fget=getPosition, fset=setPosition)
    selectionBehaviorOnRemove = pyqtProperty(QTabBar.SelectionBehavior, 
                                             fget=getSelectionBehaviorOnRemove, 
                                             fset=setSelectionBehaviorOnRemove)
    shape = pyqtProperty(QTabWidget.TabShape, fget=getShape, fset=setShape)
    tabsClosable = pyqtProperty(bool, fget=getTabsClosable, fset=setTabsClosable)
    usesScrollButtons = pyqtProperty(bool, 
                                     fget=getUsesScrollButtons, 
                                     fset=setUsesScrollButtons)
    vertical = pyqtProperty(bool, fget=getVertical)

    #==================================================#
    # Public Methods                                   #
    #==================================================#
    def addTab(self, *args):
        if len(args) == 1:
            text = args[0] if isinstance(args[0], str) else ''
            icon = QIcon()
        elif len(args) == 2:
            icon = args[0] if isinstance(args[0], QIcon) else QIcon()
            text = args[1] if isinstance(args[1], str) else ''
        else:
            raise ArgumentError
        return self.insertTab(-1, icon, text)
    
    def insertTab(self, *args) -> int:
        if len(args) == 2:
            index = args[0] if isinstance(args[0], int) else -1
            text = args[1] if isinstance(args[0], str) else ''
            icon = QIcon()
        elif len(args) == 3:
            index = args[0] if isinstance(args[0], int) else -1
            text = args[1] if isinstance(args[0], str) else ''
            icon = args[1] if isinstance(args[1], QIcon) else QIcon()
        else:
            raise ArgumentError
            return -1
        
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
        if not self.usesScrollButtons:
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
        return QSize(100, 25)

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
            
    def sizeHint(self) -> QSize:
        if self._layoutDirty:
           self._layoutTabs()
        rect = QRect()
        for tab in iter(self._tabList):
            rect = rect.united(tab.maxRect)
        return rect.size().expandedTo(QApplication.globalStrut())

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
            tab = self._tabList[index]
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
    
    def tabInserted (self, index : int):    pass
    def tabLayoutChange(self):              pass
    def tabRemoved (self, index : int):     pass
    
    def initStyleOption(self, opt : QStyleOptionTab, tabIndex : int):
        if not opt or not self.isValidIndex(tabIndex):
            return

        tab = self._tabList[tabIndex]
        opt.initFrom(self)
        opt.state &= ~(QStyle.State_HasFocus | QStyle.State_MouseOver)
        opt.rect = self.tabRect(tabIndex)
        opt.row = 0
        if tabIndex == self._pressedIndex:
            opt.state |= QStyle.State_Sunken
        if tabIndex == self.currentIndex:
            opt.state |= QStyle.State_Selected
            if self.hasFocus():
                opt.state |= QStyle.State_HasFocus
        if not tab.enabled:
            opt.state &= ~QStyle.State_Enabled
        if self.isActiveWindow():
            opt.state |= QStyle.State_Active
#        if not self._dragInProgress and opt.rect == self._hoverRect:
#            opt.state |= QStyle.State_MouseOver
        opt.shape = convertTabWidgetShape(self.position, self.shape)
        
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
        elif (tabIndex < self.count - 1) and (tabIndex + 1 == self.currentIndex):
            opt.selectedPosition = QStyleOptionTab.NextIsSelected
        else:
            opt.selectedPosition = QStyleOptionTab.NotAdjacent

        paintBeginning = ((tabIndex == 0) 
                          or (self._dragInProgress and tabIndex == self._pressedIndex + 1))
        paintEnd = ((tabIndex == self.count - 1) 
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
    #            opt.cornerWidgets |= QStyleOptionTab.LeftCornerWidget
    #        if (tw.cornerWidget(Qt.TopRightCorner) or tw.cornerWidget(Qt.BottomRightCorner))
    #            opt.cornerWidgets |= QStyleOptionTab.RightCornerWidget

        textRect = self.style().subElementRect(QStyle.SE_TabBarTabText, opt, self)
        opt.text = self.fontMetrics().elidedText(opt.text, self.elideMode, 
                                                 textRect.width(),
                                                 Qt.TextShowMnemonic)

    def initStyleBaseOption(self, optBase : QStyleOptionTabBarBaseV2):
        sz = self.size()
        tabOverlap = QStyleOptionTab()
        tabOverlap.shape = self.shape
        overlap = self.style().pixelMetric(QStyle.PM_TabBarBaseOverlap, tabOverlap, self)
        widget = self.parentWidget()
        optBase.init(self)
        optBase.shape = self.shape
        optBase.documentMode = self.documentMode
        if widget and overlap > 0:
            rect = QRect()
            if tabOverlap.shape == QTabWidget.North:
                rect.setRect(0, sz.height()-overlap, sz.width(), overlap)
            elif tabOverlap.shape == QTabWidget.South:
                rect.setRect(0, 0, sz.width(), overlap)
            elif tabOverlap.shape == QTabWidget.East:
                rect.setRect(0, 0, overlap, sz.height())
            elif tabOverlap.shape ==  QTabWidget.West:
                rect.setRect(sz.width() - overlap, 0, overlap, sz.height())
    
    def _layoutTabs(self):
        self._layoutDirty = False
#        rect = QRect()
        origin = QPoint(0, 0)
        for index in range(self.count):
            tab = self._tabList[index]
            tab.maxRect = QRect(origin, self.tabSizeHint(index))
            tab.minRect = QRect(origin, self.minimumTabSizeHint(index))
        for tab in iter(self._tabList):
            pass
        
    def _layoutTab(self, index : int):
        pass
        
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
            self._makeVisible(self.currentIndex)
            self.update()
            self.updateGeometry()
    
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
            
    def _moveTabFinished(self, index : int):
#        cleanup = (pressedIndex == index 
#                   or pressedIndex == -1 
#                   or not self.isValidIndex(index))
#        allAnimationsFinished = True
#        for tab in iter(self._tabList):
#            if tab.animation and tab.animation.state() == QAbstractAnimation.Running:
#                allAnimationsFinished = False
#                break
#        if (allAnimationsFinished and cleanup):
#            if self._movingTab:
#                self._movingTab.setVisible(False) # We might not get a mouse release
#            for tab in iter(self._tabList):
#                tab.dragOffset = 0
#            if self._pressedIndex != -1 and self.movable:
#                self._pressedIndex = -1
#                self._dragInProgress = False
#                self._dragStartPosition = QPoint()
#            self._layoutWidgets()
#        else:
#            if not self.isValidIndex(index):
#                return
#            self._tabList[index].dragOffset = 0
        self.update()
        
    def _scrollTabs(self):
        pass
        
    def _makeVisible(self, index : int):
        pass
        
    def _setNextEnabledIndex(self, offset : int):
        index = self.currentIndex + offset
        while self._isValidIndex(index):
            if self._tabList[index].enabled:
                self.currentIndex = index
                return
            index += offset
    
    def minimumTabSizeHint(self, index : int) -> QSize:
        tab = self._tabList[index]
        oldText = str(tab.text)
        tab.text = computeElidedText(self.elideMode, oldText)
        size = self.tabSizeHint(index)
        tab.text = oldText
        return size
    
    def tabSizeHint(self, index : int) -> QSize:
        #Note: this must match with the computations in QCommonStylePrivate.tabLayout
        opt = QStyleOptionTabV3()
        self.initStyleOption(opt, index)
        tab = self._tabList[index]
        opt.text = tab.text
        iconSize = QSize(0, 0) if tab.icon.isNull() else opt.iconSize
        hframe = self.style().pixelMetric(QStyle.PM_TabBarTabHSpace, opt, self)
        vframe = self.style().pixelMetric(QStyle.PM_TabBarTabVSpace, opt, self)
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

        return self.style().sizeFromContents(QStyle.CT_TabBarTab, opt, QSize(w, h), self)
    
    #==================================================#
    # Event Handling                                   #
    #==================================================#
#    def event(self, ev : QEvent) -> bool:
##        qDebug('event')
#        if (ev.type() == QEvent.ToolTip):
#            tab = self.tabAt(ev.pos())
#            if tab and tab.toolTip:
#                QToolTip.showText(ev.globalPos(), tab.toolTip, self)
#                return True
#        elif (ev.type() == QEvent.QueryWhatsThis):
#            tab = self.tabAt(ev.pos())
#            if not tab or not tab.whatsThis:
#                ev.ignore()
#            return True
#        elif (ev.type() == QEvent.WhatsThis):
#            tab = self.tabAt(ev.pos())
#            if tab and tab.whatsThis:
#                QWhatsThis.showText(ev.globalPos(), tab.whatsThis, self)
#                return True
#        elif (ev.type() == QEvent.Shortcut):
#            for tab in iter(self._tabList):
#                if tab.shortcutId == ev.shortcutId():
#                    self.currentIndex = self._tabList.index(tab)
#                    return True
#        return super(QWidget, self).event(ev)
    
    def keyPressEvent(self, ev : QEvent):
        qDebug('keyPressEvent')
        if (ev.key() != Qt.Key_Left and ev.key() != Qt.Key_Right):
            ev.ignore()
            return
        rtl = self.isRightToLeft()
        if ev.key() == Qt.Key_Right:
            offset = 1 if rtl else -1
        else:
            offset = -1 if rtl else 1
        self._setNextEnabledIndex(offset)
    
    def paintEvent(self, ev : QPaintEvent):
        qDebug('paintEvent')
        #Draw the base
        optBase = QStyleOptionTabBarBaseV2()
        self.initStyleBaseOption(optBase)

        p = QStylePainter(self)
        
        #Partially obscured tab
#        cut = -1
#        cutTab = QStyleOptionTab()
#        rtl = optBase.direction == Qt.RightToLeft
        
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
        
        #Draw the tab base if necessary
        if self.drawBase:
            p.drawPrimitive(QStyle.PE_FrameTabBarBase, optBase)

        for i in range(self.count):
            optTab = QStyleOptionTabV3()
            self.initStyleOption(optTab, i)
            if self._paintWithOffsets and self._tabList[i].dragOffset != 0:
                if self.vertical:
                    optTab.rect.moveTop(optTab.rect.y() + self._tabList[i].dragOffset)
                else:
                    optTab.rect.moveLeft(optTab.rect.x() + self._tabList[i].dragOffset)
            if not (optTab.state & QStyle.State_Enabled):
                optTab.palette.setCurrentColorGroup(QPalette.Disabled)

            # If this tab is partially obscured, make a note of it so that we can pass the information
            # along when we draw the tear.
#            if (((not self.vertical and not rtl and optTab.rect.left() < 0)
#                    or (rtl and optTab.rect.right() > width()))
#                    or (self.vertical and optTab.rect.top() < 0)):
#                cut = i
#                cutTab = optTab

            # Don't bother drawing a tab if the entire tab is outside of the visible tab bar.
            if ((not self.vertical and (optTab.rect.right() < 0 or optTab.rect.left() > width()))
                or (self.vertical and (optTab.rect.bottom() < 0 or optTab.rect.top() > height()))):
                continue

            optBase.tabBarRect |= tab.rect
            if i == selected:
                continue
            
            p.drawControl(QStyle.CE_TabBarTab, optTab)
        
    def showEvent(self, ev : QEvent):
#        qDebug('showEvent')
        if self._layoutDirty:
            self._refresh()
        if not self.isValidIndex(self.currentIndex):
            self.currentIndex = 0
        #self._updateMacBorderMetrics()

    def hideEvent(self, ev : QEvent):
        #self._updateMacBorderMetrics()
        pass
        
    def resizeEvent(self, ev : QResizeEvent):
        qDebug('resizeEvent')
        if self._layoutDirty:
            self.updateGeometry()
        self._layoutTabs()
        self._makeVisible(self.currentIndex)
