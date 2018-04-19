from Tkinter import *


class Screen(object):

    width = 0
    height = 0

    def __init__(self):

        self.w = None
        # self.width = 0
        # self.height = 0

    def set_screen_dimen(self, width, height):
        Screen.width = width
        Screen.height = height

    def get_screen_dimen(self):
        return self.width, self.height

    def make(self, master):
        self.w = Canvas(master=master, width=self.width, height=self.height)
        self.w.pack()
