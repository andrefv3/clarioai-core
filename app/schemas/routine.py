from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID

class RoutineBase(BaseModel):
    user_id: UUID
    name: str
    description: Optional[str] = None

class RoutineCreate(RoutineBase):
    pass

class RoutineUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]

class RoutineInDBBase(RoutineBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class Routine(RoutineInDBBase):
    pass
