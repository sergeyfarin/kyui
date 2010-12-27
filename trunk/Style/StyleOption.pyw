from PyQt4.QtGui import QStyleOptionComplex, QStyleOptionSlider

class StyleOptionToolButtonBox(QStyleOptionComplex):
    OptionType = 0xf000001
    OptionVersion = 1
    
    def __init__(self):
        super(QStyleOptionComplex, self).__init__(OptionVersion, OptionType)
        

class StyleOptionColorSlider(QStyleOptionSlider):
    OptionType = 0xf000002
    OptionVersion = 1
    
    def __init__(self):
        super(QStyleOptionSlider, self).__init__(OptionVersion, 0xf000002)
        self.spec = None
        self.element = None
