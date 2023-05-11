from fastapi import APIRouter
from src.endpoints import salary

router = APIRouter()
router.include_router(salary.router)
