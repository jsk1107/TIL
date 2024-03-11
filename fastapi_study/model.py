from pydantic import BaseModel, Field
from typing import List

class Item(BaseModel):
    item: str
    status: str

class Todo(BaseModel):
    id: int=Field(title="고객ID", gt=0, le=1000)
    item: str=Field(title="ToDos")

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