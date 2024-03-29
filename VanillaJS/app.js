
const loginForm = document.querySelector("#login-form");
const loginId = document.querySelector("#login-form input:first-child");
const greeting = document.querySelector("#greeting");

const ID_KEY = "ID";
const HIDDEN_KEY = "hidden"

function onLoginSubmit(event){
    
    const id = loginId.value;  
    loginForm.classList.add(HIDDEN_KEY);
    localStorage.setItem(ID_KEY, id);
    paintGreeting(id);
}

function paintGreeting(isId){
    greeting.classList.remove(HIDDEN_KEY);
    greeting.querySelector("h2").innerText = `Hello ${isId}`;

}

const isId = localStorage.getItem(ID_KEY);

if (isId === null){
    loginForm.classList.remove(HIDDEN_KEY);
    loginForm.addEventListener("submit", onLoginSubmit);
} else{
    paintGreeting(isId);
}