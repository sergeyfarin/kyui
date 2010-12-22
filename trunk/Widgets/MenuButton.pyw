from PyQt4.QtCore import *
from PyQt4.QtGui import *

class KyMenuButton(QToolButton):
    def __init__(self, parent = None, icon : QIcon = None, text : str = None, 
                 menu : QMenu = None):
        super().__init__(parent)
        self.setPopupMode(QToolButton.InstantPopup)
        self.setAutoRaise(True)
        self.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        if isinstance(icon, QIcon):
            self.setIcon(icon)
        if isinstance(text, str):
            self.setText(text)
        if isinstance(menu, QMenu):
            menu.setParent(self)
            self.setMenu(menu)
