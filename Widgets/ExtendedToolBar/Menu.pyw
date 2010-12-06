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
    
    def paintEvent(self, ev : QPaintEvent):
        p = QPainter(self)
        emptyArea = QRegion(self.rect())
        style = self.style()
        
        # Draw the panel
        menuOpt = QStyleOptionMenuItem()
        menuOpt.initFrom(self)
        menuOpt.state = QStyle.State_None
        menuOpt.checkType = QStyleOptionMenuItem.NotCheckable
        menuOpt.maxIconWidth = 0
        menuOpt.tabWidth = 0
        style.drawPrimitive(QStyle.PE_PanelMenu, menuOpt, p, self)
        opt = QStyleOptionMenuItem()
        
        #draw the items that need updating..
        for act in self.actions():
            adjustedActionRect = self.actionGeometry(act)
            if not ev.rect().intersects(adjustedActionRect) or\
                    d.widgetItems.value(action):
               continue
            #set the clip region to be extra safe (and adjust for the scrollers)
            adjustedActionReg = QRegion(adjustedActionRect)
            emptyArea -= adjustedActionReg
            p.setClipRegion(adjustedActionReg)

            
            self.initStyleOption(opt, action)
            opt.rect = adjustedActionRect
            style.drawControl(QStyle.CE_MenuItem, opt, p, self)

        fw = style.pixelMetric(QStyle.PM_MenuPanelWidth, None, self)
        #draw the scroller regions..
#        if (d.scroll)
#            menuOpt.menuItemType = QStyleOptionMenuItem.Scroller
#            menuOpt.state |= QStyle.State_Enabled;
#            if (d.scroll.scrollFlags & QMenuPrivate.QMenuScroller.ScrollUp) {
#                menuOpt.rect.setRect(fw, fw, width() - (fw * 2), d.scrollerHeight());
#                emptyArea -= QRegion(menuOpt.rect);
#                p.setClipRect(menuOpt.rect);
#                style().drawControl(QStyle.CE_MenuScroller, &menuOpt, &p, self);
#            }
#            if (d.scroll.scrollFlags & QMenuPrivate.QMenuScroller.ScrollDown) {
#                menuOpt.rect.setRect(fw, height() - d.scrollerHeight() - fw, width() - (fw * 2),
#                                         d.scrollerHeight());
#                emptyArea -= QRegion(menuOpt.rect);
#                menuOpt.state |= QStyle.State_DownArrow;
#                p.setClipRect(menuOpt.rect);
#                style().drawControl(QStyle.CE_MenuScroller, &menuOpt, &p, self);
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
            frame.lineWidth = style.pixelMetric(QStyle.PM_MenuPanelWidth)
            frame.midLineWidth = 0;
            style.drawPrimitive(QStyle.PE_FrameMenu, frame, p, self)

        #finally the rest of the space
        p.setClipRegion(emptyArea)
        menuOpt.state = QStyle.State_None
        menuOpt.menuItemType = QStyleOptionMenuItem.EmptyArea
        menuOpt.checkType = QStyleOptionMenuItem.NotCheckable
        menuOpt.rect = self.rect()
        menuOpt.menuRect = self.rect();
        style.drawControl(QStyle.CE_MenuEmptyArea, menuOpt, p, self)
        
    def initStyleOption(option : QStyleOptionMenuItem, action : QAction):
        if not option or not action:
            return;

#        Q_D(const QMenu);
        option.initFrom(self);
        option.palette = self.palette();
        option.state = QStyle.State_None;
        
        #Check if the item is enabled/active
        if window().isActiveWindow():
            option.state |= QStyle.State_Active
        if self.isEnabled() and action.isEnabled() \
                and (not action.menu() or action.menu().isEnabled()):
            option.state |= QStyle.State_Enabled
        else:
            option.palette.setCurrentColorGroup(QPalette.Disabled)

        option.font = action.font().resolve(self.font())
        option.fontMetrics = QFontMetrics(option.font)
    
        activeAct = self.activeAction()
        if (activeAct and activeAct == action and not activeAct.isSeparator()):
            option.state |= QStyle.State_Selected
            if d.mouseDown: option.state |= QStyle.State_Sunken  ###
            else: option.state |= QStyle.State_None
        ###
        option.menuHasCheckableItems = d.hasCheckableItems;
        if not action.isCheckable():
            option.checkType = QStyleOptionMenuItem.NotCheckable
        else:
            if action.actionGroup() and action.actionGroup().isExclusive():
                option.checkType = QStyleOptionMenuItem.Exclusive 
            else: 
                option.checkType = QStyleOptionMenuItem.NonExclusive;
            option.checked = action.isChecked()
            
        if action.menu():
            option.menuItemType = QStyleOptionMenuItem.SubMenu
        elif action.isSeparator():
            option.menuItemType = QStyleOptionMenuItem.Separator
        elif self.defaultAction() == action:
            option.menuItemType = QStyleOptionMenuItem.DefaultItem
        else:
            option.menuItemType = QStyleOptionMenuItem.Normal
        if action.isIconVisibleInMenu():
            option.icon = action.icon()
        textAndAccel = action.text();
        if not textAndAccel.contains('\t'):
            seq = action.shortcut();
            if not seq.isEmpty():
                textAndAccel += QLatin1Char('\t') + seq.toString();
        option.text = textAndAccel
        option.tabWidth = d.tabWidth         ###
        option.maxIconWidth = d.maxIconWidth ###
        option.menuRect = self.rect()
