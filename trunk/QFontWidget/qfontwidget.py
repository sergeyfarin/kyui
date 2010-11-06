# QFontWidget

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class QFontWidget(QFrame):
    currentFontChanged = pyqtSignal('QFont')
    fontFamilyChanged = pyqtSignal('QString')
    fontSizeChanged = pyqtSignal('int')
    boldToggled = pyqtSignal('bool')
    italicToggled = pyqtSignal('bool')
    underlineToggled = pyqtSignal('bool')
    
    def __init__(self, font = None, parent = None):
        super().__init__(parent)
        if not font:
            font = self.font()
        self._setupWidgets(font)
        self._setupLayout()
        self.retranslateUi()
        self._connectSignals()

    def _setupWidgets(self, font):
        fontLabel = QLabel(self)
        fontLabel.setObjectName("fontLabel")
        
        comboBox = QFontComboBox(self)
        comboBox.setFont(font)
        comboBox.setWritingSystem(QFontDatabase.Latin)
        comboBox.setFontFilters(QFontComboBox.AllFonts)
        comboBox.setCurrentFont(self.font())
        comboBox.setObjectName("comboBox")
        
        sizeLabel = QLabel(self)
        sizeLabel.setObjectName("sizeLabel")
        
        spinBox = QSpinBox(self)
        spinBox.setObjectName("spinBox")
        spinBox.setSuffix("")
        spinBox.setMinimum(1)
        spinBox.setMaximum(32)
        spinBox.setProperty("value", font.pointSize())
        
        boldButton = QPushButton(self)
        boldButton.setObjectName("boldButton")
        boldButton.setMaximumSize(QSize(24, 24))
        boldButton.setFont(QFont("Tahoma", 11, 75, False))
        boldButton.setCheckable(True)
        boldButton.setChecked(font.bold())        
        
        italicButton = QPushButton(self)
        italicButton.setObjectName("italicButton")
        italicButton.setMaximumSize(QSize(24, 24))
        italicButton.setFont(QFont("Tahoma", 11, 50, True))
        italicButton.setCheckable(True)
        italicButton.setChecked(font.italic())
        
        underlineButton = QPushButton(self)
        underlineButton.setObjectName("underLineButton")
        underlineButton.setMaximumSize(QSize(24, 24))
        buttonFont = QFont("Tahoma", 11)
        buttonFont.setUnderline(True)
        underlineButton.setFont(buttonFont)
        underlineButton.setCheckable(True)
        underlineButton.setChecked(font.underline())
        
        fontLabel.setBuddy(comboBox)
        sizeLabel.setBuddy(spinBox) 
        
        self.__fontLabel = fontLabel
        self.__fontComboBox = comboBox
        self.__sizeLabel = sizeLabel
        self.__sizeSpinBox = spinBox
        self.__boldButton = boldButton
        self.__italicButton = italicButton
        self.__underlineButton = underlineButton
        self.__currentFont = QFont(font)
        
    # Broken off as a separate function for the sake of inherited classes that
    # use grid layouts
    def _setupLayout(self):
        layout = QHBoxLayout(self)
        layout.setObjectName("layout")
        
        layout.addWidget(self.__fontLabel)
        layout.addWidget(self.__fontComboBox)
        layout.addWidget(self.__sizeLabel)
        layout.addWidget(self.__sizeSpinBox)
        layout.addWidget(self.__boldButton)
        layout.addWidget(self.__italicButton)
        layout.addWidget(self.__underlineButton)
        
        self.__boldButton.hide()
        self.__italicButton.hide()
        self.__underlineButton.hide()
        
        self.__layout = layout
    
    # Broken off for the sake of inherited classes that have additional
    # widgets to connect to re-impliment and use a super() call
    def _connectSignals(self):
        self.__fontComboBox.currentFontChanged.connect(self._onComboBoxValueChanged)
        self.__sizeSpinBox.valueChanged.connect(self._onSpinBoxValueChanged)
        self.__boldButton.toggled.connect(self._onBoldToggled)
        self.__italicButton.toggled.connect(self._onItalicToggled)
        self.__underlineButton.toggled.connect(self._onUnderlineToggled)

    def retranslateUi(self):
        self.__fontLabel.setText(self.trUtf8("Font"))
        self.__sizeLabel.setText(self.trUtf8("Size"))
        self.__boldButton.setToolTip(self.trUtf8("Bold"))
        self.__boldButton.setText(self.trUtf8("B"))
        self.__italicButton.setToolTip(self.trUtf8("Italic"))
        self.__italicButton.setText(self.trUtf8("I"))
        self.__underlineButton.setToolTip(self.trUtf8("Underline"))
        self.__underlineButton.setText(self.trUtf8("U"))
        
    def boldButton(self): return self.__boldButton
    def comboBox(self): return self.__fontComboBox
    def comboBoxLabel(self): return self.__fontLabel
    def currentFont(self): return self.__currentFont
    def italicButton(self): return self.__italicButton
    def layout(self): return self.__layout
    def spinBox(self): return self.__sizeSpinBox
    def spinBoxLabel(self): return self.__sizeLabel
    def underlineButton(self): return self.__underlineButton
    
    def setCurrentFont(self, font):
        if not isinstance(font, QFont):
            return
        self.blockSignals(True)
        self.__fontComboBox.setCurrentFont(font)
        self.__sizeSpinBox.setProperty("value", font.pointSize())
        self.__boldButton.setChecked(font.bold())
        self.__italicButton.setChecked(font.italic())
        self.__currentFont = QFont(font)
        self.blockSignals(False)
        self.currentFontChanged.emit(self.__currentFont)
        
    def showBoldButton(self, show = True): self.__boldButton.setVisible(show)
    def showItalicButton(self, show = True): self.__italicButton.setVisible(show)
    def showUnderlineButton(self, show = True): self.__underlineButton.setVisible(show)
    
    def _onBoldToggled(self, toggle):
        self.__currentFont.setBold(toggle)
        self.boldToggled.emit(toggle)
        self.currentFontChanged.emit(self.__currentFont)
    
    def _onItalicToggled(self, toggle):
        self.__currentFont.setItalic(toggle)
        self.italicToggled.emit(toggle)
        self.currentFontChanged.emit(self.__currentFont)
    
    def _onUnderlineToggled(self, toggle):
        self.__currentFont.setUnderline(toggle)
        self.underlineToggled.emit(toggle)
        self.currentFontChanged.emit(self.__currentFont)
        
    def _onSpinBoxValueChanged(self, size):
        self.__currentFont.setPointSize(size)
        self.fontSizeChanged.emit(size)
        self.currentFontChanged.emit(self.__currentFont)
    
    def _onComboBoxValueChanged(self, font):
        family = font.family()
        self.__currentFont.setFamily(family)
        self.fontFamilyChanged.emit(family)
        self.currentFontChanged.emit(self.__currentFont)
        
class GenericDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setObjectName('dialog')
        self.setWindowTitle('QSimpleFontWidget Test')
        #self.resize(371, 151)
        self.setFont(QFont('Segoe UI', 9))
        
        self.__setupUi()
        
        self.buttonBox.accepted.connect(self.accept)
        
    def __setupUi(self):
        self.__layout = QVBoxLayout(self)
        self.__layout.setObjectName('layout')
        
        self.widget = QFontWidget(self.font(), self)
        self.widget.showBoldButton(True)
        self.widget.showItalicButton(True)
        self.widget.showUnderlineButton(True)

        self.__layout.addWidget(self.widget)
        
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok, 
                                          Qt.Horizontal, self)
        self.__layout.addWidget(self.buttonBox)
        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = GenericDialog()
    dialog.show()
    sys.exit(app.exec_())
