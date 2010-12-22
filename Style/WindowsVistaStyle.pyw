from PyQt4.QtCore import Qt, QRect, QSize, QPoint, qDebug, qWarning, QSysInfo
from PyQt4.QtGui import *

TGB_CtrlList = [QStyle.SC_GroupBoxCheckBox, 
                QStyle.SC_GroupBoxLabel, 
                QStyle.SC_GroupBoxContents, 
                QStyle.SC_GroupBoxFrame]
                
def PrintRect(rect : QRect):
    qDebug(str.format('QRect({}, {}, {}, {})', 
                             rect.left(), rect.top(), 
                             rect.width(), rect.height()))

class KyWindowsVistaStyle(QStyle):
    ToolGroupBox = 0x00
    CE_ToolButtonIcon = 0x01
    CE_ToolButtonLabel = 0x02
    
    def __init__(self):
        super().__init__()
        self.__proxy = QStyleFactory.create('WindowsVista')
    
    def styleName(self) -> str:
        return 'WindowsVista'
    
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
                frame = opt
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
#                self.drawPrimitive(QStyle.PE_FrameGroupBox, frame, painter, widget)
                self.__drawGroupBoxFrame(frame, painter, opt.textAlignment & Qt.AlignBottom, widget)
                painter.restore()

            # Draw title
            if (opt.subControls & QStyle.SC_GroupBoxLabel) and opt.text:
                textColor = opt.textColor
                if textColor.isValid():
                    painter.setPen(textColor)
                alignment = int(opt.textAlignment)
                if not self.styleHint(QStyle.SH_UnderlineShortcut, opt, widget):
                    alignment |= Qt.TextHideMnemonic

                self.drawItemText(painter, textRect,  Qt.TextShowMnemonic | Qt.AlignHCenter | alignment,
                             opt.palette, opt.state & QStyle.State_Enabled, opt.text,
                             ( QPalette.NoRole if textColor.isValid() else QPalette.WindowText))

                if opt.state & QStyle.State_HasFocus:
                    fropt = QStyleOptionFocusRect()
                    fropt = opt
                    fropt.backgroundColor = opt.palette.window().color()
                    fropt.rect = textRect
                    self.__drawFocusRect(fropt, painter)
#                    self.drawPrimitive(QStyle.PE_FrameFocusRect, fropt, painter, widget)

            # Draw checkbox
            if opt.subControls & QStyle.SC_GroupBoxCheckBox:
                box = QStyleOptionButton()
                box = opt
                box.rect = checkBoxRect
                self.drawPrimitive(QStyle.PE_IndicatorCheckBox, box, painter, widget)
        elif control == QStyle.CC_ToolButton and opt.toolButtonStyle == Qt.ToolButtonTextUnderIcon:
            self.__drawVerticalToolButton(control, opt, painter, widget)
        else:
            self.__proxy.drawComplexControl(control, opt, painter, widget)
    
        
    def subControlRect(self, cc : QStyle.ComplexControl, opt : QStyleOptionComplex,
                        sc : QStyle.SubControl, widget : QWidget = None) -> QRect:
        if cc == QStyle.CC_ToolButton:
            if opt.toolButtonStyle != Qt.ToolButtonTextUnderIcon:
                return self.__proxy.subControlRect(cc, opt, sc, widget)
            rect = opt.rect;
            if sc == QStyle.SC_ToolButton:
                if ((opt.features
                     & (QStyleOptionToolButton.MenuButtonPopup | QStyleOptionToolButton.PopupDelay))
                    == QStyleOptionToolButton.MenuButtonPopup):
                    rect.adjust(0, 0, 0, rect.height() / 2)
            elif sc == QStyle.SC_ToolButtonMenu:
                if ((opt.features
                     & (QStyleOptionToolButton.MenuButtonPopup | QStyleOptionToolButton.PopupDelay))
                    == QStyleOptionToolButton.MenuButtonPopup):
                    rect.adjust(0, rect.height() / 2, 0, 0)
            return rect
        elif cc == QStyle.CC_GroupBox:
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
        
    
    def __drawFocusRect(self, fropt : QStyleOptionFocusRect, p : QPainter):
            ### check for d->alt_down
            if not fropt.state & QStyle.State_KeyboardFocusChange and not self.styleHint(QStyle.SH_UnderlineShortcut, fropt):
                return
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

    def __drawGroupBoxFrame(self, frame : QStyleOptionFrameV2, p : QPainter, alignBottom : bool, widget = None):
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
    
    def drawPrimitive(self, el : QStyle.PrimitiveElement, opt : QStyleOption, p : QPainter, widget : QWidget = None ) -> None:
        self.__proxy.drawPrimitive(el, opt, p, widget)
    
    def __drawVerticalToolButton(self, cc, opt, p, widget = None):
        
        if opt.toolButtonStyle != Qt.ToolButtonIconOnly and opt.text:
            hasText = True
            textSize = opt.fontMetrics.size(Qt.TextShowMnemonic, opt.text + '  ')
        else:
            hasText = False
        if opt.icon.isNull():
            hasIcon = False
        else:
            hasIcon = True
            
        # create flags for the button section
        bflags = opt.state & ~QStyle.State_Sunken

        # Determine if the button should be drawn raised
        if bflags & QStyle.State_AutoRaise:
            if not (bflags & QStyle.State_MouseOver) or not(bflags & QStyle.State_Enabled):
                bflags &= ~QStyle.State_Raised;

        # Determine if the menu and button portions are sunken
        mflags = bflags
        if opt.state & QStyle.State_Sunken:
            if opt.activeSubControls & QStyle.SC_ToolButton:
                bflags |= QStyle.State_Sunken
            mflags |= QStyle.State_Sunken
        
        if hasText and hasIcon:
            rect1 = opt.rect.adjusted(0, 0, 0, 0 - opt.rect.height() / 2)         # Icon
            rect2 = opt.rect.adjusted(0, 0 - rect1.height(), 0, 0)                # Text
            arrowRect = QRect(rect2.left(), rect2.bottom() - 9, rect2.width(), 8) # Arrow
            self.drawPrimitive(QStyle.PE_FrameButtonTool, opt, p, widget)
