# Marks 'routers' as a subpackage of 'clarioai'.
# Optional: import routers here to simplify imports in main.py.

from .routers.tasks import router as tasks
from .routers.users import router as users
from .routers.routines import router as routines
from .routers.analysis import router as analysis

def create_app():
    from fastapi import FastAPI
    app = FastAPI()

    from .routers.tasks import router as tasks
    app.include_router(tasks)
    app.include_router(users)
    app.include_router(routines)
    app.include_router(analysis)

    return app