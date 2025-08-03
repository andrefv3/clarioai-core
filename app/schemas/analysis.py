from pydantic import BaseModel
from typing import Dict, Optional
from datetime import datetime
from uuid import UUID

class AnalysisBase(BaseModel):
    task_id: UUID
    analysis_type: str
    result: Dict  # JSON field can be mapped to Dict

class AnalysisCreate(AnalysisBase):
    pass

class AnalysisUpdate(BaseModel):
    analysis_type: Optional[str]
    result: Optional[Dict]

class AnalysisInDBBase(AnalysisBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True

class Analysis(AnalysisInDBBase):
    pass
