#keypresser.py

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from catcher import KeyPressCatcher

import keypresser_rc

defaultToolTip = \
    "To set or change a shortcut's key combination, click inside the editor box\n" + \
    "and enter a new shortcut. The line editor will reflect the combination of\n" + \
    "keys as they are pressed."
defaultWhatsThis = \
"""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n<html><head><meta name="qrichtext" content="1" /><style type="text/css">\np, li { white-space: pre-wrap; }\n</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;">\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">Setting or changing a key combination:</span></p>\n<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;"></p>\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">Keys on a keyboard can be combined into </span><span style=" font-size:8pt; font-weight:600;">key combinations</span><span style=" font-size:8pt;"> (or key combos). These combinations are used to activate </span><span style=" font-size:8pt; font-weight:600;">shortcuts</span><span style=" font-size:8pt;">. Familiar examples of these are [Ctrl]+[C] to copy text and [Ctrl]+[P] to print a document. Sometimes shortcuts only use one key, such as [F1] for opening help. Typically such shortcuts use keys that will not display characters in order to avoid interfering with typing.</span></p>\n<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;"></p>\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">For purposes of making key combinations, there are three types of keys on a keyboard: </span><span style=" font-size:8pt; font-weight:600;">standard keys</span><span style=" font-size:8pt;">, </span><span style=" font-size:8pt; font-weight:600;">modifier keys</span><span style=" font-size:8pt;">, and </span><span style=" font-size:8pt; font-weight:600;">system keys</span><span style=" font-size:8pt;">. Modifiers are typically [Ctrl], [Shift], [WinKey] (the Windows key), and [Alt]. These four can be used in any combination with a standard key as a key combination.</span></p>\n<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;"></p>\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">System keys are typically not usable for key combinations. These are, normally, [Caps Lock], [Num Lock], [Scroll Lock], and sometimes [Esc], [Tab], [PrtScr], and [Pause/Break]. Standard keys are essentially any other key on the keyboard. Examples are: [G], [7], [Backspace], [F7], [Insert], and the arrow keys.</span></p>\n<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;"></p>\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">Certain key combinations are exclusively reserved by the system or cannot be changed. [Ctrl]+[C] should </span><span style=" font-size:8pt; font-style:italic;">always</span><span style=" font-size:8pt;"> copy, regardless of the application you are using, if the application allows copying. If the application can print, [Ctrl]+[P] should always be the shortcut used for this. The [F1] is the normal key to bring up help options. System shortcut examples are [Alt]+[Tab] to switch applications and [Alt]+[F4] to quit the current application.</span></p>\n<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;"></p>\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">To set a key combination, click inside the editor line and hold any combination of modifiers down and press a standard key. The editor line will update to show the key combination you've set. For example, holding [Ctrl], [Shift] and pressing the [F7] key, then releasing all three will set this as a key combination. [Ctrl], [Shift], [F7], and [G] and will not work, as only one standard key can be used in a key combination, and [F7] and [G] are both standard keys.</span></p>\n<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;"></p>\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">Shortcuts are always written (typed) with the modifier keys first, as they are always pressed first: [Ctrl]+[Shift]+[F7], for example.</span></p>\n<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;"></p>\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">Pressing the Clear button will remove the key combination for the current shortcut, the Reset button will reset the shortcut to its default key combination, OK will save your new shortcut key combination and close the dialog, and Cancel will close the dialog without saving.</span></p></body></html>"""

class KeyComboDialog(QDialog):
    debugEvent = pyqtSignal('QString')
    
    def __init__(self, parent = None, keycombo = ''):
        super().__init__(parent)
        
        self.setupUi()
        self.defaultKeyCombo = keycombo
        
        self.catcher.setText(keycombo)
        self.setWindowTitle('Shortcut Editor')
        self.catcherLabel.setText('Enter a new key combination:')
        self.setWhatsThis(defaultWhatsThis)
        
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        
    def setupUi(self):
        self.setObjectName('keyPresserDlg')
        self.resize(360, 90)
        self.setModal(True)
        
        self.layout = QVBoxLayout(self)
        self.layout.setObjectName('layout')
        
        self.catcherLabel = QLabel(self)
        self.catcherLabel.setObjectName('catcherLabel')
        self.catcherLabel.setToolTip(defaultToolTip)
        self.layout.addWidget(self.catcherLabel)
        
        self.catcherWidget = QWidget(self)
        self.catcherWidget.setObjectName('catcherWidget')
        self.layout.addWidget(self.catcherWidget)
        
        self.catcherLayout = QHBoxLayout(self.catcherWidget)
        self.catcherLayout.setObjectName('catcherLayout')
        self.catcherLayout.setSpacing(0)
        
        self.catcher = KeyPressCatcher(self.catcherWidget)
        self.catcher.setObjectName('catcher')
        self.catcher.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.catcher.setToolTip(defaultToolTip)
        self.catcherLayout.addWidget(self.catcher)
        
        self.clearButton = QPushButton(self.catcherWidget)
        self.clearButton.setObjectName('clearButton')
        self.clearButton.setIcon(QIcon(QPixmap(':keypresser/erase.png')))
        self.clearButton.setToolTip('Clear the current key combination')
        self.catcherLayout.addWidget(self.clearButton)
        
        self.catcherLabel.setBuddy(self.catcher)
        
        self.layout.addSpacing(20)
        
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok|QDialogButtonBox.Reset)
        self.buttonBox.setObjectName('buttonBox')
        self.layout.addWidget(self.buttonBox)
        
        resetButton = self.buttonBox.button(QDialogButtonBox.Reset)
        resetButton.setToolTip('Reset the current key combination to its previous state.')
        
        self.setTabOrder(self.buttonBox, self.catcher)
        self.setTabOrder(self.catcher, self.clearButton)
        
        resetButton.clicked.connect(self.onReset)
        self.clearButton.clicked.connect(self.catcher.clear)
        
    def reject(self):
        self.catcher.setText(self.defaultKeyCombo)
        super().reject()
    
    def onReset(self):
        self.catcher.setText(self.defaultKeyCombo)
        
    def keyCombo(self):
        return self.catcher.text()
        
    def setText(self, text):
        self.catcherLabel.setText(text)
        
    def setKeyCombo(self, keycombo):
        self.catcher.setText(keycombo)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = KeyComboDialog()
    dialog.show()
    sys.exit(app.exec_())
