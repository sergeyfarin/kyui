from collections import namedtuple


StyleCC = namedtuple('ComplexControl',  
   ['CC_Spinbox',      #0
    'CC_ComboBox',     #1
    'CC_Scrollbar',    #2
    'CC_Slider',       #3
    'CC_ToolButton',   #4
    'CC_TitleBar',     #5
    'CC_Q3ListView',   #6
    'CC_GroupBox',     #7
    'CC_Dial',         #8
    'CC_MdiControls',  #9
    'CC_CustomBase'])

def makeComplexControlEnum():
    return StyleCC._make(list(range(9)).append(0xf000000))

StyleCT = namedtuple('ControlType', 
    ['CT_PushButton',  #0
    'CT_CheckBox',     #1
    'CT_RadioButton',  #2
    'CT_ToolButton',   #3
    'CT_ComboBox',     #4
    'CT_Splitter',     #5
    'CT_Q3DockWindow', #6
    'CT_ProgressBar',  #7
    'CT_MenuItem',     #8
    'CT_MenuBarItem',  #9
    'CT_MenuBar',      #10
    'CT_Menu',         #11
    'CT_TabBarTab',    #12
    'CT_Slider',       #13
    'CT_ScrollBar',    #14
    'CT_Q3Header',     #15
    'CT_LineEdit',     #16
    'CT_SpinBox',      #17
    'CT_SizeGrip',     #18
    'CT_TabWidget',    #19
    'CT_DialogButtons',#20
    'CT_HeaderSection',#21
    'CT_GroupBox',     #22
    'CT_MdiControls',  #23
    'CT_ItemViewItem', #24
    'CT_CustomBase'])

def makeControlTypeEnum():
    return StyleCT._make(list(range(24)).append(0xf0000000))

StyleCT = namedtuple('ControlType', 
    ['CE_PushButton',           #0
    'CE_PushButtonBevel',       #1
    'CE_PushButtonLabel',       #2
    'CE_CheckBox',              #3
    'CE_CheckBoxLabel',         #4
    'CE_RadioButton',           #5
    'CE_RadioButtonLabel',      #6
    'CE_TabBarTab',             #7
    'CE_TabBarTabShape',        #8
    'CE_TabBarTabLabel',        #9
    'CE_ProgressBar',           #10
    'CE_ProgressBarGroove',     #11
    'CE_ProgressBarContents',   #12
    'CE_ProgressBarLabel',      #13
    'CE_MenuItem',              #14
    'CE_MenuScroller',          #15
    'CE_MenuVMargin',           #16
    'CE_MenuHMargin',           #17
    'CE_MenuTearoff',           #18
    'CE_MenuEmptyArea',         #19
    'CE_MenuBarItem',           #20
    'CE_MenuBarEmptyArea',      #21
    'CE_ToolButtonLabel',       #22
    'CE_Header',                #23
    'CE_HeaderSection',         #24
    'CE_HeaderLabel',           #25
    'CE_Q3DockWindowEmptyArea', #26
    'CE_ToolBoxTab',            #27
    'CE_SizeGrip',              #28
    'CE_Splitter',              #29
    'CE_RubberBand',            #30
    'CE_DockWidgetTitle',       #31
    'CE_ScrollBarAddLine',      #32
    'CE_ScrollBarSubLine',      #33
    'CE_ScrollBarAddPage',      #34
    'CE_ScrollBarSubPage',      #35
    'CE_ScrollBarSlider',       #36
    'CE_ScrollBarFirst',        #37
    'CE_ScrollBarLast',         #38
    'CE_FocusFrame',            #39
    'CE_ComboBoxLabel',         #40
    'CE_ToolBar',               #41
    'CE_ToolBoxTabShape',       #42
    'CE_ToolBoxTabLabel',       #43
    'CE_HeaderEmptyArea',       #44
    'CE_ColumnViewGrip',        #45
    'CE_ItemViewItem',          #46
    'CE_ShapedFrame',           #47
    'CE_CustomBase'])
    
