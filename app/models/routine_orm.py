import uuid
from sqlalchemy import Column, String, Text, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database import Base

class Routine(Base):
    __tablename__ = 'routines'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default="CURRENT_TIMESTAMP")
    updated_at = Column(TIMESTAMP(timezone=True), server_default="CURRENT_TIMESTAMP")

    # Relationships
    user = relationship("User", back_populates="routines")
    tasks = relationship("Task", secondary="task_routine", back_populates="routines")
