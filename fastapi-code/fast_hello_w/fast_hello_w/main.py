from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def index():
    return {"hello" : "World now"}
   

@app.get("/piaic")
def piaic():
    return{"batch":"panaverse"}

@app.get("/mart")
def mart():
    return{"pakistani " : "mart"}
