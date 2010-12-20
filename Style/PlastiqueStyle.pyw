from PyQt4.QtCore import *
from PyQt4.QtGui import *

from .StyleUtil import StyleHelper, StyleColor, PixelMetrics

# from windows style
windowsItemFrame        =  2 # menu item frame width
windowsSepHeight        =  2 # separator item height
windowsItemHMargin      =  3 # menu item hor text margin
windowsItemVMargin      =  2 # menu item ver text margin
windowsArrowHMargin     =  6 # arrow horizontal margin
windowsTabSpacing       = 12 # space between text and tab
windowsRightBorder      = 15 # right border on windows
windowsCheckMarkWidth   = 12 # checkmarks width on windows

TGB_CtrlList = [QStyle.SC_GroupBoxCheckBox, 
                QStyle.SC_GroupBoxLabel, 
                QStyle.SC_GroupBoxContents, 
                QStyle.SC_GroupBoxFrame]

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
    
    drawPlastiqueFrame(p, opt, widget)
    p.setPen(oldPen)

class KyPlastiqueStyle(QStyle):    
    def __init__(self):
        super().__init__()
        self.__proxy = QStyleFactory.create('Plastique')
    
    def drawControl(self, el : QStyle.ControlElement, opt : QStyleOption, p : QPainter, widget : QWidget = None ) -> None:
        if el == QStyle.CE_ToolButtonLabel:
            rect = opt.rect
            shiftX = 0
            shiftY = 0
            if (opt.state & (QStyle.State_Sunken | QStyle.State_On)):
                shiftX = self.pixelMetric(QStyle.PM_ButtonShiftHorizontal, opt, widget)
                shiftY = self.pixelMetric(QStyle.PM_ButtonShiftVertical, opt, widget)
            
            # Arrow type always overrules and is always shown
            hasArrow = opt.features & QStyleOptionToolButton.Arrow
            if (not hasArrow and opt.icon.isNull()) and not opt.text \
                or opt.toolButtonStyle == Qt.ToolButtonTextOnly:
                alignment = int(Qt.AlignCenter | Qt.TextShowMnemonic)
                if not self.styleHint(QStyle.SH_UnderlineShortcut, opt, widget):
                    alignment |= Qt.TextHideMnemonic;
                rect.translate(shiftX, shiftY)
                p.setFont(opt.font)
                self.drawItemText(p, rect, alignment, opt.palette,
                             (opt.state & QStyle.State_Enabled), opt.text,
                             QPalette.ButtonText)
            else:
                pm = QPixmap()
                pmSize = opt.iconSize
                if not opt.icon.isNull():
                    state = QIcon.State(QIcon.On if opt.state & QStyle.State_On else QIcon.Off)
                    if not (opt.state & QStyle.State_Enabled):
                        mode = QIcon.Disabled
                    elif (opt.state & QStyle.State_MouseOver) and (opt.state & QStyle.State_AutoRaise):
                        mode = QIcon.Active
                    else:
                        mode = QIcon.Normal
                    pm = opt.icon.pixmap(opt.rect.size().boundedTo(opt.iconSize),
                                                 mode, state)
                    pmSize = pm.size()

                if opt.toolButtonStyle != Qt.ToolButtonIconOnly:
                    p.setFont(opt.font);
                    pr = QRect(rect)
                    tr = QRect(rect)
                    alignment = Qt.TextShowMnemonic;
                    if not self.styleHint(QStyle.SH_UnderlineShortcut, opt, widget):
                        alignment |= Qt.TextHideMnemonic

                    if opt.toolButtonStyle == Qt.ToolButtonTextUnderIcon:
                        pr.setHeight(pmSize.height() + 6);
                        tr.adjust(0, pr.height() - 1, 0, -2);
                        pr.translate(shiftX, shiftY);
                        if not hasArrow:
                            self.drawItemPixmap(p, pr, Qt.AlignCenter, pm);
                        else:
                            drawArrow(self, toolbutton, pr, p, widget);
                        alignment |= Qt.AlignCenter
                    else:
                        pr.setWidth(pmSize.width() + 8)
                        tr.adjust(pr.width(), 0, 0, 0)
                        pr.translate(shiftX, shiftY)
                        if not hasArrow:
                            self.drawItemPixmap(p, QStyle.visualRect(opt.direction, rect, pr), Qt.AlignCenter, pm)
                        else:
                            self.__drawArrow(self, toolbutton, pr, p, widget);
                        alignment |= Qt.AlignLeft | Qt.AlignVCenter;
                    tr.translate(shiftX, shiftY)
                    self.drawItemText(p, QStyle.visualRect(opt.direction, rect, tr), alignment, opt.palette,
                                 opt.state & QStyle.State_Enabled, opt.text,
                                 QPalette.ButtonText)
                else:
                    rect.translate(shiftX, shiftY)
                    if hasArrow:
                        drawArrow(self, toolbutton, rect, p, widget)
                    else:
                        self.drawItemPixmap(p, rect, Qt.AlignCenter, pm)
        elif el == QStyle.CE_MenuItem:
            self.__drawMenuControl(el, opt, p, widget)
        elif el == QStyle.CE_MenuTearoff:
            if (opt.state & QStyle.State_Selected):
                p.fillRect(opt.rect, opt.palette.brush(QPalette.Highlight))
            else:
                p.fillRect(opt.rect, opt.palette.brush(QPalette.Button))
            p.setPen(QPen(opt.palette.dark().color(), 1, Qt.DashLine))
            p.drawLine(opt.rect.x() + 2, opt.rect.y() + opt.rect.height() / 2 - 1,
                        opt.rect.x() + opt.rect.width() - 4,
                        opt.rect.y() + opt.rect.height() / 2 - 1)
            p.setPen(QPen(opt.palette.light().color(), 1, Qt.DashLine))
            p.drawLine(opt.rect.x() + 2, opt.rect.y() + opt.rect.height() / 2,
                        opt.rect.x() + opt.rect.width() - 4, opt.rect.y() + opt.rect.height() / 2)
        else:
            self.__proxy.drawControl(el, opt, p, widget)

        
    def drawComplexControl(self, control : QStyle.ComplexControl, opt : QStyleOptionComplex, painter : QPainter, widget : QWidget = None ) -> None:
        if control == QStyle.CC_GroupBox:
            # Get the text and checkbox rects
            textRect = self.subControlRect(QStyle.CC_GroupBox, opt, QStyle.SC_GroupBoxLabel, widget)
            checkBoxRect = self.subControlRect(QStyle.CC_GroupBox, opt, QStyle.SC_GroupBoxCheckBox, widget)
            
            # Draw frame
            if opt.subControls & QStyle.SC_GroupBoxFrame:
                frame = QStyleOptionFrameV2()
                StyleHelper.copyStyleOption(opt, frame)
                frame.features = opt.features
                frame.lineWidth = opt.lineWidth
                frame.midLineWidth = opt.midLineWidth
                frame.rect = self.subControlRect(QStyle.CC_GroupBox, opt, QStyle.SC_GroupBoxFrame, widget)
                # Save the painter state before we adjust the clipping
                painter.save()
                region = QRegion(opt.rect)
                if opt.text:
                    ltr = opt.direction == Qt.LeftToRight
                    if opt.subControls & QStyle.SC_GroupBoxCheckBox:
                        finalRect = checkBoxRect.united(textRect)
                        finalRect.adjust((-4 if ltr else 0), 0, (0 if ltr else 4), 0)
                    else:
                        finalRect = textRect
                    region -= region.intersected(finalRect)
                painter.setClipRegion(region) 
                self.__proxy.drawPrimitive(QStyle.PE_FrameGroupBox, frame, painter, widget)
                painter.restore()

            # Draw title
            if (opt.subControls & QStyle.SC_GroupBoxLabel) and opt.text:
                textColor = opt.textColor
                if textColor.isValid():
                    painter.setPen(textColor)
                alignment = int(opt.textAlignment)
                if not self.styleHint(QStyle.SH_UnderlineShortcut, opt, widget):
                    alignment |= Qt.TextHideMnemonic

                self.__proxy.drawItemText(painter, textRect,  Qt.TextShowMnemonic | Qt.AlignHCenter | alignment,
                             opt.palette, opt.state & QStyle.State_Enabled, opt.text,
                             ( QPalette.NoRole if textColor.isValid() else QPalette.WindowText))

                if opt.state & QStyle.State_HasFocus:
                    fropt = QStyleOptionFocusRect()
                    StyleHelper.copyStyleOption(opt, fropt)
                    fropt.backgroundColor = opt.palette.window().color()
                    fropt.rect = textRect
                    self.drawPrimitive(QStyle.PE_FrameFocusRect, fropt, painter, widget)

            # Draw checkbox
            if opt.subControls & QStyle.SC_GroupBoxCheckBox:
                box = QStyleOptionButton()
                StyleHelper.copyStyleOption(opt, box)
                box.rect = checkBoxRect
                self.__proxy.drawPrimitive(QStyle.PE_IndicatorCheckBox, box, painter, widget)
        elif (control == QStyle.CC_ToolButton and 
                opt.toolButtonStyle == Qt.ToolButtonTextUnderIcon and (opt.features
                & (QStyleOptionToolButton.MenuButtonPopup | QStyleOptionToolButton.HasMenu))):
            self.__drawVerticalToolButton(control, opt, painter, widget)
        else:
            self.__proxy.drawComplexControl(control, opt, painter, widget)
    
    def sizeFromContents(self, ct : QStyle.ContentsType, opt : QStyleOption, sz : QSize, widget : QWidget = None ) -> QSize:
        if (ct == QStyle.CT_ToolButton and opt.toolButtonStyle == Qt.ToolButtonTextUnderIcon and (opt.features
                & (QStyleOptionToolButton.MenuButtonPopup | QStyleOptionToolButton.HasMenu))):
            return QSize(sz.width(), 66)
        elif (ct == QStyle.CT_MenuItem and opt.menuItemType == QStyleOptionMenuItem.Separator):
            if sz.height() < 20:
                sz.setHeight(20)
            return QSize(sz)            
        else:
            return self.__proxy.sizeFromContents(ct, opt, sz, widget)
    
    def subControlRect(self, cc : QStyle.ComplexControl, opt : QStyleOptionComplex,
                        sc : QStyle.SubControl, widget : QWidget = None) -> QRect:
