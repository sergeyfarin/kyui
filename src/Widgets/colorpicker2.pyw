#UTF-8
#colorpicker.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ColorPicker(QWidget):
    #==================================================#
    # Signals                                          #
    #==================================================#
    currentColorChanged = pyqtSignal([QColor], [int, int])
    colorHovered = pyqtSignal([QColor], [int, int])

    def __init__(self, 
                 parent : QWidget = None, 
                 gridsize : QSize = None,  
                 hovercolor : QColor = None, 
                 framecolor : QColor = None, 
                 shape : QFrame.Shape = QFrame.StyledPanel, 
                 boxSize : QSize = QSize(22, 22), 
                 margin : int = 2, 
                 flat = True):
        super().__init__(parent)
        self._grid = []
        
    def __initGrid(self, size):
        if len(self._grid) != 0:
            for row in iter(self._grid):
                for widget in iter(row):
                    widget.setParent(None)
                    del widget
                row = []
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

    #==================================================#
    # Getters                                          #
    #==================================================#
    def _boxSize(self) -> QSize:
        return self.__boxSize
    
    def _flat(self) -> bool:
        return self.__flat == True
    
    def _hoverColor(self) -> QColor:
        return self.__hoverColor
        
    def _frameColor(self) -> QColor:
        return self.__frameColor
        
    def _frameShape(self) -> QFrame.Shape:
        return self.__frameShape
    
    def _gridSize(self) -> QSize:
        return QSize(len(self._grid[0]), len(self._grid))
    
    def _margin(self) -> int:
        return self.__margin

    #==================================================#
    # Setters                                          #
    #==================================================#
    def setBoxSize(self, size : QSize):
        self.__boxSize = QSize(size)
        for row, column in range(self.gridsize.height()), range(self.gridsize.width()):
            self._grid[row][column].boxSize = self.__boxSize
            
    def setFlat(self, flat : bool):
        self.__flat = flat == True
        for row, column in range(self.gridsize.height()), range(self.gridsize.width()):
            self._grid[row][column].flat = self.__flat
    
    def setFrameColor(self, color : QColor):
        self.__frameColor = QColor(color)
        for row, column in range(self.gridsize.height()), range(self.gridsize.width()):
            self._grid[row][column].frameColor = self.__frameColor
    
    def setFrameShape(self, shape : QFrame.Shape):
        self.__shape = QFrame.Shape(shape)
        for row, column in range(self.gridsize.height()), range(self.gridsize.width()):
            self._grid[row][column].frameShape = self.__frameShape
            
    def setHoverColor(self, color : QColor):
        self.__hoverColor = QColor(color)
        for row, column in range(self.gridsize.height()), range(self.gridsize.width()):
            self._grid[row][column].hoverColor = self.__hoverColor
    
    def setGridSize(self, size : QSize):
        self.__initGrid(size)
        
    def setMargin(self, margin : int):
        self.__margin = margin
        for row, column in range(self.gridsize.height()), range(self.gridsize.width()):
            self._grid[row][column].margin = margin

    boxSize = pyqtProperty(QSize, fget=_boxSize, fset=setBoxSize)
    flat = pyqtProperty(bool, fget=_flat, fset=setFlat)
    frameColor = pyqtProperty(QColor, fget=_frameColor, fset=setFrameColor)
    frameShape = pyqtProperty(QFrame.Shape, fget=_frameShape, fset=setFrameShape)
    gridSize = pyqtProperty(QSize, fget=_gridSize, fset=setGridSize)
    hoverColor = pyqtProperty(QColor, fget=_hoverColor, fset=setHoverColor)
    margin = pyqtProperty(int, fget=_margin, fset=setMargin)

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
    def _boxSize(self) -> QSize:
        return self.__boxsize
    
    def _color(self) -> QColor:
        return self.__color
        
    def _flat(self) -> bool:
        return super().frameShadow() == QFrame.Plain
        
    def frameShadow(self) -> None:
        qWarning('ColorFrame: use flat property instead of frameShadow.')

    def _frameColor(self) -> QColor:
        return self.palette().color(QPalette.WindowText)
    
    def _hoverColor(self) -> QColor:
        return self.palette().color(QPalette.Highlight)
    
    def _margin(self) -> int:
        return self.__margin

    #==================================================#
    # Setters                                          #
    #==================================================#
    def setBoxSize(self, size : QSize):
        self.__boxsize = QSize(size)
        self.updateGeometry()
        self.update()
    
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
        return QSize(self.boxSize.width(), self.boxSize.height())

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
            if opt.state & QStyle.State_MouseOver:
                painter.setPen(self.hoverColor)
                fill = QColor(self.hoverColor)
                fill.setAlpha(63)
                painter.setBrush(fill)
            else:
                painter.setPen(self.frameColor)
            painter.drawRect(outerRect)
            painter.fillRect(innerRect, self.color)
        painter.end()

    def enterEvent(self, ev):
        super().enterEvent(ev)
        self.setForegroundRole(QPalette.Highlight)
        
    def leaveEvent(self, ev):
        super().enterEvent(ev)
        self.setForegroundRole(QPalette.WindowText)

    #==================================================#
    # Properties                                       #
    #==================================================#
    boxSize = pyqtProperty(QSize, fget=_boxSize, fset=setBoxSize)
    color = pyqtProperty(QColor, fget=_color, fset=setColor)
    flat = pyqtProperty(bool, fget=_flat, fset=setFlat)
    frameColor = pyqtProperty(QColor, fget=_frameColor, fset=setFrameColor)
    hoverColor = pyqtProperty(QColor, fget=_hoverColor, fset=setHoverColor)
    margin = pyqtProperty(int, fget=_margin, fset=setMargin)
