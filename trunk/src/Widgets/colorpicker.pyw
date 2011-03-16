#UTF-8
#colorpicker.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ColorFrame(QFrame):
    #==================================================#
    # Signals                                          #
    #==================================================#
    
    def __init__(self, 
                 parent : QWidget = None, 
                 color : QColor = Qt.transparent, 
                 frameColor : QColor = Qt.black, 
                 hoverColor : QColor = Qt.blue, 
                 margin : QSize = 2, 
                 boxSize : QSize = QSize(22, 22), 
                 flat : bool = True, 
                 shape : QFrame.Shape = QFrame.StyledPanel):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setFocusPolicy(Qt.StrongFocus)
        self.color = color
        self.frameColor = frameColor
        self.hoverColor = hoverColor
        self.flat = flat
        self.setFrameShape(shape)
        self.margin = margin
        self.boxSize = boxSize

    #==================================================#
    # Getters                                          #
    #==================================================#
    def getBoxSize(self) -> QSize:
        return self.__boxsize
    
    def getColor(self) -> QColor:
        return self.__color
        
    def getFlat(self) -> bool:
        return super().frameShadow() == QFrame.Plain
        
    def frameShadow(self) -> None:
        qWarning('ColorFrame: use flat property instead of frameShadow.')

    def getFrameColor(self) -> QColor:
        return self.palette().color(QPalette.WindowText)
    
    def getHoverColor(self) -> QColor:
        return self.palette().color(QPalette.Highlight)
    
    def getMargin(self) -> int:
        return self.__margin

    #==================================================#
    # Setters                                          #
    #==================================================#
    def setBoxSize(self, size : QSize):
        self.__boxsize = QSize(size)
        self.setFixedSize(size)
    
    @pyqtSlot(QColor)
    def setColor(self, color : QColor):
        self.__color = color
        self.update()

    def setFlat(self, flat : bool):
        super().setFrameShadow(QFrame.Plain if flat else QFrame.Sunken)

    def setHoverColor(self, color : QColor) -> None:
        pal = self.palette()
        pal.setColor(QPalette.Highlight, color)
        self.setPalette(pal)
    
    def setFrameColor(self, color : QColor) -> None:
        pal = self.palette()
        pal.setColor(QPalette.WindowText, color)
        self.setPalette(pal)

    def setFrameShadow(self, shadow):
        qWarning('ColorFrame: use flat property instead of frameShadow.')

    def setMargin(self, margin : int) -> None:
        self.__margin = margin if margin > 1 else 1
        self.update()

    #==================================================#
    # Public Methods                                   #
    #==================================================#
    def sizeHint(self):
        return self.minimumSizeHint()
    
    def minimumSizeHint(self):
        return QSize(self.boxSize)

    #==================================================#
    # Private Methods                                  #
    #==================================================#
    def paintEvent(self, pe : QPaintEvent):
        painter = QPainter()
        painter.begin(self)
        opt = QStyleOptionFrameV3()
        opt.initFrom(self)
        opt.frameShape = self.frameShape()
        
        opt.lineWidth = 1
        opt.midLineWidth = 0
        
        outerRect = self.rect().adjusted(0, 0, -1, -1)
        innerRect = opt.rect.adjusted(self.margin, self.margin, 
                                      -self.margin, -self.margin)
        if not self.flat:
            opt.state |= QStyle.State_Sunken
            opt.rect = innerRect
            painter.fillRect(innerRect, self.color)
            self.style().drawControl(QStyle.CE_ShapedFrame, opt, painter, self)
            if opt.state & QStyle.State_HasFocus:
                fropt = QStyleOptionFocusRect()
                fropt.initFrom(self)
                fropt.rect = outerRect
                fropt.backgroundColor = QColor(Qt.white)
                self.style().drawPrimitive(QStyle.PE_FrameFocusRect, 
                                           fropt, painter, self)
        else:
            if opt.state & QStyle.State_MouseOver or opt.state & QStyle.State_HasFocus:
                painter.setPen(self.hoverColor)
                fill = QColor(self.hoverColor)
                fill.setAlpha(63)
                painter.setBrush(fill)
            else:
                painter.setPen(self.frameColor)
            if opt.frameShape == QFrame.NoFrame:
                painter.fillRect(self.rect(), self.color)
            else:
                painter.drawRect(outerRect)
                painter.fillRect(innerRect, self.color)
        painter.end()

    def enterEvent(self, ev):
        super().enterEvent(ev)
        self.setForegroundRole(QPalette.Highlight)
        
    def leaveEvent(self, ev):
        super().enterEvent(ev)
        self.setForegroundRole(QPalette.WindowText)
        
    def mouseReleaseEvent(self, ev):
        super().mouseReleaseEvent(ev)

    #==================================================#
    # Properties                                       #
    #==================================================#
    boxSize = pyqtProperty(QSize, fget=getBoxSize, fset=setBoxSize)
    color = pyqtProperty(QColor, fget=getColor, fset=setColor)
    flat = pyqtProperty(bool, fget=getFlat, fset=setFlat)
    frameColor = pyqtProperty(QColor, fget=getFrameColor, fset=setFrameColor)
    hoverColor = pyqtProperty(QColor, fget=getHoverColor, fset=setHoverColor)
    margin = pyqtProperty(int, fget=getMargin, fset=setMargin)

