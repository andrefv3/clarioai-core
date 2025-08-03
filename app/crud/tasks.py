from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from uuid import UUID

from app.models.task_orm import Task
from app.schemas import tasks

# Get list of tasks with pagination
async def get_list_tasks(db: AsyncSession, skip: int = 0, limit: int = 100, workspace_id: UUID = None):
    query = select(Task).offset(skip).limit(limit)
    if workspace_id:
        query = query.where(Task.workspace_id == workspace_id)
    result = await db.execute(query)
    return result.scalars().all()

# Get task by ID
async def get_task(db: AsyncSession, task_id: UUID):
    result = await db.execute(select(Task).where(Task.id == task_id))
    task_orm = result.scalar_one_or_none()
    return task_orm

# Create task
async def create_task(db: AsyncSession, task: tasks.TaskCreate):
    db_task = Task(
        user_id=task.user_id,
        workspace_id=task.workspace_id,
        title=task.title,
        description=task.description,
        status=task.status,
        priority=task.priority,
    )
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task

# Update task
async def update_task(db: AsyncSession, task_id: UUID, task_update: tasks.TaskUpdate):
    query = (
        update(Task).
        where(Task.id == task_id).
        values(**task_update.dict(exclude_unset=True)).
        execution_options(synchronize_session="fetch")
    )
    await db.execute(query)
    await db.commit()
    return await get_task(db, task_id)

# Delete task
async def delete_task(db: AsyncSession, task_id: UUID):
    task = await get_task(db, task_id)
    if not task:
        return None
    await db.delete(task)
    await db.commit()
    return task
