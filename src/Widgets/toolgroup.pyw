from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ToolGroupBox(QWidget):
    def __init__(self, parent, title : str = None):
        super().__init__(parent, Qt.Popup)
        self.title = title
        
    def minimumSizeHint(self) -> QSize:
        sz = QSize(100, 100)
        return sz + QSize(4, 5)
        
    def sizeHint(self) -> QSize:
        return self.minimumSizeHint()
        
    def show(self):
        if not self.parent():
            super().show()
            return
        if QApplication.isLeftToRight():
            pos = self.parent().mapToGlobal(self.parent().rect().bottomLeft())
        else:
            pos = self.parent().mapToGlobal(self.parent().rect().bottomRight())
        pos.setY(pos.y() + 1)
        self.move(pos)
        super().show()
        
    def paintEvent(self, ev):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(Qt.gray))
        p.setBrush(QColor(Qt.white))
        p.drawRect(self.rect().adjusted(0, 0, -1, -1))
        p.end()
        
    def hideEvent(self, ev):
        if self.parent():
            self.parent().setDown(False)
        
    def getTitle(self) -> str:
        return self.__title
        
    def setTitle(self, title):
        self.__title = title
    title = pyqtProperty(str, fget=getTitle, fset=setTitle)
    
class ToolGroupButton(QAbstractButton):
    def __init__(self, parent, 
                 icon : QIcon = None, 
                 text : str = None):
        super().__init__(parent)
#        self.setFocusPolicy(Qt.NoFocus)
        self.setCheckable(False)
        self.setIconSize(QSize(22, 22))
        self.__hover = False
        if icon:
            self.setIcon(icon)
        if text:
            self.setText(text)
        self.toolGroup = ToolGroupBox(self)

    def minimumSizeHint(self) -> QSize:
        minw = 44
        minh = 86
        opt = QStyleOptionButton()
        self.initStyleOption(opt)
        tsz = opt.fontMetrics.size(Qt.TextWordWrap, self.text())
        width = tsz.width()
        height = tsz.height()
        isz = self.iconSize()
        if isz.width() + 8 > width:
            width = isz.width() + 8
        height += (isz.height() + 8) if isz.height() + 8 > 32 else 32
        height += 16 #6 on top, 10 on bottom
        if width < minw:
            width = minw
        if height < minh:
            height = minh
        return QSize(width, height)

    def sizeHint(self) -> QSize:
        return self.minimumSizeHint()

    def enterEvent(self, ev):
        if self.isEnabled():
            self.__hover = True
            self.update()
        super().enterEvent(ev)

    def leaveEvent(self, ev):
        if self.isEnabled():
            self.__hover = False
            self.update()
        super().leaveEvent(ev)
        
    def mousePressEvent(self, ev):
        if ev.button() == Qt.LeftButton:
            self.toolGroup.show()
        super().mousePressEvent(ev)
        
    def keyPressEvent(self, ev):
        key = ev.key()
        if ev.modifiers() == Qt.NoModifier:
            if ((key == Qt.Key_Space or key == Qt.Key_Enter 
                or key == Qt.Key_Return) and not self.isDown()):
                self.setDown(True)
                self.toolGroup.show()
        ev.accept()
        return
        
    def initStyleOption(self, opt):
        opt.initFrom(self)
        opt.icon = self.icon()
        opt.iconSize = self.iconSize()
        opt.text = self.text()
        opt.features = QStyleOptionButton.ButtonFeatures(0x00)
        
        if self.isEnabled():
            if self.isHovered() and not self.isChecked() and not self.isDown():
                opt.state |= QStyle.State_MouseOver
            opt.state |= QStyle.State_Raised
        if self.isChecked():
            opt.state |= QStyle.State_On
        if self.isDown():
            opt.state |= QStyle.State_Sunken
        if self.hasFocus():
            opt.state |= QStyle.State_HasFocus

    def paintEvent(self, ev):
        p = QPainter()
        p.begin(self)
        opt = QStyleOptionButton()
        self.initStyleOption(opt)
        
        self.style().drawPrimitive(QStyle.PE_PanelButtonBevel, opt, p, self)
        
        tRect = self.rect().adjusted(0, 0, -1, -1)
        bRect = QRect(tRect)
        tRect.setHeight(tRect.height() * 0.4)
        bRect.setTop(tRect.bottom() + 1)
        
        if opt.icon and not opt.icon.isNull():
            mode = QIcon.Normal if self.isEnabled() else QIcon.Disabled
            iconpm = opt.icon.pixmap(self.iconSize(), mode, QIcon.On)
            iconRect = self.style().itemPixmapRect(opt.rect, Qt.AlignCenter, iconpm)
            iconRect.moveTop(opt.rect.top() + 10)
            
            iconOpt = QStyleOption()
            iconOpt.initFrom(self)
            iconOpt.state = QStyle.State_Raised
            if self.isEnabled():
                iconOpt.state |= QStyle.State_Enabled
            iconOpt.rect = QRect(0, 0, 32, 32)
            iconOpt.rect.moveCenter(opt.rect.center())
            iconOpt.rect.moveTop(opt.rect.top() + 6)
            
            self.style().drawPrimitive(QStyle.PE_PanelButtonBevel, iconOpt, p, self)
            self.style().drawItemPixmap(p, iconRect, Qt.AlignCenter, iconpm)
            
        if opt.text:
            self.style().drawItemText(p, bRect, Qt.AlignCenter, opt.palette, 
                                      self.isEnabled(), opt.text, 
                                      QPalette.Text)
#        if opt.state & QStyle.State_HasFocus:
#            fropt = QStyleOptionFocusRect()
#            fropt.initFrom(self)
#            fropt.backgroundColor = self.palette().button().color()
#            fropt.rect = self.rect().adjusted(3, 3, -3, -3)
#            self.style().drawPrimitive(QStyle.PE_FrameFocusRect, fropt, p, self)
        p.end()
        
    def isHovered(self) -> bool:
        return self.__hover
    
    def setHovered(self, hover):
        self.__hover = hover
    
    def getToolGroup(self):
        return self.__toolgroup
        
    def setToolGroup(self, toolgroup):
        self.__toolgroup = toolgroup
        
    toolGroup = pyqtProperty(QWidget, fget=getToolGroup, fset=setToolGroup)
