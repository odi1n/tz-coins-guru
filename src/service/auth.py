from datetime import datetime, timedelta

from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.handlers.bcrypt import bcrypt
from starlette import status

from src.models import Users
from src.schemas.token import Token
from src.settings import setting

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")


async def get_current_user(token: str = Depends(oauth2_scheme)) -> Users:
    return await AuthService.validate_token(token)


class AuthService:
    @classmethod
    def verify_password(cls, password: str, hashed_pass: str) -> bool:
        return bcrypt.verify(password, hashed_pass)

    @classmethod
    def get_hashed_password(cls, password: str) -> str:
        return bcrypt.hash(password)

    @classmethod
    async def validate_token(cls, token: str) -> Users:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(
                token,
                setting.jwt_secret_key,
                algorithms=[setting.algorithm]
            )
        except JWTError:
            raise credentials_exception

        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception

        user = await Users.filter(id=user_id).first()
        if user is None:
            raise credentials_exception
        return user

    @classmethod
    def create_access_token(cls, user: Users) -> Token:
        now = datetime.utcnow()
        payload = {
            "iat": now,
            'nbf': now,
            "exp": now + timedelta(seconds=setting.refresh_token_expire_minutes),
            "sub": str(user.id),
            "users": user.username
        }
        token = jwt.encode(
            payload,
            setting.jwt_secret_key,
            setting.algorithm
        )
        return Token(access_token=token)

    async def create_user(self, user: Users):
        check_user = await Users.filter(username=user.username).first()
        if check_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email already exist"
            )
        user.password = self.get_hashed_password(user.password)
        return await Users.create(**user.dict(exclude_unset=True))

    async def login(self, form_data: OAuth2PasswordRequestForm):
        user = await Users.filter(username=form_data.username).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Incorrect email or password"
            )

        if not self.verify_password(form_data.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Incorrect email or password"
            )

        return self.create_access_token(user)
