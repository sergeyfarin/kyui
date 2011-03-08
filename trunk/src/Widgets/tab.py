from PyQt4.QtCore import *
from PyQt4.QtGui import *

#Base:
#    QStyleOptionTabBarBaseV2
#    PE_FrameTabBarBase
#    PM_TabBarBaseOverlap
#Tab:
#    QStyleOptionTabV3
#    CE_TabBarTab
#    PM_TabBarTabOverlap #Only if tab is moving
#
#TearOff: 
#    SE_TabBarTearIndicator


def _layoutTabs(self):
    scrollOffset = 0
    self._layoutDirty = False
    size = self.size()
    last = -1
    available = 0
    maxExtent = 0
    i = 0
    tabChainIndex = 0

    tabAlignment = Qt.Alignment(self.style().styleHint(QStyle.SH_TabBar_Alignment, None, self))
    QVector<QLayoutStruct> tabChain(tabList.count() + 2)

    # We put an empty item at the front and back and set its expansive attribute
    # depending on tabAlignment.
    tabChain[tabChainIndex].init()
    tabChain[tabChainIndex].expansive = (tabAlignment != Qt.AlignLeft
                                        and tabAlignment != Qt.AlignJustify)
    tabChain[tabChainIndex].empty = True
    ++tabChainIndex

    # We now go through our list of tabs and set the minimum size and the size hint
    # This will allow us to elide text if necessary. Since we don't set
    # a maximum size, tabs will EXPAND to fill up the empty space.
    # Since tab widget is rather *ahem* strict about keeping the geometry of the
    # tab bar to its absolute minimum, this won't bleed through, but will show up
    # if you use tab bar on its own (a.k.a. not a bug, but a feature).
    # Update: if expanding is false, we DO set a maximum size to prevent the tabs
    # being wider than necessary.
    if not self.vertical:
        minx = 0
        x = 0
        maxHeight = 0
        for i in range(self.count):
            sz = self.tabSizeHint(i)
            self._tabList[i].maxRect = QRect(x, 0, sz.width(), sz.height())
            x += sz.width()
            maxHeight = qMax(maxHeight, sz.height())
            sz = minimumTabSizeHint(i)
            self._tabList[i].minRect = QRect(minx, 0, sz.width(), sz.height())
            minx += sz.width()
            tabChain[tabChainIndex].init()
            tabChain[tabChainIndex].sizeHint = self._tabList[i].maxRect.width()
            tabChain[tabChainIndex].minimumSize = sz.width()
            tabChain[tabChainIndex].empty = False
            tabChain[tabChainIndex].expansive = True

            if not expanding:
                tabChain[tabChainIndex].maximumSize = tabChain[tabChainIndex].sizeHint
            

        last = minx
        available = size.width()
        maxExtent = maxHeight
    else:
        miny = 0
        y = 0
        maxWidth = 0
        for i in range(self.count):
            sz = self.tabSizeHint(i)
            self._tabList[i].maxRect = QRect(0, y, sz.width(), sz.height())
            y += sz.height()
            maxWidth = qMax(maxWidth, sz.width())
            sz = minimumTabSizeHint(i)
            self._tabList[i].minRect = QRect(0, miny, sz.width(), sz.height())
            miny += sz.height()
            tabChain[tabChainIndex].init()
            tabChain[tabChainIndex].sizeHint = self._tabList[i].maxRect.height()
            tabChain[tabChainIndex].minimumSize = sz.height()
            tabChain[tabChainIndex].empty = False
            tabChain[tabChainIndex].expansive = True

            if not expanding:
                tabChain[tabChainIndex].maximumSize = tabChain[tabChainIndex].sizeHint
            tabChainIndex +=1

        last = miny
        available = size.height()
        maxExtent = maxWidth

    assert(tabChainIndex == tabChain.count() - 1) # add an assert just to make sure.
    # Mirror our front item.
    tabChain[tabChainIndex].init()
    tabChain[tabChainIndex].expansive = (tabAlignment != Qt.AlignRight
                                        and tabAlignment != Qt.AlignJustify)
    tabChain[tabChainIndex].empty = True

    # Do the calculation
    qGeomCalc(tabChain, 0, tabChain.count(), 0, qMax(available, last), 0)

    # Use the results
    for i in range(self.count):
        lstruct = tabChain.at(i + 1)
        if not vertTabs:
            self._tabList[i].rect.setRect(lstruct.pos, 0, lstruct.size, maxExtent)
        else:
            self._tabList[i].rect.setRect(0, lstruct.pos, maxExtent, lstruct.size)


    if (useScrollButtons and tabList.count() and last > available):
        extra = extraWidth()
        if not vertTabs:
            ld = self.layoutDirection()
            arrows = QStyle.visualRect(ld, self.rect(),
                                              QRect(available - extra, 0, extra, size.height()))
            buttonOverlap = self.style().pixelMetric(QStyle.PM_TabBar_ScrollButtonOverlap, None, self)

            if (ld == Qt.LeftToRight):
                self._leftB.setGeometry(arrows.left(), arrows.top(), extra/2, arrows.height())
                self._rightB.setGeometry(arrows.right() - extra/2 + buttonOverlap, arrows.top(),
                                    extra/2, arrows.height())
                self._leftB.setArrowType(Qt.LeftArrow)
                self._rightB.setArrowType(Qt.RightArrow)
            else:
                self._rightB.setGeometry(arrows.left(), arrows.top(), extra/2, arrows.height())
                self._leftB.setGeometry(arrows.right() - extra/2 + buttonOverlap, arrows.top(),
                                    extra/2, arrows.height())
                self._rightB.setArrowType(Qt.LeftArrow)
                self._leftB.setArrowType(Qt.RightArrow)
        else:
            arrows = QRect(0, available - extra, size.width(), extra)
            self._leftB.setGeometry(arrows.left(), arrows.top(), arrows.width(), extra/2)
            self._leftB.setArrowType(Qt.UpArrow)
            self._rightB.setGeometry(arrows.left(), arrows.bottom() - extra/2 + 1,
                                arrows.width(), extra/2)
            self._rightB.setArrowType(Qt.DownArrow)
        self._leftB.setEnabled(scrollOffset > 0)
        self._rightB.setEnabled(last - scrollOffset >= available - extra)
        self._leftB.show()
        self._rightB.show()
    else:
        self.rightB.hide()
        self.leftB.hide()

    self._layoutWidgets()
    self.tabLayoutChange()
    


