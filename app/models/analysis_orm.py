import uuid
from sqlalchemy import Column, String, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from app.database import Base

class Analysis(Base):
    __tablename__ = 'analysis'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    task_id = Column(UUID(as_uuid=True), ForeignKey('tasks.id', ondelete='CASCADE'), nullable=False)
    analysis_type = Column(String(100), nullable=False)
    result = Column(JSONB, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default="CURRENT_TIMESTAMP")

    # Relationships
    task = relationship("Task", back_populates="analyses")
