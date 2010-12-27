from PyQt4.QtCore import Qt, QRect, QSize, QPoint, qDebug, qWarning, QSysInfo
from PyQt4.QtGui import *

TGB_CtrlList = [QStyle.SC_GroupBoxCheckBox, 
                QStyle.SC_GroupBoxLabel, 
                QStyle.SC_GroupBoxContents, 
                QStyle.SC_GroupBoxFrame]
                
StyleColor = {'Menu_Header'         : (235, 242, 247),  # Background for menu header
              'Menu_FrameLine'      : (207, 219, 235),  # Internal frame line for menu (light)
              'Menu_FrameDark'      : (132, 146, 166),  # Outside frame for menu (dark)
              'Menu_Sidebar'        : (243, 247, 251),  # Check column background
              'ToolBar_Label'       : (115, 131, 153),  # Toolgroup label color (alpha blend?)
              'Menu_Text'           : ( 37,  66, 100),  # Menu text color
              'Menu_HeaderText'     : ( 76,  96, 122),  # Separator label (lighter)
              'Menu_Panel'          : (252, 252, 252),  # Menu background color
              'ToolBar_LineDark'    : (188, 204, 220),  # Center line for toolbar separator (dark)
              'ToolBar_LineLight'   : (165, 184, 208),  # Center line for toolbar separator (light)
              'ToolBar_LineShadow'  : (236, 241, 250)}  # Outside line for toolbar separator

PixelMetrics = {'Menu_HeaderVertical'   : 26, 
                'Menu_Sidebar'          : 24, 
                'Menu_HeaderTextOffset' : 8}
                
menuCornerGrid = {'1x1' : .66, 
                  '0x1' : .85, 
                  '0x2' : .90}

class FormattedPrint():
    @staticmethod
    def rect(rect : QRect):
        return str.format('QRect({}, {}, {}, {})', 
                             rect.left(), rect.top(), 
                             rect.width(), rect.height())
    @staticmethod
    def point(p : QPoint):
        return str.format('QPoint({},{})', p.x(), p.y())
        
    @staticmethod
    def size(sz : QSize):
        return str.format('QSize({}, {})', sz.width(), sz.height())

