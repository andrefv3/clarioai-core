from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from uuid import UUID

# Methods from app.crud.tasks
from app.crud.tasks import get_list_tasks, get_task, create_task, update_task, delete_task
from app.schemas import tasks
from app.database import get_db
from app import database
from app.auth.dependencies import get_current_user
from app.crud.workspaces import get_workspace_by_id
from app.models.user_orm import User

router = APIRouter()

@router.get("/", response_model=List[tasks.Task])
async def read_tasks(
    workspace_id: UUID,
    db: AsyncSession = Depends(database.get_db),
    current_user: User = Depends(get_current_user)
):
    # Validar que el workspace sea del usuario actual
    workspace = await get_workspace_by_id(db, workspace_id)
    if not workspace or workspace.creator_id != current_user.id:
        raise HTTPException(status_code=403, detail="Forbidden")

    return await get_list_tasks(db, workspace_id=workspace_id)

@router.get("/{task_id}", response_model=tasks.Task)
async def read_task(task_id: UUID, db: AsyncSession = Depends(get_db)):
    task = await get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("/", response_model=tasks.Task)
async def create_task_endpoint(task: tasks.TaskCreate, db: AsyncSession = Depends(get_db)):
    return await create_task(db, task)

@router.put("/{task_id}", response_model=tasks.Task)
async def update_task_endpoint(task_id: UUID, task: tasks.TaskUpdate, db: AsyncSession = Depends(get_db)):
    updated = await update_task(db, task_id, task)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

@router.delete("/{task_id}", response_model=tasks.Task)
async def delete_task_endpoint(task_id: UUID, db: AsyncSession = Depends(get_db)):
    deleted = await delete_task(db, task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return deleted
