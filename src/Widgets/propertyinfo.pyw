#UTF-8
#property_info.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *

PropertyPairs = {'bool' : QCheckBox, 
               'int' : QSpinBox, 
               'double' : QDoubleSpinBox, 
               'str' : QLineEdit, 
               'QTime' : QTimeEdit, 
               'QDate' : QDateEdit, 
               'QDateTime' : QDateTimeEdit, 
               'Enum' : QComboBox, 
               'QKeySequence' : QLineEdit}
               
#SizePolicies = {QSizePolicy.Fixed : 'Fixed', 
#                QSizePolicy.Minimum : 'Minimum', 
#                QSizePolicy.Maximum : 'Maximum', 
#                QSizePolicy.Expanding : 'Expanding', 
#                QSizePolicy.Preferred : 'Preferred'
#                QSizePolicy.MinimumExpanding : 'MinimumExpanding', 
#                QSizePolicy.Ignored : 'Ignored'}

SizePolicies = {0 : 'Fixed', 
                1 : 'Minimum', 
                4 : 'Maximum', 
                5 : 'Preferred', 
                7 : 'Expanding', 
                3 : 'MinimumExpanding', 
                13 : 'Ignored'}

Cursors = ['ArrowCursor', 'UpArrowCursor', 'CrossCursor', 'WaitCursor', 
           'IBeamCursor', 'SizeVerCursor', 'SizeHorCursor', 'SizeBDiagCursor', 
           'SizeFDiagCursor', 'SizeAllCursor', 'BlankCursor', 'SplitVCursor', 
           'SplitHCursor', 'PointingHandCursor', 'ForbiddenCursor', 
           'OpenHandCursor', 'ClosedHandCursor', 'WhatsThisCursor', 
           'BusyCursor', 'DragMoveCursor', 'DragCopyCursor', 'DragLinkCursor', 
           'BitmapCursor']

#used for items that don't use text (QIcon, QPixmap...)
def format_none(value):
    return ''

def format_qcursor(value : QCursor) -> str:
    return Cursors[int(value.shape())]

def format_qsizepolicy(value : QSizePolicy) -> str:
    horiz = QSizePolicy.Policy(value.horizontalPolicy())
    vert = QSizePolicy.Policy(value.verticalPolicy())
    return '{}, {}, Stretch: {} x {}'.format(SizePolicies[horiz], 
                                             SizePolicies[vert], 
                                             value.horizontalStretch(), 
                                             value.verticalStretch())
def format_qfont(value : QFont) -> str:
    return '{}, {}pt, Bold: {}, Italic: {}'.format(value.family(), 
                                                   value.pointSize(), 
                                                   value.bold(), 
                                                   value.italic())

def format_qkeysequence(value: QKeySequence) -> str:
    return value.toString()

def format_qlocale(value : QLocale) -> str:
    return '{}, {}'.format(QLocale.languageToString(value.language()), 
                           QLocale.countryToString(value.country()))

def format_qsize(value : QSize) -> str:
    if not value.isValid():
        return '0 x 0'
    return '{} x {}'.format(value.width(), value.height())

def format_qpoint(value : QSize) -> str:
    return '{} x {}'.format(value.x(), value.y())
    
def format_qline(value : QSize) -> str:
    return '({}, {}), ({}, {})'.format(value.x1(), value.y1(), value.x2(), value.y2())
    
def format_qrect(value : QSize) -> str:
    return '({}, {}), {} x {}'.format(value.x(), value.y(), value.width(), value.height())

def icon_qicon(value : QIcon) -> QIcon:
    return value
    
def icon_qpixmap(value : QPixmap) -> QIcon:
    return QIcon(pixmap)
    

    
def icon_qcolor(value : QColor):
    pixmap = QPixmap(QSize(16, 16))
    pixmap.fill(value)
    return QIcon(pixmap)
    
def icon_qcursor(value : QCursor):
    pixmap = value.pixmap()
    if not pixmap.isNull():
        icon = QIcon(pixmap)
    else:
        icon = QIcon(value.bitmap())
    return icon

FormattableTypes = {'QRect'  : format_qrect, 
                    'QRectF' : format_qrect, 
                    'QSize'  : format_qsize, 
                    'QSizeF' : format_qsize,
                    'QPoint' : format_qpoint, 
                    'QPointF': format_qpoint, 
                    'QLine'  : format_qline, 
                    'QLineF' : format_qline, 
                    'QSizePolicy' : format_qsizepolicy, 
                    'QFont' : format_qfont, 
                    'QLocale' : format_qlocale, 
                    'QIcon' : format_none, 
                    'QColor' : format_none, 
                    'QKeySequence' : format_qkeysequence, 
                    'QCursor' : format_qcursor}
IconTypes = {'QIcon' : icon_qicon, 
             'QPixmap' : icon_qpixmap, 
             'QColor' : icon_qcolor, 
             'QCursor' : icon_qcursor}



def FormatQType(value, qtype):
    if qtype not in FormattableTypes.keys():
       return None
    return FormattableTypes[qtype](value)
    
def generateToolTip(prop : QMetaProperty, widget) -> str:
    tt = '<b>{}</b><br><br>'.format(prop.name())
    tt += 'Constant:   {}<br>'.format(prop.isConstant())
    tt += 'Designable:   {}<br>'.format(prop.isDesignable(widget))
    tt += 'Enum:      {}<br>'.format(prop.isEnumType())
    tt += 'Final:      {}<br>'.format(prop.isFinal())
    tt += 'Flag:      {}<br>'.format(prop.isFlagType())
    tt += 'Readable:   {}<br>'.format(prop.isReadable())
    tt += 'Resettable:   {}<br>'.format(prop.isResettable())
    tt += 'Scriptable:   {}<br>'.format(prop.isScriptable(widget))
    tt += 'Stored:      {}<br>'.format(prop.isStored(widget))
    tt += 'User:      {}<br>'.format(prop.isUser(widget))
    tt += 'Valid:      {}<br>'.format(prop.isValid())
    tt += 'Writable:   {}<br>'.format(prop.isWritable())
    return tt
    
def CreatePropertyItem(property, parent, widget):
    if (property.isValid() and property.isReadable() and property.isDesignable()
            and property.isWritable()):
        value = property.read(widget)
        propType = property.typeName()
        icon = None
        if value == None or isinstance(value, QPyNullVariant):
            text = ''
        elif property.isEnumType():
            enum = property.enumerator()
            propType = enum.name()
            if enum.isFlag():
                text = enum.valueToKeys(int(value)).data().decode()
            else:
                text = enum.valueToKey(int(value))
        elif propType in FormattableTypes:
            if propType in IconTypes:
                icon = IconTypes[propType](value)
            text = FormatQType(value, propType)
        else:
            text = str(value)
        item = QTreeWidgetItem(parent, [property.name(), text, propType])
        item.setToolTip(0, generateToolTip(property, widget))
        if icon:
            item.setIcon(1, icon)
        return item
    return None

#Bool           #QCheckBox
#Brush
#Char           #QLineEdit
#Color          
#Cursor         
#Date           #QDateEdit
#DateTime       #QDateTimeEdit
#Double         #QSpinBox
#EasingCurve
#Font
#Int            #QSpinBox
#KeySequence    
#Line           
#LineF          
#Locale         
#Pen            
#Point          
#PointF         
#Polygon
#Quaternion
#Rect
#RectF
#RegExp
#Size
#SizeF
#SizePolicy
#String         #QLineEdit
#TextLength
#Time           #QTimeEdit
#Vector2D
#Vector3D
#Vector4D


