#UTF-8
#buttonbar_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

from Widgets.tabbar2 import Tab
from Widgets.debugbox import DebugBox

class Dialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setObjectName('dialog')
        
        self.setupUi()
        self.connectSignals()
        
        version = QSysInfo.WindowsVersion
        if version & QSysInfo.WV_NT_based:
            if version == QSysInfo.WV_WINDOWS7 or testWin == QSysInfo.WV_VISTA:
                style = 'WindowsVista'
            elif version == QSysInfo.WV_XP or QSysInfo.WV_2003:
                style = 'WindowsXP'
            else:
                style = 'Windows'
        else:
            style = 'Plastique'
        self.styleBox.setCurrentIndex(self.styleBox.findText(style, Qt.MatchFixedString))
        
    def setupUi(self):
        self.layout = QVBoxLayout(self)
        self.layout.setObjectName('layout')
        
        self.testWidget = Tab(QIcon(), 'Test', self)
        self.testWidget.setObjectName('testWidget')
        
        self.layout.addWidget(self.testWidget)
        
        self.settingsBox = QGroupBox(self)
        self.settingsBox.setObjectName('settingsBox')
        self.settingsLayout = QFormLayout(self.settingsBox)
        self.settingsLayout.setObjectName('settingsLayout')
        
        self.styleLabel = QLabel(self.settingsBox)
        self.styleLabel.setObjectName('styleLabel')
        self.styleBox = QComboBox(self.settingsBox)
        self.styleBox.setObjectName('styleBox')
        
        self.styleBox.addItems(QStyleFactory.keys())
        self.styleLabel.setBuddy(self.styleBox)
        
        self.settingsLayout.addRow(self.styleLabel, self.styleBox)
        
        self.positionLabel = QLabel(self.settingsBox)
        self.positionLabel.setObjectName('positionLabel')
        self.positionBox = QComboBox(self.settingsBox)
        self.positionBox.setObjectName('positionBox')
        
        self.positionBox.addItem('Top', QTabBar.RoundedNorth)
        self.positionBox.addItem('Left', QTabBar.RoundedWest)
        self.positionBox.addItem('Bottom', QTabBar.RoundedSouth)
        self.positionBox.addItem('Right', QTabBar.RoundedEast)
        
        self.positionLabel.setBuddy(self.positionBox)
        self.settingsLayout.addRow(self.positionLabel, self.positionBox)
        
        self.elideLabel = QLabel(self.settingsBox)
        self.elideLabel.setObjectName('elideLabel')
        self.elideBox = QComboBox(self.settingsBox)
        self.elideBox.setObjectName('elideBox')
        
        self.elideBox.addItem('Elide Left', Qt.ElideLeft)
        self.elideBox.addItem('Elide Middle', Qt.ElideMiddle)
        self.elideBox.addItem('Elide Right', Qt.ElideRight)
        self.elideBox.addItem('Elide Left', Qt.ElideNone)
        
        self.elideLabel.setBuddy(self.elideBox)
        self.settingsLayout.addRow(self.elideLabel, self.elideBox)
        
        self.selectLabel = QLabel(self.settingsBox)
        self.selectLabel.setObjectName('selectLabel')
        self.selectBox = QComboBox(self.settingsBox)
        self.selectBox.setObjectName('selectBox')
        
        self.selectBox.addItem('Select Left', QTabBar.SelectLeftTab)
        self.selectBox.addItem('Select Right', QTabBar.SelectRightTab)
        self.selectBox.addItem('Select Previous', QTabBar.SelectPreviousTab)
        
        self.selectLabel.setBuddy(self.selectBox)
        self.settingsLayout.addRow(self.selectLabel, self.selectBox)
        
        self.iconSizeLabel = QLabel(self.settingsBox)
        self.iconSizeLabel.setObjectName('iconSizeLabel')
        self.iconSizeBox = QComboBox(self.settingsBox)
        self.iconSizeBox.setObjectName('iconSizeBox')
        
        self.iconSizeBox.addItem('16 x 16', QSize(16, 16))
        self.iconSizeBox.addItem('22 x 22', QSize(22, 22))
        self.iconSizeBox.addItem('24 x 24', QSize(24, 24))
        self.iconSizeBox.addItem('32 x 32', QSize(32, 32))
        
        self.iconSizeLabel.setBuddy(self.iconSizeBox)
        self.settingsLayout.addRow(self.iconSizeLabel, self.iconSizeBox)
        
        self.docModeBox = QCheckBox(self.settingsBox)
        self.docModeBox.setObjectName('docModeBox')
        self.settingsLayout.addWidget(self.docModeBox)
        
        self.closableBox = QCheckBox(self.settingsBox)
        self.closableBox.setObjectName('closableBox')
        self.settingsLayout.addWidget(self.closableBox)
        
        self.movableBox = QCheckBox(self.settingsBox)
        self.movableBox.setObjectName('movableBox')
        self.settingsLayout.addWidget(self.movableBox)
        
        self.expandingBox = QCheckBox(self.settingsBox)
        self.expandingBox.setObjectName('expandingBox')
        self.settingsLayout.addWidget(self.expandingBox)
        
        self.useScrollBox = QCheckBox(self.settingsBox)
        self.useScrollBox.setObjectName('useScrollBox')
        self.useScrollBox.setChecked(True)
        self.settingsLayout.addWidget(self.useScrollBox)
        
        self.drawBaseBox = QCheckBox(self.settingsBox)
        self.drawBaseBox.setObjectName('drawBaseBox')
        self.drawBaseBox.setChecked(True)
        self.settingsLayout.addWidget(self.drawBaseBox)
        
        self.layout.addWidget(self.settingsBox)
        
        self.debugBox = DebugBox(self)
        self.debugBox.setObjectName('debugBox')
        qInstallMsgHandler(self.debugBox.postMsg)
        self.layout.addWidget(self.debugBox)
        
        self.closeButton = QPushButton(self)
        self.closeButton.setObjectName('closeButton')
        self.closeButton.setDefault(True)
        self.layout.addWidget(self.closeButton)
        self.layout.setAlignment(self.closeButton, 
                                 Qt.AlignRight | Qt.AlignBottom)
        
        self.retranslateUi()
        
    def retranslateUi(self):
        self.setWindowTitle(self.trUtf8('Test Dialog'))
        self.settingsBox.setTitle(self.trUtf8('Options'))
        self.styleLabel.setText(self.trUtf8('St&yle'))
        self.positionLabel.setText(self.trUtf8('&Position'))
        self.positionBox.setItemText(0, self.trUtf8('Top'))
        self.positionBox.setItemText(1, self.trUtf8('Left'))
        self.positionBox.setItemText(2, self.trUtf8('Bottom'))
        self.positionBox.setItemText(3, self.trUtf8('Right'))
        self.elideLabel.setText(self.trUtf8('&Text Elide Mode'))
        self.elideBox.setItemText(0, self.trUtf8('Elide Left'))
        self.elideBox.setItemText(1, self.trUtf8('Elide Middle'))
        self.elideBox.setItemText(2, self.trUtf8('Elide Right'))
        self.elideBox.setItemText(3, self.trUtf8('Elide None'))
        self.selectLabel.setText(self.trUtf8('&Selection Behavior'))
        self.selectBox.setItemText(0, self.trUtf8('Select Left'))
        self.selectBox.setItemText(1, self.trUtf8('Select Right'))
        self.selectBox.setItemText(2, self.trUtf8('Select Previous'))
        self.iconSizeLabel.setText(self.trUtf8('&Icon Size'))
        self.iconSizeBox.setItemText(0, self.trUtf8('16 x 16'))
        self.iconSizeBox.setItemText(1, self.trUtf8('22 x 22'))
        self.iconSizeBox.setItemText(2, self.trUtf8('24 x 24'))
        self.iconSizeBox.setItemText(3, self.trUtf8('32 x 32'))
        self.docModeBox.setText(self.trUtf8('&Document Mode'))
        self.closableBox.setText(self.trUtf8('C&losable Tabs'))
        self.movableBox.setText(self.trUtf8('&Movable Tabs'))
        self.expandingBox.setText(self.trUtf8('&Expanding Tabs'))
        self.useScrollBox.setText(self.trUtf8('&Use Scroll Buttons'))
        self.drawBaseBox.setText(self.trUtf8('Draw TabBar &Base'))
        self.closeButton.setText(self.trUtf8('&Close'))
    
    def connectSignals(self):
        self.styleBox.currentIndexChanged[str].connect(self.changeStyle)
        self.positionBox.currentIndexChanged[int].connect(self.changeShape)
        self.elideBox.currentIndexChanged[int].connect(self.changeElideMode)
        self.selectBox.currentIndexChanged[int].connect(self.changeSelectionBehavior)
        self.iconSizeBox.currentIndexChanged[int].connect(self.changeIconSize)
        self.docModeBox.toggled.connect(self.documentModeToggled)
        self.closableBox.toggled.connect(self.closableToggled)
        self.movableBox.toggled.connect(self.movableToggled)
        self.expandingBox.toggled.connect(self.expandingToggled)
        self.useScrollBox.toggled.connect(self.useScrollButtonsToggled)
        self.drawBaseBox.toggled.connect(self.drawBaseToggled)
        self.closeButton.clicked.connect(self.close)

    def changeStyle(self, style : str):
        qApp.setStyle(QStyleFactory.create(style))

    def changeShape(self, index : int):
        self.testWidget.setShape(self.positionBox.itemData(index))
        
    def changeElideMode(self, index : int):
        self.testWidget.setElideMode(self.elideBox.itemData(index))
        
    def changeSelectionBehavior(self, index : int):
        self.testWidget.setSelectionBehaviorOnRemove(self.selectBox.itemData(index))
        
    def changeIconSize(self, index : int):
        self.testWidget.setIconSize(self.iconSizeBox.itemData(index))
        
    def documentModeToggled(self, enabled : bool):
        self.testWidget.setDocumentMode(enabled)
        
    def closableToggled(self, enabled : bool):
        self.testWidget.setTabsClosable(enabled)
        
    def movableToggled(self, enabled : bool):
        self.testWidget.setMovable(enabled)
        
    def expandingToggled(self, enabled : bool):
        self.testWidget.setExpanding(enabled)
        
    def useScrollButtonsToggled(self, enabled : bool):
        self.testWidget.setUsesScrollButtons(enabled)
        
    def drawBaseToggled(self, enabled : bool):
        self.testWidget.setDrawBase(enabled)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
