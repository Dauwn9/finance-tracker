from typing import Optional
from pydantic import BaseModel, EmailStr, PastDatetime, PastDate

class UserCreate(BaseModel):
    username: str
    password: str
    email: EmailStr

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: PastDatetime

    class Config:
        from_attributes = True

class Categories(BaseModel):
    id: Optional[int] = None
    name: str
    color: str
    class Config:
        from_attributes = True

class ExpenseCreate(BaseModel):
    category_id: int
    amount: float
    description: str
    spent_on: PastDate

class ExpenseResponse(BaseModel):
    id: int
    category_id: int
    amount: float
    description: str
    spent_on: PastDate
    created_at: PastDatetime
    class Config:
        from_attributes = True