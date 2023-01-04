from fastapi import APIRouter, Depends

from src.schemas.linkprofile import LinkProfile
from src.service.account import AccountService
from src.models import Users, Sessions_Pydantic, AccountsQueryset, Accounts_Pydantic
from src.service.auth import get_current_user

router_account = APIRouter(prefix="/accounts", tags=['accounts'])


@router_account.post("/", response_model=Sessions_Pydantic)
async def create(
        links_profile: LinkProfile,
        user: Users = Depends(get_current_user),
        service: AccountService = Depends(),

):
    return await service.create(links_profile=links_profile, user=user)


@router_account.get("/{twitter_username}", response_model=Accounts_Pydantic)
async def get_username(
        twitter_username: str,
        user: Users = Depends(get_current_user),
        service: AccountService = Depends()
):
    return await service.get_for_tw_username(twitter_username=twitter_username)


@router_account.get("/status/{session_id}", response_model=AccountsQueryset)
async def get(
        session_id: int,
        user: Users = Depends(get_current_user),
        service: AccountService = Depends(),
):
    service_info = await service.get(session_id=session_id, user=user)
    return await AccountsQueryset.from_queryset(service_info.account_session.all())
