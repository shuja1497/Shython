from Initializer.screen import Screen


class Circle(object):
    radius = 0
    fill_color = ''

    def __init__(self):
        self.w = Screen().w

    def set_radius(self, radius):
        Circle.radius = radius

    def draw(self):
        width, height = Screen().get_screen_dimen()
        x = int(width)/2
        y = int(height)/2
        self.w.create_oval(x-Circle.radius, y-Circle.radius, x+Circle.radius, y+Circle.radius, fill=Circle.fill_color)

    def set_fill_color(self, fill_color):
        Circle.fill_color = fill_color


