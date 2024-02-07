from pydantic import BaseModel, Field

class Item(BaseModel):
    item: str
    status: str



class Todo(BaseModel):
    id: int=Field(title="고객ID", gt=0, le=1000)
    item: Item

    class Config:
        json_schema_extra = {
            "example": {
                "id": 122,
                "item": {
                    "item": "빨리 자러가고싶다.",
                    "status": "DOING"
                }
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
