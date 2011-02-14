#UTF-8
#colorbutton_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

from Widgets.colorbutton import ColorButton
from Widgets.debugbox import DebugBox

class Dialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setObjectName('dialog')
        self.setFont(QFont('Segoe Ui', 9))
        
        self.setupUi()
        self.connectSignals()
        
    def setupUi(self):
        self.layout = QVBoxLayout(self)
        self.layout.setObjectName('layout')
        
        self.testWidget = ColorButton(color=Qt.white, 
                                      text='Test', 
                                      parent=self)
        self.testWidget.setObjectName('testWidget')
        self.testWidget.setIconSize(QSize(16, 16))
#        self.testWidget.setPopupMode(QToolButton.MenuButtonPopup)
        self.layout.addWidget(self.testWidget)
        
        self.settingsBox = QGroupBox(self)
        self.settingsBox.setObjectName('settingsBox')
        self.settingsLayout = QGridLayout(self.settingsBox)
        self.settingsLayout.setObjectName('settingsLayout')
        
        self.sizeLabel = QLabel(self.settingsBox)
        self.sizeLabel.setObjectName('sizeLabel')
        self.settingsLayout.addWidget(self.sizeLabel, 0, 0)
        self.sizeBox = QComboBox(self.settingsBox)
        self.sizeBox.setObjectName('sizeBox')
        self.sizeBox.addItem('16 x 16', QSize(16, 16))
        self.sizeBox.addItem('22 x 22', QSize(22, 22))
        self.sizeBox.addItem('24 x 24', QSize(24, 24))
        self.sizeBox.addItem('32 x 32', QSize(32, 32))
        self.settingsLayout.addWidget(self.sizeBox, 0, 1)
        self.sizeLabel.setBuddy(self.sizeBox)
        
        self.colorLabel = QLabel(self.settingsBox)
        self.colorLabel.setObjectName('colorLabel')
        self.settingsLayout.addWidget(self.colorLabel, 1, 0)
        self.colorBox = QComboBox(self.settingsBox)
        self.colorBox.setObjectName('colorBox')
        self.colorBox.addItem('White', QColor(Qt.white))
        self.colorBox.addItem('Black', QColor(Qt.black))
        self.colorBox.addItem('Red', QColor(Qt.red))
        self.colorBox.addItem('Dark Red', QColor(Qt.darkRed))
        self.colorBox.addItem('Green', QColor(Qt.green))
        self.colorBox.addItem('Dark Green', QColor(Qt.darkGreen))
        self.colorBox.addItem('Blue', QColor(Qt.blue))
        self.colorBox.addItem('Dark Blue', QColor(Qt.darkBlue))
        self.colorBox.addItem('Cyan', QColor(Qt.cyan))
        self.colorBox.addItem('Dark Cyan', QColor(Qt.darkCyan))
        self.colorBox.addItem('Magenta', QColor(Qt.magenta))
        self.colorBox.addItem('Dark Magenta', QColor(Qt.darkMagenta))
        self.colorBox.addItem('Yellow', QColor(Qt.yellow))
        self.colorBox.addItem('Dark Yellow', QColor(Qt.darkYellow))
        self.colorBox.addItem('Gray', QColor(Qt.gray))
        self.colorBox.addItem('Dark Gray', QColor(Qt.darkGray))
        self.colorBox.addItem('Light Gray', QColor(Qt.lightGray))
        self.settingsLayout.addWidget(self.colorBox, 1, 1)
        self.colorLabel.setBuddy(self.colorBox)
        
        self.layout.addWidget(self.settingsBox)
        
        self.styleLabel = QLabel(self.settingsBox)
        self.styleLabel.setObjectName('styleLabel')
        self.settingsLayout.addWidget(self.styleLabel, 2, 0)
        self.styleBox = QComboBox(self.settingsBox)
        self.styleBox.setObjectName('styleBox')
        self.styleBox.addItem('Icon Only', Qt.ToolButtonIconOnly)
        self.styleBox.addItem('Text Beside Icon', Qt.ToolButtonTextBesideIcon)
        self.styleBox.addItem('Text Under Icon', Qt.ToolButtonTextUnderIcon)
        self.styleBox.setCurrentIndex(1)
        self.settingsLayout.addWidget(self.styleBox, 2, 1)
        self.styleLabel.setBuddy(self.styleBox)

        self.closeButton = QPushButton(self)
        self.closeButton.setObjectName('closeButton')
        self.closeButton.setDefault(True)
        self.layout.addWidget(self.closeButton)
        self.layout.setAlignment(self.closeButton, 
                                 Qt.AlignRight | Qt.AlignBottom)
        
        self.retranslateUi()
        
    def connectSignals(self):
        self.sizeBox.currentIndexChanged[int].connect(self.onSizeChanged)
        self.colorBox.currentIndexChanged[int].connect(self.onColorChanged)
        self.styleBox.currentIndexChanged[int].connect(self.onStyleChanged)
        self.testWidget.clicked.connect(self.onColorButtonClicked)
        self.closeButton.clicked.connect(self.close)
        
    def retranslateUi(self):
        self.setWindowTitle(self.trUtf8('Test Dialog'))
        self.settingsBox.setTitle(self.trUtf8('Options'))
        self.sizeLabel.setText(self.trUtf8('&Icon Size'))
        self.colorLabel.setText(self.trUtf8('C&olor'))
        self.styleLabel.setText(self.trUtf8('&Style'))
        self.closeButton.setText(self.trUtf8('&Close'))
        
        self.sizeBox.setItemText(0, self.trUtf8('16 x 16'))
        self.sizeBox.setItemText(1, self.trUtf8('22 x 22'))
        self.sizeBox.setItemText(2, self.trUtf8('24 x 24'))
        self.sizeBox.setItemText(3, self.trUtf8('32 x 32'))
        
        self.colorBox.setItemText(0, self.trUtf8('White'))
        self.colorBox.setItemText(1, self.trUtf8('Black'))
        self.colorBox.setItemText(2, self.trUtf8('Red'))
        self.colorBox.setItemText(3, self.trUtf8('Dark Red'))
        self.colorBox.setItemText(4, self.trUtf8('Green'))
        self.colorBox.setItemText(5, self.trUtf8('Dark Green'))
        self.colorBox.setItemText(6, self.trUtf8('Blue'))
        self.colorBox.setItemText(7, self.trUtf8('Dark Blue'))
        self.colorBox.setItemText(8, self.trUtf8('Cyan'))
        self.colorBox.setItemText(9, self.trUtf8('Dark Cyan'))
        self.colorBox.setItemText(10, self.trUtf8('Magenta'))
        self.colorBox.setItemText(11, self.trUtf8('Dark Magenta'))
        self.colorBox.setItemText(12, self.trUtf8('Yellow'))
        self.colorBox.setItemText(13, self.trUtf8('Dark Yellow'))
        self.colorBox.setItemText(14, self.trUtf8('Gray'))
        self.colorBox.setItemText(15, self.trUtf8('Dark Gray'))
        self.colorBox.setItemText(16, self.trUtf8('Light Gray'))

    def onSizeChanged(self, index : int):
        self.testWidget.setIconSize(self.sizeBox.itemData(index, Qt.UserRole))

    def onColorChanged(self, index : int):
        self.testWidget.setColor(self.colorBox.itemData(index, Qt.UserRole))
        
    def onStyleChanged(self, index : int):
        self.testWidget.setToolButtonStyle(self.styleBox.itemData(index, Qt.UserRole))
    
    def onColorButtonClicked(self):
        color = QColorDialog.getColor(self.testWidget.color, self)
        self.testWidget.setColor(color)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
