
const loginForm = document.querySelector("#login-form");
const loginId = document.querySelector("#login-form input:first-child");
const greeting = document.querySelector("#greeting");

const idKey = "ID";

function onLoginSubmit(event){
    event.preventDefault(); // Submit이후 Page 새로고침 방지
    
    const id = loginId.value;  
    loginForm.classList.add("hidden");
    localStorage.setItem(idKey, id);
    paintGreeting(id);
}

function paintGreeting(isId){
    greeting.classList.remove('hidden');
    greeting.innerText = `Hello ${isId}`;

}

const isId = localStorage.getItem(idKey);

if (isId === null){
    loginForm.classList.remove("hidden");
    loginForm.addEventListener("submit", onLoginSubmit);
} else{
    paintGreeting(isId);
}