class StyleHelper():
    ToolGroupBox = 0x00
    CE_ToolButtonIcon = 0x01
    CE_ToolButtonLabel = 0x02
    
    @staticmethod
    def copyStyleOption(source, target):
        target.direction = source.direction
        target.fontMetrics = source.fontMetrics
        target.palette = source.palette
        target.rect = source.rect
        target.state = source.state
        
    def drawPlastiqueGradient(painter : QPainter, rect : QRect, gradientStart : QColor,
                              gradientStop : QColor):
        gradientName = str.format("qplastique-g-{}-{}-{}-{}", 
                                  rect.width(), rect.height(), 
                                  gradientStart.rgba(), gradientStop.rgba())

        cache = QPixmap()
        p = painter
        r = QRect(rect)

        doPixmapCache = p.deviceTransform().isIdentity() and p.worldMatrix().isIdentity()
        if doPixmapCache and QPixmapCache.find(gradientName, cache):
            painter.drawPixmap(rect, cache)
        else:
            if doPixmapCache:
                cache = QPixmap(rect.size())
                cache.fill(Qt.transparent)
                p = QPainter(cache)
            r = QRect(0, 0, rect.width(), rect.height())

            x = r.center().x()
            gradient = QLinearGradient(x, r.top(), x, r.bottom())
            gradient.setColorAt(0, gradientStart)
            gradient.setColorAt(1, gradientStop)
            p.fillRect(r, gradient)

            if doPixmapCache:
                p.end()
                painter.drawPixmap(rect, cache)
                QPixmapCache.insert(gradientName, cache)
    
    @staticmethod
    def drawWinFocusRect(fropt : QStyleOptionFocusRect, p : QPainter):
            r = fropt.rect
            p.save()
            p.setBackgroundMode(Qt.TransparentMode)
            bg_col = fropt.backgroundColor
            if not bg_col.isValid():
                bg_col = p.background().color();
            # Create an "XOR" color.
            patternCol = QColor((bg_col.red() ^ 0xff) & 0xff,
                                (bg_col.green() ^ 0xff) & 0xff,
                                (bg_col.blue() ^ 0xff) & 0xff)
            p.setBrush(QBrush(patternCol, Qt.Dense4Pattern))
            p.setBrushOrigin(r.topLeft())
            p.setPen(Qt.NoPen)
            p.drawRect(r.left(), r.top(), r.width(), 1)    # Top
            p.drawRect(r.left(), r.bottom(), r.width(), 1) # Bottom
            p.drawRect(r.left(), r.top(), 1, r.height())   # Left
            p.drawRect(r.right(), r.top(), 1, r.height())  # Right
            p.restore()

    @staticmethod
    def drawWinGroupBoxFrame(frame : QStyleOptionFrameV2, p : QPainter, alignBottom : bool):
        if frame.features & QStyleOptionFrameV2.Flat:
            fr = frame.rect
            if not alignBottom:
                p1 = QPoint(fr.x(), fr.y() + 1)
                p2 = QPoint(fr.x() + fr.width(), p1.y())
            else:
                p1 = QPoint(fr.x(), fr.bottom() - 1)
                p2 = QPoint(fr.x() + fr.width(), p1.y())
            qDrawShadeLine(p, p1, p2, frame.palette, True,
                           frame.lineWidth, frame.midLineWidth)
        else:
            qDrawShadeRect(p, frame.rect.x(), frame.rect.y(), frame.rect.width(),
                           frame.rect.height(), frame.palette, True,
                           frame.lineWidth, frame.midLineWidth)
    @staticmethod
    def drawMenuArrow(palette : QPalette) -> None:
            image = QImage(5, 5, QImage.Format_ARGB32)
            image.fill(Qt.transparent)
            imagePainter = QPainter(image)
            imagePainter.setPen(palette.buttonText().color())
            imagePainter.drawLine(0, 0, 4, 0)
            imagePainter.drawLine(1, 1, 3, 1)
            imagePainter.drawPoint(2, 2)
            
            imagePainter.setPen(QColor(255, 255, 255, 127))
            imagePainter.drawPoints(QPoint(0, 1), 
                                     QPoint(1, 2), 
                                     QPoint(2, 3), 
                                     QPoint(3, 2), 
                                     QPoint(4, 1))
            imagePainter.end()
            
            return QPixmap.fromImage(image)
            
    @staticmethod
    def mergedColors(colorA : QColor, colorB : QColor, factor : int = 50) -> QColor:
        maxFactor = 100
        tmp = QColor(colorA)
        tmp.setRed((tmp.red() * factor) / maxFactor + (colorB.red() * (maxFactor - factor)) / maxFactor)
        tmp.setGreen((tmp.green() * factor) / maxFactor + (colorB.green() * (maxFactor - factor)) / maxFactor)
        tmp.setBlue((tmp.blue() * factor) / maxFactor + (colorB.blue() * (maxFactor - factor)) / maxFactor)
        return tmp
    
    @staticmethod
    def setBrushAlphaF(brush : QBrush, alpha) -> None:
        if brush.gradient():
            gradient = brush.gradient()
            # Use the gradient. Call QColor.setAlphaF() on all color stops.
            for pair in gradient.stops():
                pair[1].setAlphaF(alpha * pair[1].alphaF())
                gradient.setColorAt(*pair)
                
            if gradient.type() == QGradient.RadialGradient:
                grad = QRadialGradient(gradient);
                grad.setStops(stops)
                brush = QBrush(grad)
            elif gradient.type() == QGradient.ConicalGradient:
                grad = QConicalGradient(gradient);
                grad.setStops(stops)
                brush = QBrush(grad)
            else:
                grad = QLinearGradient(gradient)
                grad.setStops(stops)
                brush = QBrush(grad)
        elif not brush.texture().isNull():
            # Modify the texture - ridiculously expensive.
            texture = brush.texture()
            pixmap = QPixmap()
            name = str.format("qbrushtexture-alpha-{}-{}", alpha, texture.cacheKey())
            if not QPixmapCache.find(name, pixmap):
                image = texture.toImage();
                imageBits = image.bits()
                pixels = image.width() * image.height()
                tmpColor = QColor()
                for i in range(pixels - 1):
                    rgb = imageBits[i]
                    tmpColor.setRgb(rgb)
                    tmpColor.setAlphaF(alpha * tmpColor.alphaF())
                    rgb = tmpColor.rgba()
                pixmap = QPixmap.fromImage(image)
                QPixmapCache.insert(name, pixmap)
            brush.setTexture(pixmap)
        else:
            # Use the color
            tmpColor = brush.color()
            tmpColor.setAlphaF(alpha * tmpColor.alphaF())
            brush.setColor(tmpColor)
