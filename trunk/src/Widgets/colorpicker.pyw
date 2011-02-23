from PyQt4.QtCore import pyqtSignal, pyqtSlot, Qt, pyqtProperty, qWarning
from PyQt4.QtCore import QEvent, QSize
from PyQt4.QtGui import QFrame, QWidget, QPushButton, QFocusFrame
from PyQt4.QtGui import QGridLayout, QSpacerItem, QSizePolicy
from PyQt4.QtGui import QPainter, QStyle
from PyQt4.QtGui import QStyleOptionFrameV3, QStyleOptionFocusRect
from PyQt4.QtGui import QColor, QPalette
from PyQt4.QtGui import QPaintEvent
from PyQt4.QtGui import QButtonGroup

class ColorData():
    __slots__ = ['size', 'colors']
    def __init__(self, size, colors):
        self.size = size
        if len(colors) > size.height():
            qWarning('ColorData: row count exceeds specified size; expanding')
            self.size.setHeight(len(colors))
        for row in iter(colors):
            if len(row) > size.width():
                qWarning('ColorData: column count exceeds specified size; expanding')
                self.size.setWidth(len(row))
        self.colors = colors

class ColorPicker(QWidget):
    #==================================================#
    # Signals                                          #
    #==================================================#
    currentColorChanged = pyqtSignal([QColor], [int, int])
    colorHovered = pyqtSignal([QColor], [int, int])
    
    def __init__(self, 
                 parent : QWidget = None, 
                 boxsize : QSize = None, 
                 colordata : ColorData = None, 
                 focuscolor : QColor = None, 
                 framecolor : QColor = None, 
                 framewidth : int = None, 
                 frameshape : QFrame.Shape = QFrame.Box, 
                 spacing : QSize = None):
        super().__init__(parent)
