from PyQt4.QtCore import *
from PyQt4.QtGui import *

from .format import *

class PropertyView(QTreeView):
    bgColors = [(QColor(255, 230, 191), QColor(255, 242, 222)), #Orange
                (QColor(255, 255, 191), QColor(255, 255, 222)), #Yellow
                (QColor(191, 255, 191), QColor(222, 255, 222)), #Green
                (QColor(199, 255, 255), QColor(230, 255, 255)), #Blue
                (QColor(234, 191, 255), QColor(244, 222, 255)), #Purple
                (QColor(255, 191, 239), QColor(255, 222, 247))] #Pink
                
    def __init__(self, qobj : QObject = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = QStandardItemModel(self)
        self.__initPrototypeItems()
        self.setModel(self.model)
        
        if qobj:
            self.__initModel(qobj)
        self.setColumnWidth(0, 200)
        self.setColumnWidth(1, 300)
        
        
    def __initPrototypeItems(self):
        item = QStandardItem('')
        #item.setRowCount(rows)
        item.setSelectable(True)
        item.setEnabled(True)
        item.setEditable(False)
        font = QFont('Segoe UI', 9)
        item.setFont(font)
        
        self.model.setItemPrototype(item)
        
        font.setBold(True)
        self.grpItem = item.clone()
        self.grpItem.setFont(font)
        self.grpItem.setBackground(QBrush(Qt.gray))
        self.grpItem.setForeground(QBrush(Qt.white))
        
        self.col1Item = item.clone()
        self.col2Item = item.clone()
        self.col2Item.setEditable(True)
        self.col3Item = item.clone()

        #item.setCheckState(state)
        #item.setSizeHint(size)
        
        #item.setData(value, role)

        #item.setIcon(icon)
        #item.setText(text)
        
        #item.setTextAlignment(alignment)
        #item.setAccessibleDescription(accessibleDescription)
        #item.setAccessibleText(accessibleText)
        #item.setStatusTip(statusTip)
        #item.setToolTip(toolTip)
        #item.setWhatsThis(whatsThis)
        
        #item.setChild(row, column, item)
        #item.setChild(row, item)
        
    def __initModel(self, qobj):
        assert(isinstance(qobj, QObject))
        
        self.model.clear()
        self.model.setHorizontalHeaderLabels(['Property', 'Value', 'Type'])
        mobj = qobj.metaObject()
        
        classes = [mobj, ]
        while mobj.superClass():
            mobj = mobj.superClass()
            classes.insert(0, mobj)
        self.colorindex = 0
        for mobj in classes:
            parent = self.grpItem.clone()
            parent.setText(mobj.className())
            parent.setData(mobj, Qt.UserRole)
            
            if mobj.propertyCount():
                offset = mobj.propertyOffset()
                light = False
                for index in range(offset, mobj.propertyCount()):
                    prop = mobj.property(index)
                    row = self.createPropertyRow(prop, parent, qobj, light)
                    if row: parent.appendRow(row)
                    light = False if light else True
            self.model.appendRow(parent)
            
            pidx = self.model.indexFromItem(parent)
            self.setExpanded(self.model.indexFromItem(parent), True)
            self.setFirstColumnSpanned(pidx.row(), pidx.parent(), True)
            
            if self.colorindex < len(PropertyView.bgColors) -1:
                self.colorindex += 1
            else:
                self.colorindex = 0

    def createPropertyRow(self, prop, parent, widget, light):
        if (prop.isValid() and prop.isReadable() and prop.isDesignable()
                and prop.isWritable()):
            value = prop.read(widget)
            propType = prop.typeName()
            icon = None
            enum = None
            if value == None or isinstance(value, QPyNullVariant):
                text = ''
            elif prop.isEnumType():
                enum = prop.enumerator()
                propType = enum.name()
                if enum.isFlag():
                    text = enum.valueToKeys(int(value)).data().decode()
                else:
                    text = enum.valueToKey(int(value))
            elif propType in FormattableTypes:
                if propType in IconTypes:
                    icon = IconTypes[propType](value)
                text = FormatQType(value, propType)
            else:
                text = str(value)
            #get background brush
            if light:
                brush = QBrush(PropertyView.bgColors[self.colorindex][1])
            else:
                brush = QBrush(PropertyView.bgColors[self.colorindex][0])
            
            #clone items
            item1 = self.col1Item.clone()
            item2 = self.col2Item.clone()
            item3 = self.col3Item.clone()
            
            item1.setText(prop.name())
            item1.setBackground(brush)
            item1.setData(prop, Qt.UserRole)
            
            item2.setText(text)
            item2.setBackground(brush)
            item2.setData(value, Qt.UserRole)
            
            item3.setText(propType)
            item3.setBackground(brush)
            item3.setData(enum, Qt.UserRole)
            
            if icon:
                item2.setIcon(icon)
            return [item1, item2, item3]
        return None
