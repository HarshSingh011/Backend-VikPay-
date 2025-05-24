from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routers import videos
from .database import engine
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Video Server API")

# Mount static files directory for serving videos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include routers
app.include_router(videos.router)