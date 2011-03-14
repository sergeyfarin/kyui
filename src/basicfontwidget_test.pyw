#UTF-8
#basicfontwidget_test.pyw

from PyQt4.QtCore import Qt
from PyQt4.QtGui import *

from Widgets.basicfontwidget import KyBasicFontWidget
from Widgets.fontpreviewwidget import KyFontPreviewWidget

from template_test import TemplateDialog

class Dialog(TemplateDialog):
    def __init__(self, parent = None):
        super(QDialog, self).__init__(parent)
        self.setObjectName('dialog')
        
        self.setupUi()
        self.connectSignals()
        
    def setupUi(self):
        super().setupUi()
        self.testWidget = KyBasicFontWidget(self.font(), self)
        self.testWidget.setObjectName('testWidget')
        self.testWidget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.testWidget.setBoldButtonVisible(True)
        self.testWidget.setItalicButtonVisible(True)
        self.testWidget.setUnderlineButtonVisible(True)
        self.layout.insertWidget(0, self.testWidget)
        
        self.previewWidget = KyFontPreviewWidget('Sample 123', 
                                                self.font(), 
                                                self)
        self.previewWidget.setFrameShape(QFrame.Panel)
        self.layout.insertWidget(1, self.previewWidget)
        
        self.writingSysLabel = QLabel(self.settingsBox)
        self.writingSysLabel.setObjectName('writingSysLabel')
        self.writingSysBox = QComboBox(self.settingsBox)
        self.writingSysBox.setObjectName('writingSysBox')
        self.writingSysBox.addItem('Any', QFontDatabase.Any)
        self.writingSysBox.addItem('Latin', QFontDatabase.Latin)
        self.writingSysBox.addItem('Greek', QFontDatabase.Greek)
        self.writingSysBox.addItem('Cyrillic', QFontDatabase.Cyrillic)
        self.writingSysBox.addItem('Hebrew', QFontDatabase.Hebrew)
        self.writingSysBox.addItem('Arabic', QFontDatabase.Arabic)
        self.writingSysBox.addItem('Japanese', QFontDatabase.Japanese)
        self.writingSysBox.addItem('Symbol', QFontDatabase.Symbol)
        self.settingsLayout.addRow(self.writingSysLabel, self.writingSysBox)
        self.writingSysLabel.setBuddy(self.writingSysBox)
        
        self.filterLabel = QLabel(self.settingsBox)
        self.filterLabel.setObjectName('filterLabel')
        
        self.filterBox = QComboBox(self.settingsBox)
        self.filterBox.setObjectName('filterBox')
        self.filterBox.addItem('All Fonts', QFontComboBox.AllFonts)
        self.filterBox.addItem('Scalable', QFontComboBox.ScalableFonts)
        self.filterBox.addItem('Non-Scalable', QFontComboBox.NonScalableFonts)
        self.filterBox.addItem('Monospaced', QFontComboBox.MonospacedFonts)
        self.filterBox.addItem('Proportional', QFontComboBox.ProportionalFonts)
        self.settingsLayout.addRow(self.filterLabel, self.filterBox)
        self.filterLabel.setBuddy(self.filterBox)
        
        self.sizeLabel = QLabel(self.settingsBox)
        self.sizeLabel.setObjectName('sizeLabel')
        self.sizeBox = QComboBox(self.settingsBox)
        self.sizeBox.setObjectName('sizeBox')
        self.sizeBox.addItem('Default Sizes', KyBasicFontWidget.DefaultSizes)
        self.sizeBox.addItem('Range(5, 21)', list(range(5, 21)))
        self.sizeBox.addItem('Range(12, 34, 2)', list(range(12, 34, 2)))
        self.settingsLayout.addRow(self.sizeLabel, self.sizeBox)
        self.sizeLabel.setBuddy(self.sizeBox)
        
        self.boldBox = QCheckBox(self.settingsBox)
        self.boldBox.setObjectName('boldBox')
        self.boldBox.setChecked(True)
        self.settingsLayout.addWidget(self.boldBox)
        
        self.italicBox = QCheckBox(self.settingsBox)
        self.italicBox.setObjectName('italicBox')
        self.italicBox.setChecked(True)
        self.settingsLayout.addWidget(self.italicBox)
        
        self.underlineBox = QCheckBox(self.settingsBox)
        self.underlineBox.setObjectName('underlineBox')
        self.underlineBox.setChecked(True)
        self.settingsLayout.addWidget(self.underlineBox)
        
        self.retranslateUi()
        
    def retranslateUi(self):
        super().retranslateUi()
        tr = self.trUtf8
        self.settingsBox.setTitle(tr('&Options'))
        self.writingSysLabel.setText(tr('&Writing System'))
        self.filterLabel.setText(tr('Font &Filter'))
        self.sizeLabel.setText(tr('&Size List'))
        self.boldBox.setText(tr('Show &Bold Button'))
        self.italicBox.setText(tr('Show &Italic Button'))
        self.underlineBox.setText(tr('Show &Underline Button'))
    
    def connectSignals(self):
        super().connectSignals()
        self.writingSysBox.currentIndexChanged.connect(self.onWritingSystemChanged)
        self.filterBox.currentIndexChanged.connect(self.onFontFilterChanged)
        self.sizeBox.currentIndexChanged.connect(self.onFontSizesChanged)
        self.boldBox.toggled.connect(self.onBoldToggled)
        self.italicBox.toggled.connect(self.onItalicToggled)
        self.underlineBox.toggled.connect(self.onUnderlineToggled)
        self.closeButton.clicked.connect(self.close)
        
        self.testWidget.currentFontChanged.connect(self.previewWidget.setCurrentFont)
    
    def onWritingSystemChanged(self, index : int):
        data = self.writingSysBox.itemData(index, Qt.UserRole)
        self.testWidget.setWritingSystem = data
        
    def onFontFilterChanged(self, index : int):
        data = self.filterBox.itemData(index, Qt.UserRole)
        self.testWidget.fontFilters = data
        
    def onFontSizesChanged(self, index : int):
        data = self.sizeBox.itemData(index, Qt.UserRole)
        self.testWidget.setFontSizeItems(data)
        
    def onBoldToggled(self, checked : bool):
        self.testWidget.boldButtonVisible = checked
        
    def onItalicToggled(self, checked : bool):
        self.testWidget.italicButtonVisible = checked
        
    def onUnderlineToggled(self, checked : bool):
        self.testWidget.underlineButtonVisible = checked

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec_())
