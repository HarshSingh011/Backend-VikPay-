from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class VideoBase(BaseModel):
    title: str
    description: Optional[str] = None

class VideoCreate(VideoBase):
    pass

class Video(VideoBase):
    id: int
    file_url: str
    created_at: datetime

    class Config:
        orm_mode = True