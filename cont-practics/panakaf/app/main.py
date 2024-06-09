from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def panacluod():
    return{ "Hello": " Panaversity"}
