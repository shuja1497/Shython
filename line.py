from screen import Screen


class Line(object):
    x1, x2, y1, y2 = 0, 0, 0, 0

    def __init__(self):
        self.w = Screen().w

    def set_line_dimension(self, x1, y1, x2, y2):
        Line.x1 = x1
        Line.y1 = y1
        Line.x2 = x2
        Line.y2 = y2

    def draw(self):
        self.w.create_line(Line.x1, Line.y1, Line.x2, Line.y2)
