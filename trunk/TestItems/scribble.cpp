enum {
	TP_BUTTON = 1,
	TP_DROPDOWNBUTTON = 2,
	TP_SPLITBUTTON = 3,
	TP_SPLITBUTTONDROPDOWN = 4,
	TP_SEPARATOR = 5,
	TP_SEPARATORVERT = 6
};
enum {
	TS_NORMAL = 1,      //normal state
	TS_HOT = 2,         //State_MouseOver
	TS_PRESSED = 3,     //State_Sunken
	TS_DISABLED = 4,    //State_Disabled
	TS_CHECKED = 5,     //State_On
	TS_HOTCHECKED = 6   //State_On and State_MouseOver
};

enum {
    State_Hover = 0,
    State_Normal = 0,
    State_Checked = 1
} Icon_Shift_Vertical;

enum {
    IconPadding = 6,
    TextPadding = 4,
} VertToolButtonPadding;

enum {
    State_Enabled,  //Set if the button is enabled.
    State_HasFocus, //Set if the button has input focus.
    State_Raised,   //Set if the button is not down, not on and not flat.
    State_On,       //Set if the button is a toggle button and is toggled on.
    State_Sunken,   //Set if the button is down (i.e., the mouse button or the space bar is pressed on the button).
} State;

/* ToolButton Compononents:
 * Button : QStyleOptionToolButton
 * MenuButton (if menubuttonpopup)
 * Frame : QStyleOptionFrameV3
 * FocusRect
 * Label
 * Icon
 * Splitter
 * Arrow
 */

