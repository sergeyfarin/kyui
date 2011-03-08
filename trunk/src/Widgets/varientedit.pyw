from PyQt4.QtCore import *
from PyQt4.QtGui import *

class QDataType():
    __slots__ = ['name', 'variantType', 'editor', 'properties', 'data']
    def __init__(self):
        self.name = 'Invalid'
        self.variantType = QVariant.Invalid
        self.editor = QWidget
        self.data = {}
        self.properties = self.data.keys()
        
    @staticmethod
    def generateEditor(self) -> QWidget:
        return self.editor(parent)
    
class QBoolType(QDataType):
    __slots__ = []
    def __init__(self, value : bool = False):
        super().__init__()
        self.name = 'Bool'
        self.variantType = QVariant.Bool
        self.editor = QCheckBox
        self.data['bool'] = False

class QIntType(QDataType):
    __slots__ = []
    def __init__(self, value : int = 0):
        self.name = 'Int'
        self.variantType = QVariant.Int
        self.editor = QSpinBox
        self.data['int'] = value

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

