from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    is_active: Optional[int] = 1

class UserCreate(UserBase):
    password: str  # Plain password for creation (will be hashed)

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    is_active: Optional[int] = None
    password: Optional[str] = None  # Optional update of password

class UserInDBBase(UserBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

class User(UserInDBBase):
    pass

class UserPublic(UserBase):
    """Schema to expose only public user info (e.g., no hashed password)"""
    pass
