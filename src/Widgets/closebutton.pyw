from PyQt4.QtCore import Qt, QSize, QEvent
from PyQt4.QtGui import QAbstractButton, QTabBar, QWidget
from PyQt4.QtGui import QStyle, QStyleOption
from PyQt4.QtGui import QPainter

class CloseButton(QAbstractButton):
    def __init__(self, parent : QWidget):
        super().__init__(parent)
        self.setFocusPolicy(Qt.NoFocus)
        self.setCursor(Qt.ArrowCursor)
        self.setToolTip(self.trUtf8("Close Tab"))
        self.resize(self.sizeHint())

    def sizeHint(self) -> QSize:
        self.ensurePolished();
        width = self.style().pixelMetric(QStyle.PM_TabCloseIndicatorWidth, None, self)
        height = self.style().pixelMetric(QStyle.PM_TabCloseIndicatorHeight, None, self)
        return QSize(width, height)

    def enterEvent(self, ev : QEvent):
        if self.isEnabled():
            self.update()
        super(QAbstractButton, self).enterEvent(ev)

    def leaveEvent(self, ev : QEvent):
        if self.isEnabled():
            self.update()
        super(QAbstractButton, self).leaveEvent(ev)

    def paintEvent(self, ev : QEvent):
        p = QPainter(self)
        opt = QStyleOption()
        opt.init(self)
        opt.state |= QStyle.State_AutoRaise
        if (self.isEnabled() 
                and self.underMouse() 
                and not self.isChecked() 
                and not self.isDown()):
            opt.state |= QStyle.State_Raised
        if self.isChecked():
            opt.state |= QStyle.State_On
        if self.isDown():
            opt.state |= QStyle.State_Sunken;

        if isinstance(self.parent(), QTabBar):
            tb = self.parent()
            index = tb.currentIndex
            position = self.style().styleHint(QStyle.SH_TabBar_CloseButtonPosition, None, tb);
            if (tb.tabButton(index, position) == self):
                opt.state |= QStyle.State_Selected
        self.style().drawPrimitive(QStyle.PE_IndicatorTabClose, opt, p, self)
