#UTF-8
#splitter_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

from Widgets.splitter import Splitter
#from Widgets.divider import Divider
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
                                   frameShape=QFrame.StyledPanel, 
                                   frameShadow=QFrame.Plain)
        self.testWidget.setFixedSize(QSize(400, 150))
        self.layout.insertWidget(0, self.testWidget)
        
        #populate the splitter
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
        
        #set the widget backgrounds to white
        pal = widget1.palette()
        pal.setColor(QPalette.Window, QColor(Qt.white))
        widget1.setPalette(pal)
        widget2.setPalette(pal)
        
        self.testWidget.addWidget(widget1)
        self.testWidget.addWidget(widget2)
        
#        divider1 = Divider(Qt.Horizontal, 
#                               self.settingsBox,
#                               objectName='divider1', 
#                               thickness=3)
#        self.settingsLayout.addWidget(divider1)
        
        self.shapeBox = QComboBox(self.settingsBox, 
                                   objectName='shapeBox')
        self.settingsLayout.addRow('Frame &Shape', self.shapeBox)
        
        self.shadowBox = QComboBox(self.settingsBox, 
                                   objectName='shapeBox')
        self.settingsLayout.addRow('Frame S&hadow', self.shadowBox)
        
#        divider2 = Divider(Qt.Horizontal, 
#                               self.settingsBox,
#                               objectName='divider2', 
#                               thickness=3)
#        self.settingsLayout.addWidget(divider2)
        
        self.handleBox = QComboBox(self.settingsBox, 
                                   objectName='handleBox')
        self.settingsLayout.addRow('&Handle Style', self.handleBox)
        
        self.highlightBox = QComboBox(self.settingsBox, 
                                      objectName='highlightBox')
        self.settingsLayout.addRow('Ho&ver Highlight', self.highlightBox)
        
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
        
        self.populateComboBoxes()
        
        self.retranslateUi()
    
    def populateComboBoxes(self):
        self.shapeBox.addItem('No Frame', QFrame.NoFrame)
        self.shapeBox.addItem('Box', QFrame.Box)
        self.shapeBox.addItem('Panel', QFrame.Panel)
        self.shapeBox.addItem('Styled Panel', QFrame.StyledPanel)
        self.shapeBox.addItem('Windows Panel', QFrame.WinPanel)
        self.shapeBox.setCurrentIndex(3)
        
        self.shadowBox.addItem('Plain', QFrame.Plain)
        self.shadowBox.addItem('Raised', QFrame.Raised)
        self.shadowBox.addItem('Sunken', QFrame.Sunken)
        
        self.handleBox.addItem('Plain', Splitter.Plain)
        self.handleBox.addItem('Centered Dashes', Splitter.CenteredDashes)
        self.handleBox.addItem('Centered Dotted', Splitter.CenteredDotted)
        self.handleBox.addItem('Parallel Dotted', Splitter.ParallelDotted)
        self.handleBox.addItem('Parallel Line', Splitter.ParallelLine)
        self.handleBox.addItem('Parallel Grooved Line', Splitter.ParallelGroovedLine)
        
        self.highlightBox.addItem('None', Splitter.NoHighlight)
        self.highlightBox.addItem('Plain', Splitter.PlainHighlight)
        self.highlightBox.addItem('Raised', Splitter.RaisedHighlight)
        self.highlightBox.addItem('Local', Splitter.LocalHighlight)
        
    
    def retranslateUi(self):
        self.settingsLayout.labelForField(self.shapeBox).setText(self.trUtf8('Frame &Shape'))
        self.settingsLayout.labelForField(self.shadowBox).setText(self.trUtf8('Frame S&hadow'))
        self.settingsLayout.labelForField(self.handleBox).setText(self.trUtf8('&Handle Style'))
        self.settingsLayout.labelForField(self.highlightBox).setText(self.trUtf8('Ho&ver Highlight'))
        self.settingsLayout.labelForField(self.widthBox).setText(self.trUtf8('Handle &Width'))
        self.orientBox.setText(self.trUtf8('&Vertical Orientation'))
        self.opaqueResizeBox.setText(self.trUtf8('&Opaque Resize'))
        super().retranslateUi()
        
    def connectSignals(self):
        self.shapeBox.currentIndexChanged[int].connect(self.changeSplitterShape)
        self.shadowBox.currentIndexChanged[int].connect(self.changeSplitterShadow)
        self.handleBox.currentIndexChanged[int].connect(self.changeHandleStyle)
        self.highlightBox.currentIndexChanged[int].connect(self.changeHighlightStyle)
        self.widthBox.valueChanged[int].connect(self.testWidget.setHandleWidth)
        self.orientBox.toggled.connect(self.changeOrientation)
        self.opaqueResizeBox.toggled.connect(self.testWidget.setOpaqueResize)
        
        super().connectSignals()
    
    def changeSplitterShadow(self, idx):
        self.testWidget.setFrameShadow(self.shadowBox.itemData(idx))

    def changeSplitterShape(self, idx):
        self.testWidget.setFrameShape(self.shapeBox.itemData(idx))
        
    def changeHandleStyle(self, idx):
        self.testWidget.setHandleStyle(self.handleBox.itemData(idx))
    
    def changeHighlightStyle(self, idx):
        pass
    
    def changeOrientation(self, vertical = False):
        self.testWidget.setOrientation(Qt.Vertical if vertical else Qt.Horizontal)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
