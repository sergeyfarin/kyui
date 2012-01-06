#UTF-8
#colorbutton_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Widgets.progressindicator import ProgressIndicator
from template_test import TemplateDialog

colorPairs = (('White', QColor(Qt.white)),
            ('Black', QColor(Qt.black)),
            ('Red', QColor(Qt.red)),
            ('Dark Red', QColor(Qt.darkRed)),
            ('Green', QColor(Qt.green)),
            ('Dark Green', QColor(Qt.darkGreen)),
            ('Blue', QColor(Qt.blue)),
            ('Dark Blue', QColor(Qt.darkBlue)),
            ('Cyan', QColor(Qt.cyan)),
            ('Dark Cyan', QColor(Qt.darkCyan)),
            ('Magenta', QColor(Qt.magenta)),
            ('Dark Magenta', QColor(Qt.darkMagenta)),
            ('Yellow', QColor(Qt.yellow)),
            ('Dark Yellow', QColor(Qt.darkYellow)),
            ('Gray', QColor(Qt.gray)),
            ('Dark Gray', QColor(Qt.darkGray)),
            ('Light Gray', QColor(Qt.lightGray)))

class Dialog(TemplateDialog):
    def __init__(self, parent = None):
        super(QDialog, self).__init__(parent)
        self.setObjectName('dialog')
        
        self.setupUi()
        self.retranslateUi()
        self.connectSignals()
        
    def setupUi(self):
        super().setupUi()
        
        self.testWidget = ProgressIndicator(parent=self, 
                                            objectName='testWidget', 
                                            color=Qt.white)
        self.layout.insertWidget(0, self.testWidget)
        
        self.colorBox = QComboBox(self.settingsBox, 
                                  objectName='colorBox')
        self.settingsLayout.addRow('C&olor', self.colorBox)
        for name, color in colorPairs:
            self.colorBox.addItem(name, color)
        self.colorBox.setCurrentIndex(1)
        
        self.delayBox = QSpinBox(parent=self, 
                                 objectName='delayBox', 
                                 minimum=10, 
                                 maximum=200, 
                                 singleStep=5, 
                                 value=80, 
                                 suffix=' msec')
        self.settingsLayout.addRow('&Delay', self.delayBox)
        
        self.visibleBox = QCheckBox(parent=self, 
                                    objectName='visibleBox')
        self.settingsLayout.addWidget(self.visibleBox)
        
        self.busyButton = QPushButton(parent=self, 
                                      objectName='busyButton', 
                                      checkable=True, 
                                      checked=False)
        self.settingsLayout.addWidget(self.busyButton)
        
    def retranslateUi(self):
        super().retranslateUi()
        tr = self.trUtf8
        self.setWindowTitle(tr('ProgressIndicator Test'))
        self.settingsLayout.labelForField(self.delayBox).setText(tr('&Delay'))
        self.settingsLayout.labelForField(self.colorBox).setText(tr('C&olor'))
        self.visibleBox.setText('Always &Visible')
        self.busyButton.setText('&Busy')
        
        for idx in range(len(colorPairs)):
            self.colorBox.setItemText(idx, tr(colorPairs[idx][0]))

    def connectSignals(self):
        super().connectSignals()
        self.colorBox.currentIndexChanged[int].connect(self.onColorChanged)
        self.delayBox.valueChanged[int].connect(self.testWidget.setAnimationDelay)
        self.visibleBox.toggled.connect(self.testWidget.setAlwaysVisible)
        self.busyButton.toggled.connect(self.testWidget.setBusy)

    def onColorChanged(self, idx : int):
        self.testWidget.setColor(self.colorBox.itemData(idx, Qt.UserRole))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
