SRCCOPY = 13369376

# Handle
HWND_BROADCAST = 65535
HWND_DESKTOP = 0
HWND_TOP = 0
HWND_BOTTOM = 1
HWND_TOPMOST = -1
HWND_NOTOPMOST = -2
HWND_MESSAGE = -3

# Window
GW_HWNDFIRST = 0
GW_HWNDLAST = 1
GW_HWNDNEXT = 2
GW_HWNDPREV = 3
GW_OWNER = 4
GW_CHILD = 5
GW_ENABLEDPOPUP = 6
GWL_EXSTYLE  = -20
GWL_HINSTANCE = -6
GWL_HWNDPARENT = -8
GWL_ID = -12
GWL_STYLE = -16
GWL_USERDATA = -21
GWL_WNDPROC = -4 

WS_OVERLAPPED = 0
WS_POPUP = -2147483648
WS_CHILD = 1073741824
WS_MINIMIZE = 536870912
WS_VISIBLE = 268435456
WS_DISABLED = 134217728
WS_CLIPSIBLINGS = 67108864
WS_CLIPCHILDREN = 33554432
WS_MAXIMIZE = 16777216
WS_CAPTION = 12582912
WS_BORDER = 8388608
WS_DLGFRAME = 4194304
WS_VSCROLL = 2097152
WS_HSCROLL = 1048576
WS_SYSMENU = 524288
WS_THICKFRAME = 262144
WS_GROUP = 131072
WS_TABSTOP = 65536
WS_MINIMIZEBOX = 131072
WS_MAXIMIZEBOX = 65536
WS_TILED = WS_OVERLAPPED
WS_ICONIC = WS_MINIMIZE
WS_SIZEBOX = WS_THICKFRAME
WS_OVERLAPPEDWINDOW = (WS_OVERLAPPED|WS_CAPTION|WS_SYSMENU| \
                       WS_THICKFRAME|WS_MINIMIZEBOX|WS_MAXIMIZEBOX)

WS_POPUPWINDOW = (WS_POPUP|WS_BORDER|WS_SYSMENU)
WS_CHILDWINDOW = WS_CHILD
WS_TILEDWINDOW = WS_OVERLAPPEDWINDOW
WS_EX_DLGMODALFRAME = 1
WS_EX_NOPARENTNOTIFY = 4
WS_EX_TOPMOST = 8
WS_EX_ACCEPTFILES = 16
WS_EX_TRANSPARENT = 32
WS_EX_MDICHILD = 64
WS_EX_TOOLWINDOW = 128
WS_EX_WINDOWEDGE = 256
WS_EX_CLIENTEDGE = 512
WS_EX_CONTEXTHELP = 1024
WS_EX_RIGHT = 4096
WS_EX_LEFT = 0
WS_EX_RTLREADING = 8192
WS_EX_LTRREADING = 0
WS_EX_LEFTSCROLLBAR = 16384
WS_EX_RIGHTSCROLLBAR = 0
WS_EX_CONTROLPARENT = 65536
WS_EX_STATICEDGE = 131072
WS_EX_APPWINDOW = 262144
WS_EX_OVERLAPPEDWINDOW = (WS_EX_WINDOWEDGE|WS_EX_CLIENTEDGE)
WS_EX_PALETTEWINDOW = (WS_EX_WINDOWEDGE|WS_EX_TOOLWINDOW|WS_EX_TOPMOST)
WS_EX_LAYERED = 0x00080000
WS_EX_NOINHERITLAYOUT = 0x00100000
WS_EX_LAYOUTRTL = 0x00400000
WS_EX_COMPOSITED = 0x02000000
WS_EX_NOACTIVATE = 0x08000000

# Keyboard
KEYBD_EXTENDEDKEY = 1
KEYBD_KEYUP       = 2
KEYBD_UNICODE     = 4
KEYBD_SCANCODE    = 8

