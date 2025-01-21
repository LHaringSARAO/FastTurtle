import turtle
from time import sleep
from random import randint





class TurtleWorld():
    """The place where all turtle related stuff happens"""
    def __init__(self):
        self.screen = turtle.Screen()
        self.turtle_list = []

        # self.bgcolor()
        # self.T_screen.title("Turtle World")

    def reset(self):
        """Should reset canvas and get rid of all turtles"""
        



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
    

    def _create_world_racing(self):
        """Creates a world """
        num_turtles = 5


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
        while not winner:
            if counter > 500:
                break
            for turbo in self.turtle_list:
                sleep(0.5)
                distancee_to_travel = randint(1, 100)
                turbo.forward(distancee_to_travel)
                print(turbo.pos())
                if turbo.xcor() > 100:
                    winner = True
                    data["winner_distance"] = str(turbo.xcor())
                    # how are the turtles named?

        return data


        