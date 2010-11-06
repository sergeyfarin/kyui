#!/usr/bin/env python

"""PyQt4 port of the dialogs/extension example from Qt v4.x"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class FindDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        label = QLabel("Find &what:")
        lineEdit = QLineEdit()
        label.setBuddy(lineEdit)

        caseCheckBox = QCheckBox("Match &case")
        fromStartCheckBox = QCheckBox("Search from &start")
        fromStartCheckBox.setChecked(True)

        moreButton = QPushButton("&More")
        moreButton.setCheckable(True)
        moreButton.setAutoDefault(False)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel, 
                                     Qt.Vertical, 
                                     self)
        buttonBox.addButton(moreButton, QDialogButtonBox.ActionRole)

        extension = QWidget(self)

        wholeWordsCheckBox = QCheckBox("&Whole words", extension)
        backwardCheckBox = QCheckBox("Search &backward", extension)
        searchSelectionCheckBox = QCheckBox("Search se&lection", extension)

        moreButton.toggled.connect(extension.setVisible)

        extensionLayout = QVBoxLayout()
        extensionLayout.setMargin(0)
        extensionLayout.addWidget(wholeWordsCheckBox)
        extensionLayout.addWidget(backwardCheckBox)
        extensionLayout.addWidget(searchSelectionCheckBox)
        extension.setLayout(extensionLayout)
        
        topLeftLayout = QHBoxLayout()
        topLeftLayout.addWidget(label)
        topLeftLayout.addWidget(lineEdit)

        leftLayout = QVBoxLayout()
        leftLayout.addLayout(topLeftLayout)
        leftLayout.addWidget(caseCheckBox)
        leftLayout.addWidget(fromStartCheckBox)
        leftLayout.addStretch(1)

        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(leftLayout, 0, 0)
        mainLayout.addWidget(buttonBox, 0, 1)
        mainLayout.addWidget(extension, 1, 0, 1, 2)
        self.setLayout(mainLayout)

        self.setWindowTitle("Extension")
        extension.hide()


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    dialog = FindDialog()
    sys.exit(dialog.exec_())