#        return self.__proxy.subControlRect(cc, opt, sc, widget)
        if cc == QStyle.CC_GroupBox:
            rect = QRect()
            if sc == QStyle.SC_GroupBoxFrame or sc == QStyle.SC_GroupBoxContents:
                margin = 0
                h = 0
                verticalAlignment = self.styleHint(QStyle.SH_GroupBox_TextLabelVerticalAlignment, opt, widget)
                if opt.text or (opt.subControls & QStyle.SC_GroupBoxCheckBox):
                    h = opt.fontMetrics.height()
                    if (verticalAlignment & Qt.AlignVCenter):
                        margin = h / 2
                    elif (verticalAlignment & Qt.AlignTop):
                        margin = h

                frameRect = QRect(opt.rect)
                if opt.textAlignment & Qt.AlignBottom:
                    frameRect.setBottom(frameRect.bottom() - margin)
                else:
                    frameRect.setTop(margin)
                
                # We can safely return here if we're looking for the FrameRect
                if sc == QStyle.SC_GroupBoxFrame:
                    return frameRect

                frameWidth = 0
                
                if widget and not (opt.features & QStyleOptionFrameV2.Flat):
                    frameWidth = self.pixelMetric(QStyle.PM_DefaultFrameWidth, opt, widget)
                return frameRect.adjusted(frameWidth, frameWidth + h - margin,
                                         0 - frameWidth, 0 - frameWidth)

            elif sc == QStyle.SC_GroupBoxCheckBox or sc == QStyle.SC_GroupBoxLabel:
                fontMetrics = opt.fontMetrics
                h = fontMetrics.height()
                tw = fontMetrics.size(Qt.TextShowMnemonic, opt.text + ' ').width()
                margin = 0 if (opt.features & QStyleOptionFrameV2.Flat) else 8
                rect = opt.rect.adjusted(margin, 0, 0 - margin, 0)
                if opt.textAlignment & Qt.AlignBottom:
                    rect.setTop(rect.bottom() - h)
                else:
                    rect.setHeight(h)

                indicatorWidth = self.pixelMetric(QStyle.PM_IndicatorWidth, opt, widget)
                indicatorSpace = self.pixelMetric(QStyle.PM_CheckBoxLabelSpacing, opt, widget) - 1
                hasCheckBox = opt.subControls & QStyle.SC_GroupBoxCheckBox
                checkBoxSize = (indicatorWidth + indicatorSpace) if hasCheckBox else 0
                
                # Adjusted rect for label + indicatorWidth + indicatorSpace
                totalRect = QStyle.alignedRect(opt.direction, opt.textAlignment,
                                        QSize(tw + checkBoxSize, h), rect)
                # Adjust totalRect if checkbox is set
                if hasCheckBox:
                    ltr = opt.direction == Qt.LeftToRight
                    left = 0
                    # Adjust for check box
                    if sc == QStyle.SC_GroupBoxCheckBox:
                        indicatorHeight = self.pixelMetric(QStyle.PM_IndicatorHeight, opt, widget)
                        left = totalRect.left() if ltr else (totalRect.right() - indicatorWidth)
                        top = totalRect.top() + (fontMetrics.height() - indicatorHeight) / 2
                        totalRect.setRect(left, top, indicatorWidth, indicatorHeight)
                    # Adjust for label
                    else:
                        left = (totalRect.left() + checkBoxSize - 2) if ltr else totalRect.left()
                        totalRect.setRect(left, totalRect.top(),
                                          totalRect.width() - checkBoxSize, totalRect.height())
                
                return totalRect
        elif cc == QStyle.CC_ToolButton:
            if opt.toolButtonStyle != Qt.ToolButtonTextUnderIcon:
                return self.__proxy.subControlRect(cc, opt, sc, widget)
            rect = QRect(opt.rect);
            if sc == QStyle.SC_ToolButton:
                if (opt.features
                     & (QStyleOptionToolButton.MenuButtonPopup | QStyleOptionToolButton.HasMenu)):
                    rect.setHeight(opt.iconSize.height() + 6)
            elif sc == QStyle.SC_ToolButtonMenu:
                if (opt.features
                     & (QStyleOptionToolButton.MenuButtonPopup | QStyleOptionToolButton.HasMenu)):
                    rect.setTop(rect.top() + opt.iconSize.height() + 6)
            return rect
        else:
            return self.__proxy.subControlRect(cc, opt, sc, widget)
            
    def hitTestComplexControl(self, cc : QStyle.ComplexControl, opt : QStyleOptionComplex, pos : QPoint, widget : QWidget = None ) -> QStyle.SubControl:
        sc = QStyle.SC_None
        if cc == QStyle.CC_ToolButton:
            rect = self.subControlRect(cc, opt, QStyle.SC_ToolButton, widget)
            if rect.isValid() and rect.contains(pos):
                return QStyle.SC_ToolButton
            rect = self.subControlRect(cc, opt, QStyle.SC_ToolButtonMenu, widget)
            if rect.isValid() and rect.contains(pos):
                return QStyle.SC_ToolButtonMenu
            return sc
        elif cc == QStyle.CC_GroupBox:
            for i in range(len(TGB_CtrlList)):
                r = self.subControlRect(cc, opt, TGB_CtrlList[i], widget)
                if r.isValid() and r.contains(pos):
                    sc = TGB_CtrlList[i]
                    break
            return sc
        else:
            return self.__proxy.hitTestComplexControl(cc, opt, pos, widget)
        
    def drawPrimitive(self, el : QStyle.PrimitiveElement, opt : QStyleOption, p : QPainter, widget : QWidget = None ) -> None:
        if el == QStyle.PE_FrameMenu:
            # Draws the frame around a popup menu.
            oldPen = p.pen()
            borderColor = QColor(*StyleColor['Menu_FrameDark'])
            alphaCornerColor = StyleHelper.mergedColors(QColor(*StyleColor['Menu_Panel']), borderColor)
            p.setPen(borderColor)
            p.drawRect(opt.rect.adjusted(0, 0, -1, -1))
            p.setPen(alphaCornerColor);
            p.drawPoints(opt.rect.topLeft(), opt.rect.topRight(), 
                         opt.rect.bottomLeft(), opt.rect.bottomRight())
            p.setPen(oldPen)
        elif el == QStyle.PE_PanelMenu:
            pass
        else:
            self.__proxy.drawPrimitive(el, opt, p, widget)
        
    def __drawVerticalToolButton(self, cc, opt, p, widget = None):
        disabled = not (opt.state & QStyle.State_Enabled)
        visible = (not opt.state & QStyle.State_AutoRaise or (opt.state & 
                    (QStyle.State_Sunken | QStyle.State_MouseOver | QStyle.State_On)))
        down = opt.state & (QStyle.State_Sunken | QStyle.State_On)
        hover = opt.state & QStyle.State_MouseOver
        hasmenu = opt.features & (QStyleOptionToolButton.HasMenu | QStyleOptionToolButton.Menu)
        
        bopt, mopt = QStyleOption(), QStyleOption()
        StyleHelper.copyStyleOption(opt, bopt)
        StyleHelper.copyStyleOption(opt, bopt)
        
        if hasmenu:
            bopt.rect = self.subControlRect(QStyle.CC_ToolButton, opt, 
                                            QStyle.SC_ToolButton, widget)
            mopt.rect = self.subControlRect(QStyle.CC_ToolButton, opt, 
                                            QStyle.SC_ToolButtonMenu, widget)
        else:
            bopt.rect = QRect(opt.rect)
        #####
        # Create flags for the button section
        
        # We want to clear the sunken state if only the menu control is depressed
        bopt.state = opt.state & ~QStyle.State_Sunken
        
        # Clear the raised flag if autoraise is enabled and we're not moused over
        if not visible:
            bopt.state &= ~QStyle.State_Raised
        
        #Copy the button flags for the menu portion
        mopt.state = QStyle.State(bopt.state)
        
        # Determine which portion of the button is sunken
        if down:
            if opt.activeSubControls & QStyle.SC_ToolButton:
                bopt.state |= QStyle.State_Sunken
            mopt.state |= QStyle.State_Sunken
            
        # End flags
        ######
        
        # Draw Frame and Split
        if visible:
            drawPlastiqueShadedPanel(p, opt, False)
            if opt.subControls & QStyle.SC_ToolButtonMenu:
                p1 = bopt.rect.bottomLeft()
                p2 = bopt.rect.bottomRight()
                p1.setX(p1.x() + 1) 
                qDrawShadeLine(p, p1, p2, opt.palette, 1, 1, 0)
            

        # Shift if the button is depressed
