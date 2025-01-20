from fastapi import FastAPI


from backend import func_turtle

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello" : "Root"}


@app.get("/test_turtle")
def test_turtle():
    func_turtle()
    return None