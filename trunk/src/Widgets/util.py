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
    """
    A collection of methods useful for various purposes bundled in one class
    """
    __slots__ = []
    
    @staticmethod
    def mergedColors(colorA, colorB, factor = 50):
        """
        Python version of internal QPlastiqueStyle to blend two colors
        @brief Blends two colors.
        @param colorA QColor
        @param colorB QColor
        @param factor int: Balance between the two colors. Must be between 0 and 100.
        @returns QColor
        """
        return QColor(
            (colorA.red() * factor) / 100 + (colorB.red() * (100 - factor)) / 100, 
            (colorA.green() * factor) / 100 + (colorB.green() * (100 - factor)) / 100, 
            (colorA.blue() * factor) / 100 + (colorB.blue() * (100 - factor)) / 100)
    
    @staticmethod
    def directionFromOrientation(orientation):
        """
        Determines the direction to set a QBoxLayout layout based on the
        orientation of  widget. This method takes into account right-to-left locales.
        
        This method is useful when a layout is dependant on the orientation of
        a widget like a QSlider. If the orientation of the slider changes,
        labels or other associated widgets in the layout will need re-arranging.
        
        @brief Determines direction for a layout based on widget orientation.
        @param orientation Qt.Orientation
        @returns QBoxLayout.Direction
        @see orientationFromDirection
        """
        if orientation == Qt.Vertical:
            return QBoxLayout.TopToBottom
        elif QApplication.isLeftToRight():
            return QBoxLayout.LeftToRight
        else:
            return QBoxLayout.RightToLeft
    
    @staticmethod
    def orientationFromDirection(direction : QBoxLayout.Direction):
        """
        Determines the orienation a widget should have based on the direction
        used in a layout. This can be useful for QSliders or other 
        Qt.Orientation-dependant widgets inside of a QBoxLayout
        
        @brief Determines orientation for a widget based on layout direction.
        @param direction QBoxLayout.Direction
        @returns Qt.Orientation
        @see directionFromOrientation
        """
        if (direction == QBoxLayout.TopToBottom 
            or direction == QBoxLayout.BottomToTop):
            return Qt.Vertical
        else:
            return Qt.Horizontal

