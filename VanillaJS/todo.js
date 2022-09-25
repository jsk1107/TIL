const todoForm = document.querySelector("#todo-form");
const todo = document.querySelector("#todo-form input");
const todoList = document.querySelector("#todo-list");

const list = [];
const TODOLIST_KEY = "todoList";

function paintTodo(todoLists){

}

function addTodoList(event){
    event.preventDefault();
    const li = document.createElement("li");
    const tmp = todo.value;
    list.push(tmp);
    li.innerText = tmp;
    todoList.appendChild(li);
    localStorage.setItem(TODOLIST_KEY, JSON.stringify(list));
    }


if (isId === null){
    todoForm.classList.add(HIDDEN_KEY);

} else{
    todoForm.classList.remove(HIDDEN_KEY);

    const savedTodoList = localStorage.getItem(TODOLIST_KEY);
    if (savedTodoList === null){
        todoForm.addEventListener("submit", addTodoList);
    } 
    
    
}