#            qDrawShadePanel(p, rect1, opt.palette,
#                bflags & (QStyle.State_Sunken | QStyle.State_On), 1,
#                opt.palette.brush(QPalette.Button))
#            qDrawShadePanel(p, rect2, opt.palette,
#                mflags & (QStyle.State_Sunken | QStyle.State_On), 1,
#                opt.palette.brush(QPalette.Button))
        elif hasIcon:
            rect1 = opt.rect.adjusted(0, 0, 0, 0 - opt.rect.height() / 2)
            arrowRect = opt.rect - opt.rect.intersected(rect1)
            qDrawShadePanel(p, rect1, opt.palette,
                bflags & (QStyle.State_Sunken | QStyle.State_On), 1,
                opt.palette.brush(QPalette.Button))
            qDrawShadePanel(p, arrowRect, opt.palette,
                mflags & (QStyle.State_Sunken | QStyle.State_On), 1,
                opt.palette.brush(QPalette.Button))
        else: #It's either text or blank
            rect2 = opt.rect.adjusted(0, 0, 0, 0 - opt.rect.height() / 2)
            rect1 = None
            arrowRect = opt.rect - opt.rect.intersected(rect2)
            qDrawShadePanel(p, rect2, opt.palette,
                bflags & (QStyle.State_Sunken | QStyle.State_On), 1,
                opt.palette.brush(QPalette.Button))
            qDrawShadePanel(p, arrowRect, opt.palette,
                mflags & (QStyle.State_Sunken | QStyle.State_On), 1,
                opt.palette.brush(QPalette.Button))
            
        if hasIcon:
            ...
#            self.__drawIcon(opt, rect1, p, widget)
        if hasText:
            ...