#        self.setFocusPolicy(Qt.StrongFocus)
        self._layout = QGridLayout(self)
        self._btnGrp = QButtonGroup(self)
        self._btnGrp.setExclusive(True)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setHorizontalSpacing(spacing.width() if spacing else 3)
        self._layout.setVerticalSpacing(spacing.height() if spacing else 3)
        
        self._gridsize = colordata.size if colordata else QSize(1, 1)
        self._boxsize = boxsize if boxsize else QSize(16, 16)
        self._shape = frameshape if frameshape else QFrame.Box
        self._framewidth = framewidth if framewidth else 1
        self._framecolor = framecolor if framecolor else QColor(Qt.black)
        self._focuscolor = focuscolor if focuscolor else QColor(Qt.blue)
        self._focuswidget = QFocusFrame()
        
        self._initGrid(colordata.colors if colordata else [])

    #==================================================#
    # Reimplemented Public Methods                     #
    #==================================================#
    def minimumSizeHint(self) -> QSize:
        width = ( self._gridsize.width() * self._boxsize.width()
                 + (self._gridsize.width() - 1) * self._layout.horizontalSpacing()
                 + self.contentsMargins().left() + self.contentsMargins().right())
        height = (self._gridsize.height() * self._boxsize.height()
                 +(self._gridsize.height() - 1) * self._layout.verticalSpacing()
                 + self.contentsMargins().top() + self.contentsMargins().bottom())
        return QSize(width, height)
        
    def sizeHint(self) -> QSize:
        return self.minimumSizeHint()
    
    #==================================================#
    # Private Methods                                  #
    #==================================================#
    def _initGrid(self, colors : list):
        for row in range(self._gridsize.height()):
            for column in range(self._gridsize.width()):
                if len(colors) - 1 < row or len(colors[row]) - 1 < column:
                    item = QSpacerItem(self._boxsize.width(), 
                                       self._boxsize.height(), 
                                       QSizePolicy.Fixed, 
                                       QSizePolicy.Fixed)
                    self._layout.addItem(item, row, column)
                else:                    
                    item = ColorFrame(color=colors[row][column], 
                                      framecolor=self._framecolor, 
                                      focuscolor=self._focuscolor, 
                                      shape=self._shape)
                    item.setFixedSize(self._boxsize)
                    item.setFlat(True)
                    item.setCheckable(True)
                    self._layout.addWidget(item, row, column)
                    idx = self._layout.indexOf(item)
                    self._btnGrp.addButton(item, idx)
    #==================================================#
    # Event Handling                                   #
    #==================================================#
    def keyPressEvent(self, ev):
        if ev.modifiers() != Qt.NoModifier:
            super().keyPressEvent(ev)
            return
        
        index = self._layout.indexOf(self.focusWidget())
        (row, column, rspan, cspan) = self._layout.getItemPosition(index)
        endrow = self._layout.rowCount() -1
        endcol = self._layout.columnCount() - 1
        
        key = ev.key()
        if key == Qt.Key_Right:
            if column < endcol: column += 1
            else:               column = 0
        elif key == Qt.Key_Left:
            if column > 0:      column -= 1
            else:               column = endcol
        elif key == Qt.Key_Up:
            if row > 0:         row -= 1
            else:               row = endrow
        elif key == Qt.Key_Down:
            if row < endrow:    row += 1
            else:               row = 0
        else:
            super().keyPressEvent(ev)
            return
        #FIXME: does not account for LayoutItems without a widget
        item = self._layout.itemAtPosition(row, column)
        item.widget().setFocus(Qt.TabFocusReason)
        ev.accept()
    
    def hoverEvent(self, ev):
        if ev.type() == QEvent.HoverLeave:
            self._focuswidget.setWidget(None)
            ev.accept()
            return
        else:
            self._focuswidget.setWidget(self.childAt(ev.pos()))
    #==================================================#
    # Getters                                          #
    #==================================================#
    def boxSize(self) -> QSize:
        return self._boxsize
        
    def color(self, row : int = 0, column : int = 0):
        if row > self._layout.rowCount() - 1:
            row = self._layout.rowCount() - 1
        if column > self._layout.columnCount() - 1:
            column = self._layout.columnCount()
        item = self._layout.itemAt(row, column)
        if item.widget():
            return item.widget().color()
        return QColor()
        
    def gridSize(self) -> QSize:
        return self._gridsize
    
    def focusColor(self) -> QColor:
        return self._focuscolor
    
    def frameColor(self) -> QColor:
        return self._focuscolor
        
    def frameWidth(self) -> int:
        return self._framewidth
        
    def frameShape(self) -> QFrame.Shape:
        return self._shape
        
    def spacing(self) -> QSize:
        return QSize(self._layout.horizontalSpacing(), 
                     self._layout.verticalSpacing())
        
    #==================================================#
    # Setters                                          #
    #==================================================#
    def setBoxSize(self, size : QSize) -> None:
        for button in iter(self._btnGrp.buttons()):
            button.setFixedSize(size)
        self._boxsize = size
        
    def setColors(self, colors : ColorData) -> None:
        while self._layout.count() != 0:
            item = self._layout.takeAt(0)
            del item
        for item in iter(self._btnGrp.buttons()):
            self._btnGrp.removeButton(item)
            item.setParent(None)
            del item
        self._gridsize = colors.size
        self._initGrid(colors.colors)
        
    def setColor(self, color : QColor, row = 0, column = 0) -> None:
        if row > self._layout.rowCount() - 1:
            row = self._layout.rowCount() - 1
        if column > self._layout.columnCount() - 1:
            column = self._layout.columnCount()
        item = self._layout.itemAt(row, column)
        if item.widget():
            item.widget().setColor(color)
        else:
            item = ColorFrame(color=color, 
                                  framecolor=self._framecolor, 
                                  focuscolor=self._focuscolor, 
                                  shape=self._shape)
            item.setFixedSize(self._boxsize)
            item.setFlat(True)
            item.setCheckable(True)
            self._layout.addWidget(item, row, column)
            idx = self._layout.indexOf(item)
            self._btnGrp.addButton(item, idx)

    def setFocusColor(self, color : QColor) -> None:
        for button in iter(self._btnGrp.buttons()):
            button.setFocusColor(color)
        self._focuscolor = color
        
    def setFrameColor(self, color : QColor) -> None:
        for button in iter(self._btnGrp.buttons()):
            button.setFrameColor(color)
        self._framecolor = color
        
    def setFrameWidth(self, width : int) -> None:
        for button in iter(self._btnGrp.buttons()):
            button.setFrameWidth(width)
        self._framewidth = width
        
    def setFrameShape(self, frameshape : QFrame.Shape) -> None:
        for button in iter(self._btnGrp.buttons()):
            button.setFrameShape(frameshape)
        self._shape = frameshape
        
    def setSpacing(self, spacing : QSize):
        self._layout.setHorizontalSpacing(spacing.width())
        self._layout.setVerticalSpacing(spacing.height())
    
    boxSize = pyqtProperty(QSize, fget=boxSize, fset=setBoxSize)
    focusColor = pyqtProperty(QColor, fget=focusColor, fset=setFocusColor)
    frameColor = pyqtProperty(QColor, fget=frameColor, fset=setFrameColor)
    frameWidth = pyqtProperty(int, fget=frameWidth, fset=setFrameWidth)
    frameShape = pyqtProperty(QFrame.Shape, fget=frameShape, fset=setFrameShape)
    spacing = pyqtProperty(QSize, fget=spacing, fset=setSpacing)
    