VK_LBUTTON = 1
VK_RBUTTON = 2
VK_CANCEL = 3
VK_MBUTTON = 4
VK_BACK = 8
VK_TAB = 9
VK_CLEAR = 12
VK_RETURN = 13
VK_ENTER = 13
VK_SHIFT = 16
VK_CONTROL = 17
VK_MENU = 18
VK_PAUSE = 19
VK_CAPITAL = 20
VK_KANA = 21
VK_HANGUL = 21
VK_JUNJA = 23
VK_FINAL = 24
VK_HANJA = 25
VK_KANJI = 25
VK_ESCAPE = 27
VK_CONVERT = 28
VK_NONCONVERT = 29
VK_ACCEPT = 30
VK_MODECHANGE = 31
VK_SPACE = 32
VK_PRIOR = 33
VK_NEXT = 34
VK_END = 35
VK_HOME = 36
VK_LEFT = 37
VK_UP = 38
VK_RIGHT = 39
VK_DOWN = 40
VK_SELECT = 41
VK_PRINT = 42
VK_EXECUTE = 43
VK_SNAPSHOT = 44
VK_INSERT = 45
VK_DELETE = 46
VK_HELP = 47
VK_LWIN = 91
VK_RWIN = 92
VK_APPS = 93
VK_NUMPAD0 = 96
VK_NUMPAD1 = 97
VK_NUMPAD2 = 98
VK_NUMPAD3 = 99
VK_NUMPAD4 = 100
VK_NUMPAD5 = 101
VK_NUMPAD6 = 102
VK_NUMPAD7 = 103
VK_NUMPAD8 = 104
VK_NUMPAD9 = 105
VK_MULTIPLY = 106
VK_ADD = 107
VK_SEPARATOR = 108
VK_SUBTRACT = 109
VK_DECIMAL = 110
VK_DIVIDE = 111
VK_F1 = 112
VK_F2 = 113
VK_F3 = 114
VK_F4 = 115
VK_F5 = 116
VK_F6 = 117
VK_F7 = 118
VK_F8 = 119
VK_F9 = 120
VK_F10 = 121
VK_F11 = 122
VK_F12 = 123
VK_F13 = 124
VK_F14 = 125
VK_F15 = 126
VK_F16 = 127
VK_F17 = 128
VK_F18 = 129
VK_F19 = 130
VK_F20 = 131
VK_F21 = 132
VK_F22 = 133
VK_F23 = 134
VK_F24 = 135
VK_NUMLOCK = 144
VK_SCROLL = 145
VK_LSHIFT = 160
VK_RSHIFT = 161
VK_LCONTROL = 162
VK_RCONTROL = 163
VK_LMENU = 164
VK_RMENU = 165
VK_PROCESSKEY = 229
VK_ATTN = 246
VK_CRSEL = 247
VK_EXSEL = 248
VK_EREOF = 249
VK_PLAY = 250
VK_ZOOM = 251
VK_NONAME = 252
VK_PA1 = 253
VK_OEM_CLEAR = 254

# multi-media related "keys"
VK_XBUTTON1 = 0x05
VK_XBUTTON2 = 0x06
VK_VOLUME_MUTE = 0xAD
VK_VOLUME_DOWN = 0xAE
VK_VOLUME_UP = 0xAF
VK_MEDIA_NEXT_TRACK = 0xB0
VK_MEDIA_PREV_TRACK = 0xB1
VK_MEDIA_PLAY_PAUSE = 0xB3
VK_BROWSER_BACK = 0xA6
VK_BROWSER_FORWARD = 0xA7

# Mouse related
MOUSE_ABSOLUTE = 32768
MOUSE_MOVE = 1
MOUSE_LEFTDOWN = 2
MOUSE_LEFTUP = 4
MOUSE_RIGHTDOWN = 8
MOUSE_RIGHTUP = 16
MOUSE_MIDDLEDOWN = 32
MOUSE_MIDDLEUP = 64
MOUSE_ABSOLUTE = 32768
MOUSE_XDOWN = 0x0080
MOUSE_XUP = 0x0100
MOUSE_WHEEL = 0x0800
MOUSE_HWHEEL = 0x01000

IDC_ARROW = 32512
IDC_IBEAM = 32513
IDC_WAIT = 32514
IDC_CROSS = 32515
IDC_UPARROW = 32516
IDC_SIZE = 32640 # OBSOLETE: use IDC_SIZEALL
IDC_ICON = 32641 # OBSOLETE: use IDC_ARROW
IDC_SIZENWSE = 32642
IDC_SIZENESW = 32643
IDC_SIZEWE = 32644
IDC_SIZENS = 32645
IDC_SIZEALL = 32646
IDC_NO = 32648
IDC_HAND = 32649
IDC_APPSTARTING = 32650
IDC_HELP = 32651

# Screen releated
SM_XVIRTUALSCREEN = 76
SM_YVIRTUALSCREEN = 77
SM_CXVIRTUALSCREEN = 78
SM_CYVIRTUALSCREEN = 79

# Error handling
ERROR_SUCCESS = 0
ERROR_INVALID_FUNCTION = 1
ERROR_FILE_NOT_FOUND = 2
ERROR_PATH_NOT_FOUND = 3
ERROR_ACCESS_DENIED = 5
ERROR_INVALID_HANDLE = 6
ERROR_NOT_ENOUGH_MEMORY = 8
ERROR_INVALID_DRIVE = 15
ERROR_NO_MORE_FILES = 18