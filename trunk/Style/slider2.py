void QPlastiqueStyle::drawComplexControl(ComplexControl control, const QStyleOptionComplex *option,
                                         QPainter *painter, const QWidget *widget) const
{
    QColor borderColor = option->palette.background().color().darker(178);
    QColor alphaCornerColor;
   if (widget) {
        // ### backgroundrole/foregroundrole should be part of the style option
        alphaCornerColor = mergedColors(option->palette.color(widget->backgroundRole()), borderColor);
    } else {
        alphaCornerColor = mergedColors(option->palette.background().color(), borderColor);
    }
    QColor gradientStartColor = option->palette.button().color().lighter(104);
    QColor gradientStopColor = option->palette.button().color().darker(105);
    QColor highlightedGradientStartColor = option->palette.button().color().lighter(101);
    QColor highlightedGradientStopColor = mergedColors(option->palette.button().color(), option->palette.highlight().color(), 85);
    QColor highlightedDarkInnerBorderColor = mergedColors(option->palette.button().color(), option->palette.highlight().color(), 35);
    QColor highlightedLightInnerBorderColor = mergedColors(option->palette.button().color(), option->palette.highlight().color(), 58);

    switch (control) {
#ifndef QT_NO_SLIDER
    case CC_Slider:
        if (const QStyleOptionSlider *slider = qstyleoption_cast<const QStyleOptionSlider *>(option)) {
            QRect grooveRegion = proxy()->subControlRect(CC_Slider, option, SC_SliderGroove, widget);
            QRect handle = proxy()->subControlRect(CC_Slider, option, SC_SliderHandle, widget);
            QRect ticks = proxy()->subControlRect(CC_Slider, option, SC_SliderTickmarks, widget);
            bool horizontal = slider->orientation == Qt::Horizontal;
            bool ticksAbove = slider->tickPosition & QSlider::TicksAbove;
            bool ticksBelow = slider->tickPosition & QSlider::TicksBelow;

            QRect groove;
            //The clickable region is 5 px wider than the visible groove for improved usability
            if (grooveRegion.isValid())
                groove = horizontal ? grooveRegion.adjusted(0, 5, 0, -5) : grooveRegion.adjusted(5, 0, -5, 0);


            QPixmap cache;

            if ((option->subControls & SC_SliderGroove) && groove.isValid()) {
                BEGIN_STYLE_PIXMAPCACHE(QString::fromLatin1("slider_groove-%0-%1").arg(ticksAbove).arg(ticksBelow))
                p->fillRect(groove, option->palette.background());

                // draw groove
                if (horizontal) {
                    p->setPen(borderColor);
                    const QLine lines[4] = {
                        QLine(groove.left() + 1, groove.top(),
                              groove.right() - 1, groove.top()),
                        QLine(groove.left() + 1, groove.bottom(),
                              groove.right() - 1, groove.bottom()),
                        QLine(groove.left(), groove.top() + 1,
                              groove.left(), groove.bottom() - 1),
                        QLine(groove.right(), groove.top() + 1,
                              groove.right(), groove.bottom() - 1) };
                    p->drawLines(lines, 4);

                    p->setPen(alphaCornerColor);
                    const QPoint points[4] = {
                        QPoint(groove.left(), groove.top()),
                        QPoint(groove.left(), groove.bottom()),
                        QPoint(groove.right(), groove.top()),
                        QPoint(groove.right(), groove.bottom()) };
                    p->drawPoints(points, 4);
                } else {
                    p->setPen(borderColor);
                    const QLine lines[4] = {
                        QLine(groove.left() + 1, groove.top(),
                              groove.right() - 1, groove.top()),
                        QLine(groove.left() + 1, groove.bottom(),
                              groove.right() - 1, groove.bottom()),
                        QLine(groove.left(), groove.top() + 1,
                              groove.left(), groove.bottom() - 1),
                        QLine(groove.right(), groove.top() + 1,
                              groove.right(), groove.bottom() - 1) };
                    p->drawLines(lines, 4);

                    p->setPen(alphaCornerColor);
                    const QPoint points[4] = {
                        QPoint(groove.left(), groove.top()),
                        QPoint(groove.right(), groove.top()),
                        QPoint(groove.left(), groove.bottom()),
                        QPoint(groove.right(), groove.bottom()) };
                    p->drawPoints(points, 4);
                }
                END_STYLE_PIXMAPCACHE
            }

            if ((option->subControls & SC_SliderHandle) && handle.isValid()) {
                QString handlePixmapName = QStyleHelper::uniqueName(QLatin1String("slider_handle"), option, handle.size());
                if (ticksAbove && !ticksBelow)
                    handlePixmapName += QLatin1String("-flipped");
                if ((option->activeSubControls & SC_SliderHandle) && (option->state & State_Sunken))
                    handlePixmapName += QLatin1String("-sunken");

                if (!QPixmapCache::find(handlePixmapName, cache)) {
                    cache = QPixmap(handle.size());
                    cache.fill(Qt::white);
                    QRect pixmapRect(0, 0, handle.width(), handle.height());
                    QPainter handlePainter(&cache);
                    handlePainter.fillRect(pixmapRect, option->palette.background());

                    // draw handle
                    if (horizontal) {
                        QPainterPath path;
                        if (ticksAbove && !ticksBelow) {
                            path.moveTo(QPoint(pixmapRect.right(), pixmapRect.bottom()));
                            path.lineTo(QPoint(pixmapRect.right(), pixmapRect.bottom() - 10));
                            path.lineTo(QPoint(pixmapRect.right() - 5, pixmapRect.bottom() - 14));
                            path.lineTo(QPoint(pixmapRect.left() + 1, pixmapRect.bottom() - 10));
                            path.lineTo(QPoint(pixmapRect.left() + 1, pixmapRect.bottom()));
                            path.lineTo(QPoint(pixmapRect.right(), pixmapRect.bottom()));
                        } else {
                            path.moveTo(QPoint(pixmapRect.right(), pixmapRect.top() + 1));
                            path.lineTo(QPoint(pixmapRect.right(), pixmapRect.top() + 10));
                            path.lineTo(QPoint(pixmapRect.right() - 5, pixmapRect.top() + 14));
                            path.lineTo(QPoint(pixmapRect.left() + 1, pixmapRect.top() + 10));
                            path.lineTo(QPoint(pixmapRect.left() + 1, pixmapRect.top() + 1));
                            path.lineTo(QPoint(pixmapRect.right(), pixmapRect.top() + 1));
                        }
                        if (slider->state & State_Enabled) {
                            QLinearGradient gradient(pixmapRect.center().x(), pixmapRect.top(),
                                                     pixmapRect.center().x(), pixmapRect.bottom());
                            if ((option->activeSubControls & SC_SliderHandle) && (option->state & State_Sunken)) {
                                gradient.setColorAt(0, gradientStartColor.lighter(110));
                                gradient.setColorAt(1, gradientStopColor.lighter(110));
                            } else {
                                gradient.setColorAt(0, gradientStartColor);
                                gradient.setColorAt(1, gradientStopColor);
                            }
                            handlePainter.fillPath(path, gradient);
                        } else {
                            handlePainter.fillPath(path, slider->palette.background());
                        }
                    } else {
                        QPainterPath path;
                        if (ticksAbove && !ticksBelow) {
                            path.moveTo(QPoint(pixmapRect.right(), pixmapRect.top() + 1));
                            path.lineTo(QPoint(pixmapRect.right() - 10, pixmapRect.top() + 1));
                            path.lineTo(QPoint(pixmapRect.right() - 14, pixmapRect.top() + 5));
                            path.lineTo(QPoint(pixmapRect.right() - 10, pixmapRect.bottom()));
                            path.lineTo(QPoint(pixmapRect.right(), pixmapRect.bottom()));
                            path.lineTo(QPoint(pixmapRect.right(), pixmapRect.top() + 1));
                        } else {
                            path.moveTo(QPoint(pixmapRect.left() + 1, pixmapRect.top() + 1));
                            path.lineTo(QPoint(pixmapRect.left() + 10, pixmapRect.top() + 1));
                            path.lineTo(QPoint(pixmapRect.left() + 14, pixmapRect.top() + 5));
                            path.lineTo(QPoint(pixmapRect.left() + 10, pixmapRect.bottom()));
                            path.lineTo(QPoint(pixmapRect.left() + 1, pixmapRect.bottom()));
                            path.lineTo(QPoint(pixmapRect.left() + 1, pixmapRect.top() + 1));
                        }
                        if (slider->state & State_Enabled) {
                            QLinearGradient gradient(pixmapRect.center().x(), pixmapRect.top(),
                                                     pixmapRect.center().x(), pixmapRect.bottom());
                            gradient.setColorAt(0, gradientStartColor);
                            gradient.setColorAt(1, gradientStopColor);
                            handlePainter.fillPath(path, gradient);
                        } else {
                            handlePainter.fillPath(path, slider->palette.background());
                        }
                    }

                    QImage image;
                    if (horizontal) {
                        image = QImage((ticksAbove && !ticksBelow) ? qt_plastique_slider_horizontalhandle_up : qt_plastique_slider_horizontalhandle);
                    } else {
                        image = QImage((ticksAbove && !ticksBelow) ? qt_plastique_slider_verticalhandle_left : qt_plastique_slider_verticalhandle);
                    }

                    image.setColor(1, borderColor.rgba());
                    image.setColor(2, gradientStartColor.rgba());
                    image.setColor(3, alphaCornerColor.rgba());
                    if (option->state & State_Enabled) {
                        image.setColor(4, 0x80ffffff);
                        image.setColor(5, 0x25000000);
                    }
                    handlePainter.drawImage(pixmapRect, image);
                    handlePainter.end();
                    QPixmapCache::insert(handlePixmapName, cache);
                }

                painter->drawPixmap(handle.topLeft(), cache);

                if (slider->state & State_HasFocus) {
                    QStyleOptionFocusRect fropt;
                    fropt.QStyleOption::operator=(*slider);
                    fropt.rect = subElementRect(SE_SliderFocusRect, slider, widget);
                    proxy()->drawPrimitive(PE_FrameFocusRect, &fropt, painter, widget);
                }
            }

            if (option->subControls & SC_SliderTickmarks) {
                QPen oldPen = painter->pen();
                painter->setPen(borderColor);
                int tickSize = proxy()->pixelMetric(PM_SliderTickmarkOffset, option, widget);
                int available = proxy()->pixelMetric(PM_SliderSpaceAvailable, slider, widget);
                int interval = slider->tickInterval;
                if (interval <= 0) {
                    interval = slider->singleStep;
                    if (QStyle::sliderPositionFromValue(slider->minimum, slider->maximum, interval,
                                                        available)
                        - QStyle::sliderPositionFromValue(slider->minimum, slider->maximum,
                                                          0, available) < 3)
                        interval = slider->pageStep;
                }
                if (interval <= 0)
                    interval = 1;

                int v = slider->minimum;
                int len = proxy()->pixelMetric(PM_SliderLength, slider, widget);
                QVarLengthArray<QLine, 32> lines;
                while (v <= slider->maximum + 1) {
                    if (v == slider->maximum + 1 && interval == 1)
                        break;
                    const int v_ = qMin(v, slider->maximum);
                    int pos = sliderPositionFromValue(slider->minimum, slider->maximum,
                                                      v_, (horizontal
                                                          ? slider->rect.width()
                                                          : slider->rect.height()) - len,
                                                      slider->upsideDown) + len / 2;

                    int extra = 2 - ((v_ == slider->minimum || v_ == slider->maximum) ? 1 : 0);

                    if (horizontal) {
                        if (ticksAbove) {
                            lines.append(QLine(pos, slider->rect.top() + extra,
                                               pos, slider->rect.top() + tickSize));
                        }
                        if (ticksBelow) {
                            lines.append(QLine(pos, slider->rect.bottom() - extra,
                                               pos, slider->rect.bottom() - tickSize));
                        }
                    } else {
                        if (ticksAbove) {
                            lines.append(QLine(slider->rect.left() + extra, pos,
                                               slider->rect.left() + tickSize, pos));
                        }
                        if (ticksBelow) {
                            lines.append(QLine(slider->rect.right() - extra, pos,
                                               slider->rect.right() - tickSize, pos));
                        }
                    }

                    // in the case where maximum is max int
                    int nextInterval = v + interval;
                    if (nextInterval < v)
                        break;
                    v = nextInterval;
                }
                painter->drawLines(lines.constData(), lines.size());
                painter->setPen(oldPen);
            }
        }
        break;
#endif // QT_NO_SLIDER

QSize QPlastiqueStyle::sizeFromContents(ContentsType type, const QStyleOption *option,
                                        const QSize &size, const QWidget *widget) const
    QSize newSize = QWindowsStyle::sizeFromContents(type, option, size, widget);
    switch (type) {
    case CT_Slider:
        if (const QStyleOptionSlider *slider = qstyleoption_cast<const QStyleOptionSlider *>(option)) {
            int tickSize = proxy()->pixelMetric(PM_SliderTickmarkOffset, option, widget);
            if (slider->tickPosition & QSlider::TicksBelow) {
                if (slider->orientation == Qt::Horizontal)
                    newSize.rheight() += tickSize;
                else
                    newSize.rwidth() += tickSize;
            }
            if (slider->tickPosition & QSlider::TicksAbove) {
                if (slider->orientation == Qt::Horizontal)
                    newSize.rheight() += tickSize;
                else
                    newSize.rwidth() += tickSize;
            }
        }
        break;

QRect QPlastiqueStyle::subControlRect(ComplexControl control, const QStyleOptionComplex *option,
                                      SubControl subControl, const QWidget *widget) const
{
    QRect rect = QWindowsStyle::subControlRect(control, option, subControl, widget);

    switch (control) {
#ifndef QT_NO_SLIDER
    case CC_Slider:
        if (const QStyleOptionSlider *slider = qstyleoption_cast<const QStyleOptionSlider *>(option)) {
            int tickSize = proxy()->pixelMetric(PM_SliderTickmarkOffset, option, widget);

            switch (subControl) {
            case SC_SliderHandle:
                if (slider->orientation == Qt::Horizontal) {
                    rect.setWidth(11);
                    rect.setHeight(15);
                    int centerY = slider->rect.center().y() - rect.height() / 2;
                    if (slider->tickPosition & QSlider::TicksAbove)
                        centerY += tickSize;
                    if (slider->tickPosition & QSlider::TicksBelow)
                        centerY -= tickSize;
                    rect.moveTop(centerY);
                } else {
                    rect.setWidth(15);
                    rect.setHeight(11);
                    int centerX = slider->rect.center().x() - rect.width() / 2;
                    if (slider->tickPosition & QSlider::TicksAbove)
                        centerX += tickSize;
                    if (slider->tickPosition & QSlider::TicksBelow)
                        centerX -= tickSize;
                    rect.moveLeft(centerX);
                }
                break;
            case SC_SliderGroove: {
                QPoint grooveCenter = slider->rect.center();
                if (slider->orientation == Qt::Horizontal) {
                    rect.setHeight(14);
                    --grooveCenter.ry();
                    if (slider->tickPosition & QSlider::TicksAbove)
                        grooveCenter.ry() += tickSize;
                    if (slider->tickPosition & QSlider::TicksBelow)
                        grooveCenter.ry() -= tickSize;
                } else {
                    rect.setWidth(14);
                    --grooveCenter.rx();
                    if (slider->tickPosition & QSlider::TicksAbove)
                        grooveCenter.rx() += tickSize;
                    if (slider->tickPosition & QSlider::TicksBelow)
                        grooveCenter.rx() -= tickSize;
                }
                rect.moveCenter(grooveCenter);
                break;
            }
            default:
                break;
            }
        }
        break;
#endif // QT_NO_SLIDER

int QPlastiqueStyle::pixelMetric(PixelMetric metric, const QStyleOption *option, const QWidget *widget) const
#ifndef QT_NO_SLIDER
    case PM_SliderThickness:
        ret = 15;
        break;
    case PM_SliderLength:
    case PM_SliderControlThickness:
        ret = 11;
        break;
    case PM_SliderTickmarkOffset:
        ret = 5;
        break;
    case PM_SliderSpaceAvailable:
        if (const QStyleOptionSlider *slider = qstyleoption_cast<const QStyleOptionSlider *>(option)) {
            int size = 15;
            if (slider->tickPosition & QSlider::TicksBelow)
                ++size;
            if (slider->tickPosition & QSlider::TicksAbove)
                ++size;
            ret = size;
            break;
        }
#endif // QT_NO_SLIDER
