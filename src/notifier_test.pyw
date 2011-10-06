#UTF-8
#notifier_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from template_test import TemplateDialog
from Widgets.notifier import NotifierPopup

class NotifierDialog(TemplateDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi()
        self.connectSignals()
        
    def setupUi(self):
        super().setupUi()
        self.visibilityButton = QPushButton(parent=self, 
                                            checkable=False, 
                                            objectName='visibilityButton')
        self.visibilityButton.setFixedWidth(100)
        self.layout.insertWidget(0, self.visibilityButton)
        self.layout.setAlignment(self.visibilityButton, Qt.AlignCenter)
        
        self.opacityLabel = QLabel(self.settingsBox, objectName='opacityLabel')
        self.opacityBox = QDoubleSpinBox(self.settingsBox, 
                                         decimals=2, 
                                         minimum=0.0, 
                                         maximum=1.0, 
                                         singleStep=0.05, 
                                         objectName='opacityBox', 
                                         buttonSymbols=QAbstractSpinBox.NoButtons)
        self.opacityBox.setValue(1.0)
        self.settingsLayout.addRow(self.opacityLabel, self.opacityBox)
        
        self.showBox = QGroupBox(self, objectName='showBox')
        self.showLayout = QGridLayout(self.showBox, objectName='showLayout')
        
        self.showTypeLabel = QLabel(self.showBox, objectName='showTypeLabel')
        self.showLayout.addWidget(self.showTypeLabel, 0, 0, 1, 1)
        
        self.showTypeBox = QComboBox(self.showBox, objectName='showTypeBox')
        self.showTypeBox.addItem('None')
        self.showTypeBox.addItem('Animate (Slide)')
        self.showTypeBox.addItem('Fade')
        self.showLayout.addWidget(self.showTypeBox, 0, 1, 1, 1)
        
        self.showDurationLabel = QLabel(self.showBox, 
                                        enabled=False, 
                                        objectName='showDurationLabel')
        self.showLayout.addWidget(self.showDurationLabel, 1, 0, 1, 1)
        
        self.showDurationBox = QSpinBox(self.showBox, 
                                        enabled=False, 
                                        maximum=10000, 
                                        objectName='showDurationBox', 
                                        buttonSymbols=QAbstractSpinBox.NoButtons)
        self.showDurationBox.setValue(300)
        self.showLayout.addWidget(self.showDurationBox, 1, 1, 1, 1)
        
        self.showDependancyBox = QCheckBox(self.showBox, 
                                           enabled=False, 
                                           objectName='showDependancyBox')
        self.showLayout.addWidget(self.showDependancyBox, 2, 0, 1, 2)
        self.layout.insertWidget(2, self.showBox)
        
        self.hideBox = QGroupBox(self, objectName='hideBox')
        self.hideLayout = QGridLayout(self.hideBox, objectName='hideLayout')
        
        self.hideTypeLabel = QLabel(self.hideBox, objectName='hideTypeLabel')
        self.hideLayout.addWidget(self.hideTypeLabel, 0, 0, 1, 1)
        
        self.hideTypeBox = QComboBox(self.hideBox, objectName='hideTypeBox')
        self.hideTypeBox.addItem('None')
        self.hideTypeBox.addItem('Animate (Slide)')
        self.hideTypeBox.addItem('Fade')
        self.hideLayout.addWidget(self.hideTypeBox, 0, 1, 1, 1)
        
        self.hideDurationLabel = QLabel(self.hideBox, 
                                        enabled=False, 
                                        objectName='hideDurationLabel')
        self.hideLayout.addWidget(self.hideDurationLabel, 1, 0, 1, 1)
        
        self.hideDurationBox = QSpinBox(self.hideBox,
                                        objectName='hideDurationBox', 
                                        maximum=10000, 
                                        enabled=False, 
                                        buttonSymbols=QAbstractSpinBox.NoButtons)
        self.hideDurationBox.setValue(300)
        self.hideLayout.addWidget(self.hideDurationBox, 1, 1, 1, 1)
        
        self.hideDependancyBox = QCheckBox(self.hideBox, 
                                           objectName='hideDependancyBox', 
                                           enabled=False)
        self.hideLayout.addWidget(self.hideDependancyBox, 2, 0, 1, 2)
        self.layout.insertWidget(3, self.hideBox)
        
        self.testWidget = NotifierPopup(self)
        self.testWidget.hideStyle = None
        self.showTypeBox.setCurrentIndex(1)
        self.changeShowStyle(1)
        self.testWidget.setObjectName('testWidget')
        
        self.opacityLabel.setBuddy(self.opacityBox)
        self.showTypeLabel.setBuddy(self.showTypeBox)
        self.showDurationLabel.setBuddy(self.showDurationBox)
        self.hideTypeLabel.setBuddy(self.showTypeBox)
        self.hideDurationLabel.setBuddy(self.showDurationBox)

        self.retranslateUi()
        
    def connectSignals(self):
        super().connectSignals()
        self.visibilityButton.clicked.connect(self.changeVisibility)
        self.opacityBox.valueChanged.connect(self.testWidget.setOpacity)
        self.showTypeBox.currentIndexChanged[int].connect(self.changeShowStyle)
        self.showDurationBox.valueChanged.connect(self.testWidget.setShowDuration)
        self.hideTypeBox.currentIndexChanged[int].connect(self.changeHideStyle)
        self.hideDurationBox.valueChanged.connect(self.testWidget.setHideDuration)

    def retranslateUi(self):
        super().retranslateUi()
        self.setWindowTitle(self.trUtf8('Notification Test Dialog'))
        self.visibilityButton.setText(self.trUtf8('set&Visible()'))
        self.opacityLabel.setText(self.trUtf8('&Opacity'))
        self.showBox.setTitle(self.trUtf8('&Show'))
        self.showTypeLabel.setText(self.trUtf8('Animation Type'))
        self.showTypeBox.setItemText(0, self.trUtf8('None'))
        self.showTypeBox.setItemText(1, self.trUtf8('Animate (Slide)'))
        self.showTypeBox.setItemText(2, self.trUtf8('Fade'))
        self.showDurationLabel.setText(self.trUtf8('Duration'))
        self.showDependancyBox.setToolTip(self.trUtf8('Make the duration value depend on the size of the widget. This is only valid for AnimateMenu (slide) effect.'))
        self.showDependancyBox.setText(self.trUtf8('Duration depends on widget size'))
        self.hideBox.setTitle(self.trUtf8('&Hide'))
        self.hideTypeLabel.setText(self.trUtf8('Animation Type'))
        self.hideTypeBox.setItemText(0, self.trUtf8('None'))
        self.hideTypeBox.setItemText(1, self.trUtf8('Animate (Slide)'))
        self.hideTypeBox.setItemText(2, self.trUtf8('Fade'))
        self.hideDurationLabel.setText(self.trUtf8('Duration'))
        self.hideDependancyBox.setToolTip(self.trUtf8('Make the duration value depend on the size of the widget. This is only valid for AnimateMenu (slide) effect.'))
        self.hideDependancyBox.setText(self.trUtf8('Duration depends on widget size'))
        
    def changeVisibility(self):
        if self.testWidget.isVisible():
            self.testWidget.hide()
        else:
            self.testWidget.show()

    def changeShowStyle(self, idx):
        if idx == 0:
            self.testWidget.showStyle = None
            self.showDurationLabel.setEnabled(False)
            self.showDurationBox.setEnabled(False)
        elif idx == 1:
            self.testWidget.showStyle = Qt.UI_AnimateMenu
            self.showDurationLabel.setEnabled(True)
            self.showDurationBox.setEnabled(True)
        elif idx == 2:
            self.testWidget.showStyle = Qt.UI_FadeMenu
            self.showDurationLabel.setEnabled(True)
            self.showDurationBox.setEnabled(True)

    def changeHideStyle(self, idx):
        if idx == 0:
            self.testWidget.hideStyle = None
            self.hideDurationLabel.setEnabled(False)
            self.hideDurationBox.setEnabled(False)
        elif idx == 1:
            self.testWidget.hideStyle = Qt.UI_AnimateMenu
            self.hideDurationLabel.setEnabled(True)
            self.hideDurationBox.setEnabled(True)
        elif idx == 2:
            self.testWidget.hideStyle = Qt.UI_FadeMenu
            self.hideDurationLabel.setEnabled(True)
            self.hideDurationBox.setEnabled(True)
            
    def closeEvent(self, ev):
        super().closeEvent(ev)
        QApplication.exit()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = NotifierDialog()
    ui.show()
    sys.exit(app.exec_())
