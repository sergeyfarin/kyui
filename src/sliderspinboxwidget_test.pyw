from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Widgets.sliderspinboxwidget import SliderSpinBoxWidget

class Defaults():
    __slots__ = ['label', 'min', 'max', 'pagestep', 'singlestep', 
                 'prefix', 'suffix', 'tracking', 'value']
    label = 'Testing'
    adjust = True
    min = 0
    max = 200
    pagestep = 10
    singlestep = 5
    prefix = 'te'
    suffix = 'st'
    tracking = True
    value = 0

class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setObjectName('dialog')
        self.setupUi()
        self.setDefaults()
        
    def setupUi(self):
        self.setMinimumSize(QSize(350, 275))
        self.setFont(QFont('Segoe UI', 9))
        
        self.layout = QGridLayout(self)
        
        self.testWidget = SliderSpinBoxWidget(parent=self, 
                                              adjust=Defaults.adjust, 
                                              text=Defaults.label, 
                                              min=Defaults.min, 
                                              max=Defaults.max, 
                                              name='testWidget', 
                                              pagestep=Defaults.pagestep, 
                                              singlestep=Defaults.singlestep, 
                                              prefix=Defaults.prefix, 
                                              suffix=Defaults.suffix, 
                                              tracking=Defaults.tracking, 
                                              value=Defaults.value)
        self.layout.addWidget(self.testWidget, 0, 0, 1, 2)
        
        self.textBox = QGroupBox(self)
        self.textBox.setObjectName('textBox')
        self.textLayout = QGridLayout(self.textBox)
        self.textLayout.setObjectName('textLayout')
        
        self.textLabel = QLabel(self.textBox)
        self.textLabel.setObjectName('textLabel')
        self.textLayout.addWidget(self.textLabel, 0, 0)
        
        self.textLineEdit = QLineEdit(self.textBox)
        self.textLineEdit.setObjectName('textLineEdit')
        self.textLineEdit.setMaxLength(12)
        self.textLayout.addWidget(self.textLineEdit, 0, 1)
        
        self.prefixLabel = QLabel(self.textBox)
        self.prefixLabel.setObjectName('prefixLabel')
        self.textLayout.addWidget(self.prefixLabel, 1, 0)
        
        self.prefixLineEdit = QLineEdit(self.textBox)
        self.prefixLineEdit.setObjectName('prefixLineEdit')
        self.prefixLineEdit.setMaxLength(4)
        self.textLayout.addWidget(self.prefixLineEdit, 1, 1)
        
        self.suffixLabel = QLabel(self.textBox)
        self.suffixLabel.setObjectName('suffixLabel')
        self.textLayout.addWidget(self.suffixLabel, 2, 0)
        
        self.suffixLineEdit = QLineEdit(self.textBox)
        self.suffixLineEdit.setObjectName('suffixLineEdit')
        self.suffixLineEdit.setMaxLength(4)
        self.textLayout.addWidget(self.suffixLineEdit, 2, 1)
        
        self.textButton = QPushButton(self.textBox)
        self.textButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.textLayout.setAlignment(self.textButton, 
                                    Qt.AlignRight | Qt.AlignBottom)
        self.textLayout.addWidget(self.textButton, 3, 0, 1, 2)
        
        self.layout.addWidget(self.textBox, 1, 0)
        
        self.rangeValueBox = QGroupBox(self)
        self.rangeValueBox.setGeometry(QRect(10, 40, 131, 101))
        self.rangeValueBox.setObjectName('rangeValueBox')
        self.rangeValueLayout = QGridLayout(self.rangeValueBox)
        self.rangeValueLayout.setObjectName('rangeValueLayout')
        self.minLabel = QLabel(self.rangeValueBox)
        self.minLabel.setObjectName('minLabel')
        self.rangeValueLayout.addWidget(self.minLabel, 0, 0)
        self.minSpinBox = QSpinBox(self.rangeValueBox)
        self.minSpinBox.setObjectName('minSpinBox')
        self.rangeValueLayout.addWidget(self.minSpinBox, 0, 1)
        self.maxLabel = QLabel(self.rangeValueBox)
        self.maxLabel.setObjectName('maxLabel')
        self.rangeValueLayout.addWidget(self.maxLabel, 1, 0)
        self.maxSpinBox = QSpinBox(self.rangeValueBox)
        self.maxSpinBox.setObjectName('maxSpinBox')
        self.rangeValueLayout.addWidget(self.maxSpinBox, 1, 1)
        self.valueLabel = QLabel(self.rangeValueBox)
        self.valueLabel.setObjectName('valueLabel')
        self.rangeValueLayout.addWidget(self.valueLabel, 2, 0)
        self.valueSpinBox = QSpinBox(self.rangeValueBox)
        self.valueSpinBox.setObjectName('valueSpinBox')
        self.rangeValueLayout.addWidget(self.valueSpinBox, 2, 1)
        
        self.rangeValueButton = QPushButton(self.rangeValueBox)
        self.rangeValueButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.rangeValueLayout.addWidget(self.rangeValueButton, 3, 0, 1, 2)
        self.rangeValueLayout.setAlignment(self.rangeValueButton, 
                                           Qt.AlignRight | Qt.AlignBottom)
        self.layout.addWidget(self.rangeValueBox, 1, 1)
        
        self.stepTrackingBox = QGroupBox(self)
        self.stepTrackingBox.setObjectName('stepTrackingBox')
        self.stepTrackingLayout = QGridLayout(self.stepTrackingBox)
        self.stepTrackingLayout.setObjectName('stepTrackingLayout')
        
        self.singleLabel = QLabel(self.stepTrackingBox)
        self.singleLabel.setObjectName('singleLabel')
        self.stepTrackingLayout.addWidget(self.singleLabel, 0, 0)
        self.singleSpinBox = QSpinBox(self.stepTrackingBox)
        self.singleSpinBox.setObjectName('singleSpinBox')
        self.stepTrackingLayout.addWidget(self.singleSpinBox, 0, 1)
        self.pageLabel = QLabel(self.stepTrackingBox)
        self.pageLabel.setObjectName('pageLabel')
        self.stepTrackingLayout.addWidget(self.pageLabel, 1, 0)
        self.pageSpinBox = QSpinBox(self.stepTrackingBox)
        self.pageSpinBox.setObjectName('pageSpinBox')
        self.stepTrackingLayout.addWidget(self.pageSpinBox, 1, 1)
        self.trackingBox = QCheckBox(self.stepTrackingBox)
        self.trackingBox.setObjectName('trackingBox')
        self.stepTrackingLayout.addWidget(self.trackingBox, 2, 0, 1, 2)
        self.adjustBox = QCheckBox(self.stepTrackingBox)
        self.adjustBox.setObjectName('adjustBox')
        self.stepTrackingLayout.addWidget(self.adjustBox, 3, 0, 1, 2)
        self.stepTrackingButton = QPushButton(self.stepTrackingBox)
        self.stepTrackingButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.stepTrackingLayout.addWidget(self.stepTrackingButton, 4, 0, 1, 2)
        self.stepTrackingLayout.setAlignment(self.stepTrackingButton, 
                                             Qt.AlignRight | Qt.AlignBottom)
        self.layout.addWidget(self.stepTrackingBox, 2, 0)
        
        self.closeButton = QPushButton(self)
        self.closeButton.setGeometry(QRect(260, 230, 75, 23))
        self.closeButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.closeButton.setObjectName('closeButton')
        self.layout.addWidget(self.closeButton, 2, 1)
        self.layout.setAlignment(self.closeButton, Qt.AlignRight | Qt.AlignBottom)
        
        self.textLabel.setBuddy(self.textLineEdit)
        self.prefixLabel.setBuddy(self.prefixLineEdit)
        self.suffixLabel.setBuddy(self.suffixLineEdit)
        self.minLabel.setBuddy(self.minSpinBox)
        self.maxLabel.setBuddy(self.maxSpinBox)
        self.valueLabel.setBuddy(self.valueSpinBox)
        self.singleLabel.setBuddy(self.singleSpinBox)
        self.pageLabel.setBuddy(self.pageSpinBox)
        
        self.retranslateUi(self)
        self.closeButton.clicked.connect(self.close)
        self.textButton.clicked.connect(self.onTextButtonClicked)
        self.rangeValueButton.clicked.connect(self.onRangeValueButtonClicked)
        self.stepTrackingButton.clicked.connect(self.onStepTrackingButtonClicked)
        
    def setDefaults(self):
        self.minSpinBox.setMinimum(0)
        self.minSpinBox.setMaximum(99)
        self.minSpinBox.setValue(Defaults.min)
        
        self.maxSpinBox.setMinimum(100)
        self.maxSpinBox.setMaximum(255)
        self.maxSpinBox.setValue(Defaults.max)
        
        self.singleSpinBox.setMinimum(1)
        self.singleSpinBox.setMaximum(10)
        self.singleSpinBox.setValue(Defaults.singlestep)
        
        self.pageSpinBox.setMinimum(5)
        self.pageSpinBox.setMaximum(20)
        self.pageSpinBox.setValue(Defaults.pagestep)
        
        self.valueSpinBox.setMinimum(Defaults.min)
        self.valueSpinBox.setMaximum(Defaults.max)
        self.valueSpinBox.setValue(Defaults.value)
        
        self.trackingBox.setChecked(Defaults.tracking)
        self.trackingBox.setChecked(Defaults.adjust)
        
        self.prefixLineEdit.setText(Defaults.prefix)
        self.suffixLineEdit.setText(Defaults.suffix)
        self.textLineEdit.setText(Defaults.label)

    def retranslateUi(self, Form):
        self.setWindowTitle(self.trUtf8('SliderSpinBoxWidget Test'))
        
        self.rangeValueBox.setTitle(self.trUtf8('Range and Value'))
        self.stepTrackingBox.setTitle(self.trUtf8('Step and Tracking'))
        self.textBox.setTitle(self.trUtf8('Text'))
        
        self.textButton.setText('Apply')
        self.stepTrackingButton.setText('Apply')
        self.rangeValueButton.setText('Apply')
        
        self.textLabel.setText(self.trUtf8('&Label Text'))
        self.prefixLabel.setText(self.trUtf8('&Prefix'))
        self.suffixLabel.setText(self.trUtf8('&Suffix'))
        self.minLabel.setText(self.trUtf8('Mi&nimum'))
        self.maxLabel.setText(self.trUtf8('Ma&ximum'))
        self.valueLabel.setText(self.trUtf8('&Value'))
        self.singleLabel.setText(self.trUtf8('S&ingle Step'))
        self.pageLabel.setText(self.trUtf8('Pa&ge Step'))
        self.trackingBox.setText(self.trUtf8('&Tracking Enabled'))
        self.adjustBox.setText(self.trUtf8('&Adjust to Range'))
        self.closeButton.setText(self.trUtf8('Close'))
        
    def onTextButtonClicked(self):
        self.testWidget.setPrefix(self.prefixLineEdit.text())
        self.testWidget.setSuffix(self.suffixLineEdit.text())
        self.testWidget.setLabelText(self.textLineEdit.text())
        
    def onRangeValueButtonClicked(self):
        min = self.minSpinBox.value()
        max = self.maxSpinBox.value()
        self.testWidget.setRange(min, max)
        self.valueSpinBox.setMinimum(min)
        self.valueSpinBox.setMaximum(max)
        self.testWidget.setValue(self.valueSpinBox.value())
        
    def onStepTrackingButtonClicked(self):
        self.testWidget.setSingleStep(self.singleSpinBox.value())
        self.testWidget.setPageStep(self.pageSpinBox.value())
        self.testWidget.setTracking(self.trackingBox.isChecked())
        self.testWidget.setAdjustToRange(self.adjustBox.isChecked())

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = Dialog()
    ui.show()
    sys.exit(app.exec_())

