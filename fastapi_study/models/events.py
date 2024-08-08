from pydantic import BaseModel
from sqlmodel import JSON, SQLModel, Field, Column
from typing import List, Optional

class Event(SQLModel, table=True):

    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://computistics.tistory.co.kr",
                "description": "나의 기술블로그",
                "tags": ["python", "fastapi", "tech blog"],
                "location": "Tistory kakao"
            }
        }

class EventUpdate(SQLModel):
    title: Optional[str]=None
    image: Optional[str]=None
    description: Optional[str]=None
    tags: Optional[str]=None
    location: Optional[str]=None

    class Config:
        json_schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "hahahaha",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }