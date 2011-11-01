#utf-8
#debugbox.pyw

from PyQt4.QtCore import QtDebugMsg, QtWarningMsg, QtCriticalMsg, QtFatalMsg
from PyQt4.QtGui import QPlainTextEdit, QFrame


class DebugBox(QPlainTextEdit):
    """
    @brief Class to print Qt debug messages inside a GUI window.
    Use qInstallMsgHandler() with the DebugBox instance's postMsg() method
    to enable DebugBox to print debug output. Critical and Fatal errors will
    be shunted to the console. Warning messages will be prepended with 'Warning: '
    to differentiate them from debug messages.
    """
    
    def __init__(self, *args, **kwargs):
        """
        @brief Uses the same argument options as QPlainTextEdit's constructor.
        """
        if len(args) == 2:
            kwargs['plainText'] = args[0]
            parent = args[1]
        elif len(args) == 1:
            parent = args[0]
        else:
            parent = kwargs['parent', None]
            
        kwargs['readOnly'] = True
        if 'frameShape' not in kwargs:
            kwargs['frameShape'] = QFrame.StyledPanel
        if 'frameShadow' not in kwargs:
            kwargs['frameShadow'] = QFrame.Sunken
        super().__init__(parent, **kwargs)
    
    def postMsg(self, msgType = QtDebugMsg, text : str = None):
        """
        @brief Processes debug messages.
        @param msgType QtMsgType Message type
        @param text str Contents of the generated message
        """
        if msgType == QtDebugMsg:
            self.appendPlainText(bytes.decode(text))
        elif msgType == QtWarningMsg:
            self.appendPlainText('Warning: ' + bytes.decode(text))
        elif msgType == QtCriticalMsg:
            print('Critical: ' + bytes.decode(text))
        elif msgType == QtFatalMsg:
            print('Fatal: ' + bytes.decode(text))
        else:
            print('Unknown Error: ' + bytes.decode(text))
