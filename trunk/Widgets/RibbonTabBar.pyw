from PyQt4.QtCore import *
from PyQt4.QtGui import *

# Uses tab shape to determine if widget is oriented Horizontally or Vertically
ShapeOrientation = {QTabBar.RoundedNorth : Qt.Horizontal, 
                    QTabBar.RoundedSouth : Qt.Horizontal, 
                    QTabBar.TriangularNorth : Qt.Horizontal, 
                    QTabBar.TriangularSouth : Qt.Horizontal, 
                    QTabBar.RoundedWest : Qt.Vertical, 
                    QTabBar.RoundedEast : Qt.Vertical, 
                    QTabBar.TriangularWest : Qt.Vertical, 
                    QTabBar.TriangularEast : Qt.Vertical}

class KyRibbonTabBar(QTabBar):
    def __init__(self, parent : QWidget = None):
        super().__init__(parent)
        self.__minimumTabSize = QSize(25, 23)
        if ShapeOrientation[self.shape()] == Qt.Horizontal:
            self.__orientation = Qt.Horizontal
        else:
            self.__orientation = Qt.Vertical
        
    # Uses the tab count and orientation to calculate the minimum size for the tab bar
    def minimumSizeHint(self) -> QSize:
        if self.__orientation == Qt.Horizontal:
            hint = QSize(self.count() * self.__minimumTabSize.width(),
                         self.__minimumTabSize.height())
        else:
            hint = QSize(self.__minimumTabSize.width(), 
                         self.count() * self.__minimumTabSize.height())
        return hint
        
    def resizeEvent(self, event : QResizeEvent) -> None:
        size = event.size()
        if size < self.sizeHint():
            tabRects = self._calculateTabRects(size)
        event.accept()
        
    def _calculateTabRects(self, size: QSize) -> tuple:
        rects = tuple()
        for tab in range(self.count() - 1):
            pass
    
    # Defines orientation to help calculate minimum tab size hint
    def setShape(self, shape : QTabBar.Shape = QTabBar.RoundedNorth) -> None:
        self.__orientation = ShapeOrientation[shape]
        super().setShape(shape)
        
    def sizeHint(self) -> QSize:
        return super().sizeHint()
        
    def tabSizeHint(self, index = 0) -> QSize:
        return super().tabSizeHint(index)
        
    # Ribbons should never be in document mode, so this does nothing, really
    def setDocumentMode(self, mode = False) -> None:
        super().setDocumentMode(False)
        
    # Ribbon tabs should never auto-expand, so this does nothing, really
    def setExpanding(self, expanding = False) -> None:
        super().setExpanding(False)
