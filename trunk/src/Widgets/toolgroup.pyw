from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ToolGroupButton(QAbstractButton):
    def __init__(self, parent, 
                 icon : QIcon = None, 
                 text : str = None):
        super().__init__(parent)
        self.setFocusPolicy(Qt.NoFocus)
        self.setCheckable(False)
        self.__hover = False
        if icon:
            self.setIcon(icon)
        if text:
            self.setText(text)

    def minimumSizeHint(self) -> QSize:
        return QSize(86, 44)

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
        
    def initStyleOption(self, opt):
        opt.initFrom(self)
        if self.isEnabled():
            if self.isHovered() and not self.isChecked() and not self.isDown():
                opt.state |= QStyle.State_MouseOver
            opt.state |= QStyle.State_Raised
        if self.isChecked():
            opt.state |= QStyle.State_On
        if self.isDown():
            opt.state |= QStyle.State_Sunken

    def paintEvent(self, ev):
        p = QPainter(self)
        opt = QStyleOption()
        self.initStyleOption(opt)
        
        self.style().drawPrimitive(QStyle.PE_PanelButtonBevel, opt, p, self)
        
        tRect = self.rect().adjusted(0, 0, -1, -1)
        bRect = QRect(tRect)
        tRect.setHeight(tRect.height() * 0.4)
        bRect.setTop(tRect.bottom() + 1)
        
        if not self.icon().isNull():
            icon = self.icon()
            mode = QIcon.Normal if self.isEnabled() else QIcon.Disabled
            icon.paint(p, tRect, Qt.AlignCenter, mode, QIcon.On)
        if self.text():
            self.style().drawItemText(p, bRect, Qt.AlignCenter, self.palette(), 
                                      self.isEnabled(), self.text(), 
                                      QPalette.Text)
        
    def isHovered(self) -> bool:
        return self.__hover
    
    def setHovered(self, hover):
        self.__hover = hover