from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def count_root():
    return{" hello sir": " zia khan shb"}
