from PyQt4.QtCore import Qt
from PyQt4.QtGui import QGroupBox, QWidget

#from Style import KyStyle

#def DrawGroupBoxFrameV3(frame, p, widget = None):
#    if frame.version == QStyleOptionFrameV3.Version:    
#        shape  = frame.frameShape
#        if frame.state & QStyle.State_Sunken:
#            shadow = QFrame.Sunken
#        elif frame.state & QStyle.State_Raised:
#            shadow = QFrame.Raised
#        else:
#            shadow = QFrame.Plain
#        
#        lw = frame.lineWidth
#        mlw = frame.midLineWidth
#        
#        fgRole = widget.foregroundRole() if widget else QPalette.WindowText
#
#        if shape == QFrame.Box:
#            if (shadow == QFrame.Plain):
#                qDrawPlainRect(p, frame.rect, frame.palette.color(fgRole), lw)
#            else:
#                qDrawShadeRect(p, frame.rect, frame.palette, shadow == QFrame.Sunken, lw, mlw)
#        elif shape == QFrame.StyledPanel:
#            if (shadow == QStyle.State_Sunken) or (shadow == QStyle.State_Raised):
#                qDrawShadePanel(p, frame.rect, frame.palette, 
#                                shadow == QStyle.State_Sunken, 
#                                frame.lineWidth)
#            else:
#                qDrawPlainRect(p, frame.rect, frame.palette.foreground().color(), frame.lineWidth)
#        elif shape == QFrame.Panel:
#            if shadow == QFrame.Plain:
#                qDrawPlainRect(p, frame.rect, frame.palette.color(fgRole), lw)
#            else:
#                qDrawShadePanel(p, frame.rect, frame.palette, shadow == QFrame.Sunken, lw)
#        elif shape == QFrame.WinPanel:
#            if (shadow == QFrame.Plain):
#                qDrawPlainRect(p, frame.rect, frame.palette.color(fgRole), lw)
#            else:
#                qDrawWinPanel(p, frame.rect, frame.palette, shadow == QFrame.Sunken)
#        elif shape == QFrame.HLine or shape == QFrame.VLine:
#            p1, p2 = QPoint(), QPoint()
#            if (shape == QFrame.HLine):
#                p1 = QPoint(frame.rect.x(), frame.rect.height() / 2)
#                p2 = QPoint(frame.rect.x() + frame.rect.width(), p1.y())
#            else:
#                p1 = QPoint(frame.rect.x()+frame.rect.width() / 2, 0)
#                p2 = QPoint(p1.x(), frame.rect.height())
#            if shadow == QFrame.Plain:
#                oldPen = p.pen()
#                p.setPen(QPen(frame.palette.brush(fgRole), lw))
#                p.drawLine(p1, p2)
#                p.setPen(oldPen)
#            else:
#                qDrawShadeLine(p, p1, p2, frame.palette, shadow == QFrame.Sunken, lw, mlw)


class ToolGroupBox(QGroupBox):
    
    def __init__(self, 
                 title : str = None, 
                 parent : QWidget = None, 
#                 action : ExtendedAction = None, 
                 alignment : Qt.Alignment = Qt.AlignHCenter | Qt.AlignTop, 
                 checkable : bool = False, 
                 checked : bool = True):
        if title:
            super().__init__(title, parent)
        else:
            super().__init__(parent)
        self.setAlignment(alignment)
        if checkable: self.setCheckable(checkable)
        if not checked: self.setChecked(checked)

#class DebugBox(QPlainTextEdit):
#    def __init__(self, parent : QWidget = None, text : str = None):
#        super().__init__(parent)
#        if text:
#            self.setPlainText(text)
#        self.setReadOnly(True)
#        self.setFrameShape(QFrame.StyledPanel)
#        self.setFrameShadow(QFrame.Sunken)
#    
#    def postMsg(self, msgType = QtDebugMsg, text : str = None) -> None:
#        if msgType == QtDebugMsg:
#            self.appendPlainText('Debug: ' + bytes.decode(text))
#        elif msgType == QtWarningMsg:
#            self.appendPlainText('Warning: ' + bytes.decode(text))
#        elif msgType == QtCriticalMsg:
#            print('Critical: ' + bytes.decode(text))
#        elif msgType == QtFatalMsg:
#            print('Fatal: ' + bytes.decode(text))
#        else:
#            print('Unknown Error: ' + bytes.decode(text))
        
#class GenericDialog(QDialog):
#    def __init__(self, parent = None):
#        super().__init__(parent)
#        
#        self.setObjectName('dialog')
#        self.setWindowTitle('Test Dialog')
#        self.setFont(QFont('Segoe Ui', 9))
#        
#        self.__setupUi()
#        
#        self.buttonBox.accepted.connect(self.accept)
#        
#    def __setupUi(self):
#        self.layout = QVBoxLayout(self)
#        self.layout.setObjectName('layout')
#        
#        toolGroupBox = ToolGroupBox(title = 'Test&2', 
#                                    parent = self,
#                                    checkable=True, 
#                                    alignment = Qt.AlignHCenter | Qt.AlignBottom)
#        toolGroupBox.setFixedSize(300, 100)
#        toolGroupBox.setFlat(True)
#        self.layout.addWidget(toolGroupBox)
#        
#        grpBox = QGroupBox('&Test2', self)
#        grpBox.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
#        grpBox.setFixedSize(300, 20)
#        grpBox.setCheckable(True)
#        grpBox.setFlat(False)
#        self.layout.addWidget(grpBox)
#        
#        dbgBox = DebugBox(self)
#        self.layout.addWidget(dbgBox)
#        qInstallMsgHandler(dbgBox.postMsg)
#        
#        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok, 
#                                          Qt.Horizontal, self)
#        self.layout.addWidget(self.buttonBox)
#        
#
#if __name__ == '__main__':
#    import sys
#    app = QApplication(sys.argv)
#    app.setStyle(KyStyle())
#    dialog = GenericDialog()
#    dialog.show()
#    sys.exit(app.exec_())
