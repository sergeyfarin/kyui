from PyQt4.QtCore import *
from PyQt4.QtGui import *

def drawComplexControl(self, cc, opt, p, widget):
    if cc == QStyle.CC_Slider:
        thickness  = self.proxy().pixelMetric(QStyle.PM_SliderControlThickness, opt, widget)
        len        = self.proxy().pixelMetric(QStyle.PM_SliderLength, opt, widget)
        ticks = opt.tickPosition
        groove = self.proxy().subControlRect(QStyle.CC_Slider, opt, QStyle.SliderGroove, widget)
        handle = self.proxy().subControlRect(QStyle.CC_Slider, opt, QStyle.SliderHandle, widget)

        if (opt.subControls & QStyle.SliderGroove) and groove.isValid():
            mid = int(thickness / 2)

            if ticks & QSlider.TicksAbove:
                mid += len / 8
            if ticks & QSlider.TicksBelow:
                mid -= len / 8

            p.setPen(opt.palette.shadow().color())
            if opt.orientation == Qt.Horizontal:
                qDrawWinPanel(p, groove.x(), groove.y() + mid - 2,
                               groove.width(), 4, opt.palette, true)
                p.drawLine(groove.x() + 1, groove.y() + mid - 1,
                            groove.x() + groove.width() - 3, groove.y() + mid - 1)
            else:
                qDrawWinPanel(p, groove.x() + mid - 2, groove.y(),
                              4, groove.height(), opt.palette, true)
                p.drawLine(groove.x() + mid - 1, groove.y() + 1,
                            groove.x() + mid - 1, groove.y() + groove.height() - 3)
            
        

        if opt.subControls & QStyle.SliderTickmarks:
            tmpSlider = QStyleOptionSlider(opt)
            tmpSlider.subControls = QStyle.SliderTickmarks
            QCommonStyle.drawComplexControl(cc, tmpSlider, p, widget)
        

        if (opt.subControls & QStyle.SliderHandle):
            c0 = opt.palette.shadow().color()
            c1 = opt.palette.dark().color()
            c3 = opt.palette.midlight().color()
            c4 = opt.palette.light().color()

            if opt.state & QStyle.State_Enabled:
                handleBrush = opt.palette.color(QPalette.Button)
            else:
                handleBrush = QBrush(opt.palette.color(QPalette.Button),
                                     Qt.Dense4Pattern)
            
            x = handle.x()
            y = handle.y(),
            wi = handle.width()
            he = handle.height()

            x1 = int(x)
            x2 = x + wi - 1
            y1 = int(y)
            y2 = y + he - 1

            orient = opt.orientation
            tickAbove = opt.tickPosition == QSlider.TicksAbove
            tickBelow = opt.tickPosition == QSlider.TicksBelow

            if (opt.state & QStyle.State_HasFocus):
                fropt = QStyleOptionFocusRect()
                fropt.initFrom(opt)
                fropt.rect = self.subElementRect(QStyle.SE_SliderFocusRect, opt, widget)
                self.proxy().drawPrimitive(QStyle.FrameFocusRect, fropt, p, widget)

            if (tickAbove and tickBelow) or (not tickAbove and not tickBelow):
                oldMode = p.backgroundMode()
                p.setBackgroundMode(Qt.OpaqueMode)
                qDrawWinButton(p, QRect(x, y, wi, he), opt.palette, False,
                               handleBrush)
                p.setBackgroundMode(oldMode)
                return
            

            dir = QSliderDirection()

            if (orient == Qt.Horizontal):
                dir = SlUp if tickAbove else SlDown
            else:
                dir = SlLeft if tickAbove else SlRight

            a = QPolygon()

            if dir == SlUp:
                y1 = y1 + wi/2
                d =  (wi + 1) / 2 - 1
                a.setPoints(5, x1,y1, x1,y2, x2,y2, x2,y1, x1+d,y1-d)
            elif dir == SlDown:
                y2 = y2 - wi/2
                d =  (wi + 1) / 2 - 1
                a.setPoints(5, x1,y1, x1,y2, x1+d,y2+d, x2,y2, x2,y1)
            elif dir == SlLeft:
                d =  (he + 1) / 2 - 1
                x1 = x1 + he/2
                a.setPoints(5, x1,y1, x1-d,y1+d, x1,y2, x2,y2, x2,y1)
            elif dir == SlRight:
                d =  (he + 1) / 2 - 1
                x2 = x2 - he/2
                a.setPoints(5, x1,y1, x1,y2, x2,y2, x2+d,y1+d, x2,y1)
            
            oldBrush = p.brush()
            p.setPen(Qt.NoPen)
            p.setBrush(handleBrush)
            oldMode = p.backgroundMode()
            p.setBackgroundMode(Qt.OpaqueMode)
            p.drawRect(x1, y1, x2-x1+1, y2-y1+1)
            p.drawPolygon(a)
            p.setBrush(oldBrush)
            p.setBackgroundMode(oldMode)

            if (dir != SlUp):
                p.setPen(c4)
                p.drawLine(x1, y1, x2, y1)
                p.setPen(c3)
                p.drawLine(x1, y1+1, x2, y1+1)
            
            if (dir != SlLeft):
                p.setPen(c3)
                p.drawLine(x1+1, y1+1, x1+1, y2)
                p.setPen(c4)
                p.drawLine(x1, y1, x1, y2)
            
            if (dir != SlRight):
                p.setPen(c0)
                p.drawLine(x2, y1, x2, y2)
                p.setPen(c1)
                p.drawLine(x2-1, y1+1, x2-1, y2-1)
            
            if (dir != SlDown):
                p.setPen(c0)
                p.drawLine(x1, y2, x2, y2)
                p.setPen(c1)
                p.drawLine(x1+1, y2-1, x2-1, y2-1)
            

            if dir == SlUp:
                p.setPen(c4)
                p.drawLine(x1, y1, x1+d, y1-d)
                p.setPen(c0)
                d = wi - d - 1
                p.drawLine(x2, y1, x2-d, y1-d)
                d -= 1
                p.setPen(c3)
                p.drawLine(x1+1, y1, x1+1+d, y1-d)
                p.setPen(c1)
                p.drawLine(x2-1, y1, x2-1-d, y1-d)
            elif dir == SlDown:
                p.setPen(c4)
                p.drawLine(x1, y2, x1+d, y2+d)
                p.setPen(c0)
                d = wi - d - 1
                p.drawLine(x2, y2, x2-d, y2+d)
                d -= 1
                p.setPen(c3)
                p.drawLine(x1+1, y2, x1+1+d, y2+d)
                p.setPen(c1)
                p.drawLine(x2-1, y2, x2-1-d, y2+d)
            elif dir == SlLeft:
                p.setPen(c4)
                p.drawLine(x1, y1, x1-d, y1+d)
                p.setPen(c0)
                d = he - d - 1
                p.drawLine(x1, y2, x1-d, y2-d)
                d -= 1
                p.setPen(c3)
                p.drawLine(x1, y1+1, x1-d, y1+1+d)
                p.setPen(c1)
                p.drawLine(x1, y2-1, x1-d, y2-1-d)
            elif dir == SlRight:
                p.setPen(c4)
                p.drawLine(x2, y1, x2+d, y1+d)
                p.setPen(c0)
                d = he - d - 1
                p.drawLine(x2, y2, x2+d, y2-d)
                d -= 1
                p.setPen(c3)
                p.drawLine(x2, y1+1, x2+d, y1+1+d)
                p.setPen(c1)
                p.drawLine(x2, y2-1, x2+d, y2-1-d)


