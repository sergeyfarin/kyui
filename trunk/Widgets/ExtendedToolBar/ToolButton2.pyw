from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ToolButton(QToolButton):
    def __init__(self, parent = None):
        super().__init__(parent)
        

#    def paintEvent(self, ev : QPaintEvent) -> None:
#        p = QStylePainter(self)
#        opt = QStyleOptionToolButton()
#        self.initStyleOption(opt)
#        p.drawComplexControl(QStyle.CC_ToolButton, opt)
        
#    def sizeHint(self) -> QSize:
#        w, h = 0, 0
#        opt = QStyleOptionToolButton()
#        self.initStyleOption(opt)
#
#        fm = self.fontMetrics()
#        if opt.toolButtonStyle != Qt.ToolButtonTextOnly and not opt.icon.isNull():
#            w = opt.iconSize.width()
#            h = opt.iconSize.height()
#
#        if opt.toolButtonStyle != Qt.ToolButtonIconOnly and opt.text:
#            textSize = fm.size(Qt.TextShowMnemonic, opt.text);
#            textSize.setWidth(textSize.width() + fm.width(' ')*2);
#            if opt.toolButtonStyle == Qt.ToolButtonTextUnderIcon:
#                h += 4 + textSize.height()
#                if textSize.width() > w:
#                    w = textSize.width()
#            elif opt.toolButtonStyle == Qt.ToolButtonTextBesideIcon:
#                w += 4 + textSize.width();
#                if textSize.height() > h:
#                    h = textSize.height();
#            else: # TextOnly
#                w = textSize.width()
#                h = textSize.height()
#
#        opt.rect.setSize(QSize(w, h)); # PM_MenuButtonIndicator depends on the height
#        if self.popupMode() == QToolButton.MenuButtonPopup:
#            if opt.toolButtonStyle == Qt.ToolButtonTextUnderIcon:
#                h += self.style().pixelMetric(QStyle.PM_MenuButtonIndicator, opt, self);
#            else:
#                w += self.style().pixelMetric(QStyle.PM_MenuButtonIndicator, opt, self);
#
#        sh = self.style().sizeFromContents(QStyle.CT_ToolButton, opt, QSize(w, h), self).expandedTo(QApplication.globalStrut());
#        return sh

#    def initStyleOption(self, opt):
#        super().initStyleOption(opt)
#        opt.orientation = Qt.Vertical
