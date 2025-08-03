from asyncio import Task
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID

class WorkspaceBase(BaseModel):
    name: str

class WorkspaceCreate(WorkspaceBase):
    creator_id: UUID

class WorkspaceInDB(WorkspaceBase):
    id: UUID
    creator_id: UUID

    class Config:
        from_attributes = True

class Workspace(WorkspaceInDB):
    tasks: Optional[List[Task]] = []  # Import Task from your schemas