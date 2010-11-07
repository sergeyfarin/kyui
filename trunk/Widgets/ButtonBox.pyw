from PyQt4.QtCore import *
from PyQt4.QtGui import *

from SizePolicies import SizePolicies

class ButtonBox(QFrame):
    def __init__(self, parent = None, depth = 2, orientation = Qt.Horizontal):
        super().__init__(parent)
        
        self.__orientation = orientation
        # depth is the number of rows if orientation is Qt.Horizontal,
        # otherwise depth counts columns
        self.__depth = depth
        
        self.setFrameShape(QFrame.NoFrame)
        self.__layout = QGridLayout(self)
        self.__layout.setSpacing(0)
        self.__layout.setSizeConstraint(QLayout.SetFixedSize)
        
        if orientation == Qt.Horizontal:
            self.setSizePolicy(SizePolicies.Preferred)
        elif orientation == Qt.Vertical:
            self.setSizePolicy(SizePolicies.Preferred)
            
        self.__group = QButtonGroup(self)
        
    def addButton(self, button : QAbstractButton = None, position = 0, 
                  rowspan = 0, columnspan = 0, alignment : Qt.Alignment = 0) -> None:
#        assert isinstance(button, QAbstractButton)
        assert position < self.__depth
        assert position >= 0
        
        if self.__group.id(button) != -1:
            qDebug('Button cannot be added to a button group twice')
            return
        
        
        if self.__orientation == Qt.Horizontal:
            assert rowspan + position < self.__depth
            button.setParent(self)
            self.__layout.addWidget(button, self.__layout.rowCount(),
                                    position, rowspan, columnspan)
            self.__group.addButton(button)
        else: # Qt.Vertical
            assert columnspan + position < self.__depth
            button.setParent(self)
            self.__layout.addWidget(button, position, self.__layout.rowCount(), 
                                    position, rowspan, columnspan, alignment)
            self.__group.addButton(button)
            
    
    def layout(self):
        return self.__layout
