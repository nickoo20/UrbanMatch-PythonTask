from pydantic import BaseModel, EmailStr
from typing import List

class UserBase(BaseModel):
    name: str
    age: int
    gender: str
    city: str
    interests: str  

class UserCreate(UserBase):
    email: EmailStr

class UserUpdate(BaseModel):
    email: EmailStr = None
    name: str = None
    age: int = None
    gender: str = None
    city: str = None
    interests: str = None  

class UserOut(UserBase):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True
