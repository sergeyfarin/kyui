#UTF-8
#sysmsg.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *

#Qt.UI_AnimateMenu	1	Show animated menus.
#Qt.UI_FadeMenu	    2	Show faded menus.

class SystrayPopup(QWidget):
    def __init__(self, parent : QObject = None):
        super().__init__(parent, Qt.Popup)
        self.desktop = QApplication.desktop()
        self.updateDesktop()
        self.desktop.screenCountChanged.connect(self.screenCountChanged)
        self.desktop.workAreaResized.connect(self.workAreaResized)
        
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        
        self.__showStyle = Qt.UI_AnimateMenu
        if self.style().styleHint(QStyle.SH_Menu_FadeOutOnHide):
            self.__hideStyle = Qt.UI_FadeMenu
        else:
            self.__hideStyle = None
            
    def minimumSizeHint(self):
        return QSize(100, 100)
        
    def sizeHint(self):
        return self.minimumSizeHint()
        
    def screenCountChanged(self):
        if self.primary != self.desktop.primaryScreen():
            self.updateDesktop()
            
    def workAreaResized(self, screen):
        if self.primary == screen:
            self.availGeom = self.desktop.availableGeometry(self.primary)
            self.geom = self.desktop.screenGeometry(self.primary)
    
    def updateDesktop(self):
        self.primary = self.desktop.primaryScreen()
        self.availGeom = self.desktop.availableGeometry(self.primary)
        self.geom = self.desktop.screenGeometry(self.primary)
        
        #Find the taskbar/dock location
        if self.availGeom.left() > self.geom.left(): #Left side of screen
            self.corner = Qt.BottomLeftCorner
            self.cornerPos = self.availGeom.bottomLeft()
        elif self.availGeom.top() > self.geom.top(): #Top of screen
            self.corner = Qt.TopRightCorner
            self.cornerPos = self.availGeom.topRight()
        elif self.availGeom.right() < self.geom.right(): #Right side
            self.corner = Qt.BottomRightCorner
            self.cornerPos = self.availGeom.bottomRight()
        elif self.availGeom.bottom() < self.geom.bottom(): #Bottom
            self.corner = Qt.BottomRightCorner
            self.cornerPos = self.availGeom.bottomRight()
        else: #Taskbar is hidden or on another monitor, guess bottom right
            self.corner = Qt.BottomRightCorner
            self.cornerPos = self.availGeom.bottomRight()

    #==================================================#
    # Property Getters                                 #
    #==================================================#
    def getShowStyle(self) -> Qt.UIEffect:
        return self.__showStyle
    
    def getHideStyle(self) -> Qt.UIEffect:
        return self.__hideStyle
    
    #==================================================#
    # Property Setters                                 #
    #==================================================#
    def setShowStyle(self, style : Qt.UIEffect):
        if style != Qt.UI_FadeMenu or style != Qt.UI_AnimateMenu:
            qWarning('Use Qt.UIFadeMenu or Qt.UI_AnimateMenu')
            return
        self.__showStyle = style
        
    def setHideStyle(self, style : Qt.UIEffect):
        if style != Qt.UI_FadeMenu or style != Qt.UI_AnimateMenu:
            qWarning('Use Qt.UIFadeMenu or Qt.UI_AnimateMenu')
            return
        self.__hideStyle = style
        
    showStyle = pyqtProperty(Qt.UIEffect, fget=getShowStyle, fset=setShowStyle)
    hideStyle = pyqtProperty(Qt.UIEffect, fget=getHideStyle, fset=setHideStyle)
