from typing import Union
from fastapi import APIRouter, HTTPException, status

from models.users import User, UserSignIn


user_router = APIRouter(tags=["User"])

users = {}


@user_router.post("/signup")
async def sign_user_up(data: User) -> Union[dict, None]:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied username exists"
        )

    users[data.email] = data

    return {"message": "User successfully registered!"}


@user_router.post("/signin")
async def sign_use_in(user: UserSignIn) -> Union[dict, None]:
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )

    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credential passed"
        )
    return {
        "message": "User signed in successfully"
    }
