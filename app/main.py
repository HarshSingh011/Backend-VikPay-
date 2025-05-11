 
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "🚀 FastAPI Project from nwnfwk;lwkp CMD is working!"}
@app.get("/home")
def home2():
    return {"message": "🚀 FastAPI Project from CMD is working!"}

