# UTF-8
# KySimpleFontWidget

from PyQt4.QtCore import pyqtSlot, pyqtSignal, pyqtProperty, QSize
from PyQt4.QtGui import QFrame, QWidget
from PyQt4.QtGui import QFontComboBox, QComboBox, QPushButton
from PyQt4.QtGui import QHBoxLayout, QSizePolicy
from PyQt4.QtGui import QFont, QFontDatabase, QIntValidator

class KyBasicFontWidget(QFrame):
    DefaultSizes = ['6', '7', '8', '9', '10', '11', '12', '14', '16', '18', 
                    '20', '22', '24', '26', '28', '30', '32','36', '48', '72']
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
        
        sizeBox = QComboBox(self)
        sizeBox.setObjectName("sizeBox")
        sizeBox.setSizePolicy(preferredSizePolicy)
        sizeBox.setInsertPolicy(QComboBox.NoInsert)
        sizeBox.setEditable(True)
        sizeBox.setValidator(QIntValidator(6, 72, sizeBox))
        sizeBox.addItems(KyBasicFontWidget.DefaultSizes)
        sizeBox.lineEdit().setText(str(font.pointSize()))
        
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
        self._fontBox.currentFontChanged.connect(self._onFontFamilyChanged)
        self._sizeBox.editTextChanged.connect(self._onSizeValueChanged)
        self._sizeBox.currentIndexChanged[str].connect(self._onSizeValueChanged)
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
    def fontFilters(self) -> QFontComboBox.FontFilters:
        return self._fontBox.fontFilters()
    def maximumFontSize(self) -> int:
        return self._sizeBox.maximum()
    def minimumFontSize(self) -> int:
        return self._sizeBox.minimum()
    def writingSystem(self) -> QFontDatabase.WritingSystem:
        return self._fontBox.writingSystem()
    
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
    def sizeBox(self) -> QComboBox:
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
        family = self._fontBox.currentFont().family()
        self._fontBox.setFontFilters(QFontComboBox.FontFilters(filters))
        self.blockSignals(False)
        if family != self._currentFont.family():
            self._currentFont.setFamily(self._fontBox.currentFont().family())
            self.currentFontChanged.emit(self._currentFont)
    
    @pyqtSlot(int)
    def setMaximumFontSize(self, size : int) -> None:
        self.blockSignals(True)
        self._sizeBox.validator().setTop(size)
        self.blockSignals(False)
        if int(self._sizeBox.currentText()) != self._currentFont.pointSize():
            self._currentFont.setPointSize(int(self._sizeBox.currentText()))
            self.currentFontChanged.emit(self._currentFont)
    
    @pyqtSlot(int)
    def setMinimumFontSize(self, size : int) -> None:
        self.blockSignals(True)
        self._sizeBox.validator().setBottom(size)
        self.blockSignals(False)
        if int(self._sizeBox.currentText()) != self._currentFont.pointSize():
            self._currentFont.setPointSize(int(self._sizeBox.currentText()))
            self.currentFontChanged.emit(self._currentFont)
            
    def setFontSizeItems(self, values : list) -> None:
        self.blockSignals(True)
        oldsize = int(self._sizeBox.currentText())
        values.sort()
        self._sizeBox.validator().setBottom(int(values[0]))
        self._sizeBox.validator().setTop(int(values[-1]))
        self._sizeBox.clear()
        for value in iter(values):
            self._sizeBox.addItem(str(value))
        self.blockSignals(False)
        if oldsize != self._currentFont.pointSize():
            self.currentFontChanged.emit(self._currentFont)

    def setWritingSystem(self, system : QFontDatabase.WritingSystem = QFontDatabase.Any) -> None:
        self.blockSignals(True)
        family = self._fontBox.currentFont().family()
        self._fontBox.setWritingSystem(system)
        self._fontBox.update()
        self.blockSignals(False)
        if family != self._currentFont.family():
            self._currentFont.setFamily(self._fontBox.currentFont.family())
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
        
    def _onSizeValueChanged(self, sizetext : str):
        if not sizetext.isdigit():
            return
        size = int(sizetext)
        self._currentFont.setPointSize(size)
        self.fontSizeChanged.emit(size)
        self.currentFontChanged.emit(self._currentFont)
    
    def _onFontFamilyChanged(self, font):
        family = font.family()
        self._currentFont.setFamily(family)
        self.fontFamilyChanged.emit(family)
        self.currentFontChanged.emit(self._currentFont)
        
    currentFont = pyqtProperty(QFont, fget=currentFont, fset=setCurrentFont)
    fontFilters = pyqtProperty(QFontComboBox.FontFilters, 
                               fget=fontFilters, 
                               fset=setFontFilters)
    maximumFontSize = pyqtProperty(int, 
                                   fget=maximumFontSize, 
                                   fset=setMaximumFontSize)
    minimumFontSize = pyqtProperty(int, 
                                   fget=minimumFontSize, 
                                   fset=setMinimumFontSize)
    writingSystem = pyqtProperty(QFontDatabase.WritingSystem, 
                                 fget=writingSystem, 
                                 fset=setWritingSystem)

    boldButtonVisible = pyqtProperty(bool, 
                                     fget=isBoldButtonVisible, 
                                     fset=setBoldButtonVisible)
    italicButtonVisible = pyqtProperty(bool, 
                                     fget=isItalicButtonVisible, 
                                     fset=setItalicButtonVisible)
    underlineButtonVisible = pyqtProperty(bool, 
                                     fget=isUnderlineButtonVisible, 
                                     fset=setUnderlineButtonVisible)