def makeControlElementEnum():
    return StyleCE._make(list(range(47)).append(0xf0000000))

StylePE = namedtuple('PrimitiveElement',
    ['PE_Q3CheckListController',        #0
    'PE_Q3CheckListExclusiveIndicator', #1
    'PE_Q3CheckListIndicator',          #2
    'PE_Q3DockWindowSeparator',         #3
    'PE_Q3Separator',                   #4
    'PE_Frame',                         #5
    'PE_FrameDefaultButton',            #6
    'PE_FrameDockWidget',               #7
    'PE_FrameFocusRect',                #8
    'PE_FrameGroupBox',                 #9
    'PE_FrameLineEdit',                 #10
    'PE_FrameMenu',                     #11
    'PE_FrameStatusBarItem',            #12
    'PE_FrameTabWidget',                #13
    'PE_FrameWindow',                   #14
    'PE_FrameButtonBevel',              #15
    'PE_FrameButtonTool',               #16
    'PE_FrameTabBarBase',               #17
    'PE_PanelButtonCommand',            #18
    'PE_PanelButtonBevel',              #19
    'PE_PanelButtonTool',               #20
    'PE_PanelMenuBar',                  #21
    'PE_PanelToolBar',                  #22
    'PE_PanelLineEdit',                 #23
    'PE_IndicatorArrowDown',            #24
    'PE_IndicatorArrowLeft',            #25
    'PE_IndicatorArrowRight',           #26
    'PE_IndicatorArrowUp',              #27
    'PE_IndicatorBranch',               #28
    'PE_IndicatorButtonDropDown',       #29
    'PE_IndicatorItemViewItemCheck',    #30
    'PE_IndicatorCheckBox',             #31
    'PE_IndicatorDockWidgetResizeHandle',#32
    'PE_IndicatorHeaderArrow',          #33
    'PE_IndicatorMenuCheckMark',        #34
    'PE_IndicatorProgressChunk',        #35
    'PE_IndicatorRadioButton',          #36
    'PE_IndicatorSpinDown',             #37
    'PE_IndicatorSpinMinus',            #38
    'PE_IndicatorSpinPlus',             #39
    'PE_IndicatorSpinUp',               #40
    'PE_IndicatorToolBarHandle',        #41
    'PE_IndicatorToolBarSeparator',     #42
    'PE_PanelTipLabel',                 #43
    'PE_IndicatorTabTear',              #44
    'PE_PanelScrollAreaCorner',         #45
    'PE_Widget',                        #46
    'PE_IndicatorColumnViewArrow',      #47
    'PE_IndicatorItemViewItemDrop',     #48
    'PE_PanelItemViewItem',             #49
    'PE_PanelItemViewRow',              #50
    'PE_PanelStatusBar',                #51
    'PE_IndicatorTabClose',             #52
    'PE_PanelMenu',                     #53
    'PE_FrameStatusBar',                #12
    'PE_IndicatorViewItemCheck',        #30
    'PE_CustomBase'])

def makePrimitiveElementEnum():
    vals = list(range(53))
    vals.append(12)
    vals.append(30)
    vals.append(0xf000000)
    return StylePE._make(vals)

