import uuid
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base

class TaskRoutine(Base):
    __tablename__ = 'task_routine'
    task_id = Column(UUID(as_uuid=True), ForeignKey('tasks.id', ondelete='CASCADE'), primary_key=True)
    routine_id = Column(UUID(as_uuid=True), ForeignKey('routines.id', ondelete='CASCADE'), primary_key=True)
    task_order = Column(Integer, default=0)