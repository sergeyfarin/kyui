from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ToolGroupButton(QAbstractButton):
    def __init__(self, parent, 
                 icon : QIcon = None, 
                 text : str = None):
        super().__init__(parent)
        self.setFocusPolicy(Qt.NoFocus)
        self.setCheckable(False)
        self.setIconSize(QSize(22, 22))
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
            
            mode = QIcon.Normal if self.isEnabled() else QIcon.Disabled
            iconpm = self.icon().pixmap(self.iconSize(), mode, QIcon.On)
            iconRect = self.style().itemPixmapRect(self.rect(), Qt.AlignCenter, iconpm)
            iconRect.moveTop(self.rect().top() + 10)
            
            iconOpt = QStyleOption()
            iconOpt.initFrom(self)
            iconOpt.state = QStyle.State_Raised
            if self.isEnabled():
                iconOpt.state |= QStyle.State_Enabled
            iconOpt.rect = QRect(0, 0, 32, 32)
            iconOpt.rect.moveCenter(self.rect().center())
            iconOpt.rect.moveTop(self.rect().top() + 6)
            
            self.style().drawPrimitive(QStyle.PE_PanelButtonBevel, iconOpt, p, self)
            self.style().drawItemPixmap(p, iconRect, Qt.AlignCenter, iconpm)
            
        if self.text():
            self.style().drawItemText(p, bRect, Qt.AlignCenter, self.palette(), 
                                      self.isEnabled(), self.text(), 
                                      QPalette.Text)
        
    def isHovered(self) -> bool:
        return self.__hover
    
    def setHovered(self, hover):
        self.__hover = hover
