 
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "🚀 FastAPI Project from CMD is working!"}

