import turtle
from time import sleep
from random import randint





class TurtleWorld():
    """The place where all turtle related stuff happens"""
    def __init__(self):
        self.screen = turtle.Screen()
        self.turtle_list = []

        turtle.colormode(255)
        self.screen.bgcolor((144, 236, 144))
        self.screen.title("Turtle World")
        self.screen.screensize(2000,1500)

    def reset(self):
        """Should reset canvas and get rid of all turtles"""
        # self.screen.resetscreen()
        # NOTE the resetscreen does remove settings made, but doesnt remove the turtles
        return {"message": "screen and turtles reset"}



    def create_turtles(self, color:int = ""):
        leonardo = turtle.Turtle()
        donatello = turtle.Turtle()
        michelangelo = turtle.Turtle()
        raphael = turtle.Turtle()

        self.turtle_list.append(leonardo)
        self.turtle_list.append(donatello)
        self.turtle_list.append(michelangelo)
        self.turtle_list.append(raphael)
        return {"message": "Done"}
    

    def move_turtles(self):
        counter = 0
        for ninja in self.turtle_list:
            counter += 1
            ninja.forward(100*counter)
        return
    

    def _create_world_racing(self, track_width=100, track_height=400):
        """Creates a world """
        line_draw_turt = turtle.Turtle()
        line_draw_turt.setheading(0)
        line_draw_turt.forward(track_width)
        line_draw_turt.setheading(90)
        line_draw_turt.forward(track_height)
        line_draw_turt.setheading(270)
        line_draw_turt.forward(track_width)
        line_draw_turt.setheading(360)
        line_draw_turt.forward(track_height)


        num_turtles = 5
        turtle.colormode(255)


        for _num in range(num_turtles):
            my_turtle = turtle.Turtle()
            my_turtle.shape("turtle")
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            my_turtle.color((r,g,b))
            my_turtle.forward(100*_num)
            my_turtle.left(90)
            self.turtle_list.append(my_turtle)


    def run_turtle_race(self):
        """Run the turtle race"""
        # NOTE need to add a way to detect that the finish line has been reached.
        data = {}
        winner = False
        counter = 0
        distance_finishline = 300
        # TODO add a way in this animation to let all the turtles move at the same time
        while not winner:
            if counter > 500:
                break
            for turbo in self.turtle_list:
                sleep(0.5)
                distancee_to_travel = randint(1, 100)
                turbo.forward(distancee_to_travel)
                print(turbo.pos())
                if turbo.ycor() > distance_finishline:
                    winner = True
                    data["winner_distance"] = str(turbo.pos())
                    # how are the turtles named?

        return data


        