#            self.__drawText(opt, rect2, p, widget)
        
        # Draw split
        if opt.state & QStyle.State_MouseOver:
            p1 = QPoint(1, opt.rect.height()/2)
            p2 = QPoint(opt.rect.width() - 1, p1.y())
            qDrawShadeLine(p, p1, p2, opt.palette, 1, 1, 0)
            
        self.drawItemPixmap(p, arrowRect, Qt.AlignCenter, self.__generateArrow(opt))
    
    def __drawComplexToolButton(self, cc : QStyle.ComplexControl, tbopt : QStyleOptionToolButton, p : QPainter, widget : QWidget = None):
        # Get the button rects
        button = self.subControlRect(cc, tbopt, QStyle.SC_ToolButton, widget)
        menurect = self.subControlRect(cc, tbopt, QStyle.SC_ToolButtonMenu, widget)
        PrintRect(button)
        PrintRect(menurect)
        
        # create flags for the button section
        bflags = tbopt.state & ~QStyle.State_Sunken

        # Determine if the button should be drawn raised
        if bflags & QStyle.State_AutoRaise:
            if not (bflags & State_MouseOver) or not(bflags & QStyle.State_Enabled):
                bflags &= ~State_Raised;

        # Determine if the menu and button portions are sunken
        mflags = bflags
        if tbopt.state & QStyle.State_Sunken:
            if tbopt.activeSubControls & QStyle.SC_ToolButton:
                bflags |= QStyle.State_Sunken
            mflags |= QStyle.State_Sunken
        
        # Draw the internal button
        tool = QStyleOption()
        tool.palette = tbopt.palette
        if tbopt.subControls & QStyle.SC_ToolButton:
            if bflags & (QStyle.State_Sunken | QStyle.State_On | QStyle.State_Raised):
                tool.rect = button
                tool.state = bflags
                self.drawPrimitive(QStyle.PE_PanelButtonTool, tool, p, widget)

        # Draw focus rect
        if tbopt.state & QStyle.State_HasFocus:
            fr = QStyleOptionFocusRect()
            fr = tbopt
            fr.rect.adjust(3, 3, -3, -3)
            if tbopt.features & QStyleOptionToolButton.MenuButtonPopup:
                if tbopt.toolButtonStyle == Qt.ToolButtonTextUnderIcon:
                    fr.rect.adjust(0, 0, 0, 0 - self.pixelMetric(QStyle.PM_MenuButtonIndicator, tbopt, widget))
                else:
                    fr.rect.adjust(0, 0, 0 - self.pixelMetric(QStyle.PM_MenuButtonIndicator, tbopt, widget), 0)
            self.drawPrimitive(QStyle.PE_FrameFocusRect, fr, p, widget)
        
        # Draw label and icon
        label = QStyleOptionToolButton(tbopt);
        label.state = bflags;
        fw = self.pixelMetric(QStyle.PM_DefaultFrameWidth, tbopt, widget)
        label.rect = button.adjusted(fw, fw, -fw, -fw)
        self.drawControl(QStyle.CE_ToolButtonLabel, label, p, widget)
        
        # Toolbuttonpopupmode
        if tbopt.subControls & QStyle.SC_ToolButtonMenu:
            tool.rect = menurect
            tool.state = mflags
            if mflags & (QStyle.State_Sunken | QStyle.State_On | QStyle.State_Raised):
                self.drawPrimitive(QStyle.PE_IndicatorButtonDropDown, tool, p, widget)
            self.drawPrimitive(QStyle.PE_IndicatorArrowDown, tool, p, widget)
        # Delayed or instant popup with menu
        elif tbopt.features & QStyleOptionToolButton.HasMenu:
            mbmetric = self.pixelMetric(QStyle.PM_MenuButtonIndicator, tbopt, widget);
            mbrect = tbopt.rect
            mBtn = QStyleOptionToolButton(tbopt)
            mBtn.rect = QRect(mbrect.right() + 5 - mbmetric, 
                                mbrect.y() + mbrect.height() - mbmetric + 4, 
                                mbmetric - 6, 
                                mbmetric - 6)
            self.drawPrimitive(QStyle.PE_IndicatorArrowDown, mBtn, p, widget)
            
    def __generateArrow(self, opt):
            image = QImage(5, 5, QImage.Format_ARGB32)
            image.fill(Qt.transparent)
            imagePainter = QPainter(image)
            imagePainter.setPen(opt.palette.buttonText().color())
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
    def sizeFromContents(self, ct : QStyle.ContentsType, opt : QStyleOption, sz : QSize, widget : QWidget = None ) -> QSize:
        if (ct == QStyle.CT_ToolButton and opt.toolButtonStyle == Qt.ToolButtonTextUnderIcon):
            if (opt.features
                & (QStyleOptionToolButton.MenuButtonPopup | QStyleOptionToolButton.HasMenu)):
                h = opt.iconSize.height() + 6
                w = opt.iconSize.width() + 6

                fm = opt.fontMetrics
                if opt.text:
                    textSize = fm.size(Qt.TextHideMnemonic, opt.text)
                    textSize.setWidth(textSize.width() + fm.width('  '))
                    if textSize.width() > w:
                        w = textSize.width()
                        if (textSize.height() + 8) > (66 - h):
                            h += textSize.height() + 8
                if w < 48:
                    w = 48
                if h < 76:
                    h = 76
            else:
                w = 48 if (sz.width() < 48) else sz.width()
                h = 76 if (sz.height() < 76) else sz.height()
            return QSize(w, h)
        elif (ct == QStyle.CT_MenuItem and opt.menuItemType == QStyleOptionMenuItem.Separator):
            if not opt.text:
                return QSize(sz.width(), 8)
            elif sz.height() < 20:
                sz.setHeight(20)
            return QSize(sz)            
        else:
            return self.__proxy.sizeFromContents(ct, opt, sz, widget)
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
