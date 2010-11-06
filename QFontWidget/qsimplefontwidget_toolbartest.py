

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qsimplefontwidget import QSimpleFontWidget

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle(self.trUtf8("MainWindow Test"))
        self.setObjectName("mainWindow")
        self.resize(800, 600)
        self.setFont(QFont("Segoe Ui", 9))
        self.widget = QWidget(self)
        self.widget.setObjectName("widget")
        self.setCentralWidget(self.widget)
        
        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuFile.setTitle(self.trUtf8("File"))
        self.setMenuBar(self.menubar)
        
        self.actionExit = QAction(self)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setText(self.trUtf8("&Exit"))
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.actionExit.triggered.connect(self.close)
        
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        
        self.setupToolbars()
        
    def setupToolbars(self):
        self.toolBar = QToolBar(self)
        self.toolBar.setObjectName("toolBar")
        
        fontWidget = QSimpleFontWidget(self.font())
        fontWidget.showBoldButton(True)
        fontWidget.showItalicButton(True)
        fontWidget.showUnderlineButton(True)        
        self.actionFont = self.toolBar.addWidget(fontWidget)
        
        self.addToolBar(Qt.ToolBarArea(Qt.TopToolBarArea), self.toolBar)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