#        if down:
#            shiftX = self.pixelMetric(QStyle.PM_ButtonShiftHorizontal, opt, widget)
#            shiftY = self.pixelMetric(QStyle.PM_ButtonShiftVertical, opt, widget)
#            if (bopt.state & (QStyle.State_Sunken | QStyle.State_On)):
#                bopt.rect.adjust(shiftX, shiftY, shiftX, shiftY)
#            mopt.rect.adjust(shiftX, shiftY, shiftX, shiftY)

        # Get the icon pixmap
        icon = opt.icon.pixmap(opt.iconSize, 
                                (QIcon.Normal if bopt.state & QStyle.State_Enabled
                                else QIcon.Disabled))
        # Draw the split menu button
        if opt.subControls & QStyle.SC_ToolButtonMenu:
            self.drawItemPixmap(p, bopt.rect, Qt.AlignCenter, icon)
            mopt.rect.adjust(0, 0, 0, -3)
            if opt.text:
                self.drawItemText(p, mopt.rect, Qt.AlignTop | Qt.AlignHCenter, 
                                  opt.palette, opt.state & QStyle.State_Enabled, 
                                  opt.text, QPalette.ButtonText)
            self.drawItemPixmap(p, mopt.rect, Qt.AlignBottom | Qt.AlignHCenter, 
                                    StyleHelper.drawMenuArrow(opt.palette))

        # Draw a unified menu button
        else:
            rect = QRect(opt.rect)
            rect.setHeight(opt.iconSize.height() + 6)
            self.drawItemPixmap(p, rect, Qt.AlignCenter, icon)
            rect.adjust(0, 0, 0, -3)
            if opt.text:
                rect.setTop(rect.bottom())
                rect.setBottom(opt.rect.bottom() - 3)
                self.drawItemText(p, rect, Qt.AlignCenter, 
                                  opt.palette, opt.state & QStyle.State_Enabled, 
                                  opt.text, QPalette.ButtonText)
            if hasmenu:
                self.drawItemPixmap(p, rect, Qt.AlignBottom | Qt.AlignHCenter, 
                                    StyleHelper.drawMenuArrow(opt.palette))
  
    def __drawMenuControl(self, ce, opt, p, widget):
        if ce == QStyle.CE_MenuItem:
            (x, y, w, h) = opt.rect.getRect()
            tab = opt.tabWidth
            #first let's draw the separator if it is one
            if opt.menuItemType == QStyleOptionMenuItem.Separator:
                if not opt.text:
                    yoff = y - 1 + h / 2
                    p.setPen(opt.palette.dark().color())
                    p.drawLine(x + 2, yoff, x + w - 4, yoff)
                    p.setPen(opt.palette.light().color())
                    p.drawLine(x + 2, yoff + 1, x + w - 4, yoff + 1)
                    return
                p.fillRect(opt.rect, QColor(*(StyleColor['Menu_Header'])))
                p.setPen(QColor(*StyleColor['Menu_FrameLine']))
                p.drawLine(opt.rect.topLeft(), opt.rect.topRight())
                p.drawLine(opt.rect.bottomLeft(), opt.rect.bottomRight())

                sidew = PixelMetrics['Menu_HeaderTextOffset']
                color = QColor(*(StyleColor['Menu_HeaderText']))
                p.setPen(color)
                xmargin = windowsItemFrame + sidew + windowsItemHMargin
                xpos = x + xmargin
                textRect = QRect(xpos, 
                         y + windowsItemVMargin, 
                         w - xmargin - windowsRightBorder - tab + 1, 
                         h - 2 * windowsItemVMargin)
                vTextRect = self.visualRect(opt.direction, opt.rect, textRect)
                # draw text
                if opt.text:
                    p.save()
                    s = opt.text
                    if '\t' in s:
                        s = opt.text.split('\t')[0]
                    text_flags = Qt.AlignVCenter | Qt.AlignLeft | Qt.TextHideMnemonic | Qt.TextDontClip | Qt.TextSingleLine
                    opt.font.setBold(True)
                    p.setFont(opt.font)
                    p.drawText(vTextRect, text_flags, s)
                p.restore()
                return
                
            disabled = not (opt.state & QStyle.State_Enabled)
            checked = opt.checked if opt.checkType != QStyleOptionMenuItem.NotCheckable else False
            active = opt.state & QStyle.State_Selected
            # windows always has a check column, regardless whether we have an icon or not
            checkw = opt.maxIconWidth if (opt.maxIconWidth > 20) else 20
            checkcolor = QColor(*StyleColor['Menu_Sidebar'])
            
            fill = opt.palette.brush(QPalette.Highlight if active else QPalette.Light)
            p.fillRect(opt.rect, fill)            

            vCheckRect = self.visualRect(opt.direction, opt.rect, QRect(opt.rect.x(), opt.rect.y(), checkw, opt.rect.height()))
            if checked:
                if active and not disabled:
                    qDrawShadePanel(p, vCheckRect,
                                    opt.palette, True, 1,
                                    opt.palette.brush(QPalette.Button))
                else:
                    fill = QBrush(opt.palette.light().color(), Qt.Dense4Pattern)
                    qDrawShadePanel(p, vCheckRect, opt.palette, True, 1, fill)
            elif not active:
                p.fillRect(vCheckRect, checkcolor)
                p.setPen(QColor(*StyleColor['Menu_FrameLine']))
                p.drawLine(vCheckRect.topRight(), vCheckRect.bottomRight())

            # On Windows Style, if we have a checkable item and an icon we
            # draw the icon recessed to indicate an item is checked. If we
            # have no icon, we draw a checkmark instead.
            if not opt.icon.isNull():
                iconSize = QSize(self.pixelMetric(QStyle.PM_SmallIconSize, opt, widget), 
                                 self.pixelMetric(QStyle.PM_SmallIconSize, opt, widget))
                mode = QIcon.Disabled if disabled else QIcon.Normal
                if active and not disabled:
                    mode = QIcon.Active
                if checked:
                    pixmap = opt.icon.pixmap(iconSize, mode, QIcon.On)
                else:
                    pixmap = opt.icon.pixmap(iconSize, mode)
