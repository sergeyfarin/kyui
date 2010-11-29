#ModelessPopup

from PyQt4.QtCore import *
from PyQt4.QtGui import *

#QApplication.focusChanged ( QWidget * old, QWidget * now )

class ModelessPopup(QDialog):
    def __init__(self, parent : QWidget = None):
        super().__init__(parent, Qt.Popup | Qt.CustomizeWindowHint)
        self.__popupOffset = QPoint(5, 5)
        
#    def popup(p : QPoint, atAction : QAction = None) -> None:
## We don't need this unless the dialog contains a scrollarea
##        if (d.scroll): # reset scroll state from last popup
##            d.scroll.scrollOffset = 0;
##            d.scroll.scrollFlags = QMenuPrivate.QMenuScroller.ScrollNone
##        }
#        motions = 0;
#        doChildEffects = true;
#        self.updateLayoutDirection();
#
#
#        self.aboutToShow.emit()
##        const bool actionListChanged = d->itemsDirty;
##        d->updateActionRects();
#        causedButton = d.causedPopup.widget()
##TODO: implement layoutChanged flag
#        if (self.layoutChanged && causedButton)
#            pos = QPushButtonPrivate.get(causedButton)->adjustedMenuPosition();
#        else
#            pos = p;
#
#
#        size = self.sizeHint();
#        screen = d->popupGeometry(QApplication.desktop().screenNumber(p))
#
#        desktopFrame = style()->pixelMetric(QStyle.PM_MenuDesktopFrameWidth, 0, this);
#        adjustToDesktop = !window().testAttribute(Qt.WA_DontShowOnScreen);
#    #ifdef QT_KEYPAD_NAVIGATION
#        if (!atAction && QApplication.keypadNavigationEnabled()):
#            // Try to have one item activated
#            if (d->defaultAction && d->defaultAction->isEnabled()):
#                atAction = d->defaultAction;
#                // TODO: This works for first level menus, not yet sub menus
#            else:
#                foreach (QAction *action, d->actions)
#                    if (action->isEnabled()):
#                        atAction = action;
#                        break;
#                    }
#            }
#            d->currentAction = atAction;
#        }
#    #endif
#        if (d->ncols > 1):
#            pos.setY(screen.top() + desktopFrame);
#        } else if (atAction):
#            for (int i = 0, above_height = 0; i < d->actions.count(); i++):
#                QAction *action = d->actions.at(i);
#                if (action == atAction):
#                    int newY = pos.y() - above_height;
#                    if (d->scroll && newY < desktopFrame):
#                        d->scroll->scrollFlags = d->scroll->scrollFlags
#                                                 | QMenuPrivate.QMenuScroller.ScrollUp;
#                        d->scroll->scrollOffset = newY;
#                        newY = desktopFrame;
#                    }
#                    pos.setY(newY);
#
#                    if (d->scroll && d->scroll->scrollFlags != QMenuPrivate.QMenuScroller.ScrollNone
#                        && !style()->styleHint(QStyle.SH_Menu_FillScreenWithScroll, 0, this)):
#                        int below_height = above_height + d->scroll->scrollOffset;
#                        for (int i2 = i; i2 < d->actionRects.count(); i2++)
#                            below_height += d->actionRects.at(i2).height();
#                        size.setHeight(below_height);
#                    }
#                    break;
#                else:
#                    above_height += d->actionRects.at(i).height();
#                }
#            }
#        }
#
#        QPoint mouse = QCursor.pos();
#        d->mousePopupPos = mouse;
#        const bool snapToMouse = (QRect(p.x() - 3, p.y() - 3, 6, 6).contains(mouse));
#
#        if (adjustToDesktop):
#            // handle popup falling "off screen"
#            if (isRightToLeft()):
#                if (snapToMouse) // position flowing left from the mouse
#                    pos.setX(mouse.x() - size.width());
#
#    #ifndef QT_NO_MENUBAR
#                // if in a menubar, it should be right-aligned
#                if (qobject_cast<QMenuBar*>(d->causedPopup.widget))
#                    pos.rx() -= size.width();
#    #endif //QT_NO_MENUBAR
#
#                if (pos.x() < screen.left() + desktopFrame)
#                    pos.setX(qMax(p.x(), screen.left() + desktopFrame));
#                if (pos.x() + size.width() - 1 > screen.right() - desktopFrame)
#                    pos.setX(qMax(p.x() - size.width(), screen.right() - desktopFrame - size.width() + 1));
#            else:
#                if (pos.x() + size.width() - 1 > screen.right() - desktopFrame)
#                    pos.setX(screen.right() - desktopFrame - size.width() + 1);
#                if (pos.x() < screen.left() + desktopFrame)
#                    pos.setX(screen.left() + desktopFrame);
#            }
#            if (pos.y() + size.height() - 1 > screen.bottom() - desktopFrame):
#                if(snapToMouse)
#                    pos.setY(qMin(mouse.y() - (size.height() + desktopFrame), screen.bottom()-desktopFrame-size.height()+1));
#                else
#                    pos.setY(qMax(p.y() - (size.height() + desktopFrame), screen.bottom()-desktopFrame-size.height()+1));
#            } else if (pos.y() < screen.top() + desktopFrame):
#                pos.setY(screen.top() + desktopFrame);
#            }
#
#            if (pos.y() < screen.top() + desktopFrame)
#                pos.setY(screen.top() + desktopFrame);
#            if (pos.y() + size.height() - 1 > screen.bottom() - desktopFrame):
#                if (d->scroll):
#                    d->scroll->scrollFlags |= uint(QMenuPrivate.QMenuScroller.ScrollDown);
#                    int y = qMax(screen.y(),pos.y());
#                    size.setHeight(screen.bottom() - (desktopFrame * 2) - y);
#                else:
#                    // Too big for screen, bias to see bottom of menu (for some reason)
#                    pos.setY(screen.bottom() - size.height() + 1);
#                }
#            }
#        }
#        setGeometry(QRect(pos, size));
#    #ifndef QT_NO_EFFECTS
#        int hGuess = isRightToLeft() ? QEffects.LeftScroll : QEffects.RightScroll;
#        int vGuess = QEffects.DownScroll;
#        if (isRightToLeft()):
#            if ((snapToMouse && (pos.x() + size.width() / 2 > mouse.x())) ||
#               (qobject_cast<QMenu*>(d->causedPopup.widget) && pos.x() + size.width() / 2 > d->causedPopup.widget->x()))
#                hGuess = QEffects.RightScroll;
#        else:
#            if ((snapToMouse && (pos.x() + size.width() / 2 < mouse.x())) ||
#               (qobject_cast<QMenu*>(d->causedPopup.widget) && pos.x() + size.width() / 2 < d->causedPopup.widget->x()))
#                hGuess = QEffects.LeftScroll;
#        }
#
#    #ifndef QT_NO_MENUBAR
#        if ((snapToMouse && (pos.y() + size.height() / 2 < mouse.y())) ||
#           (qobject_cast<QMenuBar*>(d->causedPopup.widget) &&
#            pos.y() + size.width() / 2 < d->causedPopup.widget->mapToGlobal(d->causedPopup.widget->pos()).y()))
#           vGuess = QEffects.UpScroll;
#    #endif
#        if (QApplication.isEffectEnabled(Qt.UI_AnimateMenu)):
#            bool doChildEffects = true;
#    #ifndef QT_NO_MENUBAR
#            if (QMenuBar *mb = qobject_cast<QMenuBar*>(d->causedPopup.widget)):
#                doChildEffects = mb->d_func()->doChildEffects;
#                mb->d_func()->doChildEffects = false;
#            } else
#    #endif
#            if (QMenu *m = qobject_cast<QMenu*>(d->causedPopup.widget)):
#                doChildEffects = m->d_func()->doChildEffects;
#                m->d_func()->doChildEffects = false;
#            }
#
#            if (doChildEffects):
#                if (QApplication.isEffectEnabled(Qt.UI_FadeMenu))
#                    qFadeEffect(this);
#                else if (d->causedPopup.widget)
#                    qScrollEffect(this, qobject_cast<QMenu*>(d->causedPopup.widget) ? hGuess : vGuess);
#                else
#                    qScrollEffect(this, hGuess | vGuess);
#            else:
#                // kill any running effect
#                qFadeEffect(0);
#                qScrollEffect(0);
#
#                show();
#            }
#        } else
#    #endif
#       :
#            show();
#        }
#
#    #ifndef QT_NO_ACCESSIBILITY
#        QAccessible.updateAccessibility(this, 0, QAccessible.PopupMenuStart);
#    #endif
#    }

