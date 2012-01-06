# Adapted by Jonathan Harper for the KyUI Project
#
# Originally by:
# Pardus Desktop Services
# Copyright (C) 2010, TUBITAK/UEKAE
# 2010 - Gökmen Göksel <gokmen:pardus.org.tr>

# The QProgressIndicator class lets an application display a progress
# indicator to show that a lengthy task is under way.
# QProgressIndicator is based on http://qt-apps.org/content/show.php?content=115762

# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.

# Qt Libraries
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QSize
from PyQt4.QtCore import pyqtProperty
from PyQt4.QtCore import pyqtSlot

from PyQt4.QtGui import QColor
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QPainter
from PyQt4.QtGui import QPalette

class ProgressIndicator(QWidget):
    def __init__(self, parent = None, color = None, **kwargs):
        # Remove property keyword arguments
        if 'alwaysVisible' in kwargs:
            alwaysVisible = kwargs.pop('alwaysVisible')
        else:
            alwaysVisible = False
        if 'animationDelay' in kwargs:
            delay = kwargs.pop('animationDelay')
        else:
            delay = 80
        color = kwargs.pop('color') if 'color' in kwargs else None
        super().__init__(parent, **kwargs)

        self.__angle = 0
        self.__timerId = -1
        self.__delay = delay
        self.__alwaysVisible = alwaysVisible
        if color:
            self.color = QColor(color)

    ### Getter Methods
    def isBusy(self):
        return self.__timerId != -1
        
    def getAnimationDelay(self):
        return self.delay
        
    def getColor(self):
        return self.palette().color(QPalette.Text)
        
    def isAlwaysVisible(self):
        return self.__alwaysVisible
    
    ### Setter Methods
    def setAlwaysVisible(self, state):
        self.__alwaysVisible = state
        if not self.isBusy() and not self.isVisible():
            self.show()

    def setAnimationDelay(self, delay):
        if not self.__timerId == -1:
            self.killTimer(self.__timerId)
        self.__delay = delay
        if self.__timerId == -1:
            self.__timerId = self.startTime(self.__delay)

    @pyqtSlot(bool)
    def setBusy(self, busy):
        if busy == self.isBusy():
            return
        if busy:
            self.startAnimation()
        else:
            self.stopAnimation()
    
    def setColor(self, color):
        pal = self.palette()
        pal.setColor(QPalette.Text, QColor(color))
        self.setPalette(pal)
    
    ### Internal Methods
    def startAnimation(self):
        if not self.isVisible():
            self.show()
        self.__angle = 0
        if self.__timerId == -1:
            self.__timerId = self.startTimer(self.__delay)

    def stopAnimation(self):
        if not self.__timerId == -1:
            self.killTimer(self.__timerId)
        self.__timerId = -1
        if not self.isAlwaysVisible():
            self.hide()
        else:
            self.update()

    ### Re-implemented
    def sizeHint(self):
        return QSize(20,20)

    def heightForWidth(self, width):
        return width

    def timerEvent(self, ev):
        self.__angle = (self.__angle + 30) % 360
        self.update()

    def paintEvent(self, ev):
        width = min(self.width(), self.height())

        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        outerRadius = (width-1) * 0.5
        innerRadius = (width-1) * 0.5 * 0.38

        capsuleHeight = outerRadius - innerRadius
        capsuleWidth  = capsuleHeight * 0.23 if width > 32 else capsuleHeight * 0.35
        capsuleRadius = capsuleWidth / 2
        if self.isBusy():
            for i in range(12):
                color = QColor(self.color)
                color.setAlphaF(float(1.0 - float(i / 12.0)))
                p.setPen(Qt.NoPen)
                p.setBrush(color)
                p.save()
                p.translate(self.rect().center())
                p.rotate(self.__angle - float(i * 30.0))
                p.drawRoundedRect(-capsuleWidth * 0.5,\
                                  -(innerRadius + capsuleHeight),\
                                  capsuleWidth,\
                                  capsuleHeight,\
                                  capsuleRadius,\
                                  capsuleRadius)
                p.restore()
        else:
            color = QColor(self.color)
            color.setAlphaF(1.0 / 3.0)
            p.setPen(Qt.NoPen)
            p.setBrush(color)
            for i in range(12):
                p.save()
                p.translate(self.rect().center())
                p.rotate(self.__angle - float(i * 30.0))
                p.drawRoundedRect(-capsuleWidth * 0.5,\
                                  -(innerRadius + capsuleHeight),\
                                  capsuleWidth,\
                                  capsuleHeight,\
                                  capsuleRadius,\
                                  capsuleRadius)
                p.restore()

    ### Properties
    animationDelay = pyqtProperty(int, fget=getAnimationDelay, fset=setAnimationDelay)
    color = pyqtProperty(QColor, fget=getColor, fset=setColor)
    alwaysVisible = pyqtProperty(bool, 
                                 fget=isAlwaysVisible, 
                                 fset=setAlwaysVisible)
