from PyQt4.QtCore import Qt, QRect, QSize, QPoint, qDebug, qWarning, QSysInfo
from PyQt4.QtGui import *

TGB_CtrlList = [QStyle.SC_GroupBoxCheckBox, 
                QStyle.SC_GroupBoxLabel, 
                QStyle.SC_GroupBoxContents, 
                QStyle.SC_GroupBoxFrame]

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
