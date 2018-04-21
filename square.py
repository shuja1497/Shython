from screen import Screen


class Square(object):
    side = 0

    def __init__(self):
        self.w = Screen().w

    def set_side_length(self, side):
        Square.side = side

    def draw(self):
        width, height = Screen().get_screen_dimen()
        x = int(width)/2
        y = int(height)/2
        s = Square.side/2
        self.w.create_rectangle(x-s, y-s, x+s, y+s)

