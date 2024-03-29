#UTF-8
#colors.pyw

# Values are in ARGB format

from PyQt4.QtCore import QSize, qWarning

class ColorData():
    __slots__ = ['size', 'colors']
    def __init__(self, size, colors):
        self.size = size
        if len(colors) > size.height():
            qWarning('ColorData: row count exceeds specified size; expanding')
            self.size.setHeight(len(colors))
        for row in iter(colors):
            if len(row) > size.width():
                qWarning('ColorData: column count exceeds specified size; expanding')
                self.size.setWidth(len(row))
        self.colors = colors
    
WordFontHighlightColors = ColorData(QSize(5, 3), 
        [[0xffffff00, 0xff00ff00, 0xff00ffff, 0xffff00ff, 0xff0000ff], 
         [0xffff0000, 0xff000080, 0xff008080, 0xff008000, 0xff800080], 
         [0xff800000, 0xff808000, 0xff808080, 0xffc0c0c0, 0xff000000]])

AcrobatColors = ColorData(QSize(8, 5), 
        [[0xff000000, 0xffaa4000, 0xff404000, 0xff004000, 0xff004055, 0xff000080, 0xff4040aa, 0xff404040], 
         [0xff800000, 0xffff5500, 0xff808000, 0xff00aa00, 0xff008080, 0xff0000ff, 0xff5555aa, 0xff808080], 
         [0xffff0000, 0xffffaa00, 0xffaabf00, 0xff40aa55, 0xff40bfbf, 0xff4055ff, 0xff800080, 0xffaaaaaa], 
         [0xffff00ff, 0xffffbf00, 0xffffff00, 0xff00ff00, 0xff00ffff, 0xff00bfff, 0xffaa4055, 0xffbfbfbf], 
         [0xffffaabf, 0xffffbfaa, 0xffffe1aa, 0xffbfffbf, 0xffbfffff, 0xffaabfff, 0xffbfaaff, 0xffffffff]])

FirefoxColors = ColorData(QSize(10, 7), 
 #Grey        Red         Orange      Yellow      YellowGreen Green       Cyan        Blue        Purple      Pink
[[0xffffffff, 0xffffcccc, 0xffffcc99, 0xffffff99, 0xffffffcc, 0xff99ff99, 0xff99ffff, 0xffccffff, 0xffccccff, 0xffffccff], 
 [0xffcccccc, 0xffff6666, 0xffff9966, 0xffffff66, 0xffffff33, 0xff66ff99, 0xff33ffff, 0xff66ffff, 0xff9999ff, 0xffff99ff], 
 [0xffc0c0c0, 0xffff0000, 0xffff9900, 0xffffcc66, 0xffffff00, 0xff33ff33, 0xff66cccc, 0xff33ccff, 0xff6666cc, 0xffcc66cc], 
 [0xff999999, 0xffcc0000, 0xffff6600, 0xffffcc33, 0xffffcc00, 0xff33cc00, 0xff00cccc, 0xff3366ff, 0xff6633ff, 0xffcc33cc], 
 [0xff666666, 0xff990000, 0xffcc6600, 0xffcc9933, 0xff999900, 0xff009900, 0xff339999, 0xff3333ff, 0xff6600cc, 0xff993399], 
 [0xff333333, 0xff660000, 0xff993300, 0xff996633, 0xff666600, 0xff006600, 0xff336666, 0xff000099, 0xff333399, 0xff663366], 
 [0xff000000, 0xff330000, 0xff663300, 0xff663333, 0xff333300, 0xff003300, 0xff003333, 0xff000066, 0xff330099, 0xff330033]])
