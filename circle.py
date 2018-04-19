from screen import Screen


class Circle(object):

    def __init__(self,radius):
        self.radius = radius
        self.w = Screen().w

    def draw(self):
        width, height = Screen().get_screen_dimen()
        x = width/2
        y = height/2
        self.w.create_oval(x-self.radius, y-self.radius, x+self.radius, y+self.radius)