from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_analysis():
    return {"message": "Analysis endpoint is working"}