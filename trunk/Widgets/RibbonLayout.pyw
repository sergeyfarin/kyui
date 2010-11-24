from PyQt4.QtCore import Qt
from PyQt4.QtGui import QWidget, QStyle, QStyleOption, QToolbar, QPainter

#QToolBarItem *QToolBarLayout::createItem(QAction *action)
#{
#    bool customWidget = false;
#    bool standardButtonWidget = false;
#    QWidget *widget = 0;
#    QToolBar *tb = qobject_cast<QToolBar*>(parentWidget());
#    if (!tb)
#        return (QToolBarItem *)0;
#
#    if (QWidgetAction *widgetAction = qobject_cast<QWidgetAction *>(action)) {
#        widget = widgetAction->requestWidget(tb);
#        if (widget != 0) {
#            widget->setAttribute(Qt::WA_LayoutUsesWidgetRect);
#            customWidget = true;
#        }
#    } else if (action->isSeparator()) {
#        QToolBarSeparator *sep = new QToolBarSeparator(tb);
#        connect(tb, SIGNAL(orientationChanged(Qt::Orientation)),
#                sep, SLOT(setOrientation(Qt::Orientation)));
#        widget = sep;
#    }
#
#    if (!widget) {
#        QToolButton *button = new QToolButton(tb);
#        button->setAutoRaise(true);
#        button->setFocusPolicy(Qt::NoFocus);
#        button->setIconSize(tb->iconSize());
#        button->setToolButtonStyle(tb->toolButtonStyle());
#        QObject::connect(tb, SIGNAL(iconSizeChanged(QSize)),
#                         button, SLOT(setIconSize(QSize)));
#        QObject::connect(tb, SIGNAL(toolButtonStyleChanged(Qt::ToolButtonStyle)),
#                         button, SLOT(setToolButtonStyle(Qt::ToolButtonStyle)));
#        button->setDefaultAction(action);
#        QObject::connect(button, SIGNAL(triggered(QAction*)), tb, SIGNAL(actionTriggered(QAction*)));
#        widget = button;
#        standardButtonWidget = true;
#    }
#
#    widget->hide();
#    QToolBarItem *result = new QToolBarItem(widget);
#    if (standardButtonWidget)
#        result->setAlignment(Qt::AlignJustify);
#    result->customWidget = customWidget;
#    result->action = action;
#    return result;
#}

class KyRibbonLayout(QLayout):
    def __init__(self, parent: QRibbonWidget = None):
        super().__init__(parent)
        self.__orient = parent.orientation()
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
    
    def orientation(self) -> Qt.Orientation:
        return self.__orientation
        
    def setOrientation(self, orient : Qt.Orientation = Qt.Horizontal) -> None:
        self.__orient = orient
        self.update()

    def initStyleOption(self, option : QStyleOption = None) -> None:
        option.initFrom(self)
        if (self.orientation() == Qt.Horizontal):
            option.state |= QStyle.State_Horizontal

    def sizeHint(self) -> QSize:
        opt = QStyleOption()
        self.initStyleOption(opt)
        extent = style().pixelMetric(QStyle.PM_ToolBarSeparatorExtent, opt, self.parentWidget())
        return QSize(extent, extent);

    def paintEvent(self, event : QPaintEvent) -> None:
        p = QPainter(self)
        opt = QStyleOption()
        self.initStyleOption(opt)
        self.style().drawPrimitive(QStyle.PE_IndicatorToolBarSeparator, opt, p, self.parentWidget())