#    def adjustedPosition() -> QPoint:
#        parent = self.parentWidget()
#        
#        # Used to determine the offset for the widget popup location
#        direction = Qt.BottomLeftCorner
#        
#        tb = parent.parentWidget()
#        if tb and isinstance(tb, QToolBar):
#            #If the toolbar is vertical, we want to adjust accordingly
#            if tb.orientation() == Qt.Vertical:
#                direction = Qt.TopRightCorner
#                
#        rect = parent.geometry()
##        rect.setRect(rect.x() - parent.x(), rect.y() - parent.y(), rect.width(), rect.height())
#
#        size = self.sizeHint()
#        globalPos = parent.mapToGlobal(rect.topLeft())
#        tlw = QApplication.topLevelAt(globalPos)
#        x = globalPos.x()
#        y = globalPos.y()
#        if (horizontal):
#            if (globalPos.y() + rect.height() + size.height() <= QApplication.desktop().availableGeometry(parent).height()):
#                y += rect.height();
#            else:
#                y -= menuSize.height();
#            if (parent.layoutDirection() == Qt.RightToLeft):
#                x += rect.width() - size.width()
#        else: #vertical
#            if (globalPos.x() + rect.width() + menu->sizeHint().width() <= QApplication.desktop().availableGeometry(parent).width())
#                x += rect.width();
#            else
#                x -= menuSize.width();
#        }
#        return QPoint(x,y)