#if ((option->state & State_Enabled || option->state & State_On) || !(option->state & State_AutoRaise))
#qt_plastique_drawShadedPanel(painter, option, true, widget);
    @staticmethod
    def drawPlastiqueToolButton(p : QPainter, opt : QStyleOption, base : bool,
                                widget : QWidget = None) -> None:
        rect = opt.rect;
        oldPen = p.pen();

        gradientStartColor = opt.palette.button().color().lighter(104)
        gradientStopColor = opt.palette.button().color().darker(105)

        # gradient fill
        if (opt.state & QStyle.State_Enabled) or  not (opt.state & QStyle.State_AutoRaise):
            if (opt.state & QStyle.State_Sunken) or (opt.state & QStyle.State_On):
                drawPlastiqueGradient(p, rect.adjusted(1, 1, -1, -1),
                        opt.palette.button().color().darker(114),
                        opt.palette.button().color().darker(106))
            else:
                drawPlastiqueGradient(p, rect.adjusted(1, 1, -1, -1),
                        opt.palette.background().color().lighter(105) if base else gradientStartColor,
                        opt.palette.background().color().darker(102) if base else gradientStopColor)
        
        drawPlastiqueFrame(p, opt, widget)
        p.setPen(oldPen)
        
    @staticmethod
    def drawNotchedRect(p : QPainter, color : QColor, rect : QRect) -> None:
        oldPen = p.pen()
        p.fillRect(rect.adjusted(-1, -1, -1, -1), color)
        p.setPen(color)
        t = rect.top()
        b = rect.bottom()
        l = rect.left()
        r = rect.right()
        p.drawLines(QLine(l + 1, t, r - 1, t), 
                    QLine(l + 1, b, r - 1, t), 
                    QLine(l, t + 1, l, b - 1), 
                    QLine(r, t + 1, r, b - 1))
        p.setPen(oldPen)
    
    @staticmethod
    def drawMenuCorners(p : QPainter, color1 : QColor, color2 : QColor, rect : QRect):
        t = rect.top()
        b = rect.bottom()
        l = rect.left()
        r = rect.right()
        color = QColor(color1)
        color.setAlphaF(0.90)
        p.setPen(color)
        p.drawPoints(QPoint(l + 2, t), QPoint(l, t + 2), #topleft
                     QPoint(l + 2, b), QPoint(l, b - 2), #bottomleft
                     QPoint(r - 2, t), QPoint(r, t + 2), #topright
                     QPoint(r - 2, b), QPoint(r, b - 2)) #bottomright
        color.setAlphaF(0.85)
        p.setPen(color)
        p.drawPoints(QPoint(l + 1, t), QPoint(l, t + 1), #topleft
                     QPoint(l + 1, b), QPoint(l, b - 1), #bottomleft
                     QPoint(r - 1, t), QPoint(r, t + 1), #topright
                     QPoint(r - 1, b), QPoint(r, b - 1)) #bottomright
        color.setAlphaF(0.66)
        p.setPen(color)
        p.drawPoints(QPoint(l + 1, t + 1), QPoint(r - 1, t + 1), #topleft, topright
                     QPoint(l + 1, b - 1), QPoint(r - 1, b - 1)) #bottomleft, bottomright
