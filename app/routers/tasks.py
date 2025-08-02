from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app import crud, database
from app.schemas import tasks

router = APIRouter()

@router.get("/", response_model=List[tasks.TaskInDB])
async def read_tasks(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(database.get_db)):
    return await crud.get_tasks(db, skip, limit)

@router.get("/{task_id}", response_model=tasks.TaskInDB)
async def read_task(task_id: int, db: AsyncSession = Depends(database.get_db)):
    task = await crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("/", response_model=tasks.TaskInDB)
async def create_task(task: tasks.TaskCreate, db: AsyncSession = Depends(database.get_db)):
    return await crud.create_task(db, task)

@router.put("/{task_id}", response_model=tasks.TaskInDB)
async def update_task(task_id: int, task: tasks.TaskUpdate, db: AsyncSession = Depends(database.get_db)):
    updated = await crud.update_task(db, task_id, task)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

@router.delete("/{task_id}", response_model=tasks.TaskInDB)
async def delete_task(task_id: int, db: AsyncSession = Depends(database.get_db)):
    deleted = await crud.delete_task(db, task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return deleted
