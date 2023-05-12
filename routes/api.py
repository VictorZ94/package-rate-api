from fastapi import APIRouter
from src.endpoints import salary, aux_trans

router = APIRouter()
router.include_router(salary.router)
router.include_router(aux_trans.router)
