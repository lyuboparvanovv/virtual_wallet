from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, constr, field_validator


class UserBase(BaseModel):
    username: constr(min_length=2, max_length=20)
    email: EmailStr
    phone: constr(min_length=10, max_length=10)
    photo: Optional[str]

class UserCreate(UserBase):
    password: constr(min_length=8)

    @field_validator('password')
    @classmethod
    def check_password(cls, v):
        if not any(c.isupper() for c in v):
            raise ValueError("Must include uppercase letter")
        if not any(c.isdigit() for c in v):
            raise ValueError("Must include digit")
        if not any(c in '+-*^&' for c in v):
            raise ValueError("Must include special character")
        return v

class UserUpdate(BaseModel):
    email: Optional[EmailStr]
    phone: Optional[constr(min_length=10, max_length=10)]
    photo: Optional[str]

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    phone: str
    photo: Optional[str]
    is_active: bool
    is_admin: bool
    is_approved: bool
    created_at: datetime

    class Config:
        from_attributes = True
