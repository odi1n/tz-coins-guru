from fastapi import APIRouter
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.models.users import User_Pydantic, UserIn_Pydantic
from src.schemas.token import Token
from src.service.auth import AuthService, get_current_user

router_user = APIRouter(tags=["user"])


@router_user.post('/signup', summary="Create new user", response_model=User_Pydantic)
async def create_user(
        user: UserIn_Pydantic,
        service: AuthService = Depends()
):
    """
    Create new user
    :param user:
    :param service:
    :return:
    """
    return await service.create_user(user=user)


@router_user.post('/login', summary="Create access tokens for user", response_model=Token)
async def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        service: AuthService = Depends()
):
    """
    Create access tokens for user
    :param form_data:
    :param service:
    :return:
    """
    return await service.login(form_data)


@router_user.get('/user', summary="Get information user", response_model=User_Pydantic)
async def get_user(
        user: User_Pydantic = Depends(get_current_user)
):
    """
    Get information user
    :param user:
    :return:
    """
    return await User_Pydantic.from_tortoise_orm(user)
