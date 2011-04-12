from PyQt4.QtCore import *
from PyQt4.QtGui import *

from .magslider_pixmap import *
from . import magslider_rc

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
        pm = QPixmapCache.find('_ky_magslider_zoomin_down')
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
        pm = QPixmapCache.find('_ky_magslider_zoomout_down')
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

class MagSlider(QWidget): pass
