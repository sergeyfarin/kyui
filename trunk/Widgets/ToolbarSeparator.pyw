from PyQt4.QtCore import Qt
from PyQt4.QtGui import QWidget, QStyle, QStyleOption, QToolbar, QPainter

class KyToolBarSeparator(QWidget):
    def __init__(self, parent: QToolBar = None):
        super().__init__(parent)
        self.__orient = parent.orientation()
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
    
    def orientation(self) -> Qt.Orientation:
        return self.__orientation
        
    def setOrientation(self, orient : Qt.Orientation = Qt.Horizontal) -> None:
        self.__orient = orient
        self.update()

    def initStyleOption(self, option : QStyleOption = None) -> None:
        option.initFrom(self)
        if (self.orientation() == Qt.Horizontal):
            option.state |= QStyle.State_Horizontal

    def sizeHint(self) -> QSize:
        opt = QStyleOption()
        self.initStyleOption(opt)
        extent = style().pixelMetric(QStyle.PM_ToolBarSeparatorExtent, opt, self.parentWidget())
        return QSize(extent, extent);

    def paintEvent(self, event : QPaintEvent) -> None:
        p = QPainter(self)
        opt = QStyleOption()
        self.initStyleOption(opt)
        self.style().drawPrimitive(QStyle.PE_IndicatorToolBarSeparator, opt, p, self.parentWidget())

