from PyQt4.QtCore import *
from PyQt4.QtGui import *

class KyMenuButton(QToolButton):
    def __init__(self, parent = None, icon : QIcon = None, text : str = None, 
                 menu : QMenu = None):
        super().__init__(parent)
        if isinstance(icon, QIcon):
            self.setIcon(icon)
        if isinstance(text, str):
            self.setText(text)
        if isinstance(menu, QMenu):
            self.setMenu(menu)
        self.setFixedHeight(25)
        self.setPopupMode(QToolButton.InstantPopup)
        self.setAutoRaise(False)
