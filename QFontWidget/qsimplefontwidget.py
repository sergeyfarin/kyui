# UTF-8
# KySimpleFontWidget

from PyQt4.QtCore import pyqtSlot, pyqtSignal, pyqtProperty, QSize
from PyQt4.QtGui import QFrame, QWidget
from PyQt4.QtGui import QFontComboBox, QSpinBox, QPushButton
from PyQt4.QtGui import QHBoxLayout, QSizePolicy
from PyQt4.QtGui import QFont, QFontDatabase

class KySimpleFontWidget(QFrame):
    #==================================================#
    # Signals                                          #
    #==================================================#
    currentFontChanged = pyqtSignal(QFont)
    fontFamilyChanged = pyqtSignal(str)
    fontSizeChanged = pyqtSignal(int)
    boldToggled = pyqtSignal(bool)
    italicToggled = pyqtSignal(bool)
    underlineToggled = pyqtSignal(bool)
    
    #==================================================#
    # Initialization Methods                           #
    #==================================================#
    def __init__(self, font : QFont = None, parent : QWidget = None):
        super().__init__(parent)
        if not font: font = self.font()
#        self.setContentsMargins(0, 0, 0, 0)
        self._setupWidgets(font)
        self._setupLayout()
        self._connectSignals()
        
        self.retranslateUi()

    def _setupWidgets(self, font):
        preferredSizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        
        fontBox = QFontComboBox(self)
        fontBox.setObjectName("fontBox")
