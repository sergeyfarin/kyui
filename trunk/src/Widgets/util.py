from PyQt4.QtCore import Qt, QLocale, QSize, QSizeF
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
    __slots__ = []
    
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
    __slots__ = []
    
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
    """
    @brief A class of static methods to create string representations of QMetaTypes.
    
    QTypeToString is useful when information is needed regarding an object that 
    does not support introspection, or when data about an object that <em>does</em>
    support introspection needs dumping to a user-readable format.
    
    This class can also be used in generating user-readable information in
    model/view classes.
    @see QTypeToIcon
    @see DebugBox
    """
    
    __slots__ = []
    @staticmethod
    def noneType(value):
        """
        @brief Convenience function for unknown types
        @param value Anything
        @returns Empty string
        """
        return ''
    
    @staticmethod
    def cursor(value):
        """
        @brief Returns the enum value of a QCursor.
        @param value QCursor
        @returns str
        """
        return Cursors[value.shape()]
    
    @staticmethod
    def sizepolicy(value):
        """
        @brief Returns a string representation of a QSizePolicy.
        @param value QSizePolicy
        @returns str
        """
        horiz = QSizePolicy.Policy(value.horizontalPolicy())
        vert = QSizePolicy.Policy(value.verticalPolicy())
        return '{}, {}, Stretch: {} x {}'.format(SizePolicies[horiz], 
                                                 SizePolicies[vert], 
                                                 value.horizontalStretch(), 
                                                 value.verticalStretch())
    
    @staticmethod
    def font(value):
        """
        @brief Returns a string describing various attributes of a QFont.
        @param value QFont
        @returns str
        """
        return '{}, {}pt, Bold: {}, Italic: {}'.format(value.family(), 
                                                       value.pointSize(), 
                                                       value.bold(), 
                                                       value.italic())
    
    @staticmethod
    def keysequence(value):
        """
        @brief Returns a string representation of a QKeySequence
        @param value QKeySequence
        @returns str
        """
        return value.toString()
    
    @staticmethod
    def locale(value):
        """
        @brief Returns a a string with information about a QLocale.
        @param value QLocale
        @returns str
        """
        return '{}, {}'.format(QLocale.languageToString(value.language()), 
                               QLocale.countryToString(value.country()))
    
    @staticmethod
    def margins(value):
        """
        @brief Returns a string representation of a QMargins
        @param value QMargin
        @returns str
        """
        if value.isNull():
            return '(Null)'
        return '({}, {}, {}, {})'.format(value.left(), value.top(), 
                                         value.right(), value.bottom())
    @staticmethod
    def size(value):
        """
        @brief Returns a string representation of a QSize or QSizeF.
        @param value QSize or QSizeF
        @returns str
        """
        if not value.isValid():
            return '0.0 x 0.0' if isinstance(value, QSizeF) else '0 x 0'
        return '{} x {}'.format(value.width(), value.height())
    
    @staticmethod
    def point(value):
        """
        @brief Returns a string representation of a QPoint or QPointF.
        @param value QPoint or QPointF
        @returns str
        """
        return '({}, {})'.format(value.x(), value.y())
    
    @staticmethod
    def line(value):
        """
        @brief Returns a string representation of a QLine or QLineF.
        @param value QLine or QLineF
        @returns str
        """
        return '({}, {}), ({}, {})'.format(value.x1(), value.y1(), value.x2(), value.y2())

    @staticmethod
    def rect(value):
        """
        @brief Returns a string representation of a QRect or QRectF.
        @param value QRect or QRectF
        @returns str
        """
        return '({}, {}), {} x {}'.format(value.x(), value.y(), value.width(), value.height())

    @staticmethod
    def icon(value):
        """
        @brief Returns the available sizes of a QIcon in string format.
        @param value QIcon
        @returns str The list of sizes in the format '[(x, y), (x, y)]'
        
        @see QTypeToIcon::icon()
        """
        if value.isNull():
            return '[]'
        retval = '['
        for size in value.sizes():
            retval.append(QTypeToString.size(size))
            retval.append(', ')
        retval.rstrip(', ')
        retval.append(']')
        return value
    
    @staticmethod
    def pixmap(value):
        """
        @brief Accepts a pixmap and returns its size in string format.
        Typically this method will be used in conjunction with QTypeToIcon.pixmap()
        to display an icon of the pixmap itself.
        
        @param value QPixmap
        @returns str
        
        @see QTypeToIcon::pixmap()
        """
        return QTypeToString(value.size())
    
    #QColor
    @staticmethod
    def color(value):
        return 'RGB({}, {}, {})'.format(value.red(), value.blue(), value.green())
