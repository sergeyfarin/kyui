#fontgroupbox

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class FontGroupBox(QGroupBox):
    def __init__(self, font = None, fontColor = None, bgColor = None, parent = None):
        super().__init__(parent)
        if not font:
            font = self.font()
        
        self.__setupUi(font, fontColor, bgColor)
        self.retranslateUi()
        
        self.connect(self.fontComboBox, SIGNAL('currentFontChanged(QFont)'), 
                     self.onFontChanged)
        self.connect(self.sizeSpinBox, SIGNAL('valueChanged(int)'),
                     self.onFontSizeChanged)
        self.boldButton.toggled.connect(self.onBoldToggled)
        self.italicButton.toggled.connect(self.onItalicToggled)
        self.fontColorButton.clicked.connect(self.changeFontColor)
        self.bgColorButton.clicked.connect(self.changeBgColor)
    
    def currentFont(self):
        return self.sampleText.font()
        
    def onFontChanged(self, newfont):
        f = self.sampleText.font()
        f.setFamily(newfont.family())
        self.sampleText.setFont(f)
        
    def onFontSizeChanged(self, newsize):
        f = self.sampleText.font()
        f.setPointSize(newsize)
        self.sampleText.setFont(f)
        
    def onBoldToggled(self, bold):
        f = self.sampleText.font()
        f.setBold(bold)
        self.sampleText.setFont(f)

    def onItalicToggled(self, italic):
        f = self.sampleText.font()
        f.setItalic(italic)
        self.sampleText.setFont(f)

    def changeFontColor(self):
        palette = self.sampleText.palette()
        color = palette.color(QPalette.WindowText)
        newcolor = QColorDialog.getColor(color,
                                         None,
                                         self.trUtf8("Select Background Color"))
        palette.setColor(QPalette.Text, newcolor)
        self.sampleText.setPalette(palette)
        palette = self.fontColorButton.palette()
        palette.setColor(QPalette.ButtonText, newcolor)
        self.fontColorButton.setPalette(palette)
        
    def changeBgColor(self):
        palette = self.sampleText.palette()
        color = palette.color(QPalette.Base)
        newcolor = QColorDialog.getColor(color,
                                         None,
                                         self.trUtf8("Select Background Color"))
        palette.setColor(QPalette.Base, newcolor)
        self.sampleText.setPalette(palette)
        palette = self.bgColorButton.palette()
        palette.setColor(QPalette.ButtonText, newcolor)
        self.bgColorButton.setPalette(palette)
    
    def __setupUi(self, font, fontColor, bgColor):
        fixedSizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        expandingSizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName('gridLayout')
        
        #First Row
        self.fontLabel = QLabel(self)
        self.fontLabel.setObjectName('fontLabel')
        self.fontLabel.setSizePolicy(fixedSizePolicy)
        self.fontLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gridLayout.addWidget(self.fontLabel, 0, 0, 1, 1)
        
        self.fontComboBox = QFontComboBox(self)
        self.fontComboBox.setObjectName('fontComboBox')
        self.fontComboBox.setSizePolicy(expandingSizePolicy)
        self.fontComboBox.setWritingSystem(QFontDatabase.Latin)
        self.fontComboBox.setFontFilters(QFontComboBox.AllFonts)
        self.fontComboBox.setCurrentFont(font)
        self.gridLayout.addWidget(self.fontComboBox, 0, 1, 1, 3)
        
        
        self.sizeLabel = QLabel(self)
        self.sizeLabel.setObjectName('sizeLabel')
        self.sizeLabel.setSizePolicy(fixedSizePolicy)
        self.sizeLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gridLayout.addWidget(self.sizeLabel, 0, 4, 1, 1)
        
        self.sizeSpinBox = QSpinBox(self)
        self.sizeSpinBox.setObjectName('sizeSpinBox')
        self.sizeSpinBox.setSizePolicy(fixedSizePolicy)        
        self.sizeSpinBox.setMinimum(1)
        self.sizeSpinBox.setMaximum(100)
        self.sizeSpinBox.setProperty('value', font.pointSize())
        self.gridLayout.addWidget(self.sizeSpinBox, 0, 5, 1, 1)
        
        self.boldButton = QPushButton(self)
        self.boldButton.setObjectName('boldButton')
        self.boldButton.setSizePolicy(fixedSizePolicy)
        self.boldButton.setMaximumSize(QSize(24, 24))
        self.boldButton.setFont(QFont('Tahoma', 11, 75, False))
        self.boldButton.setCheckable(True)
        if font.bold():
            self.boldButton.setChecked(True)
        self.gridLayout.addWidget(self.boldButton, 0, 6, 1, 1)
        
        self.italicButton = QPushButton(self)
        self.italicButton.setObjectName('italicButton')
        self.italicButton.setSizePolicy(fixedSizePolicy)
        self.italicButton.setMaximumSize(QSize(24, 24))
        self.italicButton.setFont(QFont('Tahoma', 11, 75, True))
        self.italicButton.setCheckable(True)
        if font.italic():
            self.italicButton.setChecked(True)
        self.gridLayout.addWidget(self.italicButton, 0, 7, 1, 1)
        
        #Second Row
        self.textColorLabel = QLabel(self)
        self.textColorLabel.setObjectName('textColorLabel')
        self.textColorLabel.setSizePolicy(expandingSizePolicy)
        self.textColorLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gridLayout.addWidget(self.textColorLabel, 1, 5, 1, 2)
        
        self.fontColorButton = QPushButton(self)
        self.fontColorButton.setMaximumSize(QSize(24, 24))
        self.fontColorButton.setSizePolicy(fixedSizePolicy)
        self.fontColorButton.setFont(QFont('Tahoma', 11, 75, False))
        self.fontColorButton.setObjectName('fontColorButton')
        self.fontColorButton.setCheckable(True)
        if fontColor:
            palette = self.fontColorButton.palette()
            palette.setColor(QPalette.ButtonText, fontColor)
            self.fontColorButton.setPalette(palette)
        else:
            fontColor = self.palette().color(QPalette.Text)
        self.gridLayout.addWidget(self.fontColorButton, 1, 7, 1, 1)

        self.bgColorLabel = QLabel(self)
        self.bgColorLabel.setObjectName('bgColorLabel')
        self.bgColorLabel.setSizePolicy(expandingSizePolicy)
        self.bgColorLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gridLayout.addWidget(self.bgColorLabel, 2, 5, 1, 2)
        
        self.bgColorButton = QPushButton(self)
        self.bgColorButton.setObjectName('bgColorButton')
        self.bgColorButton.setMaximumSize(QSize(24, 24))
        self.bgColorButton.setSizePolicy(fixedSizePolicy)
        self.bgColorButton.setFont(QFont('Webdings', 9))
        
        palette = self.bgColorButton.palette()
        if not bgColor:
            bgColor = palette.color(QPalette.Base)
        palette.setColor(QPalette.ButtonText, bgColor)
        self.bgColorButton.setPalette(palette)
        self.gridLayout.addWidget(self.bgColorButton, 2, 7, 1, 1)
        
        
        self.sampleTextArea = QScrollArea(self)
        self.sampleTextArea.setObjectName('textSampleArea')
        self.sampleTextArea.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.sampleTextArea.setAlignment(Qt.AlignCenter)
        self.sampleTextArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sampleTextArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  
