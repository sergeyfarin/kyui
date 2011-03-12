#UTF-8
#property_info.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *

ClassPairs = {'QWidget' : QWidget, 
              'QPushButton' : QPushButton, 
              'QToolButton' : QToolButton, 
              'QDialog' : QDialog, 
              'QMenu' : QMenu, 
              'QComboBox' : QComboBox, 
              'QFrame' : QFrame, 
              'QSpinBox' : QSpinBox}

PropertyPairs = {'bool' : QCheckBox, 
               'int' : QSpinBox, 
               'double' : QDoubleSpinBox, 
               'str' : QLineEdit, 
               'QTime' : QTimeEdit, 
               'QDate' : QDateEdit, 
               'QDateTime' : QDateTimeEdit, 
               'Enum' : QComboBox, 
               'QKeySequence' : QLineEdit}
               
SizePolicies = ['Fixed', 'Minimum', 'Maximum', 'Expanding', 'MinimumExpanding', 'Ignored']
                
def format_qsizepolicy(value : QSizePolicy) -> str:
    horiz = int(value.horizontalPolicy())
    vert = int(value.verticalPolicy())
    return 'Policy: {}, {}, Stretch: {} x {}'.format(SizePolicies[horiz], 
                                                     SizePolicies[vert], 
                                                     value.horizontalStretch(), 
                                                     value.verticalStretch())
def format_qfont(value : QFont) -> str:
    return '{}, {}pt, Bold: {}, Italic: {}'.format(value.family(), 
                                                   value.pointSize(), 
                                                   value.bold(), 
                                                   value.italic())

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
                    'QLocale' : format_qlocale}


def FormatQType(value, qtype):
    if qtype not in FormattableTypes.keys():
       return None
    return FormattableTypes[qtype](value)
    

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