def pixelMetric(pm, opt, widget):
    if pm == QStyle.PM_SliderLength:
        return int(QStyleHelper.dpiScaled(11.0))

        # Returns the number of pixels to use for the business part of the
        # slider (i.e., the non-tickmark portion). The remaining space is shared
        # equally between the tickmark regions.
    elif pm == QStyle.PM_SliderControlThickness:
        space = sl.rect.height() if (sl.orientation == Qt.Horizontal) else sl.rect.width()
        ticks = sl.tickPosition
        n = 0
        if (ticks & QSlider.TicksAbove):
            n += 1
        if (ticks & QSlider.TicksBelow):
            n += 1
        if not n:
            return space
        
        # Magic constant to get 5 + 16 + 5
        thick = 6
        if (ticks != QSlider.TicksBothSides and ticks != QSlider.NoTicks):
            thick += self.proxy().pixelMetric(QStyle.PM_SliderLength, sl, widget) / 4

        space -= thick
        if (space > 0):
            thick += (space * 2) / (n + 2)
        return thick
    elif m == QStyle.PM_SliderThickness:
        return int(QStyleHelper.dpiScaled(16.0))
    elif m == QStyle.PM_SliderTickmarkOffset:
        space = opt.rect.height() if (sl.orientation == Qt.Horizontal) else opt.rect.width()
        thickness = self.proxy().pixelMetric(QStyle.PM_SliderControlThickness, opt, widget)
        ticks = opt.tickPosition

        if ticks == QSlider.TicksBothSides:
            return int((space - thickness) / 2)
        elif ticks == QSlider.TicksAbove:
            return space - thickness
        else:
            return 0

    elif m == QStyle.PM_SliderSpaceAvailable:
        if opt.orientation == Qt.Horizontal:
            return opt.rect.width() - self.proxy().pixelMetric(QStyle.PM_SliderLength, opt, widget)
        else:
            return opt.rect.height() - self.proxy().pixelMetric(QStyle.PM_SliderLength, opt, widget)
    else:
        return 0

