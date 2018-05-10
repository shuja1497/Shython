from Tkinter import *


class Screen(object):

    width = 0
    height = 0
    w = None

    def __init__(self):
        pass

    def set_screen_dimen(self, width, height):
        Screen.width = width
        Screen.height = height

    def get_screen_dimen(self):
        return Screen.width, Screen.height

    def make(self, master):
        master.title("SHYTHON")
        Screen.w = Canvas(master=master, width=Screen.width, height=Screen.height)
        Screen.w.pack()
