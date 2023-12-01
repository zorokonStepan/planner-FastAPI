from typing import Optional, List
from pydantic import BaseModel, EmailStr

from models.events import Event


class User(BaseModel):
    email:    EmailStr
    password: str
    username: str
    events:   Optional[List[Event]] = []

    class Config:
        json_schema_extra = {
            "example": {
                "email":    "fastapi@packt.com",
                "password": "some2password",
                "username": "some-username",
                "events":   [],
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email":    "fastapi@packt.com",
                "password": "strong!!!",
                "events":   [],
            }
        }
