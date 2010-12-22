from PyQt4.QtCore import *
from PyQt4.QtGui import *

from WidgetViewer import KyMainWindow
#from MainWindow import KyMainWindow
from Style.StyleFactory import KyStyleFactory

orgDomain = 'white-walls.net'
orgName = 'White-Walls'
appName = 'Kyui'

class Application(QApplication):
    def __init__(self):
        QApplication.__init__(self, sys.argv)
        self.setFont(QFont('Segoe UI', 9, QFont.Normal, False))
        self.setOrganizationDomain(orgDomain)
        self.setOrganizationName(orgName)
        self.setApplicationName(appName)
        self.settings = QSettings(QSettings.IniFormat, QSettings.UserScope, orgName, appName, self)
        self.setStyle(KyStyleFactory.create('Plastique'))
        self.ui = KyMainWindow()
#        self.ui.connect(self, SIGNAL('aboutToQuit()'), self.writeSettings)
        self.ui.show()

    def writeSettings(self):
        self.settings.clear()
        self.ui.saveSettings(self.settings)
        self.settings.sync()

if __name__ == '__main__':
    import sys
    app = Application()
    sys.exit(app.exec_())
