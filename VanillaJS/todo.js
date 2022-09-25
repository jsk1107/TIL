const todoForm = document.querySelector("#todo-form");
const todo = document.querySelector("#todo-form input");
const todoList = document.querySelector("#todo-list");


function addTodoList(event){
    event.preventDefault(); // Submit이후 Page 새로고침 방지
    
    const li = document.createElement("li");
    li.innerText = todo.value;
    todoList.appendChild(li);

    localStorage.setItem("todoList", todo.value)
}


if (isId === null){
    todoForm.classList.add(HIDDEN_KEY);

} else{
    todoForm.classList.remove(HIDDEN_KEY);
    todoForm.addEventListener("submit", addTodoList);
    
}