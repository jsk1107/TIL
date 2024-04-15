from pydantic import BaseModel, Field
from typing import List, Optional
from fastapi import Form

class Item(BaseModel):
    item: str
    status: str

class Todo(BaseModel):
    id: Optional[int]=None
    item: str=Field(title="ToDos")

    @classmethod
    def as_form(cls, item: str=Form(...)):
        return cls(item=item)

    class Config:
        json_schema_extra = {
            "example": {
                "id": 122,
                "item": "DOING"
            }
        }

class TodoItem(BaseModel):
    item: str

    class Config:
        json_schema_extra = {
            "example": {
                "item": "Read the next chaper of the book."
            }
        }

class TodoItems(BaseModel):
    todos: List[TodoItem]

    class config:
        json_schema_extra = {
            "example": {
                "todos": [
                {
                    "item": "Example schema1!"
                },
                {
                    "item": "Example schema2!"
                }
            ]
            }
        }