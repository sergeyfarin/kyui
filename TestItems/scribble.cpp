enum {
	TP_BUTTON = 1,
	TP_DROPDOWNBUTTON = 2,
	TP_SPLITBUTTON = 3,
	TP_SPLITBUTTONDROPDOWN = 4,
	TP_SEPARATOR = 5,
	TP_SEPARATORVERT = 6
};
enum {
	TS_NORMAL = 1,      //inactive
	TS_HOT = 2,         //hover
	TS_PRESSED = 3,     //down
	TS_DISABLED = 4,    //
	TS_CHECKED = 5,     //
	TS_HOTCHECKED = 6   //checked and hovered
};

enum {
    State_Hover = 0,
    State_Normal = 0,
    State_Checked = 1
} Icon_Shift_Vertical;

enum {
    IconPadding = 6,
    TextPadding = 4,
} VertToolButtonPadding;

enum {
    State_Enabled,  //Set if the button is enabled.
    State_HasFocus, //Set if the button has input focus.
    State_Raised,   //Set if the button is not down, not on and not flat.
    State_On,       //Set if the button is a toggle button and is toggled on.
    State_Sunken,   //Set if the button is down (i.e., the mouse button or the space bar is pressed on the button).
} State;
