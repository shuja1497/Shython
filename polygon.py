from screen import Screen


class Polygon(object):

    points = []
    fill_color = ''

    def __init__(self):
        self.w = Screen().w

    def set_points(self, points):
        Polygon.points = points

    def draw(self):
        # print Polygon.points
        self.w.create_polygon(Polygon.points, outline='#000', fill=Polygon.fill_color)

    def set_fill_color(self, fill_color):
        Polygon.fill_color = fill_color
