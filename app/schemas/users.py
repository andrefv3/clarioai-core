from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from uuid import UUID

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    is_active: Optional[int] = 1  # 1 o 0 según tu diseño

class UserCreate(UserBase):
    password: str  # contraseña en texto plano para creación (luego se hashea)

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    is_active: Optional[int] = None
    password: Optional[str] = None  # para cambiar contraseña

class UserInDBBase(UserBase):
    id: UUID
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

class User(UserInDBBase):
    pass

class UserPublic(UserBase):
    """Solo info pública, sin campos sensibles."""
    pass
