from PyQt4.QtCore import Qt, QLocale, QSize
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QBoxLayout, QSizePolicy
from PyQt4.QtGui import QPixmap, QIcon
from PyQt4.QtGui import QColor

SizePolicies = {0 : 'Fixed', 
                1 : 'Minimum', 
                4 : 'Maximum', 
                5 : 'Preferred', 
                7 : 'Expanding', 
                3 : 'MinimumExpanding', 
                13 : 'Ignored'}

Cursors = { Qt.ArrowCursor : 'ArrowCursor', 
            Qt.UpArrowCursor : 'UpArrowCursor', 
            Qt.CrossCursor : 'CrossCursor', 
            Qt.WaitCursor : 'WaitCursor', 
            Qt.IBeamCursor : 'IBeamCursor', 
            Qt.SizeVerCursor : 'SizeVerCursor', 
            Qt.SizeHorCursor : 'SizeHorCursor', 
            Qt.SizeBDiagCursor : 'SizeBDiagCursor', 
            Qt.SizeFDiagCursor : 'SizeFDiagCursor', 
            Qt.SizeAllCursor : 'SizeAllCursor', 
            Qt.BlankCursor : 'BlankCursor', 
            Qt.SplitVCursor : 'SplitVCursor', 
            Qt.SplitHCursor : 'SplitHCursor', 
            Qt.PointingHandCursor : 'PointingHandCursor', 
            Qt.ForbiddenCursor : 'ForbiddenCursor', 
            Qt.OpenHandCursor : 'OpenHandCursor', 
            Qt.ClosedHandCursor : 'ClosedHandCursor', 
            Qt.WhatsThisCursor : 'WhatsThisCursor', 
            Qt.BusyCursor : 'BusyCursor', 
            Qt.DragMoveCursor : 'DragMoveCursor', 
            Qt.DragCopyCursor : 'DragCopyCursor', 
            Qt.DragLinkCursor : 'DragLinkCursor', 
            Qt.BitmapCursor : 'BitmapCursor'}

class Util():
    @staticmethod
    def mergedColors(colorA : QColor, colorB : QColor, factor = 50) -> QColor:
        return QColor(
            (colorA.red() * factor) / 100 + (colorB.red() * (100 - factor)) / 100, 
            (colorA.green() * factor) / 100 + (colorB.green() * (100 - factor)) / 100, 
            (colorA.blue() * factor) / 100 + (colorB.blue() * (100 - factor)) / 100)
    
    @staticmethod
    def directionFromOrientation(orientation : Qt.Orientation):
        if orientation == Qt.Vertical:
            return QBoxLayout.TopToBottom
        elif QApplication.isLeftToRight():
            return QBoxLayout.LeftToRight
        else:
            return QBoxLayout.RightToLeft
    
    @staticmethod
    def orientationFromDirection(direction : QBoxLayout.Direction):
        if (direction == QBoxLayout.TopToBottom 
            or direction == QBoxLayout.BottomToTop):
            return Qt.Vertical
        else:
            return Qt.Horizontal

class QTypeToIcon():
    @staticmethod
    def noneType(value):
        return ''

    #QIcon
    @staticmethod
    def icon(value):
        return value
    
    #QPixmap
    @staticmethod
    def pixmap(value):
        return QIcon(value)
    
    #QColor
    @staticmethod
    def color(value, size = QSize(16, 16)):
        pixmap = QPixmap(size)
        pixmap.fill(value)
        return QIcon(pixmap)
    
    #QCursor
    @staticmethod
    def cursor(value):
        pixmap = value.pixmap()
        if not pixmap.isNull():
            icon = QIcon(pixmap)
        else:
            icon = QIcon(value.bitmap())
        return icon

class QTypeToString():
    @staticmethod
    def noneType(value):
        return ''
    
    #QCursor
    @staticmethod
    def cursor(value):
        return Cursors[value.shape()]
    
    #QSizePolicy
    @staticmethod
    def sizepolicy(value):
        horiz = QSizePolicy.Policy(value.horizontalPolicy())
        vert = QSizePolicy.Policy(value.verticalPolicy())
        return '{}, {}, Stretch: {} x {}'.format(SizePolicies[horiz], 
                                                 SizePolicies[vert], 
                                                 value.horizontalStretch(), 
                                                 value.verticalStretch())
    #QFont
    @staticmethod
    def font(value):
        return '{}, {}pt, Bold: {}, Italic: {}'.format(value.family(), 
                                                       value.pointSize(), 
                                                       value.bold(), 
                                                       value.italic())
    
    #QKeySequence
    @staticmethod
    def keysequence(value):
        return value.toString()
    
    #QLocale
    @staticmethod
    def locale(value):
        return '{}, {}'.format(QLocale.languageToString(value.language()), 
                               QLocale.countryToString(value.country()))
    
    #QMargins
    @staticmethod
    def margins(value):
        if value.isNull():
            return '(Null)'
        return '({}, {}, {}, {})'.format(value.left(), value.top(), 
                                         value.right(), value.bottom())
    #QSize
    @staticmethod
    def size(value):
        if not value.isValid():
            return '0 x 0'
        return '{} x {}'.format(value.width(), value.height())
    
    #QPoint
    #QPointF
    @staticmethod
    def point(value):
        return '({}, {})'.format(value.x(), value.y())
    
    #QLine
    #QLineF
    @staticmethod
    def line(value):
        return '({}, {}), ({}, {})'.format(value.x1(), value.y1(), value.x2(), value.y2())

    #QRect
    #QRectF
    @staticmethod
    def rect(value):
        return '({}, {}), {} x {}'.format(value.x(), value.y(), value.width(), value.height())

    #QIcon
    @staticmethod
    def icon(value):
        return value
    
    #QPixmap
    @staticmethod
    def pixmap(value):
        return QIcon(value)
    
    #QColor
    @staticmethod
    def color(value, size = QSize(16, 16)):
        pixmap = QPixmap(size)
        pixmap.fill(value)
        return QIcon(pixmap)
