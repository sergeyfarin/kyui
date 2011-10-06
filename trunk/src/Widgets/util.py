from PyQt4.QtCore import Qt, QLocale, QSize, qWarning
from PyQt4.QtGui import QApplication, QKeySequence
from PyQt4.QtGui import QBoxLayout, QSizePolicy
from PyQt4.QtGui import QCursor, QFont
from PyQt4.QtGui import QPixmap, QIcon
from PyQt4.QtGui import QColor, QPalette, QPolygon

class Util():
    @staticmethod
    def mergedColors(colorA : QColor, colorB : QColor, factor = 50) -> QColor:
        return QColor(
            (colorA.red() * factor) / 100 + (colorB.red() * (100 - factor)) / 100, 
            (colorA.green() * factor) / 100 + (colorB.green() * (100 - factor)) / 100, 
            (colorA.blue() * factor) / 100 + (colorB.blue() * (100 - factor)) / 100)
    
    @staticmethod
    def directionFromOrientation(orientation : Qt.Orientation) -> QBoxLayout.Direction:
        if orientation == Qt.Vertical:
            return QBoxLayout.TopToBottom
        elif QApplication.isLeftToRight():
            return QBoxLayout.LeftToRight
        else:
            return QBoxLayout.RightToLeft
    
    @staticmethod
    def orientationFromDirection(direction : QBoxLayout.Direction) -> Qt.Orientation:
        if (direction == QBoxLayout.TopToBottom 
            or direction == QBoxLayout.BottomToTop):
            return Qt.Vertical
        else:
            return Qt.Horizontal
        
class FormatQType():
    @staticmethod
    def noneType(value) -> str:
        return ''
    
    @staticmethod
    def cursor(value : QCursor) -> str:
        return Cursors[int(value.shape())]
    
    @staticmethod
    def sizepolicy(value : QSizePolicy) -> str:
        horiz = QSizePolicy.Policy(value.horizontalPolicy())
        vert = QSizePolicy.Policy(value.verticalPolicy())
        return '{}, {}, Stretch: {} x {}'.format(SizePolicies[horiz], 
                                                 SizePolicies[vert], 
                                                 value.horizontalStretch(), 
                                                 value.verticalStretch())
    @staticmethod
    def font(value : QFont) -> str:
        return '{}, {}pt, Bold: {}, Italic: {}'.format(value.family(), 
                                                       value.pointSize(), 
                                                       value.bold(), 
                                                       value.italic())

    @staticmethod
    def keysequence(value: QKeySequence) -> str:
        return value.toString()

    @staticmethod
    def locale(value : QLocale) -> str:
        return '{}, {}'.format(QLocale.languageToString(value.language()), 
                               QLocale.countryToString(value.country()))

    @staticmethod
    def size(value : QSize) -> str:
        if not value.isValid():
            return '0 x 0'
        return '{} x {}'.format(value.width(), value.height())

    @staticmethod
    def point(value : QSize) -> str:
        return '({}, {})'.format(value.x(), value.y())

    @staticmethod
    def line(value : QSize) -> str:
        return '({}, {}), ({}, {})'.format(value.x1(), value.y1(), value.x2(), value.y2())

    @staticmethod
    def rect(value : QSize) -> str:
        return '({}, {}), {} x {}'.format(value.x(), value.y(), value.width(), value.height())

    @staticmethod
    def icon(value : QIcon) -> QIcon:
        return value
    
    @staticmethod
    def pixmap(value : QPixmap) -> QIcon:
        return QIcon(value)

    @staticmethod
    def color(value : QColor, size = QSize(16, 16)):
        pixmap = QPixmap(size)
        pixmap.fill(value)
        return QIcon(pixmap)

    @staticmethod
    def icon_qcursor(value : QCursor):
        pixmap = value.pixmap()
        if not pixmap.isNull():
            icon = QIcon(pixmap)
        else:
            icon = QIcon(value.bitmap())
        return icon
