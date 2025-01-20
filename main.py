from fastapi import FastAPI


from backend import func_turtle
from backend import TurtleWorld

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello" : "Root"}


@app.get("/test_turtle")
def test_turtle():
    func_turtle()
    return None

@app.get("/test_turtle_world")
def test_turtle_world():
    turtleworld = TurtleWorld()
    turtleworld.create_turtle()