class ColorFrame(QPushButton):
    
    def __init__(self, 
                 color : QColor = None, 
                 framecolor : QColor = None, 
                 focuscolor : QColor = None, 
                 frameshape : QFrame.Shape = QFrame.Box,
                 framewidth : int = 1, 
                 margin : int = 3, 
                 size : QSize = QSize(22, 22), 
                 parent : QWidget = None):
        super().__init__(parent)
        self.setAutoFillBackground(True)
        self.setForegroundRole(QPalette.WindowText)
        self.setFixedSize(size)
        self.focusColor = QColor(focuscolor if focuscolor else Qt.blue)
        self.frameColor = QColor(framecolor if framecolor else Qt.black)
        self.color = QColor(color if color else Qt.transparent)
        self.frameShape = frameshape
        self.margin = margin if margin else 3

    #==================================================#
    # Getters                                          #
    #==================================================#
    def _color(self) -> QColor:
        return self.__color
        
    def _focusColor(self) -> QColor:
        return self.__focuscolor
        
    def _frameShape(self) -> QFrame.Shape:
        return self.__shape
        
    def _frameColor(self) -> QColor:
        return self.__framecolor
        
    def _margin(self) -> int:
        return self.__margin
    #==================================================#
    # Setters                                          #
    #==================================================#
    @pyqtSlot(QColor)
    def setColor(self, color : QColor) -> None:
        self.__color = QColor(color)
        self.update()
        
    def setFocusColor(self, color : QColor) -> None:
        self.__focuscolor = QColor(color)
        pal = self.palette()
        pal.setColor(QPalette.BrightText, color)
        self.setPalette(pal)
        self.update()
    
    def setFrameColor(self, color : QColor) -> None:
        self.__framecolor = QColor(color)
        pal = self.palette()
        pal.setColor(QPalette.WindowText, color)
        self.setPalette(pal)
        self.update()
    
    def setFrameShape(self, shape : QFrame.Shape) -> None:
        self.__shape = QFrame.Shape(shape)
        self.update()
        
    def setMargin(self, margin) -> None:
        self.__margin = margin
        self.update()
    
    #==================================================#
    # Private Methods                                  #
    #==================================================#
    def initStyleOption(self, opt : QStyleOptionFrameV3):
        opt.initFrom(self)
        opt.frameShape = self.frameShape
        
        if self.isFlat():
            if self.isChecked():
                opt.state |= QStyle.State_Sunken
                opt.state |= QStyle.State_On
            elif self.isDown():
                opt.state |= QStyle.State_Sunken
        else:
            opt.state |= QStyle.State_Sunken
        
        opt.lineWidth = 1
        opt.midLineWidth = 0
    
    def paintEvent(self, pe : QPaintEvent):
        painter = QPainter()
        painter.begin(self)
        opt = QStyleOptionFrameV3()
        self.initStyleOption(opt)
        opt.rect = self.rect().adjusted(1, 1, -1, -1)
#        opt.rect = self.frameRect()
        if opt.state & QStyle.State_Sunken:
            pass
            
        elif opt.state & QStyle.State_MouseOver:
            pass
        painter.fillRect(opt.rect, self.color)
        self.style().drawControl(QStyle.CE_ShapedFrame, opt, painter, self)
        if opt.state & QStyle.State_HasFocus:
            fropt = QStyleOptionFocusRect()
            fropt.initFrom(self)
            fropt.rect = opt.rect.adjusted(-self.margin, -self.margin,
                                           self.margin, self.margin)
            fropt.backgroundColor = opt.palette.color(QPalette.Window)
            self.style().drawPrimitive(QStyle.PE_FrameFocusRect, fropt, painter, self)
        painter.end()
        
    color = pyqtProperty(QColor, fget=_color, fset=setColor)
    margin = pyqtProperty(int, fget=_margin, fset=setMargin)
    focusColor = pyqtProperty(QColor, fget=_focusColor, fset=setFocusColor)
    frameColor = pyqtProperty(QColor, fget=_frameColor, fset=setFrameColor)
    frameShape = pyqtProperty(QFrame.Shape, fget=_frameShape, fset=setFrameShape)

#    def enterEvent(self, ev):
#        self.setForegroundRole(QPalette.BrightText)
##        self.setLineWidth(2)
#        
#    def leaveEvent(self, ev):
#        self.setForegroundRole(QPalette.WindowText)
##        self.setLineWidth(1)
