from fastapi import FastAPI

# for dependency injection
from fastapi import Depends
from typing import Annotated


from backend import func_turtle
from turtle_world.turtleworld import TurtleWorld

app = FastAPI()

turtleworld = TurtleWorld()
def get_TurtleWorld() ->TurtleWorld:
    """Returns the instance of the world"""
    return turtleworld 

@app.get("/")
def read_root():
    return {"Hello" : "Root"}


# @app.get("/test_turtle")
# def test_turtle():
#     func_turtle()
#     return None

@app.get("/create_turtles")
async def test_turtle_world(turtleworld: Annotated[TurtleWorld, Depends(get_TurtleWorld)]):
    turtleworld.create_turtles()


@app.get("/move_turtles")
async def test_turtle_command(turtleworld: Annotated[TurtleWorld, Depends(get_TurtleWorld)]):
    turtleworld.move_turtles()