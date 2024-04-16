from pydantic import BaseModel
from typing import List, Optional
from models.events import Event

class User(BaseModel):
    email: str
    password: str
    events: Optional[List[Event]]=None

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fasapi@packt.com",
                "username": "!!!",
                "events": []
            }
        }

class UserSignIn(BaseModel):
    email: str
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "eamil": "test@naver.com",
                "password": "Strong!!",
                "events": []
            }
        }