#        self.sampleTextArea.setFrameShape(QFrame.NoFrame)
        
        self.sampleText = QLineEdit()
        self.sampleText.setObjectName('textSample')
        self.sampleText.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.sampleText.setText('Sample Text 123')
        self.sampleText.setReadOnly(True)
        self.sampleText.setAlignment(Qt.AlignCenter)
        self.sampleText.setFrame(False)
        self.sampleTextArea.setWidgetResizable(True)
        self.sampleTextArea.setWidget(self.sampleText)
#        self.sampleText.setTextInteractionFlags(Qt.NoTextInteraction)
        
        palette = self.sampleText.palette()
        palette.setColor(QPalette.Text, fontColor)
        palette.setColor(QPalette.Base, bgColor)
        self.sampleText.setPalette(palette)
        self.gridLayout.addWidget(self.sampleTextArea, 1, 0, 2, 5)
        
        self.fontLabel.setBuddy(self.fontComboBox)
        self.sizeLabel.setBuddy(self.sizeSpinBox)
        self.textColorLabel.setBuddy(self.fontColorButton)
        self.bgColorLabel.setBuddy(self.bgColorButton)

    def retranslateUi(self):
        self.setTitle(self.trUtf8('Font Settings'))
        self.fontLabel.setText(self.trUtf8('Font'))
        self.fontComboBox.setToolTip(self.trUtf8('Select the font type'))
        self.textColorLabel.setText(self.trUtf8('Text Color'))
        self.fontColorButton.setText(self.trUtf8('A'))
        self.fontColorButton.setToolTip(self.trUtf8('Click to open a dialog to select the text color'))
        self.bgColorLabel.setText(self.trUtf8('Background'))
        self.bgColorButton.setText(self.trUtf8('g'))
        self.bgColorButton.setToolTip(self.trUtf8('Click to open a dialog to select the background color'))
        self.sizeLabel.setText(self.trUtf8('Size'))
        self.sizeSpinBox.setToolTip(self.trUtf8('Select the font size'))
        self.boldButton.setText(self.trUtf8('B'))
        self.boldButton.setToolTip(self.trUtf8('Bold'))
        self.italicButton.setText(self.trUtf8('I'))
        self.italicButton.setToolTip(self.trUtf8('Italic'))

class GenericDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setObjectName('dialog')
        self.setWindowTitle('FontGroupBox Test')
        self.resize(371, 151)
        self.setFont(QFont('Segoe UI', 9))
        
        self.__setupUi()
        
        self.buttonBox.accepted.connect(self.accept)
        
    def __setupUi(self):
        self.layout = QVBoxLayout(self)
        self.layout.setObjectName('layout')
        
        self.fontGroupBox = FontGroupBox(self.font(), None, None, self)
        self.fontGroupBox.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.fontGroupBox.setGeometry(QRect(10, 10, 351, 131))
        self.fontGroupBox.setAlignment(Qt.AlignCenter)
        self.fontGroupBox.setObjectName('fontGroupBox')
        self.layout.addWidget(self.fontGroupBox)
        
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok, 
                                          Qt.Horizontal, self)
        self.layout.addWidget(self.buttonBox)
        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = GenericDialog()
    dialog.show()
    sys.exit(app.exec_())
