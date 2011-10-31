#utf-8
#debugbox.pyw

from PyQt4.QtCore import QtDebugMsg, QtWarningMsg, QtCriticalMsg, QtFatalMsg
from PyQt4.QtGui import QPlainTextEdit, QFrame


class DebugBox(QPlainTextEdit):
    """DebugBox
    A class to print Qt debug messages inside a GUI
    """
    
    def __init__(self, *args, **kwargs):
        """
        @brief 
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
    
    ## \fn postMsg(msgType, text : str = None)
    # @param msgType Message type
    # @param text Message text
    def postMsg(self, msgType = QtDebugMsg, text : str = None) -> None:
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
