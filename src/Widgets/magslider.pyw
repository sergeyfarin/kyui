from PyQt4.QtCore import *
from PyQt4.QtGui import *

from . import magslider_rc

def directionFromOrientation(orientation) -> QBoxLayout.Direction:
    if orientation == Qt.Vertical:
        return QBoxLayout.TopToBottom
    elif QApplication.isLeftToRight():
        return QBoxLayout.LeftToRight
    else:
        return QBoxLayout.RightToLeft

def orientationFromDirection(direction) -> Qt.Orientation:
    if (direction == QBoxLayout.TopToBottom 
        or direction == QBoxLayout.BottomToTop):
        return Qt.Vertical
    else:
        return Qt.Horizontal

class ZoomInButton(QAbstractButton):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFocusPolicy(Qt.NoFocus)
        self.setCursor(Qt.ArrowCursor)
        self.setToolTip(self.trUtf8('Zoom In'))
        ZoomInButton._generatePixmaps()
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.__hover = False
    
    @staticmethod
    def _generatePixmaps():
        pm = QPixmapCache.find('_ky__magslider_zoomin_normal')
        if not pm:
            pm = QPixmap(':/_ky__magslider/zoomin_normal')
            QPixmapCache.insert('_ky__magslider_zoomin_normal', pm)
        pm = QPixmapCache.find('_ky__magslider_zoomin_hover')
        if not pm:
            pm = QPixmap(':/_ky__magslider/zoomin_hover')
            QPixmapCache.insert('_ky__magslider_zoomin_hover', pm)
        pm = QPixmapCache.find('_ky__magslider_zoomin_down')
        if not pm:
            pm = QPixmap(':/_ky__magslider/zoomin_down')
            QPixmapCache.insert('_ky__magslider_zoomin_down', pm)
            
    def minimumSizeHint(self) -> QSize:
        return QSize(16, 16)

    def sizeHint(self) -> QSize:
        return self.minimumSizeHint()

    def enterEvent(self, ev):
        if self.isEnabled():
            self.__hover = True
            self.update()
        super(QAbstractButton, self).enterEvent(ev)

    def leaveEvent(self, ev):
        if self.isEnabled():
            self.__hover = False
            self.update()
        super(QAbstractButton, self).leaveEvent(ev)
        
    def paintEvent(self, ev):
        p = QPainter(self)
        if self.isChecked() or self.isDown():
            pm = QPixmapCache.find('_ky__magslider_zoomin_down')
        elif self.underMouse():
            pm = QPixmapCache.find('_ky__magslider_zoomin_hover')
        else:
            pm = QPixmapCache.find('_ky__magslider_zoomin_normal')
        p.drawPixmap(self.rect().topLeft(), pm)
        p.end()

class ZoomOutButton(QAbstractButton):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFocusPolicy(Qt.NoFocus)
        self.setCursor(Qt.ArrowCursor)
        self.setToolTip(self.trUtf8('Zoom Out'))
        ZoomOutButton._generatePixmaps()
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.__hover = False
    
    @staticmethod
    def _generatePixmaps():
        pm = QPixmapCache.find('_ky__magslider_zoomout_normal')
        if not pm:
            pm = QPixmap(':/_ky__magslider/zoomout_normal')
            QPixmapCache.insert('_ky__magslider_zoomout_normal', pm)
        pm = QPixmapCache.find('_ky__magslider_zoomout_hover')
        if not pm:
            pm = QPixmap(':/_ky__magslider/zoomout_hover')
            QPixmapCache.insert('_ky__magslider_zoomout_hover', pm)
        pm = QPixmapCache.find('_ky__magslider_zoomout_down')
        if not pm:
            pm = QPixmap(':/_ky__magslider/zoomout_down')
            QPixmapCache.insert('_ky__magslider_zoomout_down', pm)
            
    def minimumSizeHint(self) -> QSize:
        return QSize(16, 16)

    def sizeHint(self) -> QSize:
        return self.minimumSizeHint()

    def enterEvent(self, ev):
        if self.isEnabled():
            self.__hover = True
            self.update()
        super(QAbstractButton, self).enterEvent(ev)

    def leaveEvent(self, ev):
        if self.isEnabled():
            self.__hover = False
            self.update()
        super(QAbstractButton, self).leaveEvent(ev)
        
    def paintEvent(self, ev):
        p = QPainter(self)
        if self.isChecked() or self.isDown():
            pm = QPixmapCache.find('_ky__magslider_zoomout_down')
        elif self.underMouse():
            pm = QPixmapCache.find('_ky__magslider_zoomout_hover')
        else:
            pm = QPixmapCache.find('_ky__magslider_zoomout_normal')
        p.drawPixmap(self.rect().topLeft(), pm)
        p.end()

class MagSlider(QWidget):
    def __init__(self, orientation : Qt.Orientation, parent : QWidget):
        super().__init__(parent)
        self.__layout = QBoxLayout(directionFromOrientation(orientation), self)
        
        self.__slider = QSlider(orientation, self)
        self.layout.addWidget(self.slider)
        
        self.__inbtn = ZoomInButton(self)
        self.__outbtn = ZoomOutButton(self)
        
        if orientation == Qt.Vertical:
            self.layout.insertWidget(0, self.zoomInButton)
            self.layout.addWidget(self.zoomOutButton)
        else:
            self.layout.insertWidget(0, self.zoomOutButton)
            self.layout.addWidget(self.zoomInButton)
        
    def setObjectName(self, name):
        super().setObjectName(name)
        self.layout.setObjectName(name + '_layout')
        self.slider.setObjectName(name + '_slider')
        self.zoomInButton.setObjectName(name + '_zoomInButton')
        self.zoomOutButton.setObjectName(name + '_zoomOutButton')
        
    def getLayout(self):        return self.__layout
    layout = property(fget=getLayout)
    def getSlider(self):        return self.__slider
    slider = property(fget=getSlider)
    def getZoomInButton(self):  return self.__inbtn
    zoomInButton = property(fget=getZoomInButton)
    def getZoomOutButton(self): return self.__outbtn
    zoomOutButton = property(fget=getZoomOutButton)
