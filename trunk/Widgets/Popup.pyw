from PyQt4.QtCore import *
from PyQt4.QtGui import *




class GenericDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setObjectName('dialog')
        self.setWindowTitle('Sheet Test')
        self.resize(371, 151)
        self.setFont(QFont('Segoe UI', 9))
        
        self.__setupUi()
        
        self.buttonBox.accepted.connect(self.accept)
        
    def __setupUi(self):
        self.layout = QVBoxLayout(self)
        self.layout.setObjectName('layout')
        
        tb = KyToolButton
#        self.layout.addWidget(self.sheet)
        
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok, 
                                          Qt.Horizontal, self)
        self.layout.addWidget(self.buttonBox)
        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = GenericDialog()
    dialog.show()
    sys.exit(app.exec_())
