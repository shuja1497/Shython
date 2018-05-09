from Initializer.screen import Screen


class Square(object):
    side = 0
    fill_color = ''

    def __init__(self):
        self.w = Screen().w

    def set_side_length(self, side):
        Square.side = side

    def draw(self):
        width, height = Screen().get_screen_dimen()
        x = int(width)/2
        y = int(height)/2
        s = Square.side/2
        self.w.create_rectangle(x-s, y-s, x+s, y+s, fill=Square.fill_color)

    def set_fill_color(self, fill_color):
        Square.fill_color = fill_color


