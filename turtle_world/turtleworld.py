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
        # self.screen.screensize(2000,1500) remove when full screen app is present
        self.screen.setup(width=1.0, height=1.0)

    def reset(self):
        """Should reset canvas and get rid of all turtles"""
        # self.screen.resetscreen()
        self.screen.clearscreen()
        turtle.bye()
        self.__init__()
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
        line_draw_turt.setheading(90)
        line_draw_turt.forward(track_width)
        line_draw_turt.setheading(0)
        line_draw_turt.forward(track_height)
        line_draw_turt.setheading(270)
        line_draw_turt.forward(track_width)
        line_draw_turt.setheading(360)
        line_draw_turt.forward(track_height)


        num_turtles = 5
        # turtle.colormode(255)


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
            sleep(0.5)
            for turbo in self.turtle_list:
                distancee_to_travel = randint(1, 100)
                turbo.forward(distancee_to_travel)
                print(turbo.pos())
                if turbo.ycor() > distance_finishline:
                    winner = True
                    data["winner_distance"] = str(turbo.pos())
                    # how are the turtles named?

        return data



    def make_turtle_race2(self, num_racers=3):
        HEIGHT = 1000
        X_START = -900
        X_FINISHLINE = 500
        self.X_FINISHLINE = X_FINISHLINE

        POS_BOTTOM_LEFT = (-925, -525)
        POS_TOP_LEFT = (-925, 525)
        POS_TOP_RIGHT = (925, 525)
        POS_BOTTOM_RIGHT = (925, -525)

        pos_turtle = turtle.Turtle()
        pos_turtle.color('black')
        pos_turtle.penup()
        pos_turtle.goto(POS_BOTTOM_LEFT)
        pos_turtle.pendown()
        pos_turtle.goto(POS_TOP_LEFT)
        pos_turtle.goto(POS_TOP_RIGHT)
        pos_turtle.goto(POS_BOTTOM_RIGHT)
        pos_turtle.goto(POS_BOTTOM_LEFT)

        pos_turtle.penup()
        pos_turtle.goto(X_FINISHLINE, 900)
        pos_turtle.pendown()
        pos_turtle.goto(X_FINISHLINE, -900)
        pos_turtle.penup()
        pos_turtle.isvisible(False)


        colors = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purlpe', 'pink', 'brown', 'cyan']
        spacing = HEIGHT/(len(colors)+1)
        i = 0
        for num_racer in range(0, num_racers):
            i += 1
            new_turtle = turtle.Turtle()
            new_turtle.penup()
            new_turtle.goto(-925, -500+i*spacing)
            try:
                t_color = colors[num_racer]
            except:
                t_color = 'black'
            new_turtle.color(t_color)
            self.turtle_list.append(new_turtle)

        return None
    


    def race_turtles2(self):
        """Move turtles forward by distance, repeat until one crossed the finifh line"""
        winners = []
        race_in_progress = True
        while race_in_progress:
            for racer in self.turtle_list:
                racer.forward(randint(1, 50))
            for racer in self.turtle_list:
                if racer.xcor() > self.X_FINISHLINE:
                    winners.append(racer.color())
            if len(winners) >= 1:
                race_in_progress = False

        return winners

