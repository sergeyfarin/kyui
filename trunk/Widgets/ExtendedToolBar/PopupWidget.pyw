#ModelessPopup

from PyQt4.QtCore import *
from PyQt4.QtGui import *
# Control Elements
#QStyle.CE_MenuItem	    14	A menu item in a QMenu.
#QStyle.CE_MenuScroller	15	Scrolling areas in a QMenu when the style supports scrolling.
#QStyle.CE_MenuTearoff	    18	A menu item representing the tear off section of a QMenu.
#QStyle.CE_MenuEmptyArea	19	The area in a menu without menu items.
#QStyle.CE_MenuHMargin	    17	The horizontal extra space on the left/right of a menu.
#QStyle.CE_MenuVMargin	    16	The vertical extra space on the top/bottom of a menu.

# Pixel Metrics
#QStyle.PM_MenuPanelWidth	        30	Border width (applied on all sides) for a QMenu.
#QStyle.PM_MenuHMargin	            28	Additional border (used on left and right) for a QMenu.
#QStyle.PM_MenuVMargin	            29	Additional border (used for bottom and top) for a QMenu.
#QStyle.PM_MenuScrollerHeight	    27	Height of the scroller area in a QMenu.
#QStyle.PM_MenuTearoffHeight	    31	Height of a tear off area in a QMenu.
#QStyle.PM_MenuDesktopFrameWidth	32	The frame width for the menu on the desktop.

# Primitives
# QStyle.PE_FrameMenu	11	Frame for popup windows/menus; see also QMenu.
# QStyle.PE_PanelMenu	?	The panel for a menu.

# Contents Types
# QStyle.CT_Menu	11	A menu, like QMenu.

class PopupWidget(QWidget):
    def __init__(self, parent : QWidget = None):
        super().__init__(parent, Qt.Popup | Qt.CustomizeWindowHint)
        
    def adjustedPosition(self) -> QPoint:
        parent = self.parentWidget()
        desk = QApplication.desktop()
        horizontal = True
        
        if parent.parentWidget() and parent.parentWidget().orientation() == Qt.Vertical:
            horizontal = False
                
        rect = parent.geometry()
        rect.setRect(rect.x() - parent.x(), rect.y() - parent.y(), rect.width(), rect.height())

        size = self.sizeHint()
        globalPos = parent.mapToGlobal(rect.topLeft())
        x = globalPos.x()
        y = globalPos.y()
        if horizontal:
            if globalPos.y() + rect.height() + size.height() <= desk.availableGeometry(parent).height():
                y += rect.height();
            else:
                y -= size.height();
            if (parent.layoutDirection() == Qt.RightToLeft):
                x += rect.width() - size.width()
        else: #vertical
            if globalPos.x() + rect.width() + menu.sizeHint().width() <= desk.availableGeometry(parent).width():
                x += rect.width()
            else:
                x -= size.width()
        return QPoint(x,y)

    def show(self):
        pos = self.adjustedPosition()
        self.setGeometry(pos.x(), pos.y(), self.sizeHint().width(), self.sizeHint().height())
        super().show()
        
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
#        for (int i = 0; i < d->actions.count(); ++i) {
#            QAction *action = d->actions.at(i);
#            QRect adjustedActionRect = d->actionRects.at(i);
#            if (!e->rect().intersects(adjustedActionRect)
#                || d->widgetItems.value(action))
#               continue;
#            #set the clip region to be extra safe (and adjust for the scrollers)
#            QRegion adjustedActionReg(adjustedActionRect);
#            emptyArea -= adjustedActionReg;
#            p.setClipRegion(adjustedActionReg);
#
#            QStyleOptionMenuItem opt;
#            initStyleOption(&opt, action);
#            opt.rect = adjustedActionRect;
#            style()->drawControl(QStyle.CE_MenuItem, &opt, &p, self);
#        }

        fw = self.style().pixelMetric(QStyle.PM_MenuPanelWidth, None, self)
        #draw the scroller regions..
#        if (d->scroll) {
#            menuOpt.menuItemType = QStyleOptionMenuItem.Scroller;
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
            self.style().drawPrimitive(QStyle.PE_FrameMenu, frame, p, self);

        #finally the rest of the space
        p.setClipRegion(emptyArea)
        menuOpt.state = QStyle.State_None
        menuOpt.menuItemType = QStyleOptionMenuItem.EmptyArea
        menuOpt.checkType = QStyleOptionMenuItem.NotCheckable
        menuOpt.rect = self.rect()
        menuOpt.menuRect = self.rect();
        self.style().drawControl(QStyle.CE_MenuEmptyArea, menuOpt, p, self)
        
    
    
class GenericDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setObjectName('dialog')
        self.setWindowTitle('Test')
        #self.resize(371, 151)
        
        self.__setupUi()
        
    def __setupUi(self):
        self.__layout = QVBoxLayout(self)
        self.__layout.setObjectName('layout')
        
        button = QToolButton(self)
        button.setText('Test Button')
#        button.setFixedSize(75, 23)
        button.setPopupMode(QToolButton.InstantPopup)
    
        w = PopupWidget(button)
        w.layout = QVBoxLayout(w)
        w.buttonBox = QDialogButtonBox(QDialogButtonBox.Close, 
                                           Qt.Horizontal, w)
        w.layout.addWidget(w.buttonBox)
        w.buttonBox.clicked.connect(w.hide)
        button.clicked.connect(w.show)
        
        self.__layout.addWidget(button)
        
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok, 
                                          Qt.Horizontal, self)
        self.__layout.addWidget(self.buttonBox)
        self.buttonBox.accepted.connect(self.accept)
        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = GenericDialog()
    dialog.show()
    sys.exit(app.exec_())
