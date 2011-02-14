from PyQt4.QtCore import QtDebugMsg, QtWarningMsg, QtCriticalMsg, QtFatalMsg
from PyQt4.QtGui import QPlainTextEdit, QFrame, QWidget

class DebugBox(QPlainTextEdit):
    def __init__(self, parent : QWidget = None, text : str = None):
        super().__init__(parent)
        if text:
            self.setPlainText(text)
        self.setReadOnly(True)
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Sunken)
    
    def postMsg(self, msgType = QtDebugMsg, text : str = None) -> None:
        if msgType == QtDebugMsg:
            self.appendPlainText('Debug: ' + bytes.decode(text))
        elif msgType == QtWarningMsg:
            self.appendPlainText('Warning: ' + bytes.decode(text))
        elif msgType == QtCriticalMsg:
            print('Critical: ' + bytes.decode(text))
        elif msgType == QtFatalMsg:
            print('Fatal: ' + bytes.decode(text))
        else:
            print('Unknown Error: ' + bytes.decode(text))
