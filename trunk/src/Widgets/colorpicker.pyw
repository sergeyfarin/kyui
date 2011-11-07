#utf-8
#colorpicker.pyw

from PyQt4.QtCore import Qt, pyqtSlot, pyqtSignal, pyqtProperty, qWarning
from PyQt4.QtCore import QSize
from PyQt4.QtGui import QWidget, QFrame
from PyQt4.QtGui import QPainter, QStyle
from PyQt4.QtGui import QStyleOptionFrameV3, QStyleOptionFocusRect
from PyQt4.QtGui import QSizePolicy
from PyQt4.QtGui import QPalette, QColor

class ColorFrame(QFrame):
    def __init__(self, *args, **kwargs):
        if len(args) == 2:
            color = QColor(args[0])
            parent = args[1]
        elif len(args) == 1:
            color = QColor(kwargs.pop('color', Qt.transparent))
            parent = args[0]
        else:
            color = QColor(kwargs.pop('color', Qt.transparent))
            parent = kwargs.pop('parent', None)
        #extract kwargs values won't go into super().__init__() call
        flat = kwargs.pop('flat', True)
        boxSize = kwargs.pop('boxSize', QSize(22, 22))
        margin = kwargs.pop('margin', 2)
        frameColor = QColor(kwargs.pop('frameColor', Qt.black))
        hoverColor = QColor(kwargs.pop('hoverColor', Qt.blue))
        
        kwargs['focusPolicy'] = Qt.StrongFocus
        kwargs['sizePolicy'] = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        super().__init__(parent, **kwargs)
        
        self.__color = color
        self.frameColor = frameColor
        self.hoverColor = hoverColor
        self.flat = flat
        self.__margin = margin
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
        if QColor(color) == self.__color:
            return
        self.__color = QColor(color)
        self.update()

    def setFlat(self, flat : bool):
        self.setFrameShadow(QFrame.Plain if flat else QFrame.Sunken)

    def setMargin(self, margin):
        if margin == self.__margin:
            return
        self.__margin = int(margin) if margin > 1 else 1
        self.update()

    def sizeHint(self):
        """
        Reimplemented from parent class.
        """
        return self.minimumSizeHint()
    
    def minimumSizeHint(self):
        """
        Reimplemented from parent class.
        """
        return QSize(self.boxSize)

    def paintEvent(self, pe):
        """
        Reimplemented from parent class.
        @private
        """
        painter = QPainter()
        painter.begin(self)
        opt = QStyleOptionFrameV3()
        opt.initFrom(self)
        opt.frameShape = self.frameShape()
        opt.frameShadow = self.frameShadow()
        
        opt.lineWidth = 1
        opt.midLineWidth = 0
        
        outerRect = self.rect().adjusted(0, 0, -1, -1)
        innerRect = opt.rect.adjusted(self.margin, self.margin, 
                                      -self.margin, -self.margin)
        if not opt.frameShadow == QFrame.Plain:
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
        """
        Reimplemented from parent class.
        @private
        """
        super().enterEvent(ev)
        self.setForegroundRole(QPalette.Highlight)
        
    def leaveEvent(self, ev):
        """
        Reimplemented from parent class.
        @private
        """
        super().enterEvent(ev)
        self.setForegroundRole(QPalette.WindowText)

    ##@name Qt Properties
    ##@{
    boxSize = pyqtProperty(QSize, fget=getBoxSize, fset=setBoxSize)
    color = pyqtProperty(QColor, fget=getColor, fset=setColor)
    flat = pyqtProperty(bool, fget=getFlat, fset=setFlat)
    margin = pyqtProperty(int, fget=getMargin, fset=setMargin)
    ##@}
    
