from Initializer.screen import Screen


class Rectangle(object):
    x1, x2, y1, y2 = 0, 0, 0, 0
    fill_color = ''

    def __init__(self):
        self.w = Screen().w

    def set_rect_dimensions(self, x1, y1, x2, y2):
        Rectangle.x1 = x1
        Rectangle.y1 = y1
        Rectangle.x2 = x2
        Rectangle.y2 = y2

    def draw(self):
        self.w.create_rectangle(Rectangle.x1, Rectangle.y1, Rectangle.x2, Rectangle.y2, fill=Rectangle.fill_color)

    def set_fill_color(self, fill_color):
        Rectangle.fill_color = fill_color


