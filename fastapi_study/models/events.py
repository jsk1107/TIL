from pydantic import BaseModel
from typing import List

class Event(BaseModel):

    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        json_schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://computistics.tistory.co.kr",
                "description": "나의 기술블로그",
                "tags": ["python", "fastapi", "tech blog"],
                "location": "Tistory kakao"
            }
        }