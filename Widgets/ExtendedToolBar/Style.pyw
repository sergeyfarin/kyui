from PyQt4.QtCore import Qt, QRect, QSize, QPoint, qDebug
from PyQt4.QtGui import *
#from PyQt4.QtGui import *

TGB_CtrlList = [QStyle.SC_GroupBoxCheckBox, 
                QStyle.SC_GroupBoxLabel, 
                QStyle.SC_GroupBoxContents, 
                QStyle.SC_GroupBoxFrame]

class KyStyle(QStyle):
    ToolGroupBox = 0x00
    
    def __init__(self):
        super().__init__()
        self.__proxy = QStyleFactory.create('WindowsXP')
        
    def drawComplexControl(self, control : QStyle.ComplexControl, opt : QStyleOptionComplex, painter : QPainter, widget : QWidget = None ) -> None:
        if control != QStyle.CC_GroupBox:
            self.__proxy.drawComplexControl(control, opt, painter, widget)
        else:
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
                    self.__drawGroupBoxFocusRect(fropt, painter)
#                    self.drawPrimitive(QStyle.PE_FrameFocusRect, fropt, painter, widget)

            # Draw checkbox
            if opt.subControls & QStyle.SC_GroupBoxCheckBox:
                box = QStyleOptionButton()
                box = opt
                box.rect = checkBoxRect
                self.drawPrimitive(QStyle.PE_IndicatorCheckBox, box, painter, widget)
        
    def subControlRect(self, cc : QStyle.ComplexControl, opt : QStyleOptionComplex,
                        sc : QStyle.SubControl, widget : QWidget = None) -> QRect:
        #Handle anything that isn't relevant
        if cc != QStyle.CC_GroupBox:
            return super().subControlRect(cc, opt, sc, widget)
        if not isinstance(opt, QStyleOptionGroupBox):
            return QRect()
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
            
    def hitTestComplexControl(self, control : QStyle.ComplexControl, option : QStyleOptionComplex, position : QPoint, widget : QWidget = None ) -> QStyle.SubControl:
        if control != QStyle.CC_GroupBox:
            return self.__proxy.hitTestComplexControl(control, option, position, widget)
#        qDebug('Reached hitTestComplexControl call')
        sc = QStyle.SC_None
        
        
        for i in range(len(TGB_CtrlList)):
#            qDebug(str.format('Reached iteration: {}', i))
            r = self.subControlRect(control, option, TGB_CtrlList[i], widget)
            if r.isValid() and r.contains(position):
                sc = TGB_CtrlList[i]
                break
        return sc
    
    def drawPrimitive(self, element : QStyle.PrimitiveElement, option : QStyleOption, painter : QPainter, widget : QWidget = None ) -> None:
        self.__proxy.drawPrimitive(element, option, painter, widget)

    def __drawGroupBoxFocusRect(self, fropt : QStyleOptionFocusRect, p : QPainter):
            ### check for d->alt_down
            if not fropt.state & QStyle.State_KeyboardFocusChange and not self.styleHint(QStyle.SH_UnderlineShortcut, fropt):
                return
            r = fropt.rect
            p.save();
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
            
    def	combinedLayoutSpacing (self, controls1 : QSizePolicy.ControlTypes, controls2 : QSizePolicy.ControlTypes, orientation : Qt.Orientation, option : QStyleOption = None, widget : QWidget = None ) -> int:
        return self.__proxy.combinedLayoutSpacing(controls1, controls2, orientation, option, widget)
    
    def drawControl(self, element : QStyle.ControlElement, option : QStyleOption, painter : QPainter, widget : QWidget = None ) -> None:
        self.__proxy.drawControl(element, option, painter, widget)
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
        return self
    def sizeFromContents(self, item : QStyle.ContentsType, option : QStyleOption, contentsSize : QSize, widget : QWidget = None ) -> QSize:
        return self.__proxy.sizeFromContents(item, option, contentsSize, widget)
    def standardIcon(self, standardIcon : QStyle.StandardPixmap, option : QStyleOption = None, widget : QWidget = None ) -> QIcon:
        return self.__proxy.standardIcon(standardIcon, option, widget)
    def standardPalette (self) -> QPalette:
        return self.__proxy.standardPalette()
    def styleHint(self, hint : QStyle.StyleHint, option : QStyleOption = None, widget : QWidget = None, returnData : QStyleHintReturn = None ) -> int:
        return self.__proxy.styleHint(hint, option, widget, returnData)
    def subElementRect(self, element : QStyle.SubElement, option : QStyleOption, widget : QWidget = None ) -> QRect:
        return self.__proxy.subElementRect(element, option, widget)
    def unpolish(self, objectToUnpolish ) -> None:
        self.__proxy.unpolish(objectToUnpolish)
