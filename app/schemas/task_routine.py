from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class TaskRoutineBase(BaseModel):
    task_id: UUID
    routine_id: UUID
    task_order: Optional[int] = 0

class TaskRoutineCreate(TaskRoutineBase):
    pass

class TaskRoutineUpdate(BaseModel):
    task_order: Optional[int]

class TaskRoutineInDBBase(TaskRoutineBase):
    class Config:
        orm_mode = True

class TaskRoutine(TaskRoutineInDBBase):
    pass
