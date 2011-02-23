#UTF-8
#colorpicker_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

from Widgets.colorpicker import ColorFrame

def createColorIcon(color, size) -> QIcon:
    pixmap = QPixmap(size)
    pixmap.fill(color)
    return QIcon(pixmap)

class Dialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setObjectName('dialog')
        
        self.setupUi()
        self.connectSignals()
        
    def setupUi(self):
        self.layout = QVBoxLayout(self)
        self.layout.setObjectName('layout')
        
        self.testWidget = ColorFrame(parent=self, 
                                     color = QColor(Qt.black), 
                                     focuscolor = QColor(Qt.blue), 
                                     framecolor = QColor(Qt.black), 
                                     frameshape = QFrame.Box, 
                                     framewidth = 1, 
                                     margin = 3, 
                                     size = QSize(22, 22))
        self.testWidget.setObjectName('testWidget')
        self.testWidget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
#        self.testWidget.setCheckable(True)
        self.layout.addWidget(self.testWidget)
        
        self.settingsBox = QGroupBox(self)
        self.settingsBox.setObjectName('settingsBox')
        self.settingsLayout = QFormLayout(self.settingsBox)
        self.settingsLayout.setObjectName('settingsLayout')
        
        self.sizeLabel = QLabel(self.settingsBox)
        self.sizeLabel.setObjectName('sizeLabel')
        
        self.sizeBox = QComboBox(self.settingsBox)
        self.sizeBox.setObjectName('sizeBox')
        self.sizeBox.addItem('12 x 12', QSize(12, 12))
        self.sizeBox.addItem('16 x 16', QSize(16, 16))
        self.sizeBox.addItem('18 x 18', QSize(18, 18))
        self.sizeBox.addItem('22 x 22', QSize(22, 22))
        self.sizeBox.addItem('24 x 24', QSize(24, 24))
        self.sizeBox.addItem('32 x 32', QSize(32, 32))
        self.sizeBox.setCurrentIndex(3)
        
        self.settingsLayout.addRow(self.sizeLabel, self.sizeBox)
        self.sizeLabel.setBuddy(self.sizeBox)
        
        self.shapeLabel = QLabel(self.settingsBox)
        self.shapeLabel.setObjectName('shapeLabel')
        self.shapeBox = QComboBox(self.settingsBox)
        self.shapeBox.setObjectName('shapeBox')
        self.shapeBox.addItem('No Frame', QFrame.NoFrame)
        self.shapeBox.addItem('Box', QFrame.Box)
        self.shapeBox.addItem('Panel', QFrame.Panel)
        self.shapeBox.addItem('Styled Panel', QFrame.StyledPanel)
        self.shapeBox.addItem('Windows Panel', QFrame.WinPanel)
        self.shapeBox.setCurrentIndex(1)
        self.settingsLayout.addRow(self.shapeLabel, self.shapeBox)
        self.shapeLabel.setBuddy(self.shapeBox)
        
        self.sampleColorLabel = QLabel(self.settingsBox)
        self.sampleColorLabel.setObjectName('sampleColorLabel')
        self.sampleColorBox = QComboBox(self.settingsBox)
        self.sampleColorBox.setObjectName('sampleColorBox')
        self.settingsLayout.addRow(self.sampleColorLabel, self.sampleColorBox)
        self.sampleColorLabel.setBuddy(self.sampleColorBox)
        
        self.frameColorLabel = QLabel(self.settingsBox)
        self.frameColorLabel.setObjectName('frameColorLabel')
        self.frameColorBox = QComboBox(self.settingsBox)
        self.frameColorBox.setObjectName('frameColorBox')
        self.settingsLayout.addRow(self.frameColorLabel, self.frameColorBox)
        self.frameColorLabel.setBuddy(self.frameColorBox)
        
        self.focusColorLabel = QLabel(self.settingsBox)
        self.focusColorLabel.setObjectName('focusColorLabel')
        self.focusColorBox = QComboBox(self.settingsBox)
        self.focusColorBox.setObjectName('focusColorBox')
        self.settingsLayout.addRow(self.focusColorLabel, self.focusColorBox)
        self.focusColorLabel.setBuddy(self.focusColorBox)
        
        self.marginLabel = QLabel(self.settingsBox)
        self.marginLabel.setObjectName('marginLabel')
        self.marginBox = QSpinBox(self.settingsBox)
        self.marginBox.setObjectName('marginBox')
        self.marginBox.setRange(-6, 6)
        self.marginBox.setValue(3)
        self.settingsLayout.addRow(self.marginLabel, self.marginBox)
        
        self.marginLabel.setBuddy(self.marginBox)
        
        self.layout.addWidget(self.settingsBox)
        
        self.closeButton = QPushButton(self)
        self.closeButton.setObjectName('closeButton')
        self.closeButton.setDefault(True)
        self.layout.addWidget(self.closeButton)
        self.layout.setAlignment(self.closeButton, 
                                 Qt.AlignRight | Qt.AlignBottom)
        for box in (self.frameColorBox, self.focusColorBox, self.sampleColorBox):
            icon = createColorIcon(QColor(Qt.black), QSize(16, 16))
            box.addItem(icon, 'Black', QColor(Qt.black))
            icon = createColorIcon(QColor(Qt.blue), QSize(16, 16))
            box.addItem(icon, 'Blue', QColor(Qt.blue))
            icon = createColorIcon(QColor(255, 201, 14), QSize(16, 16))
            box.addItem(icon, 'Gold', QColor(255, 201, 14))
            icon = createColorIcon(QColor(Qt.gray), QSize(16, 16))
            box.addItem(icon, 'Gray', QColor(Qt.gray))
            icon = createColorIcon(QColor(Qt.transparent), QSize(16, 16))
            box.addItem(icon, 'None', QColor(Qt.transparent))
            icon = createColorIcon(QColor(255, 127, 39), QSize(16, 16))
            box.addItem(icon, 'Orange', QColor(255, 127, 39))
            icon = createColorIcon(QColor(Qt.red), QSize(16, 16))
            box.addItem(icon, 'Red', QColor(Qt.red))
            icon = createColorIcon(QColor(Qt.white), QSize(16, 16))
            box.addItem(icon, 'White', QColor(Qt.white))
            icon = createColorIcon(QColor(Qt.yellow), QSize(16, 16))
            box.addItem(icon, 'Yellow', QColor(Qt.yellow))
        
        self.retranslateUi()
        
    def connectSignals(self):
        self.closeButton.clicked.connect(self.close)
        self.sizeBox.currentIndexChanged[int].connect(self.sizeChanged)
        self.shapeBox.currentIndexChanged[int].connect(self.shapeChanged)
        self.focusColorBox.currentIndexChanged[int].connect(self.focusColorChanged)
        self.frameColorBox.currentIndexChanged[int].connect(self.frameColorChanged)
        self.sampleColorBox.currentIndexChanged[int].connect(self.sampleColorChanged)
        self.marginBox.valueChanged.connect(self.marginChanged)
        
    def retranslateUi(self):
        self.setWindowTitle(self.trUtf8('Test Dialog'))
        self.settingsBox.setTitle(self.trUtf8('&Options'))
        self.sizeLabel.setText(self.trUtf8('Frame Si&ze'))
        self.shapeLabel.setText(self.trUtf8('Frame S&hape'))
        self.sampleColorLabel.setText(self.trUtf8('&Sample Color'))
        self.focusColorLabel.setText(self.trUtf8('&Focus Color'))
        self.frameColorLabel.setText(self.trUtf8('F&rame Color'))
        self.marginLabel.setText(self.trUtf8('&Margin'))
        self.closeButton.setText(self.trUtf8('&Close'))
        
        self.sizeBox.setItemText(0, self.trUtf8('12 x 12'))
        self.sizeBox.setItemText(1, self.trUtf8('16 x 16'))
        self.sizeBox.setItemText(2, self.trUtf8('18 x 18'))
        self.sizeBox.setItemText(3, self.trUtf8('22 x 22'))
        self.sizeBox.setItemText(4, self.trUtf8('24 x 24'))
        self.sizeBox.setItemText(5, self.trUtf8('32 x 32'))
        
        self.shapeBox.setItemText(0, self.trUtf8('No Frame'))
        self.shapeBox.setItemText(1, self.trUtf8('Box'))
        self.shapeBox.setItemText(2, self.trUtf8('Panel'))
        self.shapeBox.setItemText(3, self.trUtf8('Styled Panel'))
        self.shapeBox.setItemText(4, self.trUtf8('Windows Panel'))
        
        for box in (self.frameColorBox, self.focusColorBox, self.sampleColorBox):
            box.setItemText(0, self.trUtf8('Black'))
            box.setItemText(1, self.trUtf8('Blue'))
            box.setItemText(2, self.trUtf8('Gold'))
            box.setItemText(3, self.trUtf8('Gray'))
            box.setItemText(4, self.trUtf8('None'))
            box.setItemText(5, self.trUtf8('Orange'))
            box.setItemText(6, self.trUtf8('Red'))
            box.setItemText(7, self.trUtf8('White'))
            box.setItemText(8, self.trUtf8('Yellow'))
        
    def marginChanged(self):
        self.testWidget.margin = self.marginBox.value()
    
    def sizeChanged(self, index : int):
        self.testWidget.setFixedSize(self.sizeBox.itemData(index, Qt.UserRole))
    
    def focusColorChanged(self, index : int):
        self.testWidget.focusColor = self.focusColorBox.itemData(index, Qt.UserRole)
        
    def frameColorChanged(self, index : int):
        self.testWidget.frameColor = self.frameColorBox.itemData(index, Qt.UserRole)
    
    def sampleColorChanged(self, index : int):
        self.testWidget.color = self.sampleColorBox.itemData(index, Qt.UserRole)
        
    def shapeChanged(self, index : int):
        self.testWidget.frameShape = self.shapeBox.itemData(index, Qt.UserRole)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
