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
        self.turtle_list = []

        # self.bgcolor()
        # self.T_screen.title("Turtle World")



    def create_turtles(self, color:int = ""):
        leonardo = turtle.Turtle()
        donatello = turtle.Turtle()
        michelangelo = turtle.Turtle()
        raphael = turtle.Turtle()

        self.turtle_list.append(leonardo, donatello, michelangelo, raphael)

        return {"message": "Done"}
    

    def move_turtles(self):
        turtle1 = self.turtle_list[0]
        counter = 0
        for ninja in self.turtle_list:
            counter += 1
            ninja.forward(100*counter)
        return