#        p.setPen(color2)
#        p.drawPoints(QPoint(l + 2, t + 1), QPoint(l + 2, t + 2), QPoint(l + 1, t + 2), #topleft
#                     QPoint(r - 2, t + 1), QPoint(r - 2, t + 2), QPoint(r - 1, t + 2), #topright
#                     QPoint(l + 2, b - 1), QPoint(l + 2, b - 2), QPoint(l + 1, b - 2), #bottomleft
#                     QPoint(r - 2, b - 1), QPoint(r - 2, b - 2), QPoint(r - 1, b - 2)) #bottomright
    @staticmethod
    def drawPlastiqueShadowedFrame(p : QPainter, rect : QRect, opt : QStyleOption,
                                shadow : QFrame.Shadow = QFrame.Plain) -> None:
        oldPen = p.pen()
        border = QBrush()
        corner = QBrush()
        innerTopLeft = QBrush()
        innerBottomRight = QBrush()

        if shadow != QFrame.Plain and (opt.state & QStyle.State_HasFocus):
            border = opt.palette.highlight()
            StyleHelper.setBrushAlphaF(border, 0.8)
            corner = opt.palette.highlight()
            StyleHelper.setBrushAlphaF(corner, 0.5)
            innerTopLeft = qBrushDark(opt.palette.highlight(), 125)
            innerBottomRight = opt.palette.highlight()
            StyleHelper.setBrushAlphaF(innerBottomRight, 0.65)
        else:
            border = opt.palette.shadow()
            StyleHelper.setBrushAlphaF(border, qreal(0.4))
            corner = opt.palette.shadow()
            StyleHelper.setBrushAlphaF(corner, 0.25)
            innerTopLeft = opt.palette.shadow()
            innerBottomRight = opt.palette.shadow()
            if shadow == QFrame.Sunken:
                StyleHelper.setBrushAlphaF(innerTopLeft, 0.23)
                StyleHelper.setBrushAlphaF(innerBottomRight, 0.075)
            else:
                StyleHelper.setBrushAlphaF(innerTopLeft, 0.075)
                StyleHelper.setBrushAlphaF(innerBottomRight, 0.23)

        # Opaque corner lines
        p.setPen(QPen(border, 0))
        lines = [QLine(rect.left() + 2, rect.top(), rect.right() - 2, rect.top()), 
                 QLine(rect.left() + 2, rect.bottom(), rect.right() - 2, rect.bottom()), 
                 QLine(rect.left(), rect.top() + 2, rect.left(), rect.bottom() - 2), 
                 QLine(rect.right(), rect.top() + 2, rect.right(), rect.bottom() - 2)]
        p.drawLines(lines)

        # Opaque corner dots
        p.drawPoints(QPoint(rect.left() + 1, rect.top() + 1), 
                     QPoint(rect.left() + 1, rect.bottom() - 1), 
                     QPoint(rect.right() - 1, rect.top() + 1), 
                     QPoint(rect.right() - 1, rect.bottom() - 1))
        

        # Shaded corner dots
        p.setPen(QPen(corner, 0))
        p.drawPoints(QPoint(rect.left(), rect.top() + 1), 
                     QPoint(rect.left(), rect.bottom() - 1), 
                     QPoint(rect.left() + 1, rect.top()), 
                     QPoint(rect.left() + 1, rect.bottom()), 
                     QPoint(rect.right(), rect.top() + 1), 
                     QPoint(rect.right(), rect.bottom() - 1), 
                     QPoint(rect.right() - 1, rect.top()), 
                     QPoint(rect.right() - 1, rect.bottom()))
        

        # Shadows
        if shadow != QFrame.Plain:
            p.setPen(QPen(innerTopLeft, 0))
            p.drawLines([QLine(rect.left() + 2, rect.top() + 1, rect.right() - 2, rect.top() + 1), 
                        QLine(rect.left() + 1, rect.top() + 2, rect.left() + 1, rect.bottom() - 2)])
            p.setPen(QPen(innerBottomRight, 0))
            p.drawLines([QLine(rect.left() + 2, rect.bottom() - 1, rect.right() - 2, rect.bottom() - 1), 
                        QLine(rect.right() - 1, rect.top() + 2, rect.right() - 1, rect.bottom() - 2)])

        p.setPen(oldPen)
    
    @staticmethod
    def drawPlastiqueFrame(p : QPainter, opt : QStyleOption, widget : QWidget = None) -> None:
        oldPen = p.pen()

        borderColor = opt.palette.background().color().darker(178)
        gradientStartColor = opt.palette.button().color().lighter(104)
        gradientStopColor = opt.palette.button().color().darker(105)
        if widget:
            ### backgroundrole/foregroundrole should be part of the style option
            alphaCornerColor = StyleHelper.mergedColors(opt.palette.color(widget.backgroundRole()), borderColor)
        else:
            alphaCornerColor = StyleHelper.mergedColors(opt.palette.background().color(), borderColor)
        left = opt.rect.left()
        right = opt.rect.right()
        top = opt.rect.top()
        bottom = opt.rect.bottom()
        # outline / border
        p.setPen(borderColor)
        p.drawLines([QLine(left + 2, top, right - 2, top), 
                    QLine(left + 2, bottom, right - 2, bottom), 
                    QLine(left, top + 2, left, bottom - 2), 
                    QLine(right, top + 2, right, bottom - 2)])

        p.drawPoints(QPoint(left + 1, top + 1), 
                     QPoint(right - 1, top + 1), 
                     QPoint(left + 1, bottom - 1), 
                     QPoint(right - 1, bottom - 1))

        p.setPen(alphaCornerColor)
        
        # draw corners
        p.drawPoints(QPoint(left + 1, top), 
                     QPoint(right - 1, top), 
                     QPoint(left + 1, bottom), 
                     QPoint(right - 1, bottom), 
                     QPoint(left, top + 1), 
                     QPoint(right, top + 1), 
                     QPoint(left, bottom - 1), 
                     QPoint(right, bottom - 1))

        # inner border
        if (opt.state & QStyle.State_Sunken) or (opt.state & QStyle.State_On):
            p.setPen(opt.palette.button().color().darker(118));
        else:
            p.setPen(gradientStartColor);

        p.drawLines([QLine(left + 2, top + 1, right - 2, top + 1), 
                 QLine(left + 1, top + 2, left + 1, bottom - 2)])

        if (opt.state & QStyle.State_Sunken) or (opt.state & QStyle.State_On):
            p.setPen(opt.palette.button().color().darker(110));
        else:
            p.setPen(gradientStopColor.darker(102));

        p.drawLines([QLine(left + 2, bottom - 1, right - 2, bottom - 1), 
                 QLine(right - 1, top + 2, right - 1, bottom - 2)])

        p.setPen(oldPen)
    
    @staticmethod
    def drawPlastiqueShadedPanel(p : QPainter, opt : QStyleOption, base : bool,
                                             widget : QWidget = None) -> None:
        oldPen = p.pen()

        gradientStartColor = opt.palette.button().color().lighter(104)
        gradientStopColor = opt.palette.button().color().darker(105)

        # gradient fill
        if (opt.state & QStyle.State_Enabled) or  not (opt.state & QStyle.State_AutoRaise):
            if (opt.state & QStyle.State_Sunken) or (opt.state & QStyle.State_On):
                StyleHelper.drawPlastiqueGradient(p, opt.rect.adjusted(1, 1, -1, -1),
                        opt.palette.button().color().darker(114),
                        opt.palette.button().color().darker(106))
            else:
                StyleHelper.drawPlastiqueGradient(p, opt.rect.adjusted(1, 1, -1, -1),
                        opt.palette.background().color().lighter(105) if base else gradientStartColor,
                        opt.palette.background().color().darker(102) if base else gradientStopColor)
        
        StyleHelper.drawPlastiqueFrame(p, opt, widget)
        p.setPen(oldPen)
