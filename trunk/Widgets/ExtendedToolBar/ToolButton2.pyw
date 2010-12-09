from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Style import KyStyle

class ToolButton(QToolButton):
    def __init__(self, parent = None):
        super().__init__(parent)
        

    def paintEvent(self, ev : QPaintEvent) -> None:
        p = QStylePainter(self)
        opt = QStyleOptionToolButton()
        self.initStyleOption(opt)
        p.drawComplexControl(QStyle.CC_ToolButton, opt)

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

class GenericDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setObjectName('dialog')
        self.setWindowTitle('Test')
        
        self.__setupUi()
        
    def __setupUi(self):
        self.__layout = QVBoxLayout(self)
        self.__layout.setObjectName('layout')
        
        button = QToolButton(self)
        button.setText('Test\nButton')
        button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        button.setPopupMode(QToolButton.MenuButtonPopup)
        button.setFixedSize(44, 66)
        
        menu = QMenu('Testing', button)
        menu.addAction('Item1')
        menu.addAction('Item2')
        
        button.setMenu(menu)
        
        self.__layout.addWidget(button)
        
        dbgBox = DebugBox(self)
        self.__layout.addWidget(dbgBox)
        qInstallMsgHandler(dbgBox.postMsg)
        
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok, 
                                          Qt.Horizontal, self)
        self.__layout.addWidget(self.buttonBox)
        self.buttonBox.accepted.connect(self.accept)
        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    app.setStyle(KyStyle())
    dialog = GenericDialog()
    dialog.show()
    sys.exit(app.exec_())