StyleSC = namedtuple('SubControl',
    ['SC_None', 
    'SC_ScrollBarAddLine', 
    'SC_ScrollBarSubLine', 
    'SC_ScrollBarAddPage', 
    'SC_ScrollBarSubPage', 
    'SC_ScrollBarFirst', 
    'SC_ScrollBarLast', 
    'SC_ScrollBarSlider', 
    'SC_ScrollBarGroove', 
    'SC_SpinBoxUp', 
    'SC_SpinBoxDown', 
    'SC_SpinBoxFrame', 
    'SC_SpinBoxEditField', 
    'SC_ComboBoxEditField', 
    'SC_ComboBoxArrow', 
    'SC_ComboBoxFrame', 
    'SC_ComboBoxListBoxPopup', 
    'SC_SliderGroove', 
    'SC_SliderHandle', 
    'SC_SliderTickmarks', 
    'SC_ToolButton', 
    'SC_ToolButtonMenu', 
    'SC_TitleBarSysMenu', 
    'SC_TitleBarMinButton', 
    'SC_TitleBarMaxButton', 
    'SC_TitleBarCloseButton', 
    'SC_TitleBarLabel', 
    'SC_TitleBarNormalButton', 
    'SC_TitleBarShadeButton', 
    'SC_TitleBarUnshadeButton', 
    'SC_TitleBarContextHelpButton', 
    'SC_Q3ListView', 
    'SC_Q3ListViewExpand', 
    'SC_DialHandle', 
    'SC_DialGroove', 
    'SC_DialTickmarks', 
    'SC_GroupBoxFrame', 
    'SC_GroupBoxLabel', 
    'SC_GroupBoxCheckBox', 
    'SC_GroupBoxContents', 
    'SC_MdiNormalButton', 
    'SC_MdiMinButton', 
    'SC_MdiCloseButton', 
    'SC_All'])
    
def makeSubControlEnum():
    return StyleSC._make([0x00000000, #SC_None
            0x00000001, #SC_ScrollBarAddLine
            0x00000002, #SC_ScrollBarSubLine
            0x00000004, #SC_ScrollBarAddPage
            0x00000008, #SC_ScrollBarSubPage
            0x00000010, #SC_ScrollBarFirst
            0x00000020, #SC_ScrollBarLast
            0x00000040, #SC_ScrollBarSlider
            0x00000080, #SC_ScrollBarGroove

            0x00000001, #SC_SpinBoxUp
            0x00000002, #SC_SpinBoxDown
            0x00000004, #SC_SpinBoxFrame
            0x00000008, #SC_SpinBoxEditField

            0x00000001, #SC_ComboBoxFrame
            0x00000002, #SC_ComboBoxEditField
            0x00000004, #SC_ComboBoxArrow
            0x00000008, #SC_ComboBoxListBoxPopup

            0x00000001, #SC_SliderGroove
            0x00000002, #SC_SliderHandle
            0x00000004, #SC_SliderTickmarks

            0x00000001, #SC_ToolButton
            0x00000002, #SC_ToolButtonMenu

            0x00000001, #SC_TitleBarSysMenu
            0x00000002, #SC_TitleBarMinButton
            0x00000004, #SC_TitleBarMaxButton
            0x00000008, #SC_TitleBarCloseButton
            0x00000010, #SC_TitleBarNormalButton
            0x00000020, #SC_TitleBarShadeButton
            0x00000040, #SC_TitleBarUnshadeButton
            0x00000080, #SC_TitleBarContextHelpButton
            0x00000100, #SC_TitleBarLabel

            0x00000001, #SC_Q3ListView
            0x00000002, #SC_Q3ListViewBranch
            0x00000004, #SC_Q3ListViewExpand

            0x00000001, #SC_DialGroove
            0x00000002, #SC_DialHandle
            0x00000004, #SC_DialTickmarks

            0x00000001, #SC_GroupBoxCheckBox
            0x00000002, #SC_GroupBoxLabel
            0x00000004, #SC_GroupBoxContents
            0x00000008, #SC_GroupBoxFrame

            0x00000001, #SC_MdiMinButton
            0x00000002, #SC_MdiNormalButton
            0x00000004, #SC_MdiCloseButton

            0xf0000000, #SC_CustomBase
            0xffffffff]) #SC_All)

