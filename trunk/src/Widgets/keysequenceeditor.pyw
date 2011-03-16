#UTF-8
#keysequenceeditor.pyw

from PyQt4.QtCore import Qt, pyqtProperty
from PyQt4.QtGui import QLineEdit, QWidget, QKeySequence

Keys = { \
    #Qt.Key_Escape       : 'Esc', 
    Qt.Key_Tab          : 'Tab', 
    Qt.Key_Backspace    : 'Backspace', 
    Qt.Key_Return       : 'Return', 
    Qt.Key_Enter        : 'Enter', 
    Qt.Key_Insert       : 'Ins', 
    Qt.Key_Delete       : 'Del', 
    Qt.Key_Pause        : 'Pause', 
    Qt.Key_Print        : 'PrtScr', 
    Qt.Key_SysReq       : 'SysReq', 
    Qt.Key_Clear        : 'Clear', 
    Qt.Key_Home         : 'Home', 
    Qt.Key_End          : 'End', 
    Qt.Key_Left	    	: 'Left', 
    Qt.Key_Up           : 'Up', 
    Qt.Key_Right        : 'Right', 
    Qt.Key_Down         : 'Down', 
    Qt.Key_PageUp       : 'PgUp', 
    Qt.Key_PageDown     : 'PgDown', 
    Qt.Key_F1           : 'F1', 
    Qt.Key_F2           : 'F2', 
    Qt.Key_F3           : 'F3', 
    Qt.Key_F4           : 'F4', 
    Qt.Key_F5           : 'F5', 
    Qt.Key_F6           : 'F6', 
    Qt.Key_F7           : 'F7', 
    Qt.Key_F8           : 'F8', 
    Qt.Key_F9           : 'F9', 
    Qt.Key_F10          : 'F10', 
    Qt.Key_F11          : 'F11', 
    Qt.Key_F12          : 'F12', 
    Qt.Key_Space        : 'Space', 
    Qt.Key_Apostrophe   : "'", 
    Qt.Key_Asterisk     : '*', 
    Qt.Key_Plus         : '+', 
    Qt.Key_Comma        : ',', 
    Qt.Key_Minus        : '-', 
    Qt.Key_Period       : '.', 
    Qt.Key_Slash        : '/', 
    Qt.Key_0            : '0', 
    Qt.Key_1            : '1', 
    Qt.Key_2            : '2', 
    Qt.Key_3            : '3', 
    Qt.Key_4            : '4', 
    Qt.Key_5            : '5', 
    Qt.Key_6            : '6', 
    Qt.Key_7            : '7', 
    Qt.Key_8            : '8', 
    Qt.Key_9            : '9', 
    Qt.Key_Semicolon    : ';', 
    Qt.Key_Equal        : '=', 
    Qt.Key_A            : 'A', 
    Qt.Key_B            : 'B', 
    Qt.Key_C            : 'C', 
    Qt.Key_D            : 'D', 
    Qt.Key_E            : 'E', 
    Qt.Key_F            : 'F', 
    Qt.Key_G            : 'G', 
    Qt.Key_H            : 'H', 
    Qt.Key_I            : 'I', 
    Qt.Key_J            : 'J', 
    Qt.Key_K            : 'K', 
    Qt.Key_L            : 'L', 
    Qt.Key_M            : 'M', 
    Qt.Key_N            : 'N', 
    Qt.Key_O            : 'O', 
    Qt.Key_P            : 'P', 
    Qt.Key_Q            : 'Q', 
    Qt.Key_R            : 'R', 
    Qt.Key_S            : 'S', 
    Qt.Key_T            : 'T', 
    Qt.Key_U            : 'U', 
    Qt.Key_V            : 'V', 
    Qt.Key_W            : 'W', 
    Qt.Key_X            : 'X', 
    Qt.Key_Y            : 'Y', 
    Qt.Key_Z            : 'Z', 
    Qt.Key_BracketLeft  : '[', 
    Qt.Key_Backslash    : '\\', 
    Qt.Key_BracketRight : ']', 
    #Qt.Key_AsciiCircum  : 
    #Qt.Key_Underscore   : 
    Qt.Key_QuoteLeft    : '`' }
    #Qt.Key_BraceLeft    : 
    #Qt.Key_Bar          : 
    #Qt.Key_BraceRight   : 
    #Qt.Key_AsciiTilde   : 

Modifiers = {Qt.Key_Shift   : 'Shift', 
             Qt.Key_Control : 'Ctrl', 
             Qt.Key_Meta    : 'WinKey', 
             Qt.Key_Alt     : 'Alt'}

class KeySequenceLineEdit(QLineEdit):
    
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setAcceptDrops(False)
        self.setReadOnly(True)
        self.setContextMenuPolicy(Qt.PreventContextMenu)
        self.setFocusPolicy(Qt.ClickFocus)
        self.setPlaceholderText('Click here to enter a key sequence')
        self.currentKey = ''
        self.modState = {Qt.Key_Shift   : False, 
                         Qt.Key_Control : False, 
                         Qt.Key_Meta    : False, 
                         Qt.Key_Alt     : False}
        
    def keyPressEvent(self, event):
        key = event.key()
        if key in self.modState:
            self.modState[key] = True
        elif key in Keys:
            self.currentKey = Keys[key]
        self.printKeys()
        event.accept()
        
    def keyReleaseEvent(self, event):
        key = event.key()
        if key in self.modState:
            self.modState[key] = False
        elif key in Keys:
            self.currentKey = ''
        self.printKeys()
        event.accept()
    
    def focusInEvent(self, event):
        self.grabKeyboard()
        super().focusInEvent(event)
    
    def focusOutEvent(self, event):
        self.releaseKeyboard()
        super().focusOutEvent(event)
    
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
    
class KeySequenceEditor(QWidget):
    def __init__(self, 
                 parent : QWidget, 
                 keysequence : QKeySequence = None, 
                 action = None):
        super().__init__(parent)
        self.__lineEdit = KeySequenceLineEdit(self)
        if keysequence:
            self.__ks = keysequence
        elif action: 
            pass
        else:
            self.__ks = QKeySequence()
    
    def getKeySequence(self) -> QKeySequence:
        return self.__ks
        
    def setKeySequence(self, keysequence : QKeySequence):
        self.__ks = keysequence
        self.lineEdit.setText(keysequence.toString())
    
    def getLineEdit(self) -> KeySequenceLineEdit:
        return self.__lineEdit
        
    lineEdit = pyqtProperty(KeySequenceLineEdit, fget=getLineEdit)
    keySequence = pyqtProperty(QKeySequence, fget=getKeySequence, fset=setKeySequence)