#TODO: Keypad navigation, currentColorChanged, mouse events
class ColorPicker(QWidget):
    #==================================================#
    # Signals                                          #
    #==================================================#
    currentColorChanged = pyqtSignal([QColor], [int, int])
    colorHovered = pyqtSignal([QColor], [int, int])

    def __init__(self, 
                 parent : QWidget = None, 
                 gridSize : QSize = None,  
                 hoverColor : QColor = None, 
                 frameColor : QColor = None, 
                 shape : QFrame.Shape = QFrame.StyledPanel, 
                 boxSize : QSize = QSize(22, 22), 
                 margin : int = 2, 
                 flat : bool = True, 
                 spacing : QSize = QSize(2, 2)):
        super().__init__(parent)
        self.setFocusPolicy(Qt.StrongFocus)
        self._grid = []
        
        self.spacing = spacing
        self.__hoverColor = hoverColor if hoverColor else QColor(Qt.blue)
        self.__frameColor = frameColor if frameColor else QColor(Qt.gray)
        self.__shape = shape
        self.__boxSize = boxSize
        self.__margin = margin
        self.__flat = flat
        self.__initGrid(gridSize if gridSize else QSize(2, 2))
        
    def __initGrid(self, size):
        if self._grid != []:
            for row in iter(self._grid):
                while len(row) != 0:
                    widget = row.pop()
                    widget.setParent(None)
                    del widget
            self._grid = []
        for row in range(size.height()):
            self._grid.append([])
            for column in range(size.width()):
                self._grid[row].append(ColorFrame(parent=self, 
                                                  color=Qt.transparent, 
                                                  hoverColor=self.hoverColor, 
                                                  frameColor=self.frameColor, 
                                                  shape=self.frameShape, 
                                                  margin=self.margin, 
                                                  boxSize=self.boxSize, 
                                                  flat=self.flat))
                self._grid[row][column].show()
        self.updateGeometry()
        self.update()

    #==================================================#
    # Reimplemented Public Methods                     #
    #==================================================#
    def sizeHint(self) -> QSize:
        return self.minimumSizeHint()
        
    def minimumSizeHint(self) -> QSize:
        (left, top, right, bottom) = self.getContentsMargins()
        columns = self.columnCount()
        rows = self.rowCount()
        xspacing = columns * self.spacing.width()
        yspacing = rows * self.spacing.height()
        width = left + right + xspacing + self.boxSize.width() * columns
        height = top + bottom + yspacing + self.boxSize.height() * rows
        return QSize(width, height)

    #==================================================#
    # Reimplemented Private Methods                    #
    #==================================================#
    def resizeEvent(self, ev):
        (left, top, right, bottom) = self.getContentsMargins()
        rect = self.rect()

        if rect.width() > self.sizeHint().width():
            xpad = (rect.width() - self.sizeHint().width()) / (self.columnCount() + 1)
        else:
            xpad = self.spacing.width()
        if rect.height() > self.sizeHint().height():
            ypad = (rect.height() - self.sizeHint().height()) / (self.rowCount() + 1)
        else:
            ypad = self.spacing.height()
        x = rect.x() + left + xpad
        y = rect.y() + top + ypad
        width = self.boxSize.width()
        height = self.boxSize.height()
        for row in range(self.rowCount()):
            for column in range(self.columnCount()):
                self._grid[row][column].move(x, y)
                x += xpad + width
            y += ypad + height
            x = rect.x() + left + xpad
    
    def keyPressEvent(self, ev):
        super().keyPressEvent(ev)

    #==================================================#
    # Getters                                          #
    #==================================================#
    def color(self, row, column) -> QColor:
        widget = self.index(row, column)
        return widget.color if widget else QColor()
        
    def columnCount(self) -> int:
        if len(self._grid) != 0:
            return len(self._grid[0])
        return 0
            
    def rowCount(self) -> int:
        return len(self._grid)
        
    def index(self, row, column) -> ColorFrame:
        if row < self.rowCount() and column < self.columnCount():
            return self._grid[row][column]
        qWarning('Index not found')
        return None
    #==================================================#
    # Setters                                          #
    #==================================================#
    def setColor(self, row : int, column : int, color : QColor):
        widget = self.index(row, column)
        if widget:
            widget.color = color
        
    #==================================================#
    # Property Getters                                 #
    #==================================================#
    def getBoxSize(self) -> QSize:
        return self.__boxSize
    def getFlat(self) -> bool:
        return self.__flat == True
    def getFrameColor(self) -> QColor:
        return self.__frameColor
    def getFrameShape(self) -> QFrame.Shape:
        return self.__shape
    def getGridSize(self) -> QSize:
        rows = len(self._grid)
        if rows != 0:
            return QSize(len(self._grid[0]), rows)
    def getHoverColor(self) -> QColor:
        return self.__hoverColor
    def getMargin(self) -> int:
        return self.__margin
    def getSpacing(self) -> QSize:
        return self.__spacing

    #==================================================#
    # Property Setters                                 #
    #==================================================#
    def setBoxSize(self, size : QSize):
        self.__boxSize = QSize(size)
        for row in range(self.rowCount()):
            for column in range(self.columnCount()):
                self._grid[row][column].boxSize = self.__boxSize
        self.updateGeometry()
        
    def setFlat(self, flat : bool):
        self.__flat = flat
        for row in range(self.rowCount()):
            for column in range(self.columnCount()):
                self._grid[row][column].flat = self.__flat
    
    def setFrameColor(self, color : QColor):
        self.__frameColor = QColor(color)
        for row in range(self.rowCount()):
            for column in range(self.columnCount()):
                self._grid[row][column].frameColor = self.__frameColor
    
    def setFrameShape(self, shape : QFrame.Shape):
        self.__shape = QFrame.Shape(shape)
        for row in range(self.rowCount()):
            for column in range(self.columnCount()):
                self._grid[row][column].setFrameShape(self.__shape)

    def setHoverColor(self, color : QColor):
        self.__hoverColor = QColor(color)
        for row in range(self.rowCount()):
            for column in range(self.columnCount()):
                self._grid[row][column].hoverColor = self.__hoverColor
    
    def setGridSize(self, size : QSize):
        self.__initGrid(size)
        
    def setMargin(self, margin : int):
        self.__margin = margin
        for row in range(self.rowCount()):
            for column in range(self.columnCount()):
                self._grid[row][column].margin = margin
            
    def setSpacing(self, spacing : QSize):
        self.__spacing = QSize(spacing)
        self.updateGeometry()

    #==================================================#
    # Properties                                       #
    #==================================================#
    boxSize = pyqtProperty(QSize, fget=getBoxSize, fset=setBoxSize)
    flat = pyqtProperty(bool, fget=getFlat, fset=setFlat)
    frameColor = pyqtProperty(QColor, fget=getFrameColor, fset=setFrameColor)
    frameShape = pyqtProperty(QFrame.Shape, fget=getFrameShape, fset=setFrameShape)
    gridSize = pyqtProperty(QSize, fget=getGridSize, fset=setGridSize)
    hoverColor = pyqtProperty(QColor, fget=getHoverColor, fset=setHoverColor)
    margin = pyqtProperty(int, fget=getMargin, fset=setMargin)
    spacing = pyqtProperty(QSize, fget=getSpacing, fset=setSpacing)
