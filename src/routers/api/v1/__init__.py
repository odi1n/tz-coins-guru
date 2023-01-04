from fastapi import APIRouter

from .accounts import router_account
from .tweets import router_tweet
from .user import router_user

router_v1 = APIRouter(prefix="/v1")
router_v1.include_router(router_account)
router_v1.include_router(router_tweet)
router_v1.include_router(router_user)
