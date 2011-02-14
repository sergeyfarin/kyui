if __name__ == '__main__':
    
    from PyQt4.QtCore import Qt
    from PyQt4.QtGui import QDialog, QGroupBox, QLabel, QFrame
    from PyQt4.QtGui import QComboBox, QPushButton, QCheckBox, QFontComboBox
    from PyQt4.QtGui import QApplication
    from PyQt4.QtGui import QVBoxLayout, QGridLayout, QSizePolicy
    from PyQt4.QtGui import QFont, QFontDatabase
    
    from Widgets.basicfontwidget import KyBasicFontWidget
    from Widgets.fontpreviewwidget import KyFontPreviewWidget

    class Dialog(QDialog):
        def __init__(self, parent = None):
            super().__init__(parent)
            self.setObjectName('dialog')
            self.setWindowTitle('QSimpleFontWidget Test')
            
            self.setupUi()
            self.connectSignals()
            
        def setupUi(self):
            self._layout = QVBoxLayout(self)
            self._layout.setObjectName('layout')
            
            self.testWidget = KyBasicFontWidget(self.font(), self)
            self.testWidget.setObjectName('testWidget')
            self.testWidget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            self.testWidget.setBoldButtonVisible(True)
            self.testWidget.setItalicButtonVisible(True)
            self.testWidget.setUnderlineButtonVisible(True)
            self._layout.addWidget(self.testWidget)
            
            self.previewWidget = KyFontPreviewWidget('Sample 123', 
                                                    self.font(), 
                                                    self)
            self.previewWidget.setFrameShape(QFrame.Panel)
            self._layout.addWidget(self.previewWidget)
            
            self.settingBox = QGroupBox(self)
            self.settingBox.setObjectName('settingBox')
            self.settingBoxLayout = QGridLayout(self.settingBox)
            
            self.writingSysLabel = QLabel(self.settingBox)
            self.writingSysLabel.setObjectName('writingSysLabel')
            self.settingBoxLayout.addWidget(self.writingSysLabel, 0, 0)
            
            self.writingSysBox = QComboBox(self.settingBox)
            self.writingSysBox.setObjectName('writingSysBox')
            self.writingSysBox.addItem('Any', QFontDatabase.Any)
            self.writingSysBox.addItem('Latin', QFontDatabase.Latin)
            self.writingSysBox.addItem('Greek', QFontDatabase.Greek)
            self.writingSysBox.addItem('Cyrillic', QFontDatabase.Cyrillic)
            self.writingSysBox.addItem('Hebrew', QFontDatabase.Hebrew)
            self.writingSysBox.addItem('Arabic', QFontDatabase.Arabic)
            self.writingSysBox.addItem('Japanese', QFontDatabase.Japanese)
            self.writingSysBox.addItem('Symbol', QFontDatabase.Symbol)
            self.settingBoxLayout.addWidget(self.writingSysBox, 0, 1)
            self.writingSysLabel.setBuddy(self.writingSysBox)
            
            self.filterLabel = QLabel(self.settingBox)
            self.filterLabel.setObjectName('filterLabel')
            self.settingBoxLayout.addWidget(self.filterLabel, 1, 0)
            
            self.filterBox = QComboBox(self.settingBox)
            self.filterBox.setObjectName('filterBox')
            self.filterBox.addItem('All Fonts', QFontComboBox.AllFonts)
            self.filterBox.addItem('Scalable', QFontComboBox.ScalableFonts)
            self.filterBox.addItem('Non-Scalable', QFontComboBox.NonScalableFonts)
            self.filterBox.addItem('Monospaced', QFontComboBox.MonospacedFonts)
            self.filterBox.addItem('Proportional', QFontComboBox.ProportionalFonts)
            self.settingBoxLayout.addWidget(self.filterBox, 1, 1)
            self.filterLabel.setBuddy(self.filterBox)
            
            self.sizeLabel = QLabel(self.settingBox)
            self.sizeLabel.setObjectName('sizeLabel')
            self.settingBoxLayout.addWidget(self.sizeLabel, 2, 0)
            self.sizeBox = QComboBox(self.settingBox)
            self.sizeBox.setObjectName('sizeBox')
            self.sizeBox.addItem('Default Sizes', KyBasicFontWidget.DefaultSizes)
            self.sizeBox.addItem('Range(5, 21)', list(range(5, 21)))
            self.sizeBox.addItem('Range(12, 34, 2)', list(range(12, 34, 2)))
            self.settingBoxLayout.addWidget(self.sizeBox, 2, 1)
            self.sizeLabel.setBuddy(self.sizeBox)
            
            self.boldBox = QCheckBox(self.settingBox)
            self.boldBox.setObjectName('boldBox')
            self.boldBox.setChecked(True)
            self.settingBoxLayout.addWidget(self.boldBox, 0, 2)
            
            self.italicBox = QCheckBox(self.settingBox)
            self.italicBox.setObjectName('italicBox')
            self.italicBox.setChecked(True)
            self.settingBoxLayout.addWidget(self.italicBox, 1, 2)
            
            self.underlineBox = QCheckBox(self.settingBox)
            self.underlineBox.setObjectName('underlineBox')
            self.underlineBox.setChecked(True)
            self.settingBoxLayout.addWidget(self.underlineBox, 2, 2)
            self._layout.addWidget(self.settingBox)
            
            self.closeButton = QPushButton(self)
            self.closeButton.setObjectName('closeButton')
            self.closeButton.setDefault(True)
            self._layout.addWidget(self.closeButton)
            self._layout.setAlignment(self.closeButton, 
                                      Qt.AlignRight | Qt.AlignBottom)
            
            self.retranslateUi()
            
        def retranslateUi(self):
            tr = self.trUtf8
            self.setWindowTitle(tr('SimpleFontWidget Test'))
            self.settingBox.setTitle(tr('&Options'))
            self.writingSysLabel.setText(tr('&Writing System'))
            self.filterLabel.setText(tr('Font &Filter'))
            self.sizeLabel.setText(tr('&Size List'))
            self.boldBox.setText(tr('Show &Bold Button'))
            self.italicBox.setText(tr('Show &Italic Button'))
            self.underlineBox.setText(tr('Show &Underline Button'))
            
            self.closeButton.setText('&Close')
        
        def connectSignals(self):
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
            self.testWidget.setFontFilters(data)
            
        def onFontSizesChanged(self, index : int):
            data = self.sizeBox.itemData(index, Qt.UserRole)
            self.testWidget.setFontSizeItems(data)
            
        def onBoldToggled(self, checked : bool):
            self.testWidget.setBoldButtonVisible(checked)
            
        def onItalicToggled(self, checked : bool):
            self.testWidget.setItalicButtonVisible(checked)
            
        def onUnderlineToggled(self, checked : bool):
            self.testWidget.setUnderlineButtonVisible(checked)
            
    import sys
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec_())
