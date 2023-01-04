from fastapi import APIRouter
from .api import router_api

router = APIRouter()
router.include_router(router_api)