class ColorPicker(QWidget):
    """
    @brief: Emulates the functionality of the Windows color selection gallery.
    ColorPicker is configurable to be embedded in a dialog, like QColorDialog, 
    or embedding in a palette toolbar.
    
    
    @todo Keypad navigation, mouse events
    """
    #==================================================#
    # Signals                                          #
    #==================================================#
    currentColorChanged = pyqtSignal([QColor], [int, int])
    colorHovered = pyqtSignal([QColor], [int, int])

    def __init__(self, *args, **kwargs):
        if len(args) == 2:
            gridSize = QSize(args[0])
            parent = args[1]
        elif len(args) == 1:
            gridSize = kwargs.pop('gridSize', QSize(2, 2))
            parent = args[0]
        else:
            gridSize = kwargs.pop('gridSize', QSize(2, 2))
            parent = kwargs.pop('parent', None)
        
        #extract kwargs values won't go into super().__init__() call
        flat = kwargs.pop('flat', True)
        boxSize = kwargs.pop('boxSize', QSize(22, 22))
        margin = kwargs.pop('margin', 2)
        frameColor = QColor(kwargs.pop('frameColor', QColor()))
        hoverColor = QColor(kwargs.pop('hoverColor', QColor()))
        frameShape = kwargs.pop('frameShape', QFrame.StyledPanel)
        spacing = kwargs.pop('spacing', QSize(2, 2))
        
        if 'sizePolicy' not in kwargs:
            kwargs['sizePolicy'] = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        super().__init__(parent, **kwargs)
        
        self.__grid = []
        
        if not frameColor.isValid(): 
            frameColor = self.palette().windowText().color()
        if not hoverColor.isValid():
            hoverColor = self.palette().highlight().color()
        
        self.__cfpalette = self.palette()
        self.__cfpalette.setColor(QPalette.Window, Qt.transparent)
        
        self.__cfpalette.setColor(QPalette.WindowText, frameColor)
        self.__cfpalette.setColor(QPalette.Highlight, hoverColor)
        
        self.spacing = spacing
        self.__shape = frameShape
        self.__boxSize = boxSize
        self.__margin = margin
        self.__flat = flat
        self.__initGrid(gridSize)
        
    def __initGrid(self, size):
        if self.__grid != []:
            for row in iter(self.__grid):
                while len(row) != 0:
                    widget = row.pop()
                    widget.setParent(None)
                    del widget
            self.__grid = []
        for row in range(size.height()):
            self.__grid.append([])
            for column in range(size.width()):
                cf = ColorFrame(parent=self, 
                                color=Qt.transparent, 
                                frameShape=self.frameShape, 
                                margin=self.margin, 
                                boxSize=self.boxSize, 
                                flat=self.flat, 
                                palette=self.__cfpalette)
                self.__grid[row].append(cf)
                cf.show()
        self.updateGeometry()
        self.update()

    #==================================================#
    # Reimplemented Public Methods                     #
    #==================================================#
    def sizeHint(self):
        return self.minimumSizeHint()
        
    def minimumSizeHint(self):
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
                self.__grid[row][column].move(x, y)
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
        if len(self.__grid) != 0:
            return len(self.__grid[0])
        return 0
            
    def rowCount(self) -> int:
        return len(self.__grid)
        
    def index(self, row, column) -> ColorFrame:
        if row < self.rowCount() and column < self.columnCount():
            return self.__grid[row][column]
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
        return self.__cfpalette.color(QPalette.WindowText)
    def getFrameShape(self) -> QFrame.Shape:
        return self.__shape
    def getGridSize(self) -> QSize:
        rows = len(self.__grid)
        if rows != 0:
            return QSize(len(self.__grid[0]), rows)
    def getHoverColor(self) -> QColor:
        return self.__cfpalette.color(QPalette.Highlight)
    def getMargin(self) -> int:
        return self.__margin
    def getSpacing(self) -> QSize:
        return self.__spacing

    #==================================================#
    # Property Setters                                 #
    #==================================================#
    def setBoxSize(self, size : QSize):
        self.__boxSize = QSize(size)
        for row in iter(self.__grid):
            for cf in iter(row):
                cf.boxSize = self.__boxSize
        self.updateGeometry()
        
    def setFlat(self, flat : bool):
        self.__flat = bool(flat)
        for row in iter(self.__grid):
            for cf in iter(row):
                cf.flat = self.__flat
    
    def setFrameColor(self, color : QColor):
        #handle passing Qt.GlobalColor, etc as an argument
        color = QColor(color)
        self.__cfpalette.setColor(QPalette.WindowText, color)
        for row in iter(self.__grid):
            for cf in iter(row):
                cf.setPalette(self.__cfpalette)
    
    def setFrameShape(self, shape : QFrame.Shape):
        self.__shape = QFrame.Shape(shape)
        for row in iter(self.__grid):
            for cf in iter(row):
                cf.setFrameShape(self.__shape)

    def setHoverColor(self, color):
        #handle passing Qt.GlobalColor, etc as an argument
        color = QColor(color)
        self.__cfpalette.setColor(QPalette.Highlight, color)
        for row in iter(self.__grid):
            for cf in iter(row):
                cf.setPalette(self.__cfpalette)
    
    def setGridSize(self, size : QSize):
        self.__initGrid(size)
        
    def setMargin(self, margin : int):
        self.__margin = int(margin)
        for row in iter(self.__grid):
            for cf in iter(row):
                cf.margin = margin
            
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
