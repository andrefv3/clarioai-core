from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_routines():
    return {"message": "Routines endpoint works"}