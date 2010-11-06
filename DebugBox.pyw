from PyQt4.QtCore import *
from PyQt4.QtGui import *

class DebugBox(QPlainTextEdit):
    def __init__(self, text = None, parent = None):
        super().__init__(parent)
        if text:
            self.setPlainText(text)
        self.setReadOnly(True)
        self.setFrameShape(QFrame.Panel)
        self.setFrameShadow(QFrame.Sunken)

    
    def printMessage(self, text):
            self.appendPlainText(text)
