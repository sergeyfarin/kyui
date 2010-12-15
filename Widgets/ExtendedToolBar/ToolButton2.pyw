from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ToolButton(QToolButton):
    def __init__(self, 
                 parent : QWidget = None,
                 action : QAction = None,
                 autoraise : bool = False,
                 mode : QToolButton.ToolButtonPopupMode = None,   #PopupMode
                 name : str = None,                     #ObjectName
                 size : QSize = None,                   #IconSize
                 style : Qt.ToolButtonStyle = None):
        super().__init__(parent)
        if action: self.setDefaultAction(action)
        if autoraise: self.setAutoRaise(autoraise)
        if mode: self.setPopupMode(mode)
        if name: self.setObjectName(name)
        if size: self.setIconSize(size)
        if style: self.setToolButtonStyle(style)

#    def paintEvent(self, ev : QPaintEvent) -> None:
#        p = QStylePainter(self)
#        opt = QStyleOptionToolButton()
#        self.initStyleOption(opt)
#        p.drawComplexControl(QStyle.CC_ToolButton, opt)
        
    def sizeHint(self) -> QSize:
        opt = QStyleOptionToolButton()
        self.initStyleOption(opt)
        
        if (opt.toolButtonStyle != Qt.ToolButtonTextUnderIcon or not (opt.features
                & (QStyleOptionToolButton.Menu | QStyleOptionToolButton.HasMenu))):
            return super().sizeHint()
        
        w = 0
        fm = self.fontMetrics()
        if not opt.icon.isNull():
            w = opt.iconSize.width() + 6

        if opt.text:
            textSize = fm.size(Qt.TextShowMnemonic, opt.text)
            textSize.setWidth(textSize.width() + fm.width('  '))
            if textSize.width() > w:
                w = textSize.width()

        sh = self.style().sizeFromContents(QStyle.CT_ToolButton, opt, QSize(w, 66), self).expandedTo(QApplication.globalStrut());
        return sh

    def initStyleOption(self, opt):
        super().initStyleOption(opt)
#        if (opt.toolButtonStyle == Qt.ToolButtonTextUnderIcon and (opt.features
#                & (QStyleOptionToolButton.MenuButtonPopup | QStyleOptionToolButton.PopupDelay))):
#            opt.state |= QStyle.State_Item
#        if opt.iconSize.width() > 36:
#            opt.iconSize.setWidth(32)
#        if opt.iconSize.height() > 36:
#            opt.iconSize.setHeight(36)