def subElementRect(sr, opt, widget):
    r = QRect()
    if sr == QStyle.SE_SliderFocusRect:
        tickOffset = self.proxy().pixelMetric(QStyle.PM_SliderTickmarkOffset, opt, widget)
        thickness  = self.proxy().pixelMetric(QStyle.PM_SliderControlThickness, opt, widget)
        if (opt.orientation == Qt.Horizontal):
            r.setRect(0, tickOffset - 1, opt.rect.width(), thickness + 2)
        else:
            r.setRect(tickOffset - 1, 0, thickness + 2, opt.rect.height())
        r = r.intersected(opt.rect)
        return visualRect(opt.direction, opt.rect, r)
        
def hitTestComplexControl(cc, opt, pt, widget):
    if cc == QStyle.CC_Slider:    
        r = self.proxy().subControlRect(cc, opt, QStyle.SliderHandle, widget)
        if r.isValid() and r.contains(pt):
            return QStyle.SliderHandle
        else:
            r = self.proxy().subControlRect(cc, opt, QStyle.SliderGroove, widget)
            if r.isValid() and r.contains(pt):
                return QStyle.SliderGroove


def subControlRect(cc, opt, sc, widget):
    if cc == QStyle.CC_Slider:
        tickOffset = self.proxy().pixelMetric(QStyle.PM_SliderTickmarkOffset, opt, widget)
        thickness = self.proxy().pixelMetric(QStyle.PM_SliderControlThickness, opt, widget)

        
        if sc == QStyle.SliderHandle:
            len = self.proxy().pixelMetric(QStyle.PM_SliderLength, opt, widget)
            if opt.orientation == Qt.Horizontal:
                sliderPos = sliderPositionFromValue(opt.minimum, opt.maximum,
                                                opt.sliderPosition,
                                                opt.rect.width() - len, 
                                                opt.upsideDown)
                ret = QRect(opt.rect.x() + sliderPos, opt.rect.y() + tickOffset, len, thickness)
            else:
                sliderPos = sliderPositionFromValue(opt.minimum, opt.maximum,
                                                opt.sliderPosition,
                                                opt.rect.height() - len,
                                                opt.upsideDown)
                ret = QRect(opt.rect.x() + tickOffset, opt.rect.y() + sliderPos, thickness, len)
        elif sc == QStyle.SliderGroove:
            if opt.orientation == Qt.Horizontal:
                ret = QRect(opt.rect.x(), opt.rect.y() + tickOffset,
                            opt.rect.width(), thickness)
            else:
                ret = QRect(opt.rect.x() + tickOffset, opt.rect.y(),
                            thickness, opt.rect.height())
        else:
            ret = QRect()
        
        return visualRect(opt.direction, opt.rect, ret)
