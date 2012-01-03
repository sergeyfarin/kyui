from PyQt4.QtCore import Qt, pyqtProperty
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QLineEdit
from PyQt4.QtGui import QToolButton
from PyQt4.QtGui import QHBoxLayout
from PyQt4.QtGui import QIcon
from PyQt4.QtGui import QFileDialog

class PathLineEdit(QWidget):
    def __init__(self, *args, **kwargs):
        if len(args) == 2:
            parent = args[1]
            text = args[0]
        elif len(args) == 1:
            parent = args[0]
            text = kwargs.pop('text') if 'text' in kwargs else ''
        else:
            parent = kwargs.pop('parent', None)
            text = kwargs.pop('text') if 'text' in kwargs else ''
        super().__init__(parent, **kwargs)
        
        self.editor = QLineEdit(text, self)
        self.button = QToolButton(self, 
                                  text='...', 
                                  autoRaise=False, 
                                  clicked=self.onButtonClicked)
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(2)
        self.layout.addWidget(self.editor)
        self.layout.addWidget(self.button)
        
    def setButtonIcon(self, icon):
        self.button.setIcon(icon)
        
    def setButtonText(self, text):
        self.button.setText(text)
        
    def setCurrentPath(self, path):
        self.editor.setText(path)    
    
    def setToolButtonStyle(self, style):
        self.button.setToolButtonStyle(style)

    def getToolButtonStyle(self):       return self.button.toolButtonStyle()
    def getButtonIcon(self):                  return self.button.icon()
    def getButtonText(self):            return self.button.text()
    def getCurrentPath(self):           return self.editor.text()

    buttonIcon = pyqtProperty(QIcon, fget=getButtonIcon, fset=setButtonIcon)
    buttonText = pyqtProperty(str, fget=getButtonText, fset=setButtonText)
    currentPath = pyqtProperty(str, fget=getCurrentPath, fset=setCurrentPath)
    toolButtonStyle = pyqtProperty(Qt.ToolButtonStyle, 
                               fget=getToolButtonStyle, 
                               fset=setToolButtonStyle)
    
    def onButtonClicked(self):
        path = QFileDialog.getExistingDirectory(self, 'Select download folder', self.editor.text())
        if path:
            self.editor.setText(path)
