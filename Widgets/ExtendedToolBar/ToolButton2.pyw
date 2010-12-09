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
        
#    def sizeHint(self) -> QSize:
#        w, h = 0, 0
#        opt = QStyleOptionToolButton()
#        self.initStyleOption(opt)
#
#        fm = self.fontMetrics()
#        if opt.toolButtonStyle != Qt.ToolButtonTextOnly and not opt.icon.isNull():
#            w = opt.iconSize.width()
#            h = opt.iconSize.height()
#
#        if opt.toolButtonStyle != Qt.ToolButtonIconOnly and opt.text:
#            textSize = fm.size(Qt.TextShowMnemonic, opt.text);
#            textSize.setWidth(textSize.width() + fm.width(' ')*2);
#            if opt.toolButtonStyle == Qt.ToolButtonTextUnderIcon:
#                h += 4 + textSize.height()
#                if textSize.width() > w:
#                    w = textSize.width()
#            elif opt.toolButtonStyle == Qt.ToolButtonTextBesideIcon:
#                w += 4 + textSize.width();
#                if textSize.height() > h:
#                    h = textSize.height();
#            else: # TextOnly
#                w = textSize.width()
#                h = textSize.height()
#
#        opt.rect.setSize(QSize(w, h)); # PM_MenuButtonIndicator depends on the height
#        if self.popupMode() == QToolButton.MenuButtonPopup:
#            if opt.toolButtonStyle == Qt.ToolButtonTextUnderIcon:
#                h += self.style().pixelMetric(QStyle.PM_MenuButtonIndicator, opt, self);
#            else:
#                w += self.style().pixelMetric(QStyle.PM_MenuButtonIndicator, opt, self);
#
#        sh = self.style().sizeFromContents(QStyle.CT_ToolButton, opt, QSize(w, h), self).expandedTo(QApplication.globalStrut());
#        return sh

    def initStyleOption(self, opt):
        super().initStyleOption(opt)
        opt.orientation = Qt.Vertical

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
        
        act = QAction(QIcon('editPaste.png'), 
                      'Test\nButton', self)
        menu = QMenu()
        menu.addAction('Item1')
        menu.addAction('Item2')
        act.setMenu(menu)
        button = ToolButton(self)
        button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        button.setPopupMode(QToolButton.MenuButtonPopup)
        button.setDefaultAction(act)
        button.setIconSize(QSize(32, 32))
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
