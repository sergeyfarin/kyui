from PyQt4.QtCore import *
from PyQt4.QtGui import *

from SizePolicies import SizePolicies

class ButtonBox(QFrame):
    buttonClicked = pyqtSignal(QAbstractButton)
    buttonPressed = pyqtSignal(QAbstractButton)
    buttonReleased = pyqtSignal(QAbstractButton)
    
    def __init__(self, parent = None, depth = 2, orientation = QBoxLayout.LeftToRight):
        super().__init__(parent)
        self.setFrameShape(QFrame.WinPanel)
        self.setFrameStyle(QFrame.Sunken)
        self.setContentsMargins(2, 2, 2, 2)
        
#        self.__orientation = orientation
        # depth is the number of rows if orientation is Qt.Horizontal,
        # otherwise depth counts columns
        self.__depth = depth
        
#        self.setFrameShape(QFrame.NoFrame)
        self.__layout = QBoxLayout(orientation, self)
        self.__layout.setSpacing(0)
        self.__layout.setSizeConstraint(QLayout.SetFixedSize)
        self.setLayout(self.__layout)
        
        self.__group = QButtonGroup(self)
        
        self.connect(self.__group,  SIGNAL('buttonClicked(QAbstractButton)'), self.buttonClicked.emit)
        self.connect(self.__group,  SIGNAL('buttonPressed(QAbstractButton)'), self.buttonPressed.emit)
        self.connect(self.__group,  SIGNAL('buttonReleased(QAbstractButton)'), self.buttonReleased.emit)
        
    def addButton(self, button : QAbstractButton = None) -> None:
        assert button is not None
        assert self.__group.id(button) == -1
        button.setParent(self)
        self.__layout.addWidget(button)
        self.__group.addButton(button)
        
    def addAction(self, action : QAction = None) -> QToolButton:
        assert isinstance(action, QAction)
        button = QToolButton(self)
        button.setDefaultAction(action)
        self.__layout.addWidget(button)
        self.__group.addButton(button)
        return button
        
    def insertButton(self, button : QAbstractButton = None, row = 0, column = 0) -> None:
        assert button is not None
        assert column < self.__layout.columnCount()
        assert row < self.__depth
        assert self.__group.id(button) == -1
        button.setParent(self)
        self.__layout.addWidget(button, row, column)
        self.__group.addButton(button)
        
    def removeButton(self, button : QAbstractButton = None) -> None:
        assert button is not None
        assert self.__group.id(button) != -1
        self.__group.removeButton(button)
        self.__layout.removeWidget(button)
        
    def id(self, button : QAbstractButton = None) -> int:
        assert button is not None
        return self.__group.id(button)
        
    def button(self, id = -1) -> QWidget:
        return self.__group.button(id)
    def checkedButton(self) -> QWidget:
        return self.__group.checkedButton()
    def exclusive(self) ->  bool:
        return self.__group.exclusive()
    def setExclusive(self, exclusive = True) -> None:
        self.__group.setExclusive(exclusive)
        
    def setIconSize(self, size : QSize = None) -> None:
        assert isinstance(size, QSize)
        for button in self.__group.buttons():
            button.setIconSize(size)
        
    @property
    def buttonGroup(self):
        return self.__group
    
    @property
    def layout(self):
        return self.__layout
