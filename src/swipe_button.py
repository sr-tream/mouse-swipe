class SwipeButton:
    button = ""
    swipe_right, swipe_left, swipe_up, swipe_down, click = [], [], [], [], []
    scroll_right, scroll_left, scroll_up, scroll_down = [], [], [], []
    freeze, scroll, moved, scrolled = False, False, False, False
    
    pressed = 0
    deltaX, deltaY = 0, 0
    delta = 0

    def __init__(self, button):
        self.button = button
