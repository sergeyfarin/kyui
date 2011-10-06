# UTF-8
# basicfontwidget.pyw

from PyQt4.QtCore import pyqtSlot, pyqtSignal, pyqtProperty, QSize
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QFontComboBox, QComboBox, QPushButton
from PyQt4.QtGui import QHBoxLayout, QSizePolicy
from PyQt4.QtGui import QFont, QFontDatabase, QIntValidator



class KyBasicFontWidget(QWidget):
    DefaultSizes = ['6', '7', '8', '9', '10', '11', '12', '14', '16', '18', 
                '20', '22', '24', '26', '28', '30', '32','36', '48', '72']
    #==================================================#
    # Signals                                          #
    #==================================================#
    currentFontChanged = pyqtSignal(QFont)
    
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
        name = self.objectName()
        fontBox = QFontComboBox(self)
        fontBox.setObjectName(name + 'fontBox')
        fontBox.setFont(font)
        fontBox.setWritingSystem(QFontDatabase.Latin)
        fontBox.setFontFilters(QFontComboBox.AllFonts)
        fontBox.setCurrentFont(self.font())
        
        sizeBox = QComboBox(self)
        sizeBox.setObjectName(name + 'sizeBox')
        sizeBox.setSizePolicy(preferredSizePolicy)
        sizeBox.setInsertPolicy(QComboBox.NoInsert)
        sizeBox.setEditable(True)
        sizeBox.setValidator(QIntValidator(6, 72, sizeBox))
        sizeBox.addItems(KyBasicFontWidget.DefaultSizes)
        sizeBox.lineEdit().setText(str(font.pointSize()))
        
        boldButton = QPushButton(self)
        boldButton.setObjectName(name + 'boldButton')
        boldButton.setMaximumSize(QSize(26, 26))
        boldButton.setFont(QFont('Tahoma', 11, 75, False))
        boldButton.setCheckable(True)
        boldButton.setChecked(font.bold())        
        
        italicButton = QPushButton(self)
        italicButton.setObjectName(name + 'italicButton')
        italicButton.setMaximumSize(QSize(26, 26))
        italicButton.setFont(QFont('Tahoma', 11, 50, True))
        italicButton.setCheckable(True)
        italicButton.setChecked(font.italic())
        
        underlineButton = QPushButton(self)
        underlineButton.setObjectName(name + 'underlineButton')
        underlineButton.setMaximumSize(QSize(26, 26))
        buttonFont = QFont('Tahoma', 11)
        buttonFont.setUnderline(True)
        underlineButton.setFont(buttonFont)
        underlineButton.setCheckable(True)
        underlineButton.setChecked(font.underline())
        
        self.__fontBox = fontBox
        self.__sizeBox = sizeBox
        self.__boldButton = boldButton
        self.__italicButton = italicButton
        self.__underlineButton = underlineButton
        self.__currentFont = QFont(font)
        
    # Broken off inherited classes that use different layouts (e.g. QGridLayout)
    def _setupLayout(self):
        layout = QHBoxLayout(self)
        layout.setObjectName('layout')
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.__fontBox)
        layout.addSpacing(6)
        layout.addWidget(self.__sizeBox)
        layout.addSpacing(6)
        layout.addWidget(self.__boldButton)
        layout.addWidget(self.__italicButton)
        layout.addWidget(self.__underlineButton)
        
        self.boldButton.hide()
        self.italicButton.hide()
        self.underlineButton.hide()
        
        self.__layout = layout
    
    # Broken off for the sake of inherited classes that have additional
    # widgets to connect to re-impliment and use a super() call
    def _connectSignals(self):
        self.fontBox.currentFontChanged.connect(self._onFontFamilyChanged)
        self.sizeBox.editTextChanged.connect(self._onSizeValueChanged)
        self.sizeBox.currentIndexChanged[str].connect(self._onSizeValueChanged)
        self.boldButton.toggled.connect(self._onBoldToggled)
        self.italicButton.toggled.connect(self._onItalicToggled)
        self.underlineButton.toggled.connect(self._onUnderlineToggled)

    #==================================================#
    # Public Methods                                   #
    #==================================================#
    def retranslateUi(self) -> None:
        self.sizeBox.setToolTip(self.trUtf8('Point Size'))
        self.boldButton.setToolTip(self.trUtf8('Bold'))
        self.boldButton.setText(self.trUtf8('B'))
        self.italicButton.setToolTip(self.trUtf8('Italic'))
        self.italicButton.setText(self.trUtf8('I'))
        self.underlineButton.setToolTip(self.trUtf8('Underline'))
        self.underlineButton.setText(self.trUtf8('U'))
    
    #==================================================#
    # Getters                                          #
    #==================================================#
    def getCurrentFont(self) -> QFont: 
        return self.__currentFont
    def getFontFilters(self) -> QFontComboBox.FontFilters:
        return self.fontBox.fontFilters()
    def getMaximumFontSize(self) -> int:
        return self.sizeBox.maximum()
    def getMinimumFontSize(self) -> int:
        return self.sizeBox.minimum()
    def getWritingSystem(self) -> QFontDatabase.WritingSystem:
        return self.fontBox.writingSystem()
    
    def isBoldButtonVisible(self) -> bool:
        return self.boldButton.isVisible()
    def isItalicButtonVisible(self) -> bool:
        return self.italicButton.isVisible()
    def isUnderlineButtonVisible(self) -> bool:
        return self.underlineButton.isVisible()
        
    @property
    def boldButton(self) -> QPushButton: 
        return self.__boldButton
    @property
    def fontBox(self) -> QFontComboBox:
        return self.__fontBox
    @property
    def italicButton(self) -> QPushButton: 
        return self.__italicButton
    @property
    def layout(self) -> QHBoxLayout:
        return self.__layout
    @property
    def sizeBox(self) -> QComboBox:
        return self.__sizeBox
    @property
    def underlineButton(self) -> QPushButton:
        return self.__underlineButton
    
    #==================================================#
    # Setters                                          #
    #==================================================#
    @pyqtSlot(QFont)
    def setCurrentFont(self, font):
        if not isinstance(font, QFont):
            return
        self.blockSignals(True)
        self.fontBox.setCurrentFont(font)
        self.sizeBox.setProperty('value', font.pointSize())
        self.boldButton.setChecked(font.bold())
        self.italicButton.setChecked(font.italic())
        self.__currentFont = QFont(font)
        self.blockSignals(False)
        self.currentFontChanged.emit(self.currentFont)
    
    def setFontFilters(self, filters : QFontComboBox.FontFilters):
        self.blockSignals(True)
        family = self.fontBox.currentFont().family()
        self.fontBox.setFontFilters(QFontComboBox.FontFilters(filters))
        self.blockSignals(False)
        if family != self.currentFont.family():
            self.currentFont.setFamily(self.fontBox.currentFont().family())
            self.currentFontChanged.emit(self.currentFont)
    
    @pyqtSlot(int)
    def setMaximumFontSize(self, size : int):
        self.blockSignals(True)
        self.sizeBox.validator().setTop(size)
        self.blockSignals(False)
        if int(self.sizeBox.currentText()) != self.currentFont.pointSize():
            self.currentFont.setPointSize(int(self.sizeBox.currentText()))
            self.currentFontChanged.emit(self.currentFont)
    
    @pyqtSlot(int)
    def setMinimumFontSize(self, size : int):
        self.blockSignals(True)
        self.sizeBox.validator().setBottom(size)
        self.blockSignals(False)
        if int(self.sizeBox.currentText()) != self.currentFont.pointSize():
            self.currentFont.setPointSize(int(self.sizeBox.currentText()))
            self.currentFontChanged.emit(self.currentFont)
            
    def setFontSizeItems(self, values : list):
        self.blockSignals(True)
        oldsize = int(self.sizeBox.currentText())
        values.sort()
        self.sizeBox.validator().setBottom(int(values[0]))
        self.sizeBox.validator().setTop(int(values[-1]))
        self.sizeBox.clear()
        for value in iter(values):
            self.sizeBox.addItem(str(value))
        self.blockSignals(False)
        if oldsize != self.currentFont.pointSize():
            self.currentFontChanged.emit(self.currentFont)

    def setWritingSystem(self, system : QFontDatabase.WritingSystem = QFontDatabase.Any):
        self.blockSignals(True)
        family = self.fontBox.currentFont().family()
        self.fontBox.setWritingSystem(system)
        self.fontBox.update()
        self.blockSignals(False)
        if family != self.currentFont.family():
            self.currentFont.setFamily(self.fontBox.currentFont.family())
            self.currentFontChanged.emit(self.currentFont)
        
    def setBoldButtonVisible(self, visible : bool = True):
        self.boldButton.setVisible(visible)
    def setItalicButtonVisible(self, visible : bool = True):
        self.italicButton.setVisible(visible)
    def setUnderlineButtonVisible(self, visible : bool = True):
        self.underlineButton.setVisible(visible)
        
    def setButtonsFlat(self, flat : bool):
        self.boldButton.setFlat(flat)
        self.italicButton.setFlat(flat)
        self.underlineButton.setFlat(flat)

    def setObjectName(self, name : str):
        super().setObjectName(name)
        self.fontBox.setObjectName(name + '_fontBox')
        self.sizeBox.setObjectName(name + '_sizeBox')
        self.boldButton.setObjectName(name + '_boldButton')
        self.italicButton.setObjectName(name + '_italicButton')
        self.underlineButton.setObjectName(name + '_underlineButton')
        self.layout.setObjectName(name + '_layout')
    
    #==================================================#
    # Private Methods                                  #
    #==================================================#
    def _onBoldToggled(self, toggle):
        self.currentFont.setBold(toggle)
        self.currentFontChanged.emit(self.currentFont)
    
    def _onItalicToggled(self, toggle):
        self.currentFont.setItalic(toggle)
        self.currentFontChanged.emit(self.currentFont)
    
    def _onUnderlineToggled(self, toggle):
        self.currentFont.setUnderline(toggle)
        self.currentFontChanged.emit(self.currentFont)
        
    def _onSizeValueChanged(self, sizetext : str):
        if not sizetext.isdigit():
            return
        size = int(sizetext)
        self.currentFont.setPointSize(size)
        self.currentFontChanged.emit(self.currentFont)
    
    def _onFontFamilyChanged(self, font):
        family = font.family()
        self.currentFont.setFamily(family)
        self.currentFontChanged.emit(self.currentFont)
        
    currentFont = pyqtProperty(QFont, fget=getCurrentFont, fset=setCurrentFont)
    fontFilters = pyqtProperty(QFontComboBox.FontFilters, 
                               fget=getFontFilters, 
                               fset=setFontFilters)
    maximumFontSize = pyqtProperty(int, 
                                   fget=getMaximumFontSize, 
                                   fset=setMaximumFontSize)
    minimumFontSize = pyqtProperty(int, 
                                   fget=getMinimumFontSize, 
                                   fset=setMinimumFontSize)
    writingSystem = pyqtProperty(QFontDatabase.WritingSystem, 
                                 fget=getWritingSystem, 
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
