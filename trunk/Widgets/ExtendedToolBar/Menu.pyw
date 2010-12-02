from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Menu(QMenu):
    def __init__(self, title: str = None, parent : QObject = None):
        if title:
            parent().__init__(title, parent)
        else:
            parent().__init__(parent)
        
    def addAction(self, act : QAction, iconSize : QSize = None):
        if not iconSize:
            super(QMenu, self).addAction(act)
    
    def paintEvent(self, ev : QPaintEvent) -> None:
        p = QPainter(self)
        emptyArea = QRegion(self.rect())

        menuOpt = QStyleOptionMenuItem()
        menuOpt.initFrom(self)
        menuOpt.state = QStyle.State_None
        menuOpt.checkType = QStyleOptionMenuItem.NotCheckable;
        menuOpt.maxIconWidth = 0;
        menuOpt.tabWidth = 0;
        self.style().drawPrimitive(QStyle.PE_PanelMenu, menuOpt, p, self);

        #draw the items that need updating..
        for act in self.actions():
            adjustedActionRect = d.actionRects.at(i)
            if not ev.rect().intersects(adjustedActionRect) or\
                    d.widgetItems.value(action):
               continue
            #set the clip region to be extra safe (and adjust for the scrollers)
            adjustedActionReg = QRegion(adjustedActionRect)
            emptyArea -= adjustedActionReg
            p.setClipRegion(adjustedActionReg)

            opt = QStyleOptionMenuItem()
            self.initStyleOption(opt, action)
            opt.rect = adjustedActionRect
            self.style().drawControl(QStyle.CE_MenuItem, opt, p, self)

        fw = self.style().pixelMetric(QStyle.PM_MenuPanelWidth, None, self)
        #draw the scroller regions..
#        if (d.scroll)
#            menuOpt.menuItemType = QStyleOptionMenuItem.Scroller
#            menuOpt.state |= QStyle.State_Enabled;
#            if (d->scroll->scrollFlags & QMenuPrivate.QMenuScroller.ScrollUp) {
#                menuOpt.rect.setRect(fw, fw, width() - (fw * 2), d->scrollerHeight());
#                emptyArea -= QRegion(menuOpt.rect);
#                p.setClipRect(menuOpt.rect);
#                style()->drawControl(QStyle.CE_MenuScroller, &menuOpt, &p, self);
#            }
#            if (d->scroll->scrollFlags & QMenuPrivate.QMenuScroller.ScrollDown) {
#                menuOpt.rect.setRect(fw, height() - d->scrollerHeight() - fw, width() - (fw * 2),
#                                         d->scrollerHeight());
#                emptyArea -= QRegion(menuOpt.rect);
#                menuOpt.state |= QStyle.State_DownArrow;
#                p.setClipRect(menuOpt.rect);
#                style()->drawControl(QStyle.CE_MenuScroller, &menuOpt, &p, self);
#            }
#        }
        #draw border
        if (fw):
            borderReg = QRegion();
            borderReg += QRect(0, 0, fw, self.height()) #left
            borderReg += QRect(self.width() - fw, 0, fw, self.height()) #right
            borderReg += QRect(0, 0, self.width(), fw) #top
            borderReg += QRect(0, self.height() - fw, self.width(), fw); #bottom
            p.setClipRegion(borderReg)
            emptyArea -= borderReg
            frame = QStyleOptionFrame()
            frame.rect = self.rect()
            frame.palette = self.palette()
            frame.state = QStyle.State_None;
            frame.lineWidth = self.style().pixelMetric(QStyle.PM_MenuPanelWidth)
            frame.midLineWidth = 0;
            self.style().drawPrimitive(QStyle.PE_FrameMenu, frame, p, self)

        #finally the rest of the space
        p.setClipRegion(emptyArea)
        menuOpt.state = QStyle.State_None
        menuOpt.menuItemType = QStyleOptionMenuItem.EmptyArea
        menuOpt.checkType = QStyleOptionMenuItem.NotCheckable
        menuOpt.rect = self.rect()
        menuOpt.menuRect = self.rect();
        self.style().drawControl(QStyle.CE_MenuEmptyArea, menuOpt, p, self)
