from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.database import get_db
from app.models.users import User
from app.schemas.users import UserPublic

router = APIRouter()

@router.get("/", response_model=list[UserPublic])
async def get_users(db: AsyncSession = Depends(get_db)):
    # Consulta asíncrona para obtener todos los usuarios
    result = await db.execute(select(User))
    users = result.scalars().all()

    if not users:
        # Puedes manejar si no hay usuarios con un error o devolver lista vacía
        return []

    return users
