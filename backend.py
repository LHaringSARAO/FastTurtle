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






class TurtleWorld():
    """The place where all turtle related stuff happens"""
    def __init__(self):
        self.screen = turtle.Screen()

        # self.bgcolor()
        # self.T_screen.title("Turtle World")



    def create_turtle(self, color:int ):
        leonardo = turtle.Turtle()
        possible_colors = ["red", "greed"]
        if color in possible_colors:
            leonardo.color(color=color)
        leonardo.forward(100)
        # turtle.done()
        return {"message": "Done"}