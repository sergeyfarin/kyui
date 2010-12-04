from PyQt4.QtCore import *
from PyQt4.QtGui import *

class QGroupBoxPrivate():
    hover = False
    overCheckBox = False
    pressedControl = QStyle.SC_None #QStyle.SubControl
    shortcutId = 0
    def skip(self) -> None:
        pass
    
    def __init__(self) -> None:
        self.__align = Qt.AlignLeft
        self.__shortcutId = 0
        self.__flat = False
        self.__checkable = False
        self.__checked = True
        self.__hover = False
        self.__overCheckBox = False
        self.__pressedControl = QStyle.SC_None
        self.calculateFrame()
        self.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, 
                                       QSizePolicy.Preferred, 
                                       QSizePolicy.GroupBox))
    
    def calculateFrame(self) -> None:
        pass
    
    def __setChildrenEnabled(self, b : bool) -> None:
        pass
        
    def click(self) -> None:
        pass


class ToolGroup(QGroupBox):
    def __init__(self, 
                 title : str = None, 
                 parent : QWidget = None, 
                 action : ExtendedAction = None, 
                 alignment : Qt.Alignment = Qt.AlignHCenter, 
                 flat : bool = False, 
                 checkable : bool = False, 
                 checked : bool = False):
        if title:
            self.__init__(title, parent)
        else:
            self.__init__(parent)
        if alignment: self.setAlignment(alignment)
<<<<<<< .mine
        if flat:
            self.__flat = True
        else:
            self.__flat = False
        self.__checkable = checkable
        self.__checked = checked
        
        if action:        
            self.setDefaultAction(action)
            self.__align = Qt.AlignLeft
        self.__shortcutId = 0
        
        
        self.__checked = True
        self.__hover = False
        self.__overCheckBox = False
        self.__pressedControl = QStyle.SC_None
        self.calculateFrame()
        self.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, 
                                       QSizePolicy.Preferred, 
                                       QSizePolicy.GroupBox))
            
    def paintEvent(self, ev: QPaintEvent) -> None:
        p = QStylePainter(self)
        opt = QStyleOptionGroupBox()
        self.initStyleOption(opt)
        p.drawComplexControl(QStyle.CC_GroupBox, opt)

    #reimp
    # d.click
    # d.hover
    # d.pressedControl
    # d.shortcutId
    # d.checkable
    def event(self, ev : QEvent) -> bool:
        Q_D(QGroupBox);
        if ev.type() == QEvent.Shortcut:
            if ev.shortcutId() == d.shortcutId:
                if not self.isCheckable():
                    d._q_fixFocus(Qt.ShortcutFocusReason)
                else:
                    d.click()
                    self.setFocus(Qt.ShortcutFocusReason)
                return true

        box = QStyleOptionGroupBox()
        self.initStyleOption(box)
        
        if ev.type() == QEvent.HoverEnter or ev.type() == QEvent.HoverMove:
            control = self.style().hitTestComplexControl(QStyle.CC_GroupBox, 
                                                         box, ev.pos(), self)
            oldHover = d.hover;
            d.hover = self.checkable() and \
                (control == QStyle.SC_GroupBoxLabel or control == QStyle.SC_GroupBoxCheckBox)
            if oldHover != d.hover:
                rect = self.style().subControlRect(QStyle.CC_GroupBox, box, QStyle.SC_GroupBoxCheckBox, self) \
                             | style().subControlRect(QStyle.CC_GroupBox, box, QStyle.SC_GroupBoxLabel, self)
                self.update(rect)
            return True
        elif ev.type() == QEvent.HoverLeave:
            d.hover = false
            if self.checkable():
                rect = style().subControlRect(QStyle.CC_GroupBox, box, QStyle.SC_GroupBoxCheckBox, self) \
                             | style().subControlRect(QStyle.CC_GroupBox, box, QStyle.SC_GroupBoxLabel, self)
                self.update(rect)
            return True
        elif ev.type() == QEvent.KeyPress:
            if ev.isAutoRepeat() and (ev.key() == Qt.Key_Select or ev.key() == Qt.Key_Space):
                d.pressedControl = QStyle.SC_GroupBoxCheckBox
                self.update(style().subControlRect(QStyle.CC_GroupBox, box, QStyle.SC_GroupBoxCheckBox, self))
                return True
        elif ev.type() == QEvent.KeyRelease:
            if ev.isAutoRepeat() and (ev.key() == Qt.Key_Select or ev.key() == Qt.Key_Space):
                toggle = d.pressedControl == QStyle.SC_GroupBoxLabel \
                               or d.pressedControl == QStyle.SC_GroupBoxCheckBox
                d.pressedControl = QStyle.SC_None
                if toggle:
                    d.click()
                return True
        return super(QWidget, self).event(ev)
        
    def __fixFocus(self, reason : Qt.FocusReason) -> None:
        fw = self.focusWidget()
        if not fw or self == fw:
            best = None
            candidate = None
            w = self.nextInFocusChain()
            while w != self:
                if self.isAncestorOf(w) and (w.focusPolicy() & Qt.TabFocus) == Qt.TabFocus and w.isVisibleTo(self):
                    if not best and isinstance(w, QRadioButton) and w.isChecked():
                        # we prefer a checked radio button or a widget that
                        # already has focus, if there is one
                        best = w
                    elif not candidate:
                        # but we'll accept anything that takes focus
                        candidate = w
            if best:
                fw = best
            elif candidate:
                fw = candidate
            w = w.nextInFocusChain()
        if fw:
            fw.setFocus(reason)
            
            
    def isCheckable(self) -> bool:
        if self.__checkable: return True
        return False
        
    def isChecked(self) -> bool:
        if self.__checked: return True
        return False
        
    def isFlat(self) -> bool:
        if self.__flat: return True
        return False
        
    def setFlat(self, b = False) -> None:
        if self.__flat == b:
            return
        self.__flat = b
        self.updateGeometry()
        self.update()

    def setCheckable(self, b = False) -> None:
        pass
        
    def setChecked(self, b = False) -> None:
        pass
=======
        if flat: self.setFlat(flat)
        if checkable:
            self.setCheckable(checkable)
            if checked:
                self.setChecked(checked)
                
    def paintEvent(self, ev : QPaintEvent) -> None:
        super().paintEvent(ev)
>>>>>>> .r57
