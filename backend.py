import turtle
from time import sleep

# Screen stuff


def func_turtle():

    wn = turtle.Screen()
    wn.bgcolor()
    wn.title("Title")


    skk = turtle.Turtle()
    skk.forward(100)
    turtle.done()
    sleep(2)













class TurtleWorld(turtle.Screen):
    """The place where all turtle related stuff happens"""
    def __init__(self):
        super().__init__()

        # self.bgcolor()
        # self.T_screen.title("Turtle World")



    def create_turtle(self):
        leonardo = turtle.Turtle()
        leonardo.forward(100)
        turtle.done()