#UTF-8
#gradient.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from .colors import Win7Color, Win7Color_Normal, Win7Color_Down, Win7Color_Hover
from .painter import ToolGroupPopupColors, ToolGroupButtonColors, arrowPixmap

def format_qrect(value : QSize) -> str:
    return '({}, {}), {} x {}'.format(value.x(), value.y(), value.width(), value.height())

def format_qline(value : QSize) -> str:
    return '({}, {}), ({}, {})'.format(value.x1(), value.y1(), value.x2(), value.y2())


class ToolbarGradient(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        gradient = QLinearGradient()
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, Win7Color_Normal.ToolbarUpper)
        gradient.setColorAt(0.8, Win7Color_Normal.ToolbarLower)
        gradient.setStart(0.5, 0.0)
        gradient.setFinalStop(0.5, 0.5)
        self.brush = QBrush(gradient)
        
        gradient = QLinearGradient()
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, Win7Color_Normal.ToolbarUpper)
        gradient.setColorAt(1.0, Win7Color_Normal.ToolbarLower2)
        gradient.setStart(0.5, 0.0)
        gradient.setFinalStop(0.5, 1.0)
        self.pen = QPen(QBrush(gradient), 1.0)
        
    def minimumSizeHint(self):
        return QSize(265, 95)
    
    def sizeHint(self):
        return self.minimumSizeHint()
        
    def paintEvent(self, ev):
        p = QPainter()
        p.begin(self)
        rect = self.rect().adjusted(0, 0, -1, -1)
        #Top line
        p.setPen(Win7Color_Normal.ToolbarFrameTop)
        p.drawLine(rect.topLeft(), rect.topRight())
        #Bottom line
        p.setPen(Win7Color_Normal.ToolbarFrameBottom1)
        p.drawLine(rect.bottomLeft(), rect.bottomRight())
        #Bottom line (inner)
        rect.adjust(0, 0, 0, -1)
        p.setPen(Win7Color_Normal.ToolbarFrameBottom2)
        p.drawLine(rect.bottomLeft(), rect.bottomRight())
        
        #Interior gradient
        rect.adjust(0, 1, 0, -2)
        p.setPen(self.pen)
        p.setBrush(self.brush)
        p.drawRect(rect)
        p.end()
        
