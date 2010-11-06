from PyQt4.QtCore import *
from PyQt4.QtGui import *
from keys import Keys, Modifiers

class KeyPressCatcher(QLineEdit):
    debugEvent = pyqtSignal('QString')
    
    modState = { \
        Qt.Key_Shift        : False, 
        Qt.Key_Control      : False, 
        Qt.Key_Meta         : False, 
        Qt.Key_Alt          : False, 
        Qt.Key_Super_L		: False, 
        Qt.Key_Super_R	    : False, 
        Qt.Key_Menu	        : False, 
        Qt.Key_Help	        : False,
        Qt.Key_Hyper_L	    : False, 
        Qt.Key_Hyper_R	    : False }
    currentKey = ''
    
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setAcceptDrops(False)
        self.setReadOnly(True)
        self.setContextMenuPolicy(Qt.PreventContextMenu)
        self.setFocusPolicy(Qt.ClickFocus)
        
    def keyPressEvent(self, event):
        key = event.key()
        if key in Modifiers:
            self.modState[key] = True
        elif key in Keys:
            self.currentKey = Keys[key]
        self.printKeys()
        event.accept()
        
    def keyReleaseEvent(self, event):
        key = event.key()
        if key in Modifiers:
            self.modState[key] = False
        elif key in Keys:
            self.currentKey = ''
        event.accept()
    
    def printKeys(self):
        keys = ''
        if self.modState[Qt.Key_Control]:
            keys += Modifiers[Qt.Key_Control] + '+'
        if self.modState[Qt.Key_Shift]:
            keys += Modifiers[Qt.Key_Shift] + '+'
        if self.modState[Qt.Key_Meta]:
            keys += Modifiers[Qt.Key_Meta] + '+'
        if self.modState[Qt.Key_Alt]:
            keys += Modifiers[Qt.Key_Alt] + '+'
        keys += self.currentKey
        self.setText(keys)
