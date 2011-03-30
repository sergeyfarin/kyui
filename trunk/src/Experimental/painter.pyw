#UTF-8
#painter.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from .colors import *

def ToolGroupPopupColors():
    gradient = QLinearGradient()
    gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
    gradient.setColorAt(0.0, Win7Color.PopupFrameOuterUpper)
    gradient.setColorAt(1.0, Win7Color.PopupFrameOuterLower)
    gradient.setStart(0.5, 0.0)
    gradient.setFinalStop(0.5, 1.0)
    outerPen = QPen(QBrush(gradient), 1.0)
    
    gradient = QLinearGradient()
    gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
    gradient.setColorAt(0.0, Win7Color.PopupFrameInnerUpper)
    gradient.setColorAt(1.0, Win7Color.PopupFrameInnerLower)
    gradient.setStart(0.5, 0.0)
    gradient.setFinalStop(0.5, 1.0)
    innerPen = QPen(QBrush(gradient), 1.0)

    gradient = QLinearGradient()
    gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
    gradient.setColorAt(0.0, Win7Color.ToolGroupUpper)
    gradient.setColorAt(1.0, Win7Color.ToolGroupLower)
    gradient.setStart(0.5, 0.0)
    gradient.setFinalStop(0.5, 1.0)
    brush = QBrush(gradient)
    return (outerPen, innerPen, brush)
    
class ToolGroupButtonColors():
    def __init__(self, state):
        if state == QStyle.State_Sunken:
            self.outerPen = QPen(Win7Color_Down.ToolButtonFrameOuter)
            self.innerPen = QPen(Win7Color_Down.ToolButtonFrameInner)
            gradient = QLinearGradient()
            gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
            gradient.setColorAt(0.0, Win7Color_Down.ToolButtonTopUpper)
            gradient.setColorAt(1.0, Win7Color_Down.ToolButtonTopLower)
            gradient.setStart(0.5, 0.0)
            gradient.setFinalStop(0.5, 1.0)
            self.topBrush = QBrush(gradient)
        
            gradient = QRadialGradient(QPointF(0.5, 1.0), 0.5, QPointF(0.5, 1.25))
            gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
            gradient.setColorAt(0.0, Win7Color_Down.ToolButtonBottomUpper)
#            gradient.setColorAt(0.33, QColor(213, 229, 238))
            gradient.setColorAt(1.0, Win7Color_Down.ToolButtonBottomLower)
            self.bottomBrush = QBrush(gradient)
            
            self.cornerPixmap = QPixmap(2, 2)
            self.cornerPixmap.fill(Qt.transparent)
            color = QColor(Win7Color_Down.ToolButtonFrameOuter)
            
            p = QPainter()
            p.begin(self.cornerPixmap)
            
            color.setAlphaF(0.85)
            p.setPen(color)
            p.drawPoint(QPoint(1, 0))
            p.drawPoint(QPoint(0, 1))
            
            color.setAlphaF(0.6)
            p.setPen(color)
            p.drawPoint(QPoint(1, 1))
            color.setAlphaF(0.10)
            p.setPen(color)
            p.drawPoint(QPoint(0, 0))
            p.end()
        elif state == QStyle.State_MouseOver:
            self.outerPen = QPen(Win7Color_Hover.ToolButtonFrameOuter)
            self.innerPen = QPen(Win7Color_Hover.ToolButtonFrameInner)
            
            gradient = QLinearGradient()
            gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
            gradient.setColorAt(0.0, Win7Color_Hover.ToolButtonTopUpper)
            gradient.setColorAt(1.0, Win7Color_Hover.ToolButtonTopLower)
            gradient.setStart(0.5, 0.0)
            gradient.setFinalStop(0.5, 1.0)
            self.topBrush = QBrush(gradient)
        
            gradient = QRadialGradient(QPointF(0.5, 1.0), 0.66, QPointF(0.5, 1.66))
            gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
            gradient.setColorAt(1.0, Win7Color_Hover.ToolButtonBottomLower)
            gradient.setColorAt(0.0, Win7Color_Hover.ToolButtonBottomUpper)
            self.bottomBrush = QBrush(gradient)
            self.cornerPixmap = QPixmap(2, 2)
            self.cornerPixmap.fill(Qt.transparent)
            
            color = QColor(Win7Color_Hover.ToolButtonFrameOuter)
            p = QPainter()
            p.begin(self.cornerPixmap)
            p.setPen(color)
            p.drawPoint(QPoint(1, 0))
            p.drawPoint(QPoint(0, 1))
            color.setAlphaF(0.33)
            p.setPen(color)
            p.drawPoint(QPoint(1, 1))
            color.setAlphaF(0.10)
            p.setPen(color)
            p.drawPoint(QPoint(0, 0))
            p.end()
        else:
            self.outerPen = QPen(Win7Color_Normal.ToolButtonFrameOuter)
            self.innerPen = QPen(Win7Color_Normal.ToolButtonFrameInner)
            
            gradient = QLinearGradient()
            gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
            gradient.setColorAt(0.0, Win7Color_Normal.ToolButtonTopUpper)
            gradient.setColorAt(1.0, Win7Color_Normal.ToolButtonTopLower)
            gradient.setStart(0.5, 0.0)
            gradient.setFinalStop(0.5, 1.0)
            self.topBrush = QBrush(gradient)
        
            gradient = QRadialGradient(QPointF(0.5, 1.0), 0.66, QPointF(0.5, 1.66))
            gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
            gradient.setColorAt(1.0, Win7Color_Normal.ToolButtonBottomLower)
            gradient.setColorAt(0.0, Win7Color_Normal.ToolButtonBottomUpper)
            self.bottomBrush = QBrush(gradient)
            self.cornerPixmap = QPixmap(2, 2)
            self.cornerPixmap.fill(Qt.transparent)
            
            color = QColor(Win7Color_Normal.ToolButtonFrameOuter)
            p = QPainter()
            p.begin(self.cornerPixmap)
            p.setPen(color)
            p.drawPoint(QPoint(1, 0))
            p.drawPoint(QPoint(0, 1))
            color.setAlphaF(0.33)
            p.setPen(color)
            p.drawPoint(QPoint(1, 1))
            color.setAlphaF(0.10)
            p.setPen(color)
            p.drawPoint(QPoint(0, 0))
            p.end()

def arrowPixmap() -> QPixmap:
    pixmap = QPixmapCache.find('ky_win7_arrow')
    if pixmap:
        return pixmap
    pixmap = QPixmap(QSize(5, 4))
    pixmap.fill(Qt.transparent)
    p = QPainter()
    p.begin(pixmap)
    p.setPen(Win7Color_Normal.Text)
    p.drawLine(QPoint(0, 0), QPoint(4, 0))
    p.drawLine(QPoint(1, 1), QPoint(3, 1))
    p.drawPoint(QPoint(2, 2))
    p.setPen(Win7Color_Normal.Text_Transparent)
    p.drawPoints(QPoint(0, 1), 
                 QPoint(1, 2), 
                 QPoint(2, 3), 
                 QPoint(3, 2), 
                 QPoint(4, 1))
    p.end()
    QPixmapCache.insert('ky_win7_arrow', pixmap)
    return pixmap
