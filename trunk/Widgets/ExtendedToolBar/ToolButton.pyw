from PyQt4.QtCore import *
from PyQt4.QtGui import *

from PopupWidget import PopupWidget

PopupTypes = {'None' : 0,
              'QMenu' : 1, 
              'Widget' : 2}

class ToolButton(QToolButton):
    def __init__(self,
                 parent : QWidget = None, 
                 popupWidget : PopupWidget = None, 
                 defaultAction : QAction = None):
        super().__init__(parent)
        if defaultAction:
            self.setDefaultAction(defaultAction)
            if self.menu():
                self.__popupType = PopupTypes['QMenu']
        elif popupWidget:
            self.__popupType = PopupTypes['Widget']
            self.__popup = popupWidget
        else:
            self.__popup = None
    
    def showMenu(self):
        if self.__popupType == PopupTypes['QMenu']:
            super().showMenu()
        elif self.__popupType == PopupTypes['Widget']:
            if self.__popup.isVisible():
                self.__popup.hide()
            else:
                self.__popup.show()
                
#    def mousePressEvent(self, ev : QMouseEvent):
#        if ev.button() == Qt.LeftButton and self.__popupType == PopupTypes['Widget']:
#            self.showMenu()
#            super(QAbstractButton, self).mousePressEvent(ev)
#            ev.accept()
#        else:
#            super().mousePressEvent(ev)
        
    def setMenuWidget(self, widget : QWidget = None):
        if self.menu():
            super().setMenu(None)
        if widget:
            self.__popupType = PopupTypes['Widget']
            self.__popup = widget
        else:
            self.__popup = None
            self.__popupType = PopupTypes['None']
    
    def setMenu(self, menu : QMenu = None):
        super().setMenu(menu)
        self.__popup = None
        if menu:
            self.__popupType = PopupTypes['QMenu']
        else:
            self.__popupType = PopupTypes['None']

class GenericDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setObjectName('dialog')
        self.setWindowTitle('Test')
        
        self.__setupUi()
        
    def __setupUi(self):
        self.__layout = QVBoxLayout(self)
        self.__layout.setObjectName('layout')
        
        button = ToolButton(self)
        button.setText('Test Button')
#        button.setFixedSize(75, 23)
#        button.setPopupMode(QToolButton.MenuButtonPopup)
    
        w = PopupWidget(button)
        w.layout = QVBoxLayout(w)
        w.buttonBox = QDialogButtonBox(QDialogButtonBox.Close, 
                                           Qt.Horizontal, w)
        w.layout.addWidget(w.buttonBox)
        w.buttonBox.clicked.connect(w.hide)
        button.setMenuWidget(w)
        button.clicked.connect(button.showMenu)
        
        self.__layout.addWidget(button)
        
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok, 
                                          Qt.Horizontal, self)
        self.__layout.addWidget(self.buttonBox)
        self.buttonBox.accepted.connect(self.accept)
        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = GenericDialog()
    dialog.show()
    sys.exit(app.exec_())
