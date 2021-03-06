from Xlib.display import Display
from Xlib import X
from Xlib.ext.xtest import fake_input

from .stub import MouseMeta

BUTTONS = { 
    'mbleft':       1, 
    'mbmdl':        2, 
    'mbright':      3, 
    'scroll_up':    4, 
    'scroll_down':  5,
    'scroll_left':  6,
    'scroll_right': 7,
}

class Mouse(MouseMeta):
    def __init__(self, display=None):
        MouseMeta.__init__(self)
        self.display = Display(display)

    def press(self, x, y, button=1):
        if isinstance(button, str): 
            button = BUTTONS.get(button)
            if not button: return 
        self.move(x, y)
        fake_input(self.display, X.ButtonPress, button)
        self.display.sync()

    def release(self, x, y, button=1):
        if isinstance(button, str): 
            button = BUTTONS.get(button)
            if not button: return 
        self.move(x, y)
        fake_input(self.display, X.ButtonRelease, button)
        self.display.sync()

    def btn_state(self, button=1):
        pointer = self.display.screen().root.query_pointer()
        if button == 1: return pointer.mask & X.Button1Mask > 0
        if button == 2: return pointer.mask & X.Button2Mask > 0
        if button == 3: return pointer.mask & X.Button3Mask > 0
        return False

    def move(self, x, y):
        #self.display.screen().root.warp_pointer(x,y)
        fake_input(self.display, X.MotionNotify, x=x, y=y)
        self.display.sync()

    def position(self):
        pointer = self.display.screen().root.query_pointer()
        return pointer.root_x, pointer.root_y


