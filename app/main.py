from fastapi import FastAPI
from app.routers import tasks, users, routines, analysis

app = FastAPI(title="ClarioAI Backend")

app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(routines.router, prefix="/routines", tags=["routines"])
app.include_router(analysis.router, prefix="/analysis", tags=["analysis"])