int QWindowsVistaStyle::pixelMetric(PixelMetric metric, const QStyleOption *option, const QWidget *widget) const
{
    if (!QWindowsVistaStylePrivate::useVista()) {
        return QWindowsStyle::pixelMetric(metric, option, widget);
    }
    switch (metric) {

    case PM_DockWidgetTitleBarButtonMargin:
        return int(QStyleHelper::dpiScaled(5.));
    case PM_ScrollBarSliderMin:
        return int(QStyleHelper::dpiScaled(18.));
    case PM_MenuHMargin:
    case PM_MenuVMargin:
        return 0;
    case PM_MenuPanelWidth:
        return 3;
    default:
        break;
    }
    return QWindowsXPStyle::pixelMetric(metric, option, widget);
    
int QWindowsXPStyle::pixelMetric(PixelMetric pm, const QStyleOption *option, const QWidget *widget) const
{
    if (!QWindowsXPStylePrivate::useXP())
        return QWindowsStyle::pixelMetric(pm, option, widget);

    int res = 0;
    switch (pm) {
    case PM_MenuBarPanelWidth:
        res = 0;
        break;

    case PM_DefaultFrameWidth:
        if (qobject_cast<const QListView*>(widget))
            res = 2;
        else
            res = 1;
        break;
    case PM_MenuPanelWidth:
    case PM_SpinBoxFrameWidth:
        res = 1;
        break;

    case PM_TabBarTabOverlap:
    case PM_MenuHMargin:
    case PM_MenuVMargin:
        res = 2;
        break;

    case PM_TabBarBaseOverlap:
        if (const QStyleOptionTab *tab = qstyleoption_cast<const QStyleOptionTab *>(option)) {
            switch (tab->shape) {
            case QTabBar::RoundedNorth:
            case QTabBar::TriangularNorth:
                res = 1;
                break;
            case QTabBar::RoundedSouth:
            case QTabBar::TriangularSouth:
                res = 2;
                break;
            case QTabBar::RoundedEast:
            case QTabBar::TriangularEast:
                res = 3;
                break;
            case QTabBar::RoundedWest:
            case QTabBar::TriangularWest:
                res = 1;
                break;
            }
        }
        break;

    case PM_SplitterWidth:
        res = qMax(int(QStyleHelper::dpiScaled(5.)), QApplication::globalStrut().width());
        break;

    case PM_IndicatorWidth:
    case PM_IndicatorHeight:
        {
            XPThemeData theme(widget, 0, QLatin1String("BUTTON"), BP_CHECKBOX, CBS_UNCHECKEDNORMAL);
            if (theme.isValid()) {
                SIZE size;
                pGetThemePartSize(theme.handle(), 0, theme.partId, theme.stateId, 0, TS_TRUE, &size);
                res = (pm == PM_IndicatorWidth) ? size.cx : size.cy;
            }
        }
        break;

    case PM_ExclusiveIndicatorWidth:
    case PM_ExclusiveIndicatorHeight:
        {
            XPThemeData theme(widget, 0, QLatin1String("BUTTON"), BP_RADIOBUTTON, RBS_UNCHECKEDNORMAL);
            if (theme.isValid()) {
                SIZE size;
                pGetThemePartSize(theme.handle(), 0, theme.partId, theme.stateId, 0, TS_TRUE, &size);
                res = (pm == PM_ExclusiveIndicatorWidth) ? size.cx : size.cy;
            }
        }
        break;

    case PM_ProgressBarChunkWidth:
        {
            Qt::Orientation orient = Qt::Horizontal;
            if (const QStyleOptionProgressBarV2 *pb2 = qstyleoption_cast<const QStyleOptionProgressBarV2 *>(option))
                orient = pb2->orientation;
            XPThemeData theme(widget, 0, QLatin1String("PROGRESS"), (orient == Qt::Horizontal) ? PP_CHUNK : PP_CHUNKVERT);
            if (theme.isValid()) {
                SIZE size;
                pGetThemePartSize(theme.handle(), 0, theme.partId, theme.stateId, 0, TS_TRUE, &size);
                res = (orient == Qt::Horizontal) ? size.cx : size.cy;
            }
        }
        break;

    case PM_SliderThickness:
        {
            XPThemeData theme(widget, 0, QLatin1String("TRACKBAR"), TKP_THUMB);
            if (theme.isValid()) {
                SIZE size;
                pGetThemePartSize(theme.handle(), 0, theme.partId, theme.stateId, 0, TS_TRUE, &size);
                res = size.cy;
            }
        }
        break;

    case PM_TitleBarHeight:
        {
            if (widget && (widget->windowType() == Qt::Tool))
                res = GetSystemMetrics(SM_CYSMCAPTION) + GetSystemMetrics(SM_CXSIZEFRAME);
            else
                res = GetSystemMetrics(SM_CYCAPTION) + GetSystemMetrics(SM_CXSIZEFRAME);
        }
        break;

    case PM_MdiSubWindowFrameWidth:
        {
            XPThemeData theme(widget, 0, QLatin1String("WINDOW"), WP_FRAMELEFT, FS_ACTIVE);
            if (theme.isValid()) {
                SIZE size;
                pGetThemePartSize(theme.handle(), 0, WP_FRAMELEFT, FS_ACTIVE, 0, TS_TRUE, &size);
                res = size.cx-1;
            }
        }
        break;

    case PM_MdiSubWindowMinimizedWidth:
        res = 160;
        break;

    case PM_ToolBarHandleExtent:
        res = int(QStyleHelper::dpiScaled(8.));
        break;
    case PM_DockWidgetFrameWidth:
    {
        XPThemeData theme(widget, 0, QLatin1String("WINDOW"), WP_SMALLFRAMERIGHT, FS_ACTIVE);
        if (theme.isValid()) {
            SIZE size;
            pGetThemePartSize(theme.handle(), 0, theme.partId, theme.stateId, 0, TS_TRUE, &size);
            res = size.cx;
        }
    }
    break;
    case PM_DockWidgetSeparatorExtent:
        res = int(QStyleHelper::dpiScaled(4.));
        break;
    case PM_DockWidgetTitleMargin:
        res = int(QStyleHelper::dpiScaled(4.));
        break;

    case PM_ButtonShiftHorizontal:
    case PM_ButtonShiftVertical:
        if (qstyleoption_cast<const QStyleOptionToolButton *>(option))
            res = 1;
        else
            res = 0;
        break;

    case PM_ButtonDefaultIndicator:
        res = 0;
        break;

    default:
        res = QWindowsStyle::pixelMetric(pm, option, widget);
    }

    return res;
}
int QWindowsStyle::pixelMetric(PixelMetric pm, const QStyleOption *opt, const QWidget *widget) const
{
    int ret;

    switch (pm) {
    case PM_ButtonDefaultIndicator:
    case PM_ButtonShiftHorizontal:
    case PM_ButtonShiftVertical:
    case PM_MenuHMargin:
    case PM_MenuVMargin:
        ret = 1;
        break;
    case PM_TabBarTabShiftHorizontal:
        ret = 0;
        break;
    case PM_TabBarTabShiftVertical:
        ret = 2;
        break;
    case PM_MaximumDragDistance:
#if defined(Q_WS_WIN)
        {
            HDC hdcScreen = GetDC(0);
            int dpi = GetDeviceCaps(hdcScreen, LOGPIXELSX);
            ReleaseDC(0, hdcScreen);
            ret = (int)(dpi * 1.375);
        }
#else
        ret = 60;
#endif
        break;

    case PM_SliderLength:
        ret = int(QStyleHelper::dpiScaled(11.));
        break;

        // Returns the number of pixels to use for the business part of the
        // slider (i.e., the non-tickmark portion). The remaining space is shared
        // equally between the tickmark regions.
    case PM_SliderControlThickness:
        if (const QStyleOptionSlider *sl = qstyleoption_cast<const QStyleOptionSlider *>(opt)) {
            int space = (sl->orientation == Qt::Horizontal) ? sl->rect.height() : sl->rect.width();
            int ticks = sl->tickPosition;
            int n = 0;
            if (ticks & QSlider::TicksAbove)
                ++n;
            if (ticks & QSlider::TicksBelow)
                ++n;
            if (!n) {
                ret = space;
                break;
            }

            int thick = 6;        // Magic constant to get 5 + 16 + 5
            if (ticks != QSlider::TicksBothSides && ticks != QSlider::NoTicks)
                thick += proxy()->pixelMetric(PM_SliderLength, sl, widget) / 4;

            space -= thick;
            if (space > 0)
                thick += (space * 2) / (n + 2);
            ret = thick;
        } else {
            ret = 0;
        }
        break;

    case PM_MenuBarHMargin:
        ret = 0;
        break;

    case PM_MenuBarVMargin:
        ret = 0;
        break;

    case PM_MenuBarPanelWidth:
        ret = 0;
        break;

    case PM_SmallIconSize:
        ret = int(QStyleHelper::dpiScaled(16.));
        break;

    case PM_LargeIconSize:
        ret = int(QStyleHelper::dpiScaled(32.));
        break;

    case PM_IconViewIconSize:
        ret = proxy()->pixelMetric(PM_LargeIconSize, opt, widget);
        break;

    case PM_DockWidgetTitleMargin:
        ret = int(QStyleHelper::dpiScaled(2.));
        break;
    case PM_DockWidgetTitleBarButtonMargin:
        ret = int(QStyleHelper::dpiScaled(4.));
        break;
#if defined(Q_WS_WIN)
    case PM_DockWidgetFrameWidth:
        ret = GetSystemMetrics(SM_CXFRAME);
        break;
#else
    case PM_DockWidgetFrameWidth:
        ret = 4;
        break;
#endif // Q_WS_WIN
    break;


#if defined(Q_WS_WIN)
    case PM_TitleBarHeight:
        if (widget && (widget->windowType() == Qt::Tool)) {
            // MS always use one less than they say
        } else {
            ret = GetSystemMetrics(SM_CYCAPTION) - 1;
        }

        break;

    case PM_ScrollBarExtent:
        {
            ret = QCommonStyle::pixelMetric(pm, opt, widget);
        }
        break;
#endif // Q_WS_WIN

    case PM_SplitterWidth:
        ret = qMax(4, QApplication::globalStrut().width());
        break;

#if defined(Q_WS_WIN)
    case PM_MdiSubWindowFrameWidth:
#if defined(Q_OS_WINCE)
        ret = GetSystemMetrics(SM_CYDLGFRAME);
#else
        ret = GetSystemMetrics(SM_CYFRAME);
#endif
        break;
    case PM_TextCursorWidth: {
        DWORD caretWidth = 1;
#if defined(SPI_GETCARETWIDTH)
        SystemParametersInfo(SPI_GETCARETWIDTH, 0, &caretWidth, 0);
#endif
        ret = (int)caretWidth;
        break; }
#endif
    case PM_ToolBarItemMargin:
        ret = 1;
        break;
    case PM_ToolBarItemSpacing:
        ret = 0;
        break;
    case PM_ToolBarHandleExtent:
        ret = int(QStyleHelper::dpiScaled(10.));
        break;
    default:
        ret = QCommonStyle::pixelMetric(pm, opt, widget);
        break;
    }

    return ret;
}
int QCommonStyle::pixelMetric(PixelMetric m, const QStyleOption *opt, const QWidget *widget) const
{
    int ret;

    switch (m) {
    case PM_FocusFrameVMargin:
    case PM_FocusFrameHMargin:
        ret = 2;
        break;
    case PM_MenuBarVMargin:
    case PM_MenuBarHMargin:
        ret = 0;
        break;
    case PM_DialogButtonsSeparator:
        ret = int(QStyleHelper::dpiScaled(5.));
        break;
    case PM_DialogButtonsButtonWidth:
        ret = int(QStyleHelper::dpiScaled(70.));
        break;
    case PM_DialogButtonsButtonHeight:
        ret = int(QStyleHelper::dpiScaled(30.));
        break;
    case PM_CheckListControllerSize:
    case PM_CheckListButtonSize:
        ret = int(QStyleHelper::dpiScaled(16.));
        break;
    case PM_TitleBarHeight: {
        if (const QStyleOptionTitleBar *tb = qstyleoption_cast<const QStyleOptionTitleBar *>(opt)) {
            if ((tb->titleBarFlags & Qt::WindowType_Mask) == Qt::Tool) {
                ret = qMax(widget ? widget->fontMetrics().height() : opt->fontMetrics.height(), 16);
            } else if (qobject_cast<const QDockWidget*>(widget)) {
                ret = qMax(widget->fontMetrics().height(), int(QStyleHelper::dpiScaled(13)));
            } else {
                ret = qMax(widget ? widget->fontMetrics().height() : opt->fontMetrics.height(), 18);
            }
        } else {
            ret = int(QStyleHelper::dpiScaled(18.));
        }

        break; }
    case PM_ScrollBarSliderMin:
        ret = int(QStyleHelper::dpiScaled(9.));
        break;

    case PM_ButtonMargin:
        ret = int(QStyleHelper::dpiScaled(6.));
        break;

    case PM_DockWidgetTitleBarButtonMargin:
        ret = int(QStyleHelper::dpiScaled(2.));
        break;

    case PM_ButtonDefaultIndicator:
        ret = 0;
        break;

    case PM_MenuButtonIndicator:
        ret = int(QStyleHelper::dpiScaled(12.));
        break;

    case PM_ButtonShiftHorizontal:
    case PM_ButtonShiftVertical:

    case PM_DefaultFrameWidth:
        ret = 2;
        break;

    case PM_ComboBoxFrameWidth:
    case PM_SpinBoxFrameWidth:
    case PM_MenuPanelWidth:
    case PM_TabBarBaseOverlap:
    case PM_TabBarBaseHeight:
        ret = proxy()->pixelMetric(PM_DefaultFrameWidth, opt, widget);
        break;

    case PM_MdiSubWindowFrameWidth:
        ret = int(QStyleHelper::dpiScaled(4.));
        break;

    case PM_MdiSubWindowMinimizedWidth:
        ret = int(QStyleHelper::dpiScaled(196.));
        break;

    case PM_ScrollBarExtent:
        if (const QStyleOptionSlider *sb = qstyleoption_cast<const QStyleOptionSlider *>(opt)) {
            int s = sb->orientation == Qt::Horizontal ?
                    QApplication::globalStrut().height()
                    : QApplication::globalStrut().width();
            ret = qMax(16, s);
        } else {
            ret = int(QStyleHelper::dpiScaled(16.));
        }
        break;
    case PM_MaximumDragDistance:
        ret = -1;
        break;

    case PM_SliderThickness:
        ret = int(QStyleHelper::dpiScaled(16.));
        break;

    case PM_SliderTickmarkOffset:
        if (const QStyleOptionSlider *sl = qstyleoption_cast<const QStyleOptionSlider *>(opt)) {
            int space = (sl->orientation == Qt::Horizontal) ? sl->rect.height()
                                                            : sl->rect.width();
            int thickness = proxy()->pixelMetric(PM_SliderControlThickness, sl, widget);
            int ticks = sl->tickPosition;

            if (ticks == QSlider::TicksBothSides)
                ret = (space - thickness) / 2;
            else if (ticks == QSlider::TicksAbove)
                ret = space - thickness;
            else
                ret = 0;
        } else {
            ret = 0;
        }
        break;

    case PM_SliderSpaceAvailable:
        if (const QStyleOptionSlider *sl = qstyleoption_cast<const QStyleOptionSlider *>(opt)) {
            if (sl->orientation == Qt::Horizontal)
                ret = sl->rect.width() - proxy()->pixelMetric(PM_SliderLength, sl, widget);
            else
                ret = sl->rect.height() - proxy()->pixelMetric(PM_SliderLength, sl, widget);
        } else {
            ret = 0;
        }
        break;
    case PM_DockWidgetSeparatorExtent:
        ret = int(QStyleHelper::dpiScaled(6.));
        break;

    case PM_DockWidgetHandleExtent:
        ret = int(QStyleHelper::dpiScaled(8.));
        break;
    case PM_DockWidgetTitleMargin:
        ret = 0;
        break;
    case PM_DockWidgetFrameWidth:
        ret = 1;
        break;

    case PM_SpinBoxSliderHeight:
    case PM_MenuBarPanelWidth:
        ret = 2;
        break;

    case PM_MenuBarItemSpacing:
        ret = 0;
        break;

    case PM_ToolBarFrameWidth:
        ret = 1;
        break;

    case PM_ToolBarItemMargin:
        ret = 0;
        break;

    case PM_ToolBarItemSpacing:
        ret = int(QStyleHelper::dpiScaled(4.));
        break;

    case PM_ToolBarHandleExtent:
        ret = int(QStyleHelper::dpiScaled(8.));
        break;

    case PM_ToolBarSeparatorExtent:
        ret = int(QStyleHelper::dpiScaled(6.));
        break;

    case PM_ToolBarExtensionExtent:
        ret = int(QStyleHelper::dpiScaled(12.));
        break;
    
    case PM_TabBarTabOverlap:
        ret = 3;
        break;

    case PM_TabBarTabHSpace:
        ret = int(QStyleHelper::dpiScaled(24.));
        break;

    case PM_TabBarTabShiftHorizontal:
        ret = 0;
        break;

    case PM_TabBarTabShiftVertical:
        ret = 2;
        break;

    case PM_TabBarTabVSpace: {
        const QStyleOptionTab *tb = qstyleoption_cast<const QStyleOptionTab *>(opt);
        if (tb && (tb->shape == QTabBar::RoundedNorth || tb->shape == QTabBar::RoundedSouth
                   || tb->shape == QTabBar::RoundedWest || tb->shape == QTabBar::RoundedEast))
            ret = 8;
        else
            if(tb && (tb->shape == QTabBar::TriangularWest || tb->shape == QTabBar::TriangularEast))
                ret = 3;
            else
                ret = 2;
        break; }

    case PM_ProgressBarChunkWidth:
        ret = 9;
        break;

    case PM_IndicatorWidth:
        ret = int(QStyleHelper::dpiScaled(13.));
        break;

    case PM_IndicatorHeight:
        ret = int(QStyleHelper::dpiScaled(13.));
        break;

    case PM_ExclusiveIndicatorWidth:
        ret = int(QStyleHelper::dpiScaled(12.));
        break;

    case PM_ExclusiveIndicatorHeight:
        ret = int(QStyleHelper::dpiScaled(12.));
        break;

    case PM_MenuTearoffHeight:
        ret = int(QStyleHelper::dpiScaled(10.));
        break;

    case PM_MenuScrollerHeight:
        ret = int(QStyleHelper::dpiScaled(10.));
        break;

    case PM_MenuDesktopFrameWidth:
    case PM_MenuHMargin:
    case PM_MenuVMargin:
        ret = 0;
        break;

    case PM_HeaderMargin:
        ret = int(QStyleHelper::dpiScaled(4.));
        break;
    case PM_HeaderMarkSize:
        ret = int(QStyleHelper::dpiScaled(32.));
        break;
    case PM_HeaderGripMargin:
        ret = int(QStyleHelper::dpiScaled(4.));
        break;
    case PM_TabBarScrollButtonWidth:
        ret = int(QStyleHelper::dpiScaled(16.));
        break;
    case PM_LayoutLeftMargin:
    case PM_LayoutTopMargin:
    case PM_LayoutRightMargin:
    case PM_LayoutBottomMargin:
        {
            bool isWindow = false;
            if (opt) {
                isWindow = (opt->state & State_Window);
            } else if (widget) {
                isWindow = widget->isWindow();
            }
            ret = proxy()->pixelMetric(isWindow ? PM_DefaultTopLevelMargin : PM_DefaultChildMargin);
        }
        break;
    case PM_LayoutHorizontalSpacing:
    case PM_LayoutVerticalSpacing:
        ret = proxy()->pixelMetric(PM_DefaultLayoutSpacing);
        break;

    case PM_DefaultTopLevelMargin:
        ret = int(QStyleHelper::dpiScaled(11.));
        break;
    case PM_DefaultChildMargin:
        ret = int(QStyleHelper::dpiScaled(9.));
        break;
    case PM_DefaultLayoutSpacing:
        ret = int(QStyleHelper::dpiScaled(6.));
        break;

    case PM_ToolBarIconSize:
        ret = qt_guiPlatformPlugin()->platformHint(QGuiPlatformPlugin::PH_ToolBarIconSize);
        if (!ret)
            ret = int(QStyleHelper::dpiScaled(24.));
        break;

    case PM_TabBarIconSize:
    case PM_ListViewIconSize:
        ret = proxy()->pixelMetric(PM_SmallIconSize, opt, widget);
        break;

    case PM_ButtonIconSize:
    case PM_SmallIconSize:
        ret = int(QStyleHelper::dpiScaled(16.));
        break;
    case PM_IconViewIconSize:
        ret = proxy()->pixelMetric(PM_LargeIconSize, opt, widget);
        break;

    case PM_LargeIconSize:
        ret = int(QStyleHelper::dpiScaled(32.));
        break;

    case PM_ToolTipLabelFrameWidth:
        ret = 1;
        break;
    case PM_CheckBoxLabelSpacing:
    case PM_RadioButtonLabelSpacing:
        ret = int(QStyleHelper::dpiScaled(6.));
        break;
    case PM_SizeGripSize:
        ret = int(QStyleHelper::dpiScaled(13.));
        break;
    case PM_MessageBoxIconSize:
#ifdef Q_WS_MAC
        if (QApplication::desktopSettingsAware()) {
            ret = 64; // No DPI scaling, it's handled elsewhere.
        } else
#endif
        {
            ret = int(QStyleHelper::dpiScaled(32.));
        }
        break;
    case PM_TextCursorWidth:
        ret = 1;
        break;
    case PM_TabBar_ScrollButtonOverlap:
        ret = 1;
        break;
    case PM_TabCloseIndicatorWidth:
    case PM_TabCloseIndicatorHeight:
        ret = int(QStyleHelper::dpiScaled(16.));
        break;
    case PM_ScrollView_ScrollBarSpacing:
        ret = 2 * proxy()->pixelMetric(PM_DefaultFrameWidth, opt, widget);
        break;
    case PM_SubMenuOverlap:
        ret = -proxy()->pixelMetric(QStyle::PM_MenuPanelWidth, opt, widget);
        break;
    default:
        ret = 0;
        break;
    }

    return ret;
}

