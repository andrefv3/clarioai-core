from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum
from uuid import UUID

class TaskStatus(str, Enum):
    todo = 'todo'
    in_progress = 'in_progress'
    done = 'done'

class TaskPriority(str, Enum):
    low = 'low'
    medium = 'medium'
    high = 'high'

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.todo
    priority: TaskPriority = TaskPriority.medium
    workspace_id: UUID

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[TaskStatus]
    priority: Optional[TaskPriority]

class TaskInDBBase(TaskBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # compatible con Pydantic v2

class Task(TaskInDBBase):
    pass

    class Config:
        from_attributes = True
