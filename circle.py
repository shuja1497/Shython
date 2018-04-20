from screen import Screen

from Tkinter import *

class Circle(object):
    radius = 0

    def __init__(self):
        self.w = Screen().w

    def set_radius(self, radius):
        Circle.radius = radius

    def get_radius(self):
        return Circle.radius

    def draw(self):
        width, height = Screen().get_screen_dimen()
        # print "/*/*/*/*/*/*/*/*/***/*/"
        x = int(width)/2
        y = int(height)/2
        self.w.create_oval(x-Circle.radius, y-Circle.radius, x+Circle.radius, y+Circle.radius)