#Note: need to determine direction to open, then if space is available in that
# direction. If it is not, find an alternate. If that doesn't work, open in
# the correct direction outside of the app geometry
    def calculateGeometry(self) -> QRect:
        offsetX = self.__popupOffset.x()
        offsetY = self.__popupOffset.y()
               
        activeWindow = QApplication.activeWindow()
        mainGeom = activeWindow.geometry()
        mainGeom.moveTo(activeWindow.mapToGlobal(mainGeom.topLeft()))
        
        #get the parent widget and its global geometry
        parent = self.parentWidget()
        parentGeom = parent.geometry()
        parentGeom.moveTo(activeWindow.mapToGlobal(parentGeom.topLeft()))
        
        size = self.sizeHint()
        
        if parent.parentWidget() and parent.parentWidget().orientation() == Qt.Vertical:
            horizontal = False
        else:
            horizontal = True
        
        #Determine the most appropriate direction to open
        def fit(size, centerMin, centerMax, edgeMin, edgeMax):
            if size < edgeMax - centerMin:
                return centerMin
            elif size < edgeMin - centerMax:
                return centerMax
            else:
                return centerMin
        
            
        if horizontal:
            if parent.layoutDirection() == Qt.LeftToRight:
                x = fit(size.width(), 
                        parentGeom.left() + offsetX, parentGeom.right() - offsetX, 
                        mainGeom.left(), mainGeom.right())
            else: #Left to right
                x = fit(size.width(), 
                        parentGeom.right() - offsetX, parentGeom.left() + offsetX, 
                        mainGeom.right(), mainGeom.left())
            y = fit(size.height(), 
                    parentGeom.bottom() + offsetY, parentGeom.top() - offsetY, 
                    mainGeom.bottom(), mainGeom.top())
        else:
            if size.height() < mainGeom.bottom() - parentGeom.bottom() - offsetY:
                y = parentGeom.bottom() + offsetY
            elif size.height() < parentGeom.top() - mainGeom.top() - offsetY:
                y = parentGeom.top() - offsetY - size.height()
            else:
                y = parentGeom.bottom() + offsetY
        rect = QRect(x, y, size.width(), size.height())
        return rect
            
    def show(self):
        rect = self.calculateGeometry()
        self.setGeometry(rect)
        super().show()
        
class GenericDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setObjectName('dialog')
        self.setWindowTitle('Test')
        #self.resize(371, 151)
        
        self.__setupUi()
        
    def __setupUi(self):
        self.__layout = QVBoxLayout(self)
        self.__layout.setObjectName('layout')
        
        button = QToolButton(self)
        button.setText('Test Button')
        button.setFixedSize(75, 23)
    
        w = ModelessPopup(button)
        w.layout = QVBoxLayout(w)
        w.buttonBox = QDialogButtonBox(QDialogButtonBox.Close, 
                                           Qt.Horizontal, w)
        w.layout.addWidget(w.buttonBox)
        w.buttonBox.clicked.connect(w.hide)
        button.clicked.connect(w.show)
        
        self.__layout.addWidget(button)
        
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok, 
                                          Qt.Horizontal, self)
        self.__layout.addWidget(self.buttonBox)
        self.buttonBox.accepted.connect(self.accept)
        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = GenericDialog()
    dialog.show()
    sys.exit(app.exec_())
