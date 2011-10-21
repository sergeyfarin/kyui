#UTF-8
#notifier.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *

#Qt.UI_AnimateMenu	1	Show animated menus.
#Qt.UI_FadeMenu	    2	Show faded menus.

from .util import QTypeToString

### Screen Positions:
# Top of Screen
# cornerPos: (1679, 46)
# Avail. Geom.: (0, 46), 1680 x 1004
# Screen Geom.: (0, 0), 1680 x 1050
#
# Left of Screen
# cornerPos: (62, 1049)
# Avail. Geom.: (62, 0), 1618 x 1050
# Screen Geom.: (0, 0), 1680 x 1050
#
# Right of Screen
# cornerPos: (1617, 1049)
# Avail. Geom.: (0, 0), 1618 x 1050
# Screen Geom.: (0, 0), 1680 x 1050
#
# Bottom of Screen
# cornerPos: (1679, 1003)
# Avail. Geom.: (0, 0), 1680 x 1004
# Screen Geom.: (0, 0), 1680 x 1050

styleText = {Qt.UI_AnimateMenu : 'Animate', 
             Qt.UI_FadeMenu : 'Fade', 
             None : 'None'}
directionText = {QBoxLayout.LeftToRight : 'Left To Right', 
                 QBoxLayout.RightToLeft : 'Right To Left', 
                 QBoxLayout.TopToBottom : 'Top To Bottom', 
                 QBoxLayout.BottomToTop : 'Bottom To Top'}

#158 x 236

class NotifierPopup(QFrame):
    LeftToRight = QBoxLayout.LeftToRight
    RightToLeft = QBoxLayout.RightToLeft
    TopToBottom = QBoxLayout.TopToBottom
    BottomToTop = QBoxLayout.BottomToTop
    
    def __init__(self, parent : QObject = None):
        self.__hideStyle = Qt.UI_General
        self.__showStyle = Qt.UI_General
        self.__showAnim = None
        self.__hideAnim = None
        self.__opacity = 1.0
        
        super().__init__(None, Qt.Window | Qt.FramelessWindowHint, visible=False)
        
        self.setWindowModality(False)
        self.debug = False
        self.desktop = QApplication.desktop()
        self.updateDesktop()
        self.desktop.screenCountChanged.connect(self.screenCountChanged)
        self.desktop.workAreaResized.connect(self.workAreaResized)
        
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.setFocusPolicy(Qt.NoFocus)
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Sunken)
        
        self.showStyle = Qt.UI_AnimateMenu
        if self.style().styleHint(QStyle.SH_Menu_FadeOutOnHide):
            self.hideStyle = Qt.UI_FadeMenu
        else:
            self.hideStyle = None
        self.setupDebugUi()
        
    def setupDebugUi(self):
        self.debug = True
        self.testLayout = QFormLayout(self, objectName='testLayout')
        self.testLabel1 = QLabel('Widget', self, objectName='testLabel1')
        self.testEdit1 = QPlainTextEdit(self, 
                                        objectName='testEdit1', 
                                        frameShape=QFrame.NoFrame, 
                                        horizontalScrollBarPolicy=Qt.ScrollBarAlwaysOff, 
                                        verticalScrollBarPolicy=Qt.ScrollBarAlwaysOff, 
                                        readOnly=True)
        self.testLayout.addRow(self.testLabel1, self.testEdit1)
        self.testLabel2 = QLabel('Desktop', self, objectName='testLabel2')
        self.testEdit2 = QPlainTextEdit(self, 
                                        objectName='testEdit2', 
                                        frameShape=QFrame.NoFrame, 
                                        horizontalScrollBarPolicy=Qt.ScrollBarAlwaysOff, 
                                        verticalScrollBarPolicy=Qt.ScrollBarAlwaysOff, 
                                        readOnly=True)
        self.testLayout.addRow(self.testLabel2, self.testEdit2)
        self.updateDebugUi()
        
    def updateDebugUi(self):
        wtext = 'ShowStyle: {}\nHideStyle: {}\nOpacity: {}\nDirection: '.format(\
                        styleText[self.__showStyle], 
                        styleText[self.__hideStyle], 
                        self.opacity, 
                        directionText[self.direction])
        self.testEdit1.setPlainText(wtext)
        dtext = 'Screen: {}\nScreen Geom: {}\nAvail Geom: {}\nCornerPos: {}'.format(\
                        self.primary, 
                        QTypeToString.rect(self.geom), 
                        QTypeToString.rect(self.availGeom), 
                        QTypeToString.point(self.cornerPos))
        self.testEdit2.setPlainText(dtext)
    
    def hide(self):
        self.setVisible(False)
        
    def show(self):
        self.setVisible(True)
        
    def stopAnimations(self):
        if (self.showAnim != None 
            and self.showAnim.state() != QAbstractAnimation.Stopped):
            self.showAnim.stop()
        if (self.hideAnim != None 
            and self.hideAnim.state() != QAbstractAnimation.Stopped):
            self.hideAnim.stop()
    
    def hideImmediately(self):
        super().setVisible(False)
    
    #==================================================#
    # Reimplemented Methods                            #
    #==================================================#
    def setVisible(self, visible):
        if not visible:
            #If we're already visible and there's an animation, start it
            if self.isVisible() and self.hideStyle is not None:
                self.hideAnim.start()
            else:
                self.hideImmediately()
        else:
            #If the widget isn't animated, move it to the correct position
            #Animated widgets handle movement on their own
            if self.showStyle != Qt.UI_AnimateMenu:
                self.move(self.getFinalShowPosition())
            #Ensure the widget has the correct starting opacity
            if self.showStyle == Qt.UI_FadeMenu:
                self.setWindowOpacity(self.showAnim.startValue())
            #Start the animation if there is one.
            if self.showStyle != None:
                self.showAnim.start()
            super().setVisible(True)
            
    def minimumSizeHint(self):
