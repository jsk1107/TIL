const todoForm = document.querySelector("#todo-form");
const todo = document.querySelector("#todo-form input");
const todoList = document.querySelector("#todo-list");

let list = [];
const TODOLIST_KEY = "todoList";


function paintTodo(oneOfTodoList){
    const li = document.createElement("li");
    const span = document.createElement("span");
    const deleteButton = document.createElement("button");
    deleteButton.innerText = "Del";
    deleteButton.addEventListener("click", deleteTodo);
    
    li.innerText = oneOfTodoList.text;
    li.setAttribute("id", oneOfTodoList.id); 
    li.appendChild(span);
    li.appendChild(deleteButton);
    todoList.appendChild(li);
}  

function deleteTodo(event){
    const li = event.target.parentElement;
    list = list.filter((todo) => todo.id != li.id);
    localStorage.setItem(TODOLIST_KEY, JSON.stringify(list));
    li.remove();
}

function addTodoList(event){
    event.preventDefault();
    const newTodo = todo.value;
    todo.value = "";
    const newTodoObj = {
        id: Date.now(),
        text: newTodo
    }
    list.push(newTodoObj);
    paintTodo(newTodoObj);
    localStorage.setItem(TODOLIST_KEY, JSON.stringify(list));
}

if (isId === null){
    todoForm.classList.add(HIDDEN_KEY);

} else{
    todoForm.classList.remove(HIDDEN_KEY);

    const savedTodoList = localStorage.getItem(TODOLIST_KEY);
    if (savedTodoList === null){
        todoForm.addEventListener("submit", addTodoList);
    } else {
        const parsedTodo = JSON.parse(savedTodoList);
        parsedTodo.forEach(paintTodo);
        list = parsedTodo;
        todoForm.addEventListener("submit", addTodoList);
    }
    
    
}