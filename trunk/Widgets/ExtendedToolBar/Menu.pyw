from PyQt4.QtCore import *
from PyQt4.QtGui import *

class KyMenu(QMenu):
    def __init__(self, title: str = None, parent : QObject = None):
        if title:
            super().__init__(title, parent)
        else:
            super().__init__(parent)
    
#    def paintEvent(self, ev : QPaintEvent):
#        p = QPainter(self)
#        emptyArea = QRegion(self.rect())
#        style = self.style()
#        
#        # Draw the panel
#        menuOpt = QStyleOptionMenuItem()
#        menuOpt.initFrom(self)
#        menuOpt.state = QStyle.State_None
#        menuOpt.checkType = QStyleOptionMenuItem.NotCheckable
#        menuOpt.maxIconWidth = 0
#        menuOpt.tabWidth = 0
#        style.drawPrimitive(QStyle.PE_PanelMenu, menuOpt, p, self)
#        
#        opt = QStyleOptionMenuItem()
#        #draw the items that need updating
#        for act in self.actions():
#            adjustedActionRect = self.actionGeometry(act)
#            self.initStyleOption(opt, act)
#            if act.isSeparator() and act.data() == 'named':
#                adjustedActionRect.setSize(self.__namedSeparatorSize(act, opt))
#            if not ev.rect().intersects(adjustedActionRect):
#               continue
#            #set the clip region to be extra safe (and adjust for the scrollers)
#            adjustedActionReg = QRegion(adjustedActionRect)
#            emptyArea -= adjustedActionReg
#            p.setClipRegion(adjustedActionReg)
#
#            opt.rect = adjustedActionRect
#            style.drawControl(QStyle.CE_MenuItem, opt, p, self)
#
#        fw = style.pixelMetric(QStyle.PM_MenuPanelWidth, None, self)
#        #draw the scroller regions..
##        if (d.scroll)
##            menuOpt.menuItemType = QStyleOptionMenuItem.Scroller
##            menuOpt.state |= QStyle.State_Enabled;
##            if (d.scroll.scrollFlags & QMenuPrivate.QMenuScroller.ScrollUp) {
##                menuOpt.rect.setRect(fw, fw, width() - (fw * 2), d.scrollerHeight());
##                emptyArea -= QRegion(menuOpt.rect);
##                p.setClipRect(menuOpt.rect);
##                style().drawControl(QStyle.CE_MenuScroller, &menuOpt, &p, self);
##            }
##            if (d.scroll.scrollFlags & QMenuPrivate.QMenuScroller.ScrollDown) {
##                menuOpt.rect.setRect(fw, height() - d.scrollerHeight() - fw, width() - (fw * 2),
##                                         d.scrollerHeight());
##                emptyArea -= QRegion(menuOpt.rect);
##                menuOpt.state |= QStyle.State_DownArrow;
##                p.setClipRect(menuOpt.rect);
##                style().drawControl(QStyle.CE_MenuScroller, &menuOpt, &p, self);
##            }
##        }
#        if self.isTearOffEnabled():
#            menuOpt.menuItemType = QStyleOptionMenuItem.TearOff
#            menuOpt.rect.setRect(fw, fw, width() - (fw * 2),
#                                 self.pixelMetric(QStyle.PM_MenuTearoffHeight, None, self))
##            if (d->scroll && d->scroll->scrollFlags & QMenuPrivate::QMenuScroller::ScrollUp)
##                menuOpt.rect.translate(0, d->scrollerHeight());
#            emptyArea -= QRegion(menuOpt.rect);
#            p.setClipRect(menuOpt.rect);
#            menuOpt.state = QStyle.State_None;
#            if (d->tearoffHighlighted)
#                menuOpt.state |= QStyle.State_Selected;
#            self.drawControl(QStyle.CE_MenuTearoff, menuOpt, p, self);
#            #draw border
#        if (fw):
#            borderReg = QRegion();
#            borderReg += QRect(0, 0, fw, self.height()) #left
#            borderReg += QRect(self.width() - fw, 0, fw, self.height()) #right
#            borderReg += QRect(0, 0, self.width(), fw) #top
#            borderReg += QRect(0, self.height() - fw, self.width(), fw) #bottom
#            p.setClipRegion(borderReg)
#            emptyArea -= borderReg
#            frame = QStyleOptionFrame()
#            frame.rect = self.rect()
#            frame.palette = self.palette()
#            frame.state = QStyle.State_None;
#            frame.lineWidth = style.pixelMetric(QStyle.PM_MenuPanelWidth)
#            frame.midLineWidth = 0;
#            style.drawPrimitive(QStyle.PE_FrameMenu, frame, p, self)
#
#        #finally the rest of the space
#        p.setClipRegion(emptyArea)
#        menuOpt.state = QStyle.State_None
#        menuOpt.menuItemType = QStyleOptionMenuItem.EmptyArea
#        menuOpt.checkType = QStyleOptionMenuItem.NotCheckable
#        menuOpt.rect = self.rect()
#        menuOpt.menuRect = self.rect();
#        style.drawControl(QStyle.CE_MenuEmptyArea, menuOpt, p, self)
#        
#    def initStyleOption(self, opt : QStyleOptionMenuItem, act : QAction):
#        super().initStyleOption(opt, act)
        
    def sizeHint(self) -> QSize:
        sz = super().sizeHint()
        opt = QStyleOptionMenuItem()
        for act in self.actions():
            if act.isSeparator() and act.data() == 'named':
                self.initStyleOption(opt, act)
                size = self.__namedSeparatorSize(act, opt)
                if size.width() > sz.width(): sz.setWidth(size.width())
        return sz
    
    def __namedSeparatorSize(self, act, opt):
        fm = QFontMetrics(opt.font)
        qfm = self.fontMetrics()
        
        icone = self.style().pixelMetric(QStyle.PM_SmallIconSize, opt, self)
        
        sz = QSize()
        text = act.text()
        
        #remove the shortcut key if one was accidently set
        if '\t' in text:
            text = text.rsplit('\t')[0]
        
        sz.setWidth(fm.boundingRect(QRect(), Qt.TextSingleLine | Qt.TextHideMnemonic, text).width())
        sz.setHeight(fm.height() if (fm.height() > qfm.height()) else qfm.height())

        icon = act.icon();
        if not icon.isNull() and icone > sz.height():
            sz.setHeight(icone)
        return self.style().sizeFromContents(QStyle.CT_MenuItem, opt, sz, self)
