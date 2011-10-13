from PyQt4.QtCore import Qt, QObject, pyqtProperty
from PyQt4.QtGui import QFrame
from PyQt4.QtGui import QPainter, QStyle, QStyleOption

class Separator(QFrame):
    def __init__(self, *args, **kwargs):
        if len(args) == 2:
            assert(isinstance(args[0], Qt.Orientation))
            assert(isinstance(args[1], QObject))
            orient = args[0]
            parent = args[1]
        else:
            if len(args) == 1:
                assert(isinstance(args[1], QObject))
                parent = args[1]
            else:
                if 'parent' not in kwargs:
                    raise ValueError
                parent = kwargs.pop('parent')
            
            if 'orientation' in kwargs:
                orient = kwargs.pop('orientation')
            else:
                orient = Qt.Horizontal
        super().__init__(parent, **kwargs)
        
        self.__orient = None
        self.orientation = orient
        
    def paintEvent(self, ev):
        p = QPainter(self)
        opt = QStyleOption()
        opt.initFrom(self)
        
        self.style().drawPrimitive(QStyle.PE_IndicatorToolBarSeparator, 
                                   opt, p, self)
        
    def getOrientation(self):
        return Qt.Orientation(self.__orient)
        
    def setOrientation(self, orient):
        assert(isinstance(orient, Qt.Orientation))
        if orient == self.__orient:
            return
        
        self.__orient = orient
        
        extant = self.style().pixelMetric(QStyle.PM_ToolBarSeparatorExtent)
        
        if orient == Qt.Horizontal:
            self.setFixedSize(16777215, extant)
        else:
            self.setFixedSize(extant, 16777215)
    
    orientation = pyqtProperty(Qt.Orientation, 
                               fset=setOrientation, 
                               fget=getOrientation)