class QTypeToIcon():
    """
    @brief Class of static methods to create icons representing QMetaType instances.
    QTypeToIcon is a class of static methods that can be used in conjunction 
    with QTypeToString for displaying information about different QMetaType 
    instances within a model view. QTypeToIcon is specifically meant for
    incorporation into a model/view framework. QtDesigner performs scaling with
    icons and QCursors, but this class works with more object classes.
    @see QTypeToString
    """
    
    @staticmethod
    def noneType(value, size = QSize(16, 16)):
        """
        Convenience method for unknown types.
        @param value Any object
        @param size QSize: Unused
        @returns QIcon
        """
        return QIcon()

    @staticmethod
    def icon(value, size = QSize(16, 16)):
        """
        Convenience method for QIcons.
        @param value QIcon
        @param size QSize: Unused
        @returns QIcon
        """
        return value
    
    
    @staticmethod
    def pixmap(value, size = QSize(16, 16)):
        """
        Creates an icon of a QPixmap
        @param value QPixmap
        @param size QSize: Unused
        @returns QIcon
        """
        return QIcon(value)

    @staticmethod
    def color(value, size = QSize(16, 16)):
        """
        Creates an icon representing a QColor.
        @param value QIcon
        @param size QSize: Size of the icon to generate.
        @returns QIcon
        """
        pixmap = QPixmap(size)
        pixmap.fill(value)
        return QIcon(pixmap)
    
    @staticmethod
    def cursor(value, size = QSize(16, 16)):
        """
        Creates an icon representing a QCursor.
        @param value QIcon
        @param size QSize: Size of the icon to generate.
        @returns QIcon
        """
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
    
    @staticmethod
    def noneType(value):
        """
        Convenience function for unknown types.
        @param value Any object
        @returns str: Empty string
        """
        return ''
    
    @staticmethod
    def cursor(value):
        """
        Returns the enum value of a QCursor.
        @param value QCursor
        @returns str
        """
        return Cursors[value.shape()]
    
    @staticmethod
    def sizepolicy(value):
        """
        Returns a string representation of a QSizePolicy.
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
        Returns a string describing various attributes of a QFont.
        @param value QFont
        @returns str
        """
        retval = '{}, {}pt'.format(value.family(), value.pointSize())
        if value.bold():
            retval.append(', Bold')
        if value.italic():
            retval.append(', Italic')
        return retval
    
    @staticmethod
    def keysequence(value):
        """
        Returns a string representation of a QKeySequence
        @param value QKeySequence
        @returns str: Formatted using QKeySequence::toString
        """
        return value.toString()
    
    @staticmethod
    def locale(value):
        """
        Returns a a string with information about a QLocale.
        @param value QLocale
        @returns str: Formatted as 'language, country'
        """
        return '{}, {}'.format(QLocale.languageToString(value.language()), 
                               QLocale.countryToString(value.country()))
    
    @staticmethod
    def margins(value):
        """
        Returns a string representation of a QMargins
        @param value QMargin
        @returns str: Formated as '(left, top, right, bottom)'
        """
        if value.isNull():
            return '(Null)'
        return '({}, {}, {}, {})'.format(value.left(), value.top(), 
                                         value.right(), value.bottom())
    @staticmethod
    def size(value):
        """
        Returns a string representation of a QSize or QSizeF.
        This method does a check that the object contains valid values.
        @param value QSize or QSizeF
        @returns str: Formatted as '(x, y)'
        """
        if not value.isValid():
            return '0.0 x 0.0' if isinstance(value, QSizeF) else '0 x 0'
        return '{} x {}'.format(value.width(), value.height())
    
    @staticmethod
    def point(value):
        """
        Returns a string representation of a QPoint or QPointF.
        @param value QPoint or QPointF
        @returns str: Formatted as '(x, y)'
        """
        return '({}, {})'.format(value.x(), value.y())
    
    @staticmethod
    def line(value):
        """
        Returns a string representation of a QLine or QLineF.
        @param value QLine or QLineF
        @returns str: Formatted as '(x1, y1), (x2, y2)'
        """
        return '({}, {}), ({}, {})'.format(value.x1(), value.y1(), value.x2(), value.y2())

    @staticmethod
    def rect(value):
        """
        Returns a string representation of a QRect or QRectF.
        @param value QRect or QRectF
        @returns str: Formatted as '(x, y), width x height'
        """
        return '({}, {}), {} x {}'.format(value.x(), value.y(), value.width(), value.height())

    @staticmethod
    def icon(value):
        """
        Returns the available sizes of a QIcon in string format.
        @param value QIcon
        @returns str: The list of sizes in the format '[(x, y), (x, y)]'
        @see QTypeToIcon::icon
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
        Accepts a pixmap and returns its size in string format.
        
        Typically this method will be used in conjunction with QTypeToIcon.pixmap()
        to display an icon of the pixmap itself.
        
        @param value QPixmap
        @returns str
        @see QTypeToIcon::pixmap
        """
        return QTypeToString(value.size())
    
    @staticmethod
    def color(value):
        """
        Returns a string representation of a QColor's RGB values.
        @param value QColor
        @returns str
        """
        return 'RGB({}, {}, {})'.format(value.red(), value.blue(), value.green())

FormattableIcons = {'QIcon' : QTypeToIcon.icon, 
                    'QPixmap' : QTypeToIcon.pixmap, 
                    'QColor' : QTypeToIcon.color, 
                    'QCursor' : QTypeToIcon.cursor}

FormattableStrings = {  'QRect'  : QTypeToString.rect, 
                        'QRectF' : QTypeToString.rect, 
                        'QSize'  : QTypeToString.size, 
                        'QSizeF' : QTypeToString.size,
                        'QPoint' : QTypeToString.point, 
                        'QPointF': QTypeToString.point, 
                        'QLine'  : QTypeToString.line, 
                        'QLineF' : QTypeToString.line, 
                        'QSizePolicy' : QTypeToString.sizepolicy, 
                        'QFont' : QTypeToString.font, 
                        'QLocale' : QTypeToString.locale, 
                        'QIcon' : QTypeToString.icon, 
                        'QColor' : QTypeToString.color, 
                        'QKeySequence' : QTypeToString.keysequence, 
                        'QCursor' : QTypeToString.cursor}
