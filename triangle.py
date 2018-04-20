from screen import Screen

from Tkinter import *


class Triangle(object):
    x1, x2, x3, y1, y2, y3 = 0, 0, 0, 0, 0, 0

    def __init__(self):
        self.w = Screen().w

    def set_triangle_dimensions(self, x1, y1, x2, y2, x3, y3):
        Triangle.x1 = x1
        Triangle.y1 = y1
        Triangle.x2 = x2
        Triangle.y2 = y2
        Triangle.x3 = x3
        Triangle.y3 = y3

    def draw(self):
        points = [Triangle.x1, Triangle.y1, Triangle.x2, Triangle.y2, Triangle.x3, Triangle.y3]
        self.w.create_polygon(points)