#                if active and not disabled and not checked:
#                    qDrawShadePanel(p, vCheckRect,  opt.palette, False, 1,
#                                    opt.palette.brush(QPalette.Button))
                pixrect = QRect(0, 0, pixmap.width(), pixmap.height())
                pixrect.moveCenter(vCheckRect.center())
                p.setPen(opt.palette.text().color())
                if checked:
                    p.drawPixmap(QPoint(pixrect.left() + 1, pixrect.top() + 1), pixmap)
                else:
                    p.drawPixmap(pixrect.topLeft(), pixmap)
            elif checked:
                newitem = QStyleOptionMenuItem(opt)
                newitem.state = QStyle.State_None
                if not disabled:
                    newitem.state |= QStyle.State_Enabled
                if active:
                    newitem.state |= QStyle.State_On
                newitem.rect = self.visualRect(opt.direction, opt.rect, QRect(opt.rect.x() + windowsItemFrame,
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
                if not self.styleHint(QStyle.SH_UnderlineShortcut, opt, widget):
                    text_flags |= Qt.TextHideMnemonic
                text_flags |= Qt.AlignLeft
                # Handle shortcuts
                if '\t' in s and s[0] != '\t':
                    [s, t] = s.split('\t')
                    vShortcutRect = self.visualRect(opt.direction, opt.rect,
                        QRect(textRect.topRight(), QPoint(opt.rect.right(), textRect.bottom())))
                    if disabled and not active and self.styleHint(QStyle.SH_EtchDisabledText, opt, widget):
                        p.setPen(opt.palette.light().color())
                        p.drawText(vShortcutRect.adjusted(1,1,1,1), text_flags, t)
                        p.setPen(discol)
                    p.drawText(vShortcutRect, text_flags, t)
                # Now the actual text
                font = QFont(opt.font)
                if opt.menuItemType == QStyleOptionMenuItem.DefaultItem:
                    font.setBold(True)
                p.setFont(font)
                if disabled and active and self.styleHint(QStyle.SH_EtchDisabledText, opt, widget):
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
                newitem = QStyleOptionMenuItem(opt)
                newitem.rect = vSubMenuRect
                newitem.state = QStyle.State_None if disabled else QStyle.State_Enabled
                if active:
                    newitem.palette.setColor(QPalette.ButtonText,
                                           newitem.palette.highlightedText().color())
                self.drawPrimitive(arrow, newitem, p, widget)

    def drawItemPixmap(self, painter : QPainter, rectangle : QRect, alignment : int, pixmap : QPixmap ) -> None:
        self.__proxy.drawItemPixmap(painter, rectangle, alignment, pixmap)
    def drawItemText(self, painter : QPainter, rectangle : QRect, alignment : int, palette : QPalette, enabled : bool, text : str, textRole : QPalette.ColorRole = QPalette.NoRole ) -> None:
        self.__proxy.drawItemText(painter, rectangle, alignment, palette, enabled, text, textRole)
    def generatedIconPixmap(self, iconMode: QIcon.Mode, pixmap : QPixmap, option : QStyleOption ) -> QPixmap:
        return self.__proxy.generatedIconPixmap(iconMode, pixmap, option)
    def itemPixmapRect(self, rectangle : QRect, alignment : int, pixmap : QPixmap ) -> QRect:
        return self.__proxy.itemPixmapRect(rectangle, alignment, pixmap)
    def itemTextRect(self, metrics : QFontMetrics, rectangle : QRect, alignment : int, enabled : bool, text : str ) -> QRect:
        return self.__proxy.itemTextRect(metrics, rectangle, alignment, enabled, text)
    def layoutSpacing(self, control1 : QSizePolicy.ControlType, control2 : QSizePolicy.ControlType, orientation : Qt.Orientation, option : QStyleOption = None, widget : QWidget = None ) -> int:
        return self.__proxy.layoutSpacing(control1, control2, orientation, option, widget)
    def pixelMetric(self, metric : QStyle.PixelMetric, option : QStyleOption = None, widget : QWidget = None ) -> int:
        return self.__proxy.pixelMetric(metric, option, widget)
    def polish(self, objectToPolish ) -> None:
        return self.__proxy.polish(objectToPolish)
    def proxy (self) -> QStyle:
        return self.__proxy
    def standardIcon(self, standardIcon : QStyle.StandardPixmap, option : QStyleOption = None, widget : QWidget = None ) -> QIcon:
        return self.__proxy.standardIcon(standardIcon, option, widget)
    def standardPalette (self) -> QPalette:
        return self.__proxy.standardPalette()
    def standardPixmap (self, sp : QStyle.StandardPixmap, opt : QStyleOption = None, widget : QWidget = None) -> QStyle.StandardPixmap:
        return self.__proxy.standardPixmap(sp, opt, widget)
    def styleHint(self, hint : QStyle.StyleHint, option : QStyleOption = None, widget : QWidget = None, returnData : QStyleHintReturn = None ) -> int:
        return self.__proxy.styleHint(hint, option, widget, returnData)
    def subElementRect(self, element : QStyle.SubElement, option : QStyleOption, widget : QWidget = None ) -> QRect:
        return self.__proxy.subElementRect(element, option, widget)
    def unpolish(self, objectToUnpolish ) -> None:
        self.__proxy.unpolish(objectToUnpolish)
    def	combinedLayoutSpacing (self, controls1 : QSizePolicy.ControlTypes, controls2 : QSizePolicy.ControlTypes, orientation : Qt.Orientation, option : QStyleOption = None, widget : QWidget = None ) -> int:
        return self.__proxy.combinedLayoutSpacing(controls1, controls2, orientation, option, widget)
