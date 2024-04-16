from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn

user_router = APIRouter(tags=['User'])

users = {}


@user_router.post('/signup')
async def sign_new_user(user_info: User) -> dict:
    email = user_info.email
    if email in users:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="UserEmail already exist.")
    users[email] = user_info
    return {"message": "User successfully registered!"}


@user_router.post('/signin')
async def sign_user_in(user_info: UserSignIn) -> dict:
    if user_info.email not in users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="UserID doesn't exiest")
    
    if user_info.password != users[user_info.email].password:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Wrong Password!")
    
    return {"message": "User signed in successfully"}