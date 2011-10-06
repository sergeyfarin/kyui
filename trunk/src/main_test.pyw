from PyQt4.QtCore import Qt, QPoint

from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QFont
from PyQt4.QtGui import QGridLayout
from PyQt4.QtGui import QComboBox, QLabel, QPushButton

from basicfontwidget_test import Dialog as BasicFontWidgetDialog
from colorbutton_test import Dialog as ColorButtonDialog
from colorframe_test import Dialog as ColorFrameDialog
from colorpicker_test import Dialog as ColorPickerDialog
from colorslider_test import Dialog as ColorSliderDialog
from keysequence_test import Dialog as KeySequenceDialog
from sliderspinboxwidget_test import Dialog as SliderSpinBoxWidgetDialog
from splitter_test import Dialog as SplitterDialog
from propertyinfo_test import Dialog as PropertyInfoDialog
from propertymodel_test import Dialog as PropertyModelDialog
#from colorsliderwidget_test import Dialog as ColorSliderWidgetDialog

class Dialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFont(QFont('Segoe UI', 9))
        
        self.layout = QGridLayout(self)
        self.mainLabel = QLabel(self, objectName='mainLabel')
        self.layout.addWidget(self.mainLabel, 0, 0, 1, 2)
        
        self.widgetLabel = QLabel(self, objectName='widgetLabel', wordWrap=True)
        self.widgetBox = QComboBox(self, objectName='widgetBox')
        self.widgetLabel.setBuddy(self.widgetBox)
        
        self.layout.addWidget(self.widgetLabel, 1, 0)
        self.layout.addWidget(self.widgetBox, 1, 1)
        
        self.widgetBox.addItem('BasicFontWidget', BasicFontWidgetDialog)
        self.widgetBox.addItem('ColorButton', ColorButtonDialog)
        self.widgetBox.addItem('ColorFrame', ColorFrameDialog)
        self.widgetBox.addItem('ColorPicket', ColorPickerDialog)
        self.widgetBox.addItem('ColorSlider', ColorSliderDialog)
#        self.widgetBox.addItem('ColorSliderWidget', ColorSliderWidgetDialog)
        self.widgetBox.addItem('KeySequenceLineEdit', KeySequenceDialog)
        self.widgetBox.addItem('PropertyInfo', PropertyInfoDialog)
        self.widgetBox.addItem('PropertyModel', PropertyModelDialog)
        self.widgetBox.addItem('SliderSpinBoxWidget', SliderSpinBoxWidgetDialog)
        self.widgetBox.addItem('Splitter', SplitterDialog)
        
        self.widgetBox.setCurrentIndex(-1)
        
        self.closeButton = QPushButton(self,
                                       objectName='closeButton', 
                                       clicked=self.close)
        self.layout.addWidget(self.closeButton, 2, 1)
        self.layout.setAlignment(self.closeButton, Qt.AlignRight | Qt.AlignVCenter)
        
        self.testDialog = None
        self.retranslateUi()
        self.connectSignals()
    
    def connectSignals(self):
        self.widgetBox.currentIndexChanged.connect(self.testDialogChanged)
    
    def retranslateUi(self):
        self.mainLabel.setText(self.trUtf8('Select a widget from the combobox\nto run a test dialog'))
        self.widgetLabel.setText(self.trUtf8('&Widget'))
        self.closeButton.setText(self.trUtf8('&Close'))
        
    def testDialogChanged(self, index):
        newWidget = self.widgetBox.itemData(index)(self)
        if self.testDialog and self.testDialog.isVisible():
            self.testDialog.close()
        self.testDialog = newWidget
        
        edge = self.frameGeometry().right() + 1
#        if edge + self.testDialog.frameGeometry().width() > QApplication.desktop().availableGeometry(self).right():
#            edge = self.frameGeometry().left() - 1 - self.testDialog.frameGeometry().width()
        self.testDialog.move(QPoint(edge, self.frameGeometry().y()))
        self.testDialog.show()

if __name__ == '__main__':
    from PyQt4.QtGui import QApplication
    import sys
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