#        fontBox.setSizePolicy(preferredSizePolicy)
        fontBox.setFont(font)
        fontBox.setWritingSystem(QFontDatabase.Latin)
        fontBox.setFontFilters(QFontComboBox.AllFonts)
        fontBox.setCurrentFont(self.font())
        
        sizeBox = QSpinBox(self)
        sizeBox.setObjectName("sizeBox")
        sizeBox.setSizePolicy(preferredSizePolicy)
        sizeBox.setSuffix("")
        sizeBox.setMinimum(1)
        sizeBox.setMaximum(32)
        sizeBox.setProperty("value", font.pointSize())
        
        boldButton = QPushButton(self)
        boldButton.setObjectName("boldButton")
        boldButton.setMaximumSize(QSize(26, 26))
        boldButton.setFont(QFont("Tahoma", 11, 75, False))
        boldButton.setCheckable(True)
        boldButton.setChecked(font.bold())        
        
        italicButton = QPushButton(self)
        italicButton.setObjectName("italicButton")
        italicButton.setMaximumSize(QSize(26, 26))
        italicButton.setFont(QFont("Tahoma", 11, 50, True))
        italicButton.setCheckable(True)
        italicButton.setChecked(font.italic())
        
        underlineButton = QPushButton(self)
        underlineButton.setObjectName("underlineButton")
        underlineButton.setMaximumSize(QSize(26, 26))
        buttonFont = QFont("Tahoma", 11)
        buttonFont.setUnderline(True)
        underlineButton.setFont(buttonFont)
        underlineButton.setCheckable(True)
        underlineButton.setChecked(font.underline())
        
        self._fontBox = fontBox
        self._sizeBox = sizeBox
        self._boldButton = boldButton
        self._italicButton = italicButton
        self._underlineButton = underlineButton
        self._currentFont = QFont(font)
        
    # Broken off inherited classes that use different layouts (e.g. QGridLayout)
    def _setupLayout(self):
        layout = QHBoxLayout(self)
        layout.setObjectName("layout")
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self._fontBox)
        layout.addSpacing(6)
        layout.addWidget(self._sizeBox)
        layout.addSpacing(6)
        layout.addWidget(self._boldButton)
        layout.addWidget(self._italicButton)
        layout.addWidget(self._underlineButton)
        
        self._boldButton.hide()
        self._italicButton.hide()
        self._underlineButton.hide()
        
        self._layout = layout
    
    # Broken off for the sake of inherited classes that have additional
    # widgets to connect to re-impliment and use a super() call
    def _connectSignals(self):
        self._fontBox.currentFontChanged.connect(self._onFontBoxValueChanged)
        self._sizeBox.valueChanged.connect(self._onSizeValueChanged)
        self._boldButton.toggled.connect(self._onBoldToggled)
        self._italicButton.toggled.connect(self._onItalicToggled)
        self._underlineButton.toggled.connect(self._onUnderlineToggled)

    #==================================================#
    # Public Methods                                   #
    #==================================================#
    def retranslateUi(self) -> None:
        self._sizeBox.setToolTip(self.trUtf8('Point Size'))
        self._boldButton.setToolTip(self.trUtf8("Bold"))
        self._boldButton.setText(self.trUtf8("B"))
        self._italicButton.setToolTip(self.trUtf8("Italic"))
        self._italicButton.setText(self.trUtf8("I"))
        self._underlineButton.setToolTip(self.trUtf8("Underline"))
        self._underlineButton.setText(self.trUtf8("U"))

    
    #==================================================#
    # Getters                                          #
    #==================================================#
    def currentFont(self) -> QFont: 
        return self._currentFont
    def writingSystem(self) -> QFontDatabase.WritingSystem:
        return self._fontBox.writingSystem()
    def fontFilters(self) -> QFontComboBox.FontFilters:
        return self._fontBox.fontFilters()
        
    def isBoldButtonVisible(self) -> bool:
        return self._boldButton.isVisible()
    def isItalicButtonVisible(self) -> bool:
        return self._italicButton.isVisible()
    def isUnderlineButtonVisible(self) -> bool:
        return self._underlineButton.isVisible()
        
    def boldButton(self) -> QPushButton: 
        return self._boldButton
    def fontBox(self) -> QFontComboBox:
        return self._fontBox
    def italicButton(self) -> QPushButton: 
        return self._italicButton
    def layout(self) -> QHBoxLayout:
        return self._layout
    def sizeBox(self) -> QSpinBox:
        return self._sizeBox
    def underlineButton(self) -> QPushButton:
        return self._underlineButton
    
    #==================================================#
    # Setters                                          #
    #==================================================#
    @pyqtSlot(QFont)
    def setCurrentFont(self, font) -> None:
        if not isinstance(font, QFont):
            return
        self.blockSignals(True)
        self._fontBox.setCurrentFont(font)
        self._sizeBox.setProperty("value", font.pointSize())
        self._boldButton.setChecked(font.bold())
        self._italicButton.setChecked(font.italic())
        self._currentFont = QFont(font)
        self.blockSignals(False)
        self.currentFontChanged.emit(self._currentFont)
    
    def setFontFilters(self, filters : QFontComboBox.FontFilters):
        self.blockSignals(True)
        self._fontBox.setFontFilters(QFontComboBox.FontFilters(filters))
        family = self._fontBox.currentFont().family()
        self.blockSignals(False)
        if family != self._currentFont.family():
            self._currentFont.setFontFamily(self._fontBox.currentFont.family())
            self.currentFontChanged.emit(self._currentFont)
    
    def setWritingSystem(self, system : QFontDatabase.WritingSystem = QFontDatabase.Any):
        self.blockSignals(True)
        self._fontBox.setWritingSystem(system)
        self._fontBox.update()
        family = self._fontBox.currentFont().family()
        self.blockSignals(False)
        if family != self._currentFont.family():
            self._currentFont.setFontFamily(self._fontBox.currentFont.family())
            self.currentFontChanged.emit(self._currentFont)
        
    def setBoldButtonVisible(self, visible : bool = True) -> None:
        self._boldButton.setVisible(visible)
    def setItalicButtonVisible(self, visible : bool = True) -> None:
        self._italicButton.setVisible(visible)
    def setUnderlineButtonVisible(self, visible : bool = True) -> None:
        self._underlineButton.setVisible(visible)
        
    def setButtonsFlat(self, flat : bool) -> None:
        self._boldButton.setFlat(flat)
        self._italicButton.setFlat(flat)
        self._underlineButton.setFlat(flat)

    def setObjectName(self, name : str) -> None:
        super().setObjectName(name)
        self._fontBox.setObjectName(name + '_fontBox')
        self._sizeBox.setObjectName(name + '_sizeBox')
        self._boldButton.setObjectName(name + '_boldButton')
        self._italicButton.setObjectName(name + '_italicButton')
        self._underlineButton.setObjectName(name + '_underlineButton')
        self._layout.setObjectName(name + '_layout')
    
    #==================================================#
    # Private Methods                                  #
    #==================================================#
    def _onBoldToggled(self, toggle):
        self._currentFont.setBold(toggle)
        self.boldToggled.emit(toggle)
        self.currentFontChanged.emit(self._currentFont)
    
    def _onItalicToggled(self, toggle):
        self._currentFont.setItalic(toggle)
        self.italicToggled.emit(toggle)
        self.currentFontChanged.emit(self._currentFont)
    
    def _onUnderlineToggled(self, toggle):
        self._currentFont.setUnderline(toggle)
        self.underlineToggled.emit(toggle)
        self.currentFontChanged.emit(self._currentFont)
        
    def _onSizeValueChanged(self, size):
        self._currentFont.setPointSize(size)
        self.fontSizeChanged.emit(size)
        self.currentFontChanged.emit(self._currentFont)
    
    def _onFontBoxValueChanged(self, font):
        family = font.family()
        self._currentFont.setFamily(family)
        self.fontFamilyChanged.emit(family)
        self.currentFontChanged.emit(self._currentFont)
        
    currentFont = pyqtProperty(QFont, fget=currentFont, fset=setCurrentFont)
    writingSystem = pyqtProperty(QFontDatabase.WritingSystem, 
                                 fget=writingSystem, 
                                 fset=setWritingSystem)
    fontFilters = pyqtProperty(QFontComboBox.FontFilters, 
                               fget=fontFilters, 
                               fset=setFontFilters)
    boldButtonVisible = pyqtProperty(bool, 
                                     fget=isBoldButtonVisible, 
                                     fset=setBoldButtonVisible)
    italicButtonVisible = pyqtProperty(bool, 
                                     fget=isItalicButtonVisible, 
                                     fset=setItalicButtonVisible)
    underlineButtonVisible = pyqtProperty(bool, 
                                     fget=isUnderlineButtonVisible, 
                                     fset=setUnderlineButtonVisible)
