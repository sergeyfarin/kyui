#UTF-8
#template_test.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

from Widgets.colorslider import ColorSlider
from Widgets.debugbox import DebugBox

class Dialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setObjectName('dialog')
        
        self._color = QColor(0, 0, 0)
        
        self.setupUi()
        self.connectSignals()
        
    def setupUi(self):
        self.layout = QVBoxLayout(self)
        self.layout.setObjectName('layout')
        
        self.tabWidget = QTabWidget(self)
        self.tabWidget.setObjectName('tabWidget')
        
        self.setupSliders()

        self.layout.addWidget(self.tabWidget)
        
        self.settingsBox = QGroupBox(self)
        self.settingsBox.setObjectName('settingsBox')
        self.settingsLayout = QFormLayout(self.settingsBox)
        self.settingsLayout.setObjectName('settingsLayout')
        
        self.orientBox = QCheckBox(self)
        self.orientBox.setObjectName('orientBox')
        self.settingsLayout.addWidget(self.orientBox)
        
        self.dynamicBox = QCheckBox(self)
        self.dynamicBox.setObjectName('dynamicBox')
        self.dynamicBox.setChecked(True)
        self.settingsLayout.addWidget(self.dynamicBox)
        
        self.layout.addWidget(self.settingsBox)
        
        self.debugBox = DebugBox(self)
        self.debugBox.setObjectName('debugBox')
        self.layout.addWidget(self.debugBox)
        qInstallMsgHandler(self.debugBox.postMsg)
        
        self.closeButton = QPushButton(self)
        self.closeButton.setObjectName('closeButton')
        self.closeButton.setDefault(True)
        self.layout.addWidget(self.closeButton)
        self.layout.setAlignment(self.closeButton, 
                                 Qt.AlignRight | Qt.AlignBottom)
        
        self.retranslateUi()
        
    def setupSliders(self):
        self.rgbSliders = []
        self.rgbTab = QWidget(self.tabWidget)
        self.rgbTab.setObjectName('rgbTab')
        self.rgbLayout = QBoxLayout(QBoxLayout.TopToBottom, self.rgbTab)
        self.rgbLayout.setObjectName('rgbTab')
        
        self.rgbSlider0 = ColorSlider(QColor.Rgb, 0, Qt.Horizontal, self.rgbTab)
        self.rgbSlider0.setObjectName('rgbSlider0')
        self.rgbLayout.addWidget(self.rgbSlider0)
        self.rgbSliders.append(self.rgbSlider0)
        
        self.rgbSlider1 = ColorSlider(QColor.Rgb, 1, Qt.Horizontal, self.rgbTab)
        self.rgbSlider1.setObjectName('rgbSlider1')
        self.rgbLayout.addWidget(self.rgbSlider1)
        self.rgbSliders.append(self.rgbSlider1)
        
        self.rgbSlider2 = ColorSlider(QColor.Rgb, 2, Qt.Horizontal, self.rgbTab)
        self.rgbSlider2.setObjectName('rgbSlider2')
        self.rgbLayout.addWidget(self.rgbSlider2)
        self.rgbSliders.append(self.rgbSlider2)
        self.tabWidget.addTab(self.rgbTab, '&RGB')
        
        self.hslSliders = []
        self.hslTab = QWidget(self.tabWidget)
        self.hslTab.setObjectName('hslTab')
        self.hslLayout = QBoxLayout(QBoxLayout.TopToBottom, self.hslTab)
        self.hslLayout.setObjectName('hslLayout')
        
        self.hslSlider0 = ColorSlider(QColor.Hsl, 0, Qt.Horizontal, self.hslTab)
        self.hslSlider0.setObjectName('hslSlider0')
        self.hslLayout.addWidget(self.hslSlider0)
        self.hslSliders.append(self.hslSlider0)
        
        self.hslSlider1 = ColorSlider(QColor.Hsl, 1, Qt.Horizontal, self.hslTab)
        self.hslSlider1.setObjectName('hslSlider1')
        self.hslLayout.addWidget(self.hslSlider1)
        self.hslSliders.append(self.hslSlider1)
        
        self.hslSlider2 = ColorSlider(QColor.Hsl, 2, Qt.Horizontal, self.hslTab)
        self.hslSlider2.setObjectName('hslSlider2')
        self.hslLayout.addWidget(self.hslSlider2)
        self.hslSliders.append(self.hslSlider2)
        self.tabWidget.addTab(self.hslTab, 'HS&L')
        
        self.hsvSliders = []
        self.hsvTab = QWidget(self.tabWidget)
        self.hsvTab.setObjectName('hsvTab')
        self.hsvLayout = QBoxLayout(QBoxLayout.TopToBottom, self.hsvTab)
        self.hsvLayout.setObjectName('hsvLayout')
        
        self.hsvSlider0 = ColorSlider(QColor.Hsv, 0, Qt.Horizontal, self.hsvTab)
        self.hsvSlider0.setObjectName('hsvSlider0')
        self.hsvLayout.addWidget(self.hsvSlider0)
        self.hsvSliders.append(self.hsvSlider0)
        
        self.hsvSlider1 = ColorSlider(QColor.Hsv, 1, Qt.Horizontal, self.hsvTab)
        self.hsvSlider1.setObjectName('hsvSlider1')
        self.hsvLayout.addWidget(self.hsvSlider1)
        self.hsvSliders.append(self.hsvSlider1)
        
        self.hsvSlider2 = ColorSlider(QColor.Hsv, 2, Qt.Horizontal, self.hsvTab)
        self.hsvSlider2.setObjectName('hsvSlider2')
        self.hsvLayout.addWidget(self.hsvSlider2)
        self.hsvSliders.append(self.hsvSlider2)
        
        self.tabWidget.addTab(self.hsvTab, 'HS&V')
        
        self.tabWidget.setTabEnabled(1, False)
        self.tabWidget.setTabEnabled(2, False)
        
    def retranslateUi(self):
        self.setWindowTitle(self.trUtf8('Test Dialog'))
        self.tabWidget.setTabText(0, self.trUtf8('&RGB'))
        self.tabWidget.setTabText(1, self.trUtf8('HS&L'))
        self.tabWidget.setTabText(2, self.trUtf8('HS&V'))
        self.settingsBox.setTitle(self.trUtf8('&Options'))
        self.orientBox.setText('Ver&tical Slider')
        self.dynamicBox.setText('&Dynamic Gradients')
        self.closeButton.setText(self.trUtf8('&Close'))
        
    def connectSignals(self):
        self.orientBox.toggled.connect(self.onOrientationChanged)
        self.dynamicBox.toggled.connect(self.setDynamic)
        self.closeButton.clicked.connect(self.close)
        self.setDynamic(True)
        for slider in iter(self.rgbSliders):
            slider.valueChanged.connect(self.sliderValueChanged)
        for slider in iter(self.hslSliders):
            slider.valueChanged.connect(self.sliderValueChanged)
        for slider in iter(self.hsvSliders):
            slider.valueChanged.connect(self.sliderValueChanged)
            
    def onOrientationChanged(self):
        if self.orientBox.isChecked():
            direction = QBoxLayout.LeftToRight
            orient = Qt.Vertical
        else:
            direction = QBoxLayout.TopToBottom
            orient = Qt.Horizontal
        self.rgbLayout.setDirection(direction)
        self.hslLayout.setDirection(direction)
        self.hsvLayout.setDirection(direction)
        for slider in iter(self.rgbSliders):
            slider.setOrientation(orient)
        for slider in iter(self.hslSliders):
            slider.setOrientation(orient)
        for slider in iter(self.hsvSliders):
            slider.setOrientation(orient)
        
    def setDynamic(self, dynamic):
        self.__dynamic = dynamic
        
    def sliderValueChanged(self, value):
        if not self.__dynamic:
            return
        spec = self.sender().spec()
        channel = self.sender().colorChannel()
        if spec == QColor.Rgb:
            for slider in iter(self.rgbSliders):
                if slider == self.sender():
                    continue
                slider.setChannelValue(channel, value)
        elif spec == QColor.Hsl:
            for slider in iter(self.hslSliders):
                if slider == self.sender():
                    continue
                slider.setChannelValue(channel, value)
        elif spec == QColor.Hsv:
            for slider in iter(self.hsvSliders):
                if slider == self.sender():
                    continue
                slider.setChannelValue(channel, value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