class ToolGroupBox(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        

class ToolGroupPopup(QWidget):
    aboutToHide = pyqtSignal()
    aboutToShow = pyqtSignal()
    
    def __init__(self, parent = None, toolgroup = None):
        super().__init__(parent, Qt.Popup)
        (self.outerPen, self.innerPen, self.brush) = ToolGroupPopupColors()
        self.setAutoFillBackground(False)
        if not toolgroup:
            self.__toolgroup = QWidget()
        self.hide()
        
    def minimumSizeHint(self) -> QSize:
        sz = super().minimumSizeHint()
        return sz + QSize(4, 5)
        
    def sizeHint(self) -> QSize:
        return QSize(100, 100)
        return self.minimumSizeHint()
        
    def show(self):
        self.aboutToShow.emit()
        parent = self.parentWidget()
        pos = parent.mapToGlobal(parent.rect().bottomLeft())
        super().show()
        self.setGeometry(QRect(pos, self.sizeHint()))
        
    def keyPressEvent(self, ev):
        if ev.key() == Qt.Key_Escape:
            self.hide()
            
    def hideEvent(self, ev):
        self.aboutToHide.emit()
        
    def paintEvent(self, ev):
        p = QPainter(self)
        rect = self.rect()
        p.setPen(self.outerPen)
        p.fillRect(rect, Qt.transparent)
        (x1, y1, x2, y2) = rect.getCoords()
#        p.drawRect(rect)
        lines = [QLine(x1 + 1, y1, x2 - 1, y1), 
                 QLine(x1 + 1, y2, x2 - 1, y2), 
                 QLine(x1, y1 + 1, x1, y2 - 1), 
                 QLine(x2, y1 + 1, x2, y2 - 1)]
        p.drawLines(lines)
        p.setPen(QColor(206, 219, 235))
        rect.adjust(1, 0, -2, -2)
        p.drawLine(rect.bottomLeft(), rect.bottomRight())
        p.setPen(self.innerPen)
        rect.adjust(0, 1, 0, -1)
        p.setBrush(self.brush)
        p.drawRect(rect)
        p.end()
        
    def getToolGroup(self):
        return self.__toolgroup
        
    def setToolGroup(self, toolgroup):
        self.__toolgroup = toolgroup
        
    toolGroup = pyqtProperty(QWidget, fget=getToolGroup, fset=setToolGroup)
        
class ToolGroupButton(QAbstractButton):
    def __init__(self, parent, icon : QIcon = None, text : str = None):
        super().__init__(parent)
        self.setFocusPolicy(Qt.NoFocus)
        self.setCheckable(False)
        self.setIconSize(QSize(22, 22))
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.__hover = False
        pal = self.palette()
        pal.setColor(QPalette.ButtonText, QColor(76, 96, 122))
        self.setPalette(pal)
        if icon:
            self.setIcon(icon)
        if text:
            self.setText(text)
        self.normalPalette = ToolGroupButtonColors(QStyle.State_On)
        self.hoverPalette = ToolGroupButtonColors(QStyle.State_MouseOver)
        self.downPalette = ToolGroupButtonColors(QStyle.State_Sunken)
        
        self.__popupBox = ToolGroupPopup(self)
        self.__popupBox.aboutToHide.connect(self._popupHidden)
        
    def _popupHidden(self):
        self.setDown(False)
        
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
    
    def sizeHint(self):
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
        
    def mousePressEvent(self, ev):
        if ev.button() == Qt.LeftButton and not self.isDown():
            self.__popupBox.show()
        super().mousePressEvent(ev)
        
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

    def paintEvent(self, ev):
        p = QPainter()
        p.begin(self)
        opt = QStyleOptionButton()
        self.initStyleOption(opt)
        ### Frame
        (x1, y1, x2, y2) = self.rect().getCoords()
        if self.isDown():
            # Draw the outer frame sans corners
            p.setPen(self.downPalette.outerPen)
            lines = [QLine(x1 + 2, y1, x2 - 2, y1), 
                     QLine(x1 + 2, y2, x2 - 2, y2), 
                     QLine(x1, y1 + 2, x1, y2 - 2), 
                     QLine(x2, y1 + 2, x2, y2 - 2)]
            p.drawLines(lines)
            # Draw the inner upper line
            p.setPen(self.downPalette.innerPen)
            p.drawLine(QLine(x1 + 2, y1 + 1, x2 - 2, y1 + 1))
            
            # Inner Gradients
            rect = self.rect().adjusted(1, 2, -1, -1)
            rect2 = QRect(rect)
            split = (rect.height() - 4) * 0.4
            rect.setHeight(split)
            rect2.setTop(rect.bottom() + 1)
            p.fillRect(rect, self.downPalette.topBrush)
            p.fillRect(rect2, self.downPalette.bottomBrush)
            
            # Corner pixmap
            pm = self.downPalette.cornerPixmap
            pmRect = QRectF(pm.rect())
        elif self.isHovered():
            # Outer frame
            p.setPen(self.hoverPalette.outerPen)
            lines = [QLine(x1 + 2, y1, x2 - 2, y1), 
                     QLine(x1 + 2, y2, x2 - 2, y2), 
                     QLine(x1, y1 + 2, x1, y2 - 2), 
                     QLine(x2, y1 + 2, x2, y2 - 2)]
            p.drawLines(lines)
            # Inner frame
            p.setPen(self.hoverPalette.innerPen)
            lines = [QLine(x1 + 2, y1 + 1, x2 - 2, y1 + 1), 
                     QLine(x1 + 2, y2 - 1, x2 - 2, y2 - 1), 
                     QLine(x1 + 1, y1 + 2, x1 + 1, y2 - 2), 
                     QLine(x2 - 1, y1 + 2, x2 - 1, y2 - 2)]
            p.drawLines(lines)
            
            # Inner Gradients
            rect = self.rect().adjusted(1, 2, -1, -1)
            rect2 = QRect(rect)
            split = (rect.height() - 4) * 0.4
            rect.setHeight(split)
            rect2.setTop(rect.bottom() + 1)
            p.fillRect(rect, self.hoverPalette.topBrush)
            p.fillRect(rect2, self.hoverPalette.bottomBrush)
            
            # Corner pixmap
            pm = self.hoverPalette.cornerPixmap
            pmRect = QRectF(pm.rect())
        else: #Normal state
            # Outer frame
            p.setPen(self.normalPalette.outerPen)
            lines = [QLine(x1 + 2, y1, x2 - 2, y1), 
                     QLine(x1 + 2, y2, x2 - 2, y2), 
                     QLine(x1, y1 + 2, x1, y2 - 2), 
                     QLine(x2, y1 + 2, x2, y2 - 2)]
            p.drawLines(lines)
            # Inner frame
            p.setPen(self.normalPalette.innerPen)
            lines = [QLine(x1 + 2, y1 + 1, x2 - 2, y1 + 1), 
                     QLine(x1 + 2, y2 - 1, x2 - 2, y2 - 1), 
                     QLine(x1 + 1, y1 + 2, x1 + 1, y2 - 2), 
                     QLine(x2 - 1, y1 + 2, x2 - 1, y2 - 2)]
            p.drawLines(lines)
            
            # Corner pixmap
            pm = self.normalPalette.cornerPixmap
            pmRect = QRectF(pm.rect())
            
            # Inner Gradients
            rect = self.rect().adjusted(2, 2, -2, -2)
            rect2 = QRect(rect)
            split = (rect.height() - 4) * 0.4
            rect.setHeight(split)
            rect2.setTop(rect.bottom() + 1)
            p.fillRect(rect, self.normalPalette.topBrush)
            p.fillRect(rect2, self.normalPalette.bottomBrush)
        
        # Draw corners
        pmfrags = []
        pmfrags.append(QPainter.PixmapFragment.create(QPointF(x1 + 1, y1 + 1), 
                                                      pmRect, 
                                                      1, 1, 0, 1))
        pmfrags.append(QPainter.PixmapFragment.create(QPointF(x2, y1 + 1), 
                                                      pmRect, 
                                                      1, 1, 90, 1))
        pmfrags.append(QPainter.PixmapFragment.create(QPointF(x2, y2), 
                                                      pmRect, 
                                                      1, 1, 180, 1))
        pmfrags.append(QPainter.PixmapFragment.create(QPointF(x1 + 1, y2), 
                                                      pmRect, 
                                                      1, 1, 270, 1))
        p.drawPixmapFragments(pmfrags, pm, QPainter.OpaqueHint)
        
        # Text and Icon
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
            textRect = self.style().itemTextRect(opt.fontMetrics, 
                                                 bRect, 
                                                 Qt.AlignCenter, 
                                                 self.isEnabled(), 
                                                 opt.text)
            textRect.moveTop(bRect.top() + 8)
            self.style().drawItemText(p, textRect, Qt.AlignCenter, opt.palette, 
                          self.isEnabled(), opt.text, 
                          QPalette.ButtonText)
        arrow = arrowPixmap()
        aRect = QRect(bRect.topLeft(), arrow.size())
        aRect.moveCenter(bRect.center())
        aRect.moveTop(bRect.top() + 24)
        p.drawPixmap(aRect, arrow)
        p.end()

    def isHovered(self) -> bool:
        return self.__hover
