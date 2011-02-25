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

#class ColorPicker(QWidget):
#    #==================================================#
#    # Signals                                          #
#    #==================================================#
#    currentColorChanged = pyqtSignal([QColor], [int, int])
#    colorHovered = pyqtSignal([QColor], [int, int])
#
#    def __init__(self, 
#                 parent : QWidget = None, 
#                 boxsize : QSize = None, 
#                 colordata : ColorData = None, 
#                 focuscolor : QColor = None, 
#                 framecolor : QColor = None, 
#                 framewidth : int = None, 
#                 frameshape : QFrame.Shape = QFrame.Box, 
#                 spacing : QSize = None):
#        super().__init__(parent)
#        self.__layout = QGridLayout(self)
#        self.__btnGrp = QButtonGroup(self)
#        self.__btnGrp.setExclusive(True)
#        self._layout.setHorizontalSpacing(spacing.width() if spacing else 1)
#        self._layout.setVerticalSpacing(spacing.height() if spacing else 1)

class ColorFrame(QFrame):
    #==================================================#
    # Signals                                          #
    #==================================================#
    
    def __init__(self, 
                 parent : QWidget = None, 
                 color : QColor = Qt.white, 
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
        self.shape = shape
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
        self.__margin = margin if margin > 0 else 0
        rect = self.rect().adjusted(-margin, -margin, -margin, -margin)
        self.setFrameRect(rect)
        self.update()

    #==================================================#
    # Public Methods                                   #
    #==================================================#
    def sizeHint(self):
        return self.minimumSizeHint()
    
    def minimumSizeHint(self):
        width = self.boxSize.width() + (2 * self.margin) + 2
        height = self.boxSize.height() + (2 * self.margin) + 2
        return QSize(width, height)

    #==================================================#
    # Private Methods                                  #
    #==================================================#
    def initStyleOption(self, opt : QStyleOptionFrameV3):
        opt.initFrom(self)
        opt.frameShape = super().frameShape()
        opt.frameShadow = QFrame.Plain if self.flat else QFrame.Sunken
        
        opt.lineWidth = self.lineWidth()
        opt.midLineWidth = self.midLineWidth()
        opt.rect = self.frameRect()
        if not self.flat:
            opt.state |= QStyle.State_Sunken
    
    
    def paintEvent(self, pe : QPaintEvent):
        painter = QPainter()
        painter.begin(self)
        opt = QStyleOptionFrameV3()
        self.initStyleOption(opt)
        if opt.state & QStyle.State_Sunken:
            pass
            
        elif opt.state & QStyle.State_MouseOver:
            pass
#        painter.fillRect(opt.rect, self.color)
        self.style().drawControl(QStyle.CE_ShapedFrame, opt, painter, self)
#        elif opt.state & QStyle.State_MouseOver:
#            painter.setPen(self.hoverColor)
#            painter.drawRect(opt.rect)
#        else:
#            painter.setPen(self.frameColor)
#            painter.drawRect(opt.rect)
            
        if opt.state & QStyle.State_HasFocus:
            fropt = QStyleOptionFocusRect()
            fropt.initFrom(self)
            fropt.rect = self.rect()
            fropt.backgroundColor = self.color
            self.style().drawPrimitive(QStyle.PE_FrameFocusRect, fropt, painter, self)
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
