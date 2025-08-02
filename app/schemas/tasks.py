from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = "pending"
    priority: Optional[str] = "medium"

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    status: Optional[str] = None
    priority: Optional[str] = None
    description: Optional[str] = None
    title: Optional[str] = None

class TaskInDB(TaskBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]
    status: str
    priority: str

    class Config:
        orm_mode = True