StylePM = namedtuple('PixelMetric',
   ['PM_ButtonMargin',
   'PM_ButtonDefaultIndicator',
   'PM_MenuButtonIndicator',
   'PM_ButtonShiftHorizontal',
   'PM_ButtonShiftVertical',
   'PM_DefaultFrameWidth',
   'PM_SpinBoxFrameWidth',
   'PM_ComboBoxFrameWidth',
   'PM_MaximumDragDistance',
   'PM_ScrollBarExtent',
   'PM_ScrollBarSliderMin',
   'PM_SliderThickness',
   'PM_SliderControlThickness',
   'PM_SliderLength',
   'PM_SliderTickmarkOffset',
   'PM_SliderSpaceAvailable',
   'PM_DockWidgetSeparatorExtent',
   'PM_DockWidgetHandleExtent',
   'PM_DockWidgetFrameWidth',
   'PM_TabBarTabOverlap',
   'PM_TabBarTabHSpace',
   'PM_TabBarTabVSpace',
   'PM_TabBarBaseHeight',
   'PM_TabBarBaseOverlap',
   'PM_ProgressBarChunkWidth',
   'PM_SplitterWidth',
   'PM_TitleBarHeight',
   'PM_MenuScrollerHeight',
   'PM_MenuHMargin',
   'PM_MenuVMargin',
   'PM_MenuPanelWidth',
   'PM_MenuTearoffHeight',
   'PM_MenuDesktopFrameWidth',
   'PM_MenuBarPanelWidth',
   'PM_MenuBarItemSpacing',
   'PM_MenuBarVMargin',
   'PM_MenuBarHMargin',
   'PM_IndicatorWidth',
   'PM_IndicatorHeight',
   'PM_ExclusiveIndicatorWidth',
   'PM_ExclusiveIndicatorHeight',
   'PM_CheckListButtonSize',
   'PM_CheckListControllerSize',
   'PM_DialogButtonsSeparator',
   'PM_DialogButtonsButtonWidth',
   'PM_DialogButtonsButtonHeight',
   'PM_MdiSubWindowFrameWidth',
   'PM_MdiSubWindowMinimizedWidth',
   'PM_HeaderMargin',
   'PM_HeaderMarkSize',
   'PM_HeaderGripMargin',
   'PM_TabBarTabShiftHorizontal',
   'PM_TabBarTabShiftVertical',
   'PM_TabBarScrollButtonWidth',
   'PM_ToolBarFrameWidth',
   'PM_ToolBarHandleExtent',
   'PM_ToolBarItemSpacing',
   'PM_ToolBarItemMargin',
   'PM_ToolBarSeparatorExtent',
   'PM_ToolBarExtensionExtent',
   'PM_SpinBoxSliderHeight',
   'PM_DefaultTopLevelMargin',
   'PM_DefaultChildMargin',
   'PM_DefaultLayoutSpacing',
   'PM_ToolBarIconSize',
   'PM_ListViewIconSize',
   'PM_IconViewIconSize',
   'PM_SmallIconSize',
   'PM_LargeIconSize',
   'PM_FocusFrameVMargin',
   'PM_FocusFrameHMargin',
   'PM_ToolTipLabelFrameWidth',
   'PM_CheckBoxLabelSpacing',
   'PM_TabBarIconSize',
   'PM_SizeGripSize',
   'PM_DockWidgetTitleMargin',
   'PM_MessageBoxIconSize',
   'PM_ButtonIconSize',
   'PM_DockWidgetTitleBarButtonMargin',
   'PM_RadioButtonLabelSpacing',
   'PM_LayoutLeftMargin',
   'PM_LayoutTopMargin',
   'PM_LayoutRightMargin',
   'PM_LayoutBottomMargin',
   'PM_LayoutHorizontalSpacing',
   'PM_LayoutVerticalSpacing',
   'PM_TabBar_ScrollButtonOverlap',
   'PM_TextCursorWidth',
   'PM_TabCloseIndicatorWidth',
   'PM_TabCloseIndicatorHeight',
   'PM_ScrollView_ScrollBarSpacing',
   'PM_SubMenuOverlap',
    
   'PM_MDIMinimizedWidth', #47
   'PM_MDIFrameWidth', #46
   'PM_CustomBase']) #0xf0000000

def makePixelMetricEnum():
    vals = list(range(91))
    vals.append(46)
    vals.append(47)
    vals.append(0xf0000000)
    return StylePM._make(vals)
    
