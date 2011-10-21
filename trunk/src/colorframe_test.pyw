#UTF-8
#colorpicker_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

from Widgets.colorpicker import ColorFrame

from template_test import TemplateDialog

def createColorIcon(color, size) -> QIcon:
    pixmap = QPixmap(size)
    pixmap.fill(color)
    return QIcon(pixmap)

class Dialog(TemplateDialog):
    def __init__(self, parent = None):
        super(QDialog, self).__init__(parent)
        
        self.setupUi()
        self.retranslateUi()
        self.connectSignals()
        
    def setupUi(self):
        super().setupUi()
        self.testWidget = ColorFrame(parent=self, 
                                     color = QColor(Qt.white), 
                                     hoverColor = QColor(Qt.blue), 
                                     frameColor = QColor(Qt.gray), 
                                     shape = QFrame.Panel, 
                                     flat = True, 
                                     margin = 2, 
                                     boxSize = QSize(22, 22))
        self.testWidget.setObjectName('testWidget')
        self.testWidget.setFocusPolicy(Qt.StrongFocus)
        self.layout.insertWidget(0, self.testWidget)
        
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
        self.shapeBox.setCurrentIndex(2)
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
        
        self.hoverColorLabel = QLabel(self.settingsBox)
        self.hoverColorLabel.setObjectName('hoverColorLabel')
        self.hoverColorBox = QComboBox(self.settingsBox)
        self.hoverColorBox.setObjectName('hoverColorBox')
        self.settingsLayout.addRow(self.hoverColorLabel, self.hoverColorBox)
        self.hoverColorLabel.setBuddy(self.hoverColorBox)
        
        self.marginLabel = QLabel(self.settingsBox)
        self.marginLabel.setObjectName('marginLabel')
        self.marginBox = QSpinBox(self.settingsBox)
        self.marginBox.setObjectName('marginBox')
        self.marginBox.setRange(1, 6)
        self.marginBox.setValue(2)
        self.settingsLayout.addRow(self.marginLabel, self.marginBox)
        
        self.marginLabel.setBuddy(self.marginBox)
        
        self.flatBox = QCheckBox(self.settingsBox)
        self.flatBox.setObjectName('flatBox')
        self.flatBox.setChecked(True)
        self.settingsLayout.addWidget(self.flatBox)
        
        for box in (self.frameColorBox, self.hoverColorBox, self.sampleColorBox):
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
            
        self.frameColorBox.setCurrentIndex(3)
        self.hoverColorBox.setCurrentIndex(1)
        self.sampleColorBox.setCurrentIndex(7)
        
        
    def connectSignals(self):
        super().connectSignals()
        self.sizeBox.currentIndexChanged[int].connect(self.sizeChanged)
        self.shapeBox.currentIndexChanged[int].connect(self.shapeChanged)
        self.hoverColorBox.currentIndexChanged[int].connect(self.hoverColorChanged)
        self.frameColorBox.currentIndexChanged[int].connect(self.frameColorChanged)
        self.sampleColorBox.currentIndexChanged[int].connect(self.sampleColorChanged)
        self.marginBox.valueChanged.connect(self.marginChanged)
        self.flatBox.toggled.connect(self.flatToggled)
        
    def retranslateUi(self):
        super().retranslateUi()
        
        self.setWindowTitle(self.trUtf8('ColorFrame Test'))
        self.settingsBox.setTitle(self.trUtf8('&Options'))
        self.sizeLabel.setText(self.trUtf8('Frame Si&ze'))
        self.shapeLabel.setText(self.trUtf8('Frame Sha&pe'))
        self.sampleColorLabel.setText(self.trUtf8('&Sample Color'))
        self.hoverColorLabel.setText(self.trUtf8('&Hover Color'))
        self.frameColorLabel.setText(self.trUtf8('F&rame Color'))
        self.marginLabel.setText(self.trUtf8('&Margin'))
        self.flatBox.setText(self.trUtf8('F&lat Color Frame'))
        
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
        
        for box in (self.frameColorBox, self.hoverColorBox, self.sampleColorBox):
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
        self.testWidget.boxSize = self.sizeBox.itemData(index, Qt.UserRole)
    
    def hoverColorChanged(self, index : int):
        self.testWidget.hoverColor = self.hoverColorBox.itemData(index, Qt.UserRole)
        
    def frameColorChanged(self, index : int):
        self.testWidget.frameColor = self.frameColorBox.itemData(index, Qt.UserRole)
    
    def sampleColorChanged(self, index : int):
        self.testWidget.color = self.sampleColorBox.itemData(index, Qt.UserRole)
        
    def shapeChanged(self, index : int):
        self.testWidget.setFrameShape(self.shapeBox.itemData(index, Qt.UserRole))
        
    def flatToggled(self, flat : bool):
        self.testWidget.flat = flat
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
