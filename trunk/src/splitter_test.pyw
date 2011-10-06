#UTF-8
#splitter_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

from Widgets.splitter import Splitter, SplitterHandle
from template_test import TemplateDialog

class Dialog(TemplateDialog):
    def __init__(self, parent : QWidget = None):
        super().__init__(parent)
        self.setupUi()
        self.connectSignals()
    
    def setupUi(self):
        super().setupUi()
        
        self.testWidget = Splitter(Qt.Horizontal, 
                                   self, 
                                   objectName='testWidget', 
                                   frameShape=QFrame.StyledPanel)
        self.testWidget.setFixedSize(QSize(400, 150))
#        self.testWidget.setContentsMargins(4, 4, 4, 4)
        self.layout.insertWidget(0, self.testWidget)
        
        widget1 = QFrame(parent=self.testWidget, 
                         objectName='widget1', 
                         frameShape=QFrame.StyledPanel, 
                         autoFillBackground = True)
        widget2 = QFrame(parent=self.testWidget, 
                         objectName='widget1', 
                         frameShape=QFrame.StyledPanel, 
                         autoFillBackground = True)
        widget1.setContentsMargins(2, 2, 2, 2)
        widget2.setContentsMargins(2, 2, 2, 2)
        pal = widget1.palette()
        pal.setColor(QPalette.Window, QColor(Qt.white))
        widget1.setPalette(pal)
        widget2.setPalette(pal)
        
        self.testWidget.addWidget(widget1)
        self.testWidget.addWidget(widget2)
        
        self.handleBox = QComboBox(self.settingsBox, 
                                   objectName='handleBox')
        self.settingsLayout.addRow('&Handle Style', self.handleBox)
        
        self.handleBox.addItem('Plain', Splitter.Plain)
        self.handleBox.addItem('Parallel Line', Splitter.ParallelLine)
        self.handleBox.addItem('Centered Dashes', Splitter.CenteredDashes)
        
        
        self.widthBox = QSpinBox(self.settingsBox,
                                 objectName='widthBox', 
                                 minimum = 2, 
                                 maximum = 20, 
                                 value = self.testWidget.handleWidth())
        self.settingsLayout.addRow('Handle &Width', self.widthBox)
        
        self.orientBox = QCheckBox(self.settingsBox, 
                                   objectName='orientBox')
        self.settingsLayout.addWidget(self.orientBox)
        
        self.opaqueResizeBox = QCheckBox(self.settingsBox, 
                                         objectName='opaqueResizeBox', 
                                         checked=True)
        self.settingsLayout.addWidget(self.opaqueResizeBox)
        
        self.retranslateUi()
        
    def retranslateUi(self):
        self.settingsLayout.labelForField(self.handleBox).setText(self.trUtf8('&Handle Style'))
        self.settingsLayout.labelForField(self.widthBox).setText(self.trUtf8('Handle &Width'))
        self.orientBox.setText(self.trUtf8('&Vertical Orientation'))
        self.opaqueResizeBox.setText(self.trUtf8('&Opaque Resize'))
        super().retranslateUi()
        
    def connectSignals(self):
        self.handleBox.currentIndexChanged[int].connect(self.changeHandleStyle)
        self.widthBox.valueChanged[int].connect(self.testWidget.setHandleWidth)
        self.orientBox.toggled.connect(self.changeOrientation)
        self.opaqueResizeBox.toggled.connect(self.testWidget.setOpaqueResize)
        
        super().connectSignals()
    
    def changeHandleStyle(self, idx):
        self.testWidget.setHandleStyle(self.handleBox.itemData(idx))
    
    def changeOrientation(self, vertical = False):
        self.testWidget.setOrientation(Qt.Vertical if vertical else Qt.Horizontal)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
