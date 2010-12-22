from PyQt4.QtCore import *
from PyQt4.QtGui import *

windowsItemFrame        =  2 # menu item frame width
windowsSepHeight        =  2 # separator item height
windowsItemHMargin      =  3 # menu item hor text margin
windowsItemVMargin      =  2 # menu item ver text margin
windowsArrowHMargin     =  6 # arrow horizontal margin
windowsTabSpacing       = 12 # space between text and tab
windowsRightBorder      = 15 # right border on windows
windowsCheckMarkWidth   = 12 # checkmarks width on windows

def drawControl(ce, opt, p, widget):
    if ce == CE_MenuItem:
        (x, y, w, h) = opt.rect.getRect()
        tab = opt.tabWidth
        disabled = not (opt.state & State_Enabled)
        checked = opt.checked if opt.checkType != QStyleOptionMenuItem.NotCheckable else False
        active = opt.state & State_Selected

        # windows always has a check column, regardless whether we have an icon or not
        checkw = opt.maxIconWidth if (opt.maxIconWidth > 20) else 20

        fill = opt.palette.brush(QPalette.Highlight if active else QPalette.Button)
        p.fillRect(opt.rect.adjusted(0, 0, -1, 0), fill)

        if opt.menuItemType == QStyleOptionMenuItem.Separator:
            yoff = y-1 + h / 2
            p.setPen(opt.palette.dark().color())
            p.drawLine(x + 2, yoff, x + w - 4, yoff)
            p.setPen(opt.palette.light().color())
            p.drawLine(x + 2, yoff + 1, x + w - 4, yoff + 1)
            return

        vCheckRect = self.visualRect(opt.direction, opt.rect, QRect(opt.rect.x(), opt.rect.y(), checkw, opt.rect.height()))
        if checked:
            if active and not disabled:
                qDrawShadePanel(p, vCheckRect,
                                opt.palette, True, 1,
                                opt.palette.brush(QPalette.Button))
            else:
                fill = QBrush(opt.palette.light().color(), Qt.Dense4Pattern)
                qDrawShadePanel(p, vCheckRect, opt.palette, true, 1, fill)
        elif not active:
            p.fillRect(vCheckRect, opt.palette.brush(QPalette.Button))

        # On Windows Style, if we have a checkable item and an icon we
        # draw the icon recessed to indicate an item is checked. If we
        # have no icon, we draw a checkmark instead.
        if not opt.icon.isNull():
            mode = QIcon.Disabled if disabled else QIcon.Normal
            if active and not disabled:
                mode = QIcon.Active
            if checked:
                pixmap = opt.icon.pixmap(self.pixelMetric(PM_SmallIconSize, opt, widget), mode, QIcon.On)
            else:
                pixmap = opt.icon.pixmap(self.pixelMetric(PM_SmallIconSize, opt, widget), mode)
            if active and not disabled and not checked:
                qDrawShadePanel(p, vCheckRect,  opt.palette, false, 1,
                                opt.palette.brush(QPalette.Button))
            pixrect = QRect(0, 0, pixmap.width(), pixmap.height())
            pixrect.moveCenter(vCheckRect.center())
            p.setPen(opt.palette.text().color())
            p.drawPixmap(pixrect.topLeft(), pixmap)
        elif checked:
            newitem = QStyleOptionMenuItem(opt)
            newitem.state = State_None
            if not disabled:
                newitem.state |= State_Enabled
            if active:
                newitem.state |= State_On
            newitem.rect = visualRect(opt.direction, opt.rect, QRect(opt.rect.x() + windowsItemFrame,
                                                                          opt.rect.y() + windowsItemFrame,
                                                                          checkw - 2 * windowsItemFrame,
                                                                          opt.rect.height() - 2 * windowsItemFrame))
            self.drawPrimitive(QStyle.PE_IndicatorMenuCheckMark, newitem, p, widget)

        p.setPen(opt.palette.highlightedText().color() if active else opt.palette.buttonText().color())

        if disabled:
            discol = opt.palette.text().color()
            p.setPen(discol)

        xmargin = windowsItemFrame + checkw + windowsItemHMargin
        xpos = opt.rect.x() + xmargin
        textRect = QRect(xpos, y + windowsItemVMargin,
                       w - xmargin - windowsRightBorder - tab + 1, h - 2 * windowsItemVMargin)
        vTextRect = self.visualRect(opt.direction, opt.rect, textRect)
        # draw text
        if opt.text:
            s = str(opt.text)
            p.save()
            text_flags = Qt.AlignVCenter | Qt.TextShowMnemonic | Qt.TextDontClip | Qt.TextSingleLine
            if not self.styleHint(SH_UnderlineShortcut, menuitem, widget):
                text_flags |= Qt.TextHideMnemonic
            text_flags |= Qt.AlignLeft
            # Handle shortcuts
            if '\t' in s and s[0] != '\t':
                [s, t] = s.split('\t')
                vShortcutRect = self.visualRect(opt.direction, opt.rect,
                    QRect(textRect.topRight(), QPoint(opt.rect.right(), textRect.bottom())))
                if disabled and not active and self.styleHint(SH_EtchDisabledText, opt, widget):
                    p.setPen(opt.palette.light().color())
                    p.drawText(vShortcutRect.adjusted(1,1,1,1), text_flags, t)
                    p.setPen(discol)
                p.drawText(vShortcutRect, text_flags, t)
            # Now the actual text
            font = QFont(opt.font)
            if opt.menuItemType == QStyleOptionMenuItem.DefaultItem:
                font.setBold(True)
            p.setFont(font)
            if disabled and active and self.styleHint(SH_EtchDisabledText, opt, widget):
                p.setPen(opt.palette.light().color())
                p.drawText(vTextRect.adjusted(1,1,1,1), text_flags, s)
                p.setPen(discol)
            p.drawText(vTextRect, text_flags, s)
            p.restore()
        # draw sub menu arrow
        if opt.menuItemType == QStyleOptionMenuItem.SubMenu:
            dim = (h - 2 * windowsItemFrame) / 2
            arrow = QStyle.PE_IndicatorArrowLeft if (opt.direction == Qt.RightToLeft) else QStyle.PE_IndicatorArrowRight
            xpos = x + w - windowsArrowHMargin - windowsItemFrame - dim
            vSubMenuRect = self.visualRect(opt.direction, opt.rect, QRect(xpos, y + h / 2 - dim / 2, dim, dim))
            newitem = QStyleOptionMenuItem(menuitem)
            newitem.rect = vSubMenuRect
            newitem.state = QStyle.State_None if disabled else State_Enabled
            if active:
                newitem.palette.setColor(QPalette.ButtonText,
                                       newitem.palette.highlightedText().color())
            self.drawPrimitive(arrow, newitem, p, widget)
def drawPrimitive(pe, p, opt, widget):
    if pe == QStyle.PE_IndicatorMenuCheckMark:
        #width and height of checkmark
        markW = 7 if (opt.rect.width() > 7) else opt.rect.width()
        markH = markW
        
        #center of the rect
        posX = opt.rect.x() + (opt.rect.width() - markW) / 2 + 1;
        posY = opt.rect.y() + (opt.rect.height() - markH) / 2;

        lines = []

        x = int(posX)
        y = 3 + int(posY)
        for i in range(int(markW  / 2)):
            lines.append(QLineF(x, y, x, y + 2))
            x += 1
            y += 1

        y -= 2
        for i in range(markH):
            lines.append(QLineF(x, y, x, y + 2))
            x += 1
            y -= 1
            
        if (not (opt.state & QStyle.State_Enabled) and not (opt.state & QStyle.State_On)):
            p.setPen(opt.palette.highlightedText().color())
            for point in range(len(lines)):
                lines[point].translate(1, 1)
            p.drawLines(lines)
            for point in range(len(lines)):
                lines[point].translate(1, 1)

        p.setPen(opt.palette.text().color())
        p.drawLines(lines)
