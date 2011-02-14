#UTF-8
#template_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

from Widgets.colorpicker import ColorFrame, ColorPicker, ColorData
from Widgets.colors import WordFontHighlightColors, AcrobatColors, FirefoxColors

class Dialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setObjectName('dialog')
        
        self.setupUi()
        self.connectSignals()
        
    def setupUi(self):
        self.layout = QVBoxLayout(self)
        self.layout.setObjectName('layout')
        
        self.testWidget = ColorPicker(parent=self, 
                                     boxsize=QSize(16, 16), 
                                     colordata=WordFontHighlightColors, 
                                     focuscolor=QColor(Qt.blue), 
                                     framecolor=QColor(Qt.black), 
                                     framewidth=1, 
                                     frameshape=QFrame.Panel, 
                                     spacing=QSize(2, 2))
        self.testWidget.setObjectName('testWidget')
        self.testWidget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
#        self.testWidget.setCheckable(True)
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
        self.sizeBox.addItem('12 x 12', QSize(12, 12))
        self.sizeBox.addItem('16 x 16', QSize(16, 16))
        self.sizeBox.addItem('18 x 18', QSize(18, 18))
        self.sizeBox.addItem('22 x 22', QSize(22, 22))
        self.sizeBox.addItem('24 x 24', QSize(24, 24))
        self.sizeBox.addItem('32 x 32', QSize(32, 32))
        self.sizeBox.setCurrentIndex(1)
        self.settingsLayout.addWidget(self.sizeBox, 0, 1)
        self.sizeLabel.setBuddy(self.sizeBox)
        
        self.shapeLabel = QLabel(self.settingsBox)
        self.shapeLabel.setObjectName('shapeLabel')
        self.settingsLayout.addWidget(self.shapeLabel, 1, 0)
        self.shapeBox = QComboBox(self.settingsBox)
        self.shapeBox.setObjectName('shapeBox')
        self.shapeBox.addItem('No Frame', QFrame.NoFrame)
        self.shapeBox.addItem('Box', QFrame.Box)
        self.shapeBox.addItem('Panel', QFrame.Panel)
        self.shapeBox.addItem('Styled Panel', QFrame.StyledPanel)
        self.shapeBox.addItem('Windows Panel', QFrame.WinPanel)
        self.shapeBox.setCurrentIndex(1)
        self.settingsLayout.addWidget(self.shapeBox, 1, 1)
        self.shapeLabel.setBuddy(self.shapeBox)
        
        self.gridLabel = QLabel(self.settingsBox)
        self.gridLabel.setObjectName('gridLabel')
        self.settingsLayout.addWidget(self.gridLabel, 2, 0)
        self.gridBox = QComboBox(self.settingsBox)
        self.gridBox.setObjectName('gridBox')
        self.gridBox.addItem('Acrobat 8', AcrobatColors)
        self.gridBox.addItem('Word 2007 Highlight', WordFontHighlightColors)
        self.gridBox.addItem('Firefox', FirefoxColors)
        self.gridBox.setCurrentIndex(1)
        self.settingsLayout.addWidget(self.gridBox, 2, 1)
        self.gridLabel.setBuddy(self.gridBox)
        
        self.spacingLabel = QLabel(self.settingsBox)
        self.spacingLabel.setObjectName('spacingLabel')
        self.settingsLayout.addWidget(self.spacingLabel, 3, 0)
        self.spacingHBox = QSpinBox(self.settingsBox)
        self.spacingHBox.setObjectName('spacingHBox')
        self.spacingHBox.setRange(1, 10)
        self.spacingHBox.setValue(3)
        self.settingsLayout.addWidget(self.spacingHBox, 3, 1)
        
        self.spacingLabel.setBuddy(self.spacingHBox)
        self.spacingVBox = QSpinBox(self.settingsBox)
        self.spacingVBox.setObjectName('spacingVBox')
        self.spacingVBox.setRange(1, 10)
        self.spacingVBox.setValue(3)
        self.settingsLayout.addWidget(self.spacingVBox, 4, 1)
        
        self.layout.addWidget(self.settingsBox)
        
        self.closeButton = QPushButton(self)
        self.closeButton.setObjectName('closeButton')
        self.closeButton.setDefault(True)
        self.layout.addWidget(self.closeButton)
        self.layout.setAlignment(self.closeButton, 
                                 Qt.AlignRight | Qt.AlignBottom)
        
        self.retranslateUi()
        
    def connectSignals(self):
        self.closeButton.clicked.connect(self.close)
        self.sizeBox.currentIndexChanged[int].connect(self.onSizeChanged)
        self.shapeBox.currentIndexChanged[int].connect(self.onShapeChanged)
        self.gridBox.currentIndexChanged[int].connect(self.onGridSizeChanged)
        self.spacingHBox.valueChanged.connect(self.onSpacingChanged)
        self.spacingVBox.valueChanged.connect(self.onSpacingChanged)
        
    def retranslateUi(self):
        self.setWindowTitle(self.trUtf8('Test Dialog'))
        self.settingsBox.setTitle(self.trUtf8('&Options'))
        self.sizeLabel.setText(self.trUtf8('Button &Size'))
        self.shapeLabel.setText(self.trUtf8('Button S&hape'))
        self.gridLabel.setText(self.trUtf8('Color &Grid'))
        self.spacingLabel.setText(self.trUtf8('S&pacing'))
        self.spacingHBox.setPrefix(self.trUtf8('Width: '))
        self.spacingVBox.setPrefix(self.trUtf8('Height: '))
        self.closeButton.setText(self.trUtf8('&Close'))
        
    def onSpacingChanged(self):
        self.testWidget.setSpacing(QSize(self.spacingHBox.value(), 
                                         self.spacingVBox.value()))
    
    def onSizeChanged(self, index : int):
        self.testWidget.setBoxSize(self.sizeBox.itemData(index, Qt.UserRole))
    
    def onGridSizeChanged(self, index : int):
        colordata = self.gridBox.itemData(index, Qt.UserRole)
        self.testWidget.setColors(colordata)
        
    def onShapeChanged(self, index : int):
        self.testWidget.setFrameShape(self.shapeBox.itemData(index, Qt.UserRole))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
