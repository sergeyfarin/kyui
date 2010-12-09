#QPainter utilities

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class PainterUtil():
    def __init__(self):
        ...
    def calcActionRect(self, act : QAction, showIcon : bool = True, 
                      iconSize : QSize = None) -> QRect:
        pass
        
    def updateActionRects(self, menu : QMenu) -> None:
        if not itemsDirty:
            return
        actions = menu.actions()
        menu.ensurePolished()
        actionsCount = len(actions)
        #let's reinitialize the buffer
        actionRects = []
        for rect in range(actionsCount):
            actionRects.append(QRect())

        #let's try to get the last visible action
        lastVisibleAction = actions.count()
        while lastVisibleAction >= 0:
            action = actions()[lastVisibleAction]
            if action.isVisible():
                #removing trailing separators
                if action.isSeparator() and menu().collapsibleSeparators:
                    continue
                break
            lastVisibleAction -= 1

        max_column_width = 0,
        dh = popupGeometry(menu).height()
        y = 0
        
        style = menu.style()
        
        opt = QStyleOption()
        opt.init(menu)
        
        hmargin = style.pixelMetric(QStyle.PM_MenuHMargin, opt, menu)
        vmargin = style.pixelMetric(QStyle.PM_MenuVMargin, opt, menu)
        icone = style.pixelMetric(QStyle.PM_SmallIconSize, opt, menu)
        fw = style.pixelMetric(QStyle.PM_MenuPanelWidth, opt, menu)
        deskFw = style.pixelMetric(QStyle.PM_MenuDesktopFrameWidth, opt, menu)
        
        if menu.tearOffEnabled():
            tearoffHeight = style.pixelMetric(QStyle.PM_MenuTearoffHeight, opt, menu)
        else:
            tearoffHeight = 0

        #for compatibility now - will have to refactor this away
        tabWidth = 0
        maxIconWidth = 0
        hasCheckableItems = false
        ncols = 1
        sloppyAction = 0

        for i in range(actionsCount):
            action = actions[i]
            if action.isSeparator() or not action.isVisible() or widgetItems.contains(action):
                continue
            #..and some members
            hasCheckableItems |= action.isCheckable()
            icon = action.icon();
            if not icon.isNull():
                maxIconWidth = qMax(maxIconWidth, icone + 4)

        #calculate size
        qfm = menu.fontMetrics();
        # this is true to allow removing the leading separators
        previousWasSeparator = True 
        for i in range(lastVisibleAction - 1):
            action = actions[i]
            if not action.isVisible() or\
                (menu.collapsibleSeparators() and previousWasSeparator and action.isSeparator()):
                continue # we continue, this action will get an empty QRect

            previousWasSeparator = action.isSeparator();

            #let the style modify the above size..
            opt = QStyleOptionMenuItem()
            menu.initStyleOption(opt, action)
            fm = opt.fontMetrics

            sz = QSize()
            w = widgetItems.value(action)
            if w:
              sz = w.sizeHint().expandedTo(w.minimumSize()).expandedTo(w.minimumSizeHint()).boundedTo(w.maximumSize());
            else:
                #calc what I think the size is..
                if action.isSeparator():
                    sz = QSize(2, 2);
                else:
                    s = action.text()
                    t = s.indexOf(QLatin1Char('\t'));
                    if t != -1:
                        tabWidth = qMax(int(tabWidth), qfm.width(s.mid(t+1)))
                        s = s[:t]
                    else:
                        seq = action.shortcut();
                        if not seq.isEmpty:
                            tabWidth = qMax(int(tabWidth), qfm.width(seq));
                    sz.setWidth(fm.boundingRect(QRect(), Qt.TextSingleLine | Qt.TextShowMnemonic, s).width());
                    sz.setHeight(qMax(fm.height(), qfm.height()));

                    icon = action.icon()
                    if not icon.isNull():
                        icon_sz = QSize(icone, icone)
                        if icon_sz.height() > icon.height():
                            sz.setHeight(icon_sz.height())
                sz = style.sizeFromContents(QStyle.CT_MenuItem, opt, sz, menu);

            if not size.isEmpty():
                max_column_width = qMax(max_column_width, sz.width())
                #wrapping
                if not scroll and (y + sz.height() + vmargin) > (dh - deskFw * 2):
                    ncols += 1
                    y = vmargin
                y += sz.height()
                #update the item
                actionRects[i] = QRect(0, 0, sz.width(), sz.height());

        max_column_width += tabWidth #finally add in the tab width
        sfcMargin = \
            style.sizeFromContents(QStyle.CT_Menu, opt, QApplication.globalStrut(), menu).width()\
            - QApplication.globalStrut().width()
        min_column_width = menu.minimumWidth() - (sfcMargin + leftmargin + rightmargin + 2 * (fw + hmargin));
        max_column_width = qMax(min_column_width, max_column_width);


        #calculate position
        base_y = vmargin + fw + topmargin + tearoffHeight
        if scroll: base_y += scroll.scrollOffset
        
        x = hmargin + fw + leftmargin
        y = base_y

        for i in range(actionsCount):
            rect = actionRects[i]
            if rect.isNull():
                continue
            if not scroll and y+rect.height() > dh - deskFw * 2:
                x += max_column_width + hmargin
                y = base_y
            rect.translate(x, y)
            rect.setWidth(max_column_width); #uniform width

            #update the widgets geometry
            w = widgetItems.value(actions[i])
            if w:
                widget.setGeometry(rect);
                widget.setVisible(actions[i].isVisible())
            y += rect.height()
        itemsDirty = 0;

    def actionRect(self, act : QAction) -> QRect:
        index = actions.indexOf(act)
        if index == -1:
            return QRect()

        self.updateActionRects()

        #we found the action
        return actionRects.at(index)
        
    def drawToolButton(self, cc, opt, p, widget):
        if cc != QStyle.CC_ToolButton:
            return
        
        button = self.subControlRect(cc, toolbutton, SC_ToolButton, widget);
        menuarea = self.subControlRect(cc, toolbutton, SC_ToolButtonMenu, widget);

        bflags = opt.state & ~State_Sunken
        mflags = bflags
            autoRaise = flags & State_AutoRaise
            if autoRaise:
                if not (bflags & State_MouseOver) or not (bflags & State_Enabled):
                    bflags &= ~State_Raised

            if opt.state & State_Sunken:
                if opt.activeSubControls & SC_ToolButton:
                    bflags |= State_Sunken
                    mflags |= State_MouseOver | State_Sunken
                elif opt.activeSubControls & SC_ToolButtonMenu:
                    mflags |= State_Sunken
                    bflags |= State_MouseOver

            toolopt = QStyleOption()
            toolopt.palette = opt.palette
            if opt.subControls & SC_ToolButton:
                if flags & (State_Sunken | State_On | State_Raised) or not autoRaise:
                    if (opt.features & QStyleOptionToolButton.MenuButtonPopup && autoRaise) {
                        XPThemeData theme(widget, p, QLatin1String("TOOLBAR"));
                        theme.partId = TP_SPLITBUTTON;
                        theme.rect = button;
                        if (!(bflags & State_Enabled))
                            stateId = TS_DISABLED;
                        else if (bflags & State_Sunken)
                            stateId = TS_PRESSED;
                        else if (bflags & State_MouseOver || !(flags & State_AutoRaise))
                            stateId = flags & State_On ? TS_HOTCHECKED : TS_HOT;
                        else if (bflags & State_On)
                            stateId = TS_CHECKED;
                        else
                            stateId = TS_NORMAL;
                        if (option->direction == Qt.RightToLeft)
                            theme.mirrorHorizontally = true;
                        theme.stateId = stateId;
                        d->drawBackground(theme);
                    else:
                        tool.rect = option->rect;
                        tool.state = bflags;
                        if autoRaise: # for tool bars
                            self.drawPrimitive(PE_PanelButtonTool, &tool, p, widget);
                        else:
                            self.drawPrimitive(PE_PanelButtonBevel, &tool, p, widget)

            if (opt.state & State_HasFocus) {
                QStyleOptionFocusRect fr;
                fr.QStyleOption.operator=(*toolbutton);
                fr.rect.adjust(3, 3, -3, -3);
                if (opt.features & QStyleOptionToolButton.MenuButtonPopup)
                    fr.rect.adjust(0, 0, -self.pixelMetric(QStyle.PM_MenuButtonIndicator,
                                                      toolbutton, widget), 0);
                self.drawPrimitive(PE_FrameFocusRect, &fr, p, widget);
            }
            QStyleOptionToolButton label = *toolbutton;
            label.state = bflags;
            int fw = 2;
            if (!autoRaise)
                label.state &= ~State_Sunken;
            label.rect = button.adjusted(fw, fw, -fw, -fw);
            self.drawControl(CE_ToolButtonLabel, &label, p, widget);

            if (opt.subControls & SC_ToolButtonMenu) {
                tool.rect = menuarea;
                tool.state = mflags;
                if (autoRaise) {
                    self.drawPrimitive(PE_IndicatorButtonDropDown, &tool, p, widget);
                } else {
                    tool.state = mflags;
                    menuarea.adjust(-2, 0, 0, 0);
                    // Draw menu button
                    if ((bflags & State_Sunken) != (mflags & State_Sunken)){
                        p->save();
                        p->setClipRect(menuarea);
                        tool.rect = option->rect;
                        self.drawPrimitive(PE_PanelButtonBevel, &tool, p, 0);
                        p->restore();
                    }
                    // Draw arrow
                    p->save();
                    p->setPen(option->palette.dark().color());
                    p->drawLine(menuarea.left(), menuarea.top() + 3,
                                menuarea.left(), menuarea.bottom() - 3);
                    p->setPen(option->palette.light().color());
                    p->drawLine(menuarea.left() - 1, menuarea.top() + 3,
                                menuarea.left() - 1, menuarea.bottom() - 3);

                    tool.rect = menuarea.adjusted(2, 3, -2, -1);
                    self.drawPrimitive(PE_IndicatorArrowDown, &tool, p, widget);
                    p->restore();
                }
            elif opt.features & QStyleOptionToolButton.HasMenu:
                int mbi = self.pixelMetric(PM_MenuButtonIndicator, toolbutton, widget)
                QRect ir = opt.rect
                QStyleOptionToolButton newBtn = *toolbutton
                newBtn.rect = QRect(ir.right() + 4 - mbi, ir.height() - mbi + 4, mbi - 5, mbi - 5)
                self.drawPrimitive(QStyle.PE_IndicatorArrowDown, &newBtn, p, widget)
            }
        }
