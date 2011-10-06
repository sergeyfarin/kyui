#UTF-8
#delegate.pyw

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class PropertyDelegate(QStyledItemDelegate):
    def __init__(self, parent : QObject = None):
        super().__init__(parent)
    
    def createEditor(self, parent : QWidget, option : QStyleOptionViewItem, index : QModelIndex) -> QWidget:
        return super().createEditor(parent, option, index)
    
    def displayText(self, value : QVariant, locale : QLocale) -> str:
        return super().displayText(value, locale)
    
    def itemEditorFactory(self) -> QItemEditorFactory:
        return super().itemEditorFactory()
        
    def setItemEditorFactory(self, factory : QItemEditorFactory):
        super().setItemEditorFactory(factory)
    
    def initStyleOption(self, option : QStyleOptionViewItem, index : QModelIndex):
        super().initStyleOption(option, index)
    
    def editorEvent(self, event : QEvent, model : QAbstractItemModel, 
                    option : QStyleOptionViewItem, index : QModelIndex) -> bool:
        return super().editorEvent(event, model, option, index)
    def eventFilter (self, editor : QObject, event : QEvent) -> bool:
        return super().eventFilter(editor, event)
        
class DelegateFactory():
    def createEditor(self, datatype: QVariant.Type, parent : QWidget) -> QWidget:
        pass
    def registerEditor(self, datatype : QVariant.Type , creator : QItemEditorCreatorBase):
        pass
    def valuePropertyName(self, datatype : QVariant.Type) -> QByteArray:
        pass
