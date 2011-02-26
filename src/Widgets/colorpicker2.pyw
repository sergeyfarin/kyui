#UTF-8
#colorpicker.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *

OrangeFrame = QColor(242, 148, 54)
OrangeHighlight = QColor(255, 226, 148)

#FrameStyle = namedtuple('FrameStyle', ['shape color highlight margin size'])
#
#class FrameStyle():
#    __slots__ = ['__shape', '__size', '__color', '__margin', '__highlight']
#    def __init__(self):
#        self.__shape = None
#        self.__size = QSize()
#        self.__highlight = QColor()
#        self.__color = QColor()
#        self.__margin = 0

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
                 frameshape : QFrame.Shape = QFrame.Box, 
                 margin : int = 2):
        super().__init__(parent)
        self.__layout = QGridLayout(self)
        self._layout.setHorizontalSpacing(spacing.width() if spacing else 1)
        self._layout.setVerticalSpacing(spacing.height() if spacing else 1)
        self.gridsize = gridsize if gridsize else QSize(1, 1)
        
    def _gridsize(self) -> QSize:
        return self.__gridsize
        
    def setGridSize(self, size):
        self.__gridsize = size
        while self._layout.count() != 0:
            item = self._layout.takeAt(0)
            widget = item.widget()
            del item
        for widget in self.frames:
            widget.setParent(None)
            del widget
        for (row, column) in range(size.width()), range(size.height()):
            pass

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
