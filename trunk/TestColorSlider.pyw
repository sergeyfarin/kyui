from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Style.StyleFactory import KyStyleFactory
from Widgets.ExtendedToolBar.ToolGroup2 import ToolGroupBox
from Widgets.Action import KyAction
from Widgets.ColorSelection.ColorSlider import ColorWidget
from Widgets.ColorSelection.ColorFrame import ColorFrame

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
        font = QFont('Segoe Ui', 8)
        self.setFont(font)
        self.__styleName = 'Plastique'
        QApplication.setStyle(KyStyleFactory.create(self.__styleName))
        self.__setupUi()
        
#        self.__setupTestItems()
        
    def __setupUi(self):
        self.__layout = QGridLayout(self)
        
        self.colorWidget = ColorWidget(spec=QColor.Rgb, 
                                       color=QColor(Qt.black), 
                                       orientation=Qt.Horizontal, 
                                       parent=self)
        self.colorWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.colorWidget.setMinimumSize(300, 150)
        self.__layout.addWidget(self.colorWidget, 0, 0, 1, 0)
        
        self.dbgBox = DebugBox(self)
        self.__layout.addWidget(self.dbgBox, 1, 0)
        qInstallMsgHandler(self.dbgBox.postMsg)
        
        sideLayout = QVBoxLayout()
        sideLayout.setSpacing(6)
        
        self.styleLabel = QLabel('Style', self)
        sideLayout.addWidget(self.styleLabel)
        
        self.styleBox = QComboBox(self)
        self.styleBox.addItems(KyStyleFactory.keys())
        self.styleBox.setCurrentIndex(0)
        self.connect(self.styleBox, SIGNAL('currentIndexChanged(int)'), self.changeStyle)
        sideLayout.addWidget(self.styleBox)
        
        self.specLabel = QLabel('Color Spec', self)
        sideLayout.addWidget(self.specLabel)
        
        self.specBox = QComboBox(self)
        self.specBox.addItem('RGB', QColor.Rgb)
        self.specBox.addItem('HSV', QColor.Hsv)
        self.specBox.addItem('HSL', QColor.Hsl)
        self.specBox.addItem('CMYK', QColor.Cmyk)
        self.connect(self.specBox, SIGNAL('currentIndexChanged(int)'), self.changeSpec)
        sideLayout.addWidget(self.specBox)
        
        self.colorLabel = QLabel('Color', self)
        sideLayout.addWidget(self.colorLabel)
        sideLayout.setAlignment(self.colorLabel, Qt.AlignRight)
        
        self.colorView = ColorFrame(color=QColor(0, 0, 0), 
                                    parent=self, 
                                    shadow=QFrame.Sunken, 
                                    shape=QFrame.StyledPanel)
        self.colorView.setFixedSize(QSize(48, 48))
        sideLayout.addWidget(self.colorView)
        sideLayout.setAlignment(self.colorView, Qt.AlignRight)
        
        sideLayout.addStretch(1)
        
        self.closeButton = QPushButton('Close', self)
        self.closeButton.setFixedSize(75, 23)
        sideLayout.addWidget(self.closeButton)
        sideLayout.setAlignment(self.closeButton, Qt.AlignRight)
        self.closeButton.clicked.connect(self.accept)
        
        self.__layout.addLayout(sideLayout, 1, 1)
        self.__layout.setRowStretch(0, 1)
        self.__layout.setSpacing(6)

    def changeStyle(self, index : int):
        self.__styleName = self.styleBox.itemText(index)
        style = KyStyleFactory.create(self.__styleName)
        QApplication.setStyle(style)
        
    def changeSpec(self, index : int):
        spec = self.specBox.itemData(index)
        self.colorWidget.setColorSpec(spec)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = GenericDialog()
    dialog.show()
    sys.exit(app.exec_())