#        return QSize(200, 100)
        return super().minimumSizeHint()
    def sizeHint(self):
        return super().sizeHint()

    #==================================================#
    # Property Getters                                 #
    #==================================================#
    def getShowStyle(self) -> Qt.UIEffect:
        return self.__showStyle
    
    def getHideStyle(self) -> Qt.UIEffect:
        return self.__hideStyle
        
    def getHideAnim(self) -> QAbstractAnimation:
        return self.__hideAnim
        
    def getShowAnim(self) -> QAbstractAnimation:
        return self.__showAnim
        
    def getHideDuration(self) -> int:
        return self.hideAnim.duration()
    
    def getShowDuration(self) -> int:
        return self.showAnim.duration()
        
    def getOpacity(self) -> float:
        return self.__opacity
    
    #==================================================#
    # Property Setters                                 #
    #==================================================#
    def setShowStyle(self, style : Qt.UIEffect):
        if style != Qt.UI_FadeMenu and style != Qt.UI_AnimateMenu and style is not None:
            qWarning('Use Qt.UIFadeMenu, Qt.UI_AnimateMenu, or None')
            return
        self.__showStyle = style
        duration = None
        if self.__showAnim:
            duration = self.showAnim.duration()
            self.__showAnim.stop()
            del self.__showAnim
        if style == Qt.UI_FadeMenu:
            self.__showAnim = QPropertyAnimation(self, 'windowOpacity', self)
            self.showAnim.setDuration(duration if duration else 300)
            self.showAnim.setStartValue(0.0)
            self.showAnim.setEndValue(1.0)
        elif style == Qt.UI_AnimateMenu:
            self.setWindowOpacity(self.opacity)
            self.__showAnim = QPropertyAnimation(self, 'geometry', self)
            self.showAnim.setDuration(duration if duration else 300)
            self.generateSlideAnimation(self.showAnim)
        else: #None
            self.setWindowOpacity(self.opacity)
            self.__showAnim = None
        
    def setHideStyle(self, style : Qt.UIEffect):
        if style != Qt.UI_FadeMenu and style != Qt.UI_AnimateMenu and style is not None:
            qWarning('Use Qt.UI_FadeMenu or Qt.UI_AnimateMenu, or None')
            return
        self.__hideStyle = style
        duration = None
        if self.hideAnim:
            duration = self.hideAnim.duration()
            self.hideAnim.stop()
            del self.__hideAnim
        if style == Qt.UI_FadeMenu:
            self.__hideAnim = QPropertyAnimation(self, 'windowOpacity', self)
            self.hideAnim.setDuration(duration if duration else 300)
            self.hideAnim.setStartValue(1.0)
            self.hideAnim.setEndValue(0.0)
            self.hideAnim.finished.connect(self.hideImmediately)
        elif style == Qt.UI_AnimateMenu:
            self.setWindowOpacity(self.opacity)
            self.__hideAnim = QPropertyAnimation(self, 'geometry', self)
            self.hideAnim.setDuration(duration if duration else 300)
            self.generateSlideAnimation(self.hideAnim, True)
            self.hideAnim.finished.connect(self.hideImmediately)
        else: #None
            self.__hideAnim = None
            
    def setHideDuration(self, msec : int = 300):
        assert( msec > 0 )
        self.hideAnim.setDuration(msec)
        
    def setShowDuration(self, msec : int = 300):
        assert( msec >= 0 )
        self.showAnim.setDuration(msec)
        
    def setOpacity(self, opacity : float = 1.0):
        assert( opacity >= 0.0 and opacity <= 1.0 )
        self.stopAnimation()
        self.__opacity = opacity
        if self.debug:
            self.updateDebugUi()

    hideAnim = pyqtProperty(QAbstractAnimation, fget=getHideAnim)#, fset=setHideAnim)
    showAnim = pyqtProperty(QAbstractAnimation, fget=getShowAnim)#, fset=setShowAnim)
    
    showStyle = pyqtProperty(Qt.UIEffect, fget=getShowStyle, fset=setShowStyle)
    hideStyle = pyqtProperty(Qt.UIEffect, fget=getHideStyle, fset=setHideStyle)
    
    showDuration = pyqtProperty(int, fget=getShowDuration, fset=setShowDuration)
    hideDuration = pyqtProperty(int, fget=getHideDuration, fset=setHideDuration)
    
    opacity = pyqtProperty(float, fget=getOpacity, fset=setOpacity)

    #==================================================#
    # Private Methods                                  #
    #==================================================#
        
    def screenCountChanged(self):
        if self.primary != self.desktop.primaryScreen():
            self.updateDesktop()
            
    def workAreaResized(self, screen):
        if self.primary == screen:
            self.updateDesktop()
    
    def updateDesktop(self):
        self.primary = self.desktop.primaryScreen()
        self.availGeom = self.desktop.availableGeometry(self.primary)
        self.geom = self.desktop.screenGeometry(self.primary)
        
        #Find the taskbar/dock location
        if self.availGeom.left() > self.geom.left(): #Left side of screen
            self.corner = Qt.BottomLeftCorner
            self.cornerPos = self.availGeom.bottomLeft()
            self.direction = QBoxLayout.LeftToRight
        elif self.availGeom.top() > self.geom.top(): #Top of screen
            self.corner = Qt.TopRightCorner
            self.cornerPos = self.availGeom.topRight()
            self.direction = QBoxLayout.TopToBottom
        elif self.availGeom.right() < self.geom.right(): #Right side
            self.corner = Qt.BottomRightCorner
            self.cornerPos = self.availGeom.bottomRight()
            self.direction = QBoxLayout.RightToLeft
        elif self.availGeom.bottom() < self.geom.bottom(): #Bottom
            self.corner = Qt.BottomRightCorner
            self.cornerPos = self.availGeom.bottomRight()
            self.direction = QBoxLayout.BottomToTop
        else: #Taskbar is hidden or on another monitor, guess bottom right
            self.corner = Qt.BottomRightCorner
            self.cornerPos = self.availGeom.bottomRight()
            self.direction = QBoxLayout.BottomToTop
            
        if self.showStyle == Qt.UI_AnimateMenu:
            self.generateSlideAnimation(self.showAnim)
        if self.hideStyle == Qt.UI_AnimateMenu:
            self.generateSlideAnimation(self.hideAnim)
        if self.debug:
            self.updateDebugUi()

    def getFinalShowPosition(self) -> QPoint:
        hint = self.sizeHint()
        if self.direction == QBoxLayout.TopToBottom:
            pos = QPoint(self.cornerPos.x() - hint.width(), 
                         self.cornerPos.y())
        elif self.direction == QBoxLayout.LeftToRight:
            pos = QPoint(self.cornerPos.x(), 
                         self.cornerPos.y() - hint.height())
        else: #QBoxLayout.RightToLeft and QBoxLayout.BottomToTop
            pos = QPoint(self.cornerPos.x() - hint.width(), 
                         self.cornerPos.y() - hint.height())
        return pos
    def getSlideStartPosition(self) -> QPoint:
        hint = self.sizeHint()
        if self.direction == QBoxLayout.TopToBottom:
            pos = QPoint(self.cornerPos.x() - hint.width(), 
                         self.cornerPos.y() - hint.height())
        elif self.direction == QBoxLayout.LeftToRight:
            pos = QPoint(self.cornerPos.x() - hint.width(), 
                         self.cornerPos.y() - hint.height())
        elif self.direction == QBoxLayout.RightToLeft:
            pos = QPoint(self.cornerPos.x() + hint.width(), 
                         self.cornerPos.y())
        else: #QBoxLayout.BottomToTop or unknown
            pos = QPoint(self.cornerPos.x() - hint.width(), 
                         self.cornerPos.y() + hint.height())
        return pos
        
    def generateSlideAnimation(self, anim, reverse = False):
        hint = self.sizeHint()
        startPos = QPoint(self.cornerPos.x() - hint.width(), 
                        self.cornerPos.y())
        endPos = self.getFinalShowPosition()
        if reverse:
            anim.setStartValue(QRect(endPos, hint))
            anim.setEndValue(QRect(startPos, hint))
        else:
            anim.setStartValue(QRect(startPos, hint))
            anim.setEndValue(QRect(endPos, hint))