if __name__ == '__main__':
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import QDialog, QGroupBox, QLabel
    from PyQt4.QtGui import QComboBox, QPushButton, QCheckBox
    from PyQt4.QtGui import QApplication
    from PyQt4.QtGui import QVBoxLayout, QGridLayout, QSizePolicy
    from PyQt4.QtGui import QFont

    class Dialog(QDialog):
        def __init__(self, parent = None):
            super().__init__(parent)
            self.setObjectName('dialog')
            self.setWindowTitle('QSimpleFontWidget Test')
            #self.resize(371, 151)
            self.setFont(QFont('Segoe UI', 9))
            
            self.setupUi()
            self.connectSignals()
            
        def setupUi(self):
            self._layout = QVBoxLayout(self)
            self._layout.setObjectName('layout')
            
            self.testWidget = KySimpleFontWidget(self.font(), self)
            self.testWidget.setObjectName('testWidget')
            self.testWidget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
#            self.testWidget.setBoldButtonVisible(True)
#            self.testWidget.setItalicButtonVisible(True)
#            self.testWidget.setUnderlineButtonVisible(True)
            self._layout.addWidget(self.testWidget)
            
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
            
            self.boldBox = QCheckBox(self.settingBox)
            self.boldBox.setObjectName('boldBox')
            self.settingBoxLayout.addWidget(self.boldBox, 0, 2)
            
            self.italicBox = QCheckBox(self.settingBox)
            self.italicBox.setObjectName('italicBox')
            self.settingBoxLayout.addWidget(self.italicBox, 1, 2)
            
            self.underlineBox = QCheckBox(self.settingBox)
            self.underlineBox.setObjectName('underlineBox')
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
            self.filterLabel.setText(tr('&Font Filter'))
            self.boldBox.setText(tr('Show &Bold Button'))
            self.italicBox.setText(tr('Show &Italic Button'))
            self.underlineBox.setText(tr('Show &Underline Button'))
            
            self.closeButton.setText('&Close')
        
        def connectSignals(self):
            self.writingSysBox.currentIndexChanged.connect(self.onWritingSystemChanged)
            self.filterBox.currentIndexChanged.connect(self.onFontFilterChanged)
            self.boldBox.toggled.connect(self.onBoldToggled)
            self.italicBox.toggled.connect(self.onItalicToggled)
            self.underlineBox.toggled.connect(self.onUnderlineToggled)
            self.closeButton.clicked.connect(self.close)
        
        def onWritingSystemChanged(self, index : int):
            data = self.writingSysBox.itemData(index, Qt.UserRole)
            self.testWidget.setWritingSystem = data
            
        def onFontFilterChanged(self, index : int):
            data = self.filterBox.itemData(index, Qt.UserRole)
            self.testWidget.setFontFilters(data)
            
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
