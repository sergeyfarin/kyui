from PyQt4.QtCore import Qt
from PyQt4.QtGui import QGroupBox

class ToolGroup(QGroupBox):
    def __init__(self, 
                 title : str = None, 
                 parent : QWidget = None, 
                 action : ExtendedAction = None, 
                 alignment : Qt.Alignment = Qt.AlignHCenter, 
                 flat : bool = False, 
                 checkable : bool = False, 
                 checked : bool = False):
        if title:
            self.__init__(title, parent)
        else:
            self.__init__(parent)
        if alignment: self.setAlignment(alignment)
        if flat: self.setFlat(flat)
        if checkable:
            self.setCheckable(checkable)
            if checked:
                self.setChecked(checked)
