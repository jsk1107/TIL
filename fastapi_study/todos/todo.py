from fastapi import APIRouter, Path, HTTPException, status
from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()

todo_list = []

@todo_router.post('/todo', status_code=201)
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully."}

@todo_router.get('/todo', response_model=TodoItems)
async def retrieve_todos() -> dict:
    return {"todos": todo_list}

@todo_router.get('/todo/{todo_id}') # 경로매개변수
async def get_single_todo(todo_id: int=Path(..., title="The ID of the todo to retrive", gt=0, le=1000)) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {'todo': todo}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo with supplied ID doesn't exist.")

@todo_router.put('/todo/{todo_id}')
async def update_todo(todo_data: TodoItem, todo_id: int=Path(..., title="The ID of the todo to be updated")) -> dict:
    
    for todo in todo_list:
        if todo.id != todo_id: continue
        todo.item.item = todo_data
        return {"message": "Todo updated Successfully."}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo with supplied ID doesn't exist.")
            
@todo_router.delete('/todo/{todo_id}')
async def del_todo(todo_id: int=Path(..., title="del todo")) -> dict:
    for idx, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list.pop(idx)
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo with supplied ID doesn't exist.")

@todo_router.delete('/todo')
async def del_all_todo():
    todo_list.clear()
    return {"message": "Todos deleted successfully."}