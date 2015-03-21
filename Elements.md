# Introduction #

KyUI is composed of a series of widget sets and related code to ease development and provide reusable code.

# Functional Widgets #

## BasicFontWidget & FontPreviewWidget ##

BasicFontWidget provides the familiar Font combobox font size combobox pair, with optional bold, italic, and underline buttons. This functionality is commonly used in toolbars. BasicFontWidget allows developers to simply add it to a toolbar or dialog and rely on a single `currentFontChanged(QFont)` signal rather than those of five independant widgets.

FontPreviewWidget requires no real explanation. It has a `setFont(QFont)` slot and appropriately displays a preview of the font. The sample text is, of course, changeable.

## CloseButton ##

CloseButton is also a relatively simple widget, adapted from the one used by QTabBar and QDockWidget to have a consistant appearance and behavior.

## ColorButton ##

ColorButton is a QToolButton subclass that receives a color via slot and displays it as an icon. It is useful when triggering a QColorDialog and capturing the resulting color.

## ColorFrame & ColorPicker ##

ColorFrame and ColorPicker are flexible widgets for inline (not in modal dialog) selection of colors. Used in conjunction with ColorButton, it is a powerful addition to a toolbar. It is meant to allow the developer to emulate various color display popup styles (traditional Windows, Adobe Acrobat 8, Office 2007, Windows 7, to name a few) based on the developers preference. A flat frame with padding can be used to appear similar to Acrobat or Windows 7, removing the vertical spacing between ColorFrames provides an Office 2007-style appearance. The hover color, frame color, frame style, and padding between the frame and color, and spacing between frames in the ColorPicker (both horizontal and vertical) are all configurable.

## ColorSlider & ColorSpecSliders ##

ColorSlider & ColorSpecSliders are designed to allow the selection of colors by means of slider via distinct channels, similar to Photoshop. The sliders can be currently set to any channel in RGB, HSV, and HSL, with CMYK in development. ColorSpecSliders will eventually unite the three and provide a drop-in color selection widget. The slider gradient can be set as dynamic (similar to Photoshop), or traditionally display static gradients.

## KeySequenceLineEdit & KeySequenceEditor ##

KeySequenceLineEdit emulates the functionality of Qt Designer's shortcut key line editor, allowing the user to enter a key combination without having to type the characters individually or select from a ComboBox. As the user presses and releases modifiers (Ctrl, Shift, etc.) the LineEdit displays their current state. Once a standard key is pressed, the LineEdit "locks" into place the QKeySequence, and the signal `sequenceEntered(QKeySequence)` is emitted.

KeySequenceEditor is still in the design stages.

# Future Work #

## QMenu Extension ##

QMenu will be extended to provide the following features as part of a larger menu/toolbar project:
  1. Embedding of widgets within menus
  1. The ability to change separators into menu section labels
  1. A better tear-off menu hint
  1. A resize handle for menus large enough to find such a feature useful
  1. Support for sections in the widget, delineated by separators
  1. Support for larger icons and multi-line labels for key menu entries

## ToolGroups ##

ToolGroups are a concept adapted from Microsoft's Ribbon UI and a natural extension of ActionGroups. ToolGroups are a combination of a customized GroupBox and an ActionGroup. They are designed to fit within larger toolbars to provide more visible, logical grouping of related actions. Key features are:
  1. Vertical alignment to allow labels at the bottom of the GroupBox
  1. Adding QActions and QActionGroups to the ToolGroup
  1. A layout manager for the ToolGroup to properly handle the display of actions with toolbuttons
  1. Embedded widgets within the ToolGroup
  1. A dialog launch hint for ToolGroups that need such functionality

## Toolbar Extension ##

QToolBars will be subclassed and provided with the following capabilities to utilize extended QMenus and ToolGroups:
  1. ToolGroups collapsible to ToolButtons with embedded popups, similar to the Ribbon UI's compressed layout scheme
  1. A layout manager capable of utilizing ToolGroups

## Tabbed Toolbars ##

TabbedToolBar is a concept adopted from Microsoft's Ribbon UI and other prior tabbed toolbar interfaces and extended with the following:
  1. Tab context menus that provide traditional MenuBar functionality for quick access without switching tabs
  1. Handling of extended Toolbars popout functionality to allow floating toolbars (combining floating toolbars and torn out menus)
  1. Mnemonic tab switching
  1. More functionality to handle the behavior of extended toolbars and menus