#UTF-8
#splitter_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

from Widgets.splitter import Splitter
from Widgets.splitter import drawCenteredDashedHandle
from Widgets.splitter import drawCenteredDottedHandle
from Widgets.splitter import drawParalellLineHandle
from Widgets.splitter import drawParallelGroovedLineHandle
from Widgets.separator import Separator

#from Widgets.util import QTypeToString

from template_test import TemplateDialog

class Dialog(TemplateDialog):
    def __init__(self, parent : QWidget = None):
        super().__init__(parent)
        self.setupUi()
        self.connectSignals()
    
    def setupUi(self):
        super().setupUi()
        
        self.testWidget = Splitter(parent=self, 
                                   orientation=Qt.Horizontal, 
                                   objectName='testWidget', 
                                   gripPainter=None, 
                                   hoverHint=True)
        self.testWidget.setFixedSize(QSize(200, 100))
        self.layout.insertWidget(0, self.testWidget)
        
        #populate the splitter
        widget1 = QFrame(parent=self.testWidget, 
                         objectName='widget1', 
                         frameShape=QFrame.StyledPanel, 
                         frameShadow=QFrame.Sunken, 
                         autoFillBackground = True)
        widget2 = QFrame(parent=self.testWidget, 
                         objectName='widget1', 
                         frameShape=QFrame.StyledPanel, 
                         frameShadow=QFrame.Sunken, 
                         autoFillBackground = True)
        #set the widget backgrounds to white
        pal = widget1.palette()
        pal.setColor(QPalette.Window, QColor(Qt.white))
        widget1.setPalette(pal)
        widget2.setPalette(pal)
        
        self.testWidget.addWidget(widget1)
        self.testWidget.addWidget(widget2)
        
        
        #populate the settings box
        sep1 = Separator(Qt.Horizontal, 
                         self.settingsBox,
                         objectName='separator1')
        
        self.shapeBox = QComboBox(self.settingsBox, 
                                   objectName='shapeBox')
        self.shadowBox = QComboBox(self.settingsBox, 
                                   objectName='shapeBox')
        self.marginBox = QCheckBox(self.settingsBox, 
                                   objectName='marginBox', 
                                   checked=False)
        
        sep2 = Separator(Qt.Horizontal, 
                         self.settingsBox,
                         objectName='divider2')
        
        self.handleBox = QComboBox(self.settingsBox, 
                                   objectName='handleBox')
        self.highlightBox = QCheckBox(self.settingsBox, 
                                      objectName='highlightBox', 
                                      checked=True)
        self.widthBox = QSpinBox(self.settingsBox,
                                 objectName='widthBox', 
                                 minimum = 2, 
                                 maximum = 20, 
                                 value = self.testWidget.handleWidth())
        self.orientBox = QCheckBox(self.settingsBox, 
                                   objectName='orientBox')
        self.opaqueResizeBox = QCheckBox(self.settingsBox, 
                                         objectName='opaqueResizeBox', 
                                         checked=True)
        
        self.settingsLayout.addWidget(sep1)
        self.settingsLayout.addRow('Frame &Shape', self.shapeBox)
        self.settingsLayout.addRow('Frame S&hadow', self.shadowBox)
        self.settingsLayout.addWidget(self.marginBox)
        self.settingsLayout.addWidget(sep2)
        self.settingsLayout.addRow('&Handle Style', self.handleBox)
        self.settingsLayout.addRow('Handle &Width', self.widthBox)
        self.settingsLayout.addWidget(self.highlightBox)
        
        self.settingsLayout.addWidget(self.orientBox)
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
        self.shadowBox.setCurrentIndex(2)
        
        self.handleBox.addItem('Plain', None)
        self.handleBox.addItem('Centered Dashes', drawCenteredDashedHandle)
        self.handleBox.addItem('Centered Dotted', drawCenteredDottedHandle)
        self.handleBox.addItem('Parallel Line', drawParalellLineHandle)
        self.handleBox.addItem('Parallel Grooved Line', drawParallelGroovedLineHandle)
    
    def retranslateUi(self):
        super().retranslateUi()
        
        self.setWindowTitle('Splitter & SplitterHandle Test')
        self.settingsLayout.labelForField(self.shapeBox).setText(self.trUtf8('Frame &Shape'))
        self.settingsLayout.labelForField(self.shadowBox).setText(self.trUtf8('Frame S&hadow'))
        self.marginBox.setText(self.trUtf8('Pad Contents &Margins'))
        
        self.settingsLayout.labelForField(self.handleBox).setText(self.trUtf8('Handle &Grip'))
        self.highlightBox.setText(self.trUtf8('Show ho&ver hint'))
        self.settingsLayout.labelForField(self.widthBox).setText(self.trUtf8('Handle &Width'))
        self.orientBox.setText(self.trUtf8('Vertical &Orientation'))
        self.opaqueResizeBox.setText(self.trUtf8('&Opaque Resize'))
        
        
        
    def connectSignals(self):
        super().connectSignals()
        
        self.shapeBox.currentIndexChanged[int].connect(self.changeSplitterShape)
        self.shadowBox.currentIndexChanged[int].connect(self.changeSplitterShadow)
        self.marginBox.toggled.connect(self.changeMargins)
        
        self.handleBox.currentIndexChanged[int].connect(self.changeGripPainter)
        self.highlightBox.toggled.connect(self.testWidget.setHoverHint)
        self.widthBox.valueChanged[int].connect(self.testWidget.setHandleWidth)
        self.orientBox.toggled.connect(self.changeOrientation)
        self.opaqueResizeBox.toggled.connect(self.testWidget.setOpaqueResize)
    
    def changeSplitterShadow(self, idx):
        for widget in self.testWidget.widgets():
            widget.setFrameShadow(self.shadowBox.itemData(idx))

    def changeSplitterShape(self, idx):
        for widget in self.testWidget.widgets():
            widget.setFrameShape(self.shapeBox.itemData(idx))
        
    def changeGripPainter(self, idx):
        self.testWidget.setGripPainter(self.handleBox.itemData(idx))
    
    def changeHighlightStyle(self, idx):
        pass
    
    def changeMargins(self, toggled):
        if toggled:
            for widget in self.testWidget.widgets():
                widget.setContentsMargins(2, 2, 2, 2)
        else:
            for widget in self.testWidget.widgets():
                widget.setContentsMargins(1, 1, 1, 1)
    
    def changeOrientation(self, vertical = False):
        self.testWidget.setOrientation(Qt.Vertical if vertical else Qt.Horizontal)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
