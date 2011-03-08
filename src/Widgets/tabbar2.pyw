from PyQt4.QtCore import *
from PyQt4.QtGui import *

class TabData():
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
        
class Tab(QWidget):
    def __init__(self, icon : QIcon, text : str, parent : QWidget):
        super().__init__(parent)
        self.setFocusPolicy(Qt.TabFocus)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        
        self.__text = text if isinstance(text, str) else ''
        self.__icon = icon if isinstance(icon, QIcon) else QIcon()
        iconMetric = self.style().pixelMetric(QStyle.PM_TabBarIconSize, None, self)
        self.__iconSize = QSize(iconMetric, iconMetric)
        self.__index = -1
        self.__leftWidget = None
        self.__rightWidget = None
        self.__shape = QTabBar.RoundedNorth
        self.__textColor = QColor(Qt.black)
        self.tabData = None
        
    def sizeHint(self):
        opt = QStyleOptionTabV3()
        self.initStyleOption(opt)
        iconSize = QSize(0, 0) if self.icon.isNull() else opt.iconSize
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
            w += fm.size(Qt.TextShowMnemonic, self.text).width()
            h = iconSize.width() + hframe + widgetHeight + padding
        else:
            w = fm.size(Qt.TextShowMnemonic, self.text).width()
            w += iconSize.width() + hframe + widgetWidth + padding
            h = max((maxWidgetHeight, fm.height(), iconSize.height())) + vframe
        
        return self.style().sizeFromContents(QStyle.CT_TabBarTab, opt, QSize(w, h), self)
    
    def minimumSizeHint(self):
        return QSize(75, 25)
        
    def initStyleOption(self, opt : QStyleOptionTabV3):
        opt.initFrom(self)
        opt.documentMode = False
        opt.cornerWidgets = QStyleOptionTab.NoCornerWidgets
        opt.text = self.text
        opt.row = 0
        opt.shape = self.shape
        opt.selectedPosition = QStyleOptionTab.NotAdjacent
        opt.position = QStyleOptionTab.Beginning
        if self.leftWidget:
            opt.leftButtonSize = self.leftWidget.size()
            opt.cornerWidgets |= QStyleOptionTab.LeftCornerWidget
        else:
            opt.leftButtonSize = QSize()
        if self.rightWidget:
            opt.rightButtonSize = self.rightWidget.size()
            opt.cornerWidgets |= QStyleOptionTab.RightCornerWidget
        else:
            opt.leftButtonSize = QSize()
        if self.icon:
            opt.iconSize = self.iconSize
            opt.icon = self.icon
        else:
            opt.iconSize = QSize()
            opt.icon = QIcon()
        
        opt.state &= ~(QStyle.State_HasFocus | QStyle.State_MouseOver)
#        opt.rect = self.tabRect(tabIndex)
#        if tabIndex == self._pressedIndex:
#            opt.state |= QStyle.State_Sunken
#        if self.selected:
#            opt.state |= QStyle.State_Selected
#            if self.hasFocus():
#                opt.state |= QStyle.State_HasFocus
        if not self.enabled:
            opt.state &= ~QStyle.State_Enabled
            opt.palette.setCurrentColorGroup(QPalette.Disabled)
        if self.isActiveWindow():
            opt.state |= QStyle.State_Active
        if self.textColor.isValid():
            opt.palette.setColor(self.foregroundRole(), self.textColor)
        
    def paintEvent(self, ev):
        p = QStylePainter(self)
        opt = QStyleOptionTabV3()
        self.initStyleOption(opt)
        
        p.drawControl(QStyle.CE_TabBarTab, opt)
    
    #==================================================#
    # Properties                                       #
    #==================================================#
    def isEnabled(self) -> bool:
        return super().isEnabled()
    def setEnabled(self, enabled):
        super().setEnabled(enabled)
    enabled = pyqtProperty(bool, fget=isEnabled, fset=setEnabled)
    
    def getSelected(self) -> bool:
        return self.__selected
        
    def setSelected(self, selected):
        if self.__selected == selected:
            return
        self.__selected = selected
        self.update()
    
    def getText(self) -> str:
        return self.__text[:]
    def setText(self, text) -> str:
        if self.__text == text:
            return
        self.__text = text[:]
        self.update()
        self.updateGeometry()
        
    text = pyqtProperty(str, fget=getText, fset=setText)
    
    def getIcon(self) -> QIcon:
        return self.__icon
    def setIcon(self, icon : QIcon):
        if not icon.isValid() and not self.__icon.isValid():
            return
        self.__icon = icon
        self.update()
        self.updateGeometry()
    icon = pyqtProperty(QIcon, fget=getIcon, fset=setIcon)
    
    def getIconSize(self) -> QSize:
        return self.__iconSize
    def setIconSize(self, size : QSize):
        if size.isValid() and self.__iconSize != size:
            self.__iconSize = size
    iconSize = pyqtProperty(QSize, fget=getIconSize, fset=setIconSize)
    
    def getToolTip(self) -> str:
        return self.__tooltip[:]
    def setToolTip(self, tooltip : str):
        self.__tooltip = tooltip[:]
    toolTip = pyqtProperty(str, fget=getToolTip, fset=setToolTip)
    
    def getLeftWidget(self) -> QWidget:
        return self.__leftWidget
    def setLeftWidget(self, widget):
        if self.__leftWidget == widget:
            return
        #Hide the old widget and delete it (quietly, in an poorly-lit alleyway)
        if self.__leftWidget:
            self.__leftWidget.hide()
            self.__leftWidget.setParent(None)
            del self.__leftWidget
        self.__leftWidget = widget
        #Take possession of the new widget so that it updates when the tab does
        if widget:
            widget.setParent(self)
    leftWidget = pyqtProperty(QWidget, fget=getLeftWidget, fset=setLeftWidget)
    
    def getRightWidget(self) -> QWidget:
        return self.__rightWidget
    def setRightWidget(self, widget):
        if self.__rightWidget == widget:
            return
        #Hide and delete the right widget (also done quietly, in a dark alley)
        if self.__rightWidget:
            self.__rightWidget.hide()
            self.__rightWidget.setParent(None)
            del self.__rightWidget
        self.__rightWidget = widget
        #Take possession of the new widget so that it updates when the tab does
        if widget:
            widget.setParent(self)
    
    rightWidget = pyqtProperty(QWidget, fget=getRightWidget, fset=setRightWidget)
    
    def getShape(self) -> QTabBar.Shape:
        return self.__shape
    def setShape(self, shape : QTabBar.Shape):
        if shape == self.__shape:
            return
        self.__shape = shape
        self.update()
        self.updateGeometry()
    shape = pyqtProperty(QTabBar.Shape, fget=getShape, fset=setShape)
    
    def getTextColor(self) -> QColor:
        return self.__textColor
        
    def setTextColor(self, color : QColor):
        self.__textColor = color
        self.update()
    textColor = pyqtProperty(QColor, fget=getTextColor, fset=setTextColor)

    def getWhatsThis(self) -> str:
        return self.__whatsThis
    def setWhatsThis(self, whatsthis):
        self.__whatsThis = whatsthis
    whatsThis = pyqtProperty(str, fget=getWhatsThis, fset=setWhatsThis)
    
    def getVertical(self) -> bool:
        return (self.shape == QTabBar.RoundedWest
                or self.shape == QTabBar.RoundedEast)
    vertical = pyqtProperty(bool, fget=getVertical)
