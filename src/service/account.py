from fastapi import HTTPException
from starlette import status

from src.schemas.linkprofile import LinkProfile
from src.models import Users, Sessions, Accounts
from src.utils.trim_link import get_username_with_links


class AccountService:
    async def create(
            self,
            links_profile: LinkProfile,
            user: Users
    ) -> Sessions:
        links = get_username_with_links(links_profile.links)
        session = await Sessions.create(user=user)
        accounts = (Accounts(username=link, session=session) for link in links)
        await Accounts.bulk_create(accounts)
        return session

    async def get(
            self,
            session_id: int,
            user: Users
    ) -> Sessions:
        session = await Sessions.filter(
            id=session_id,
            user=user
        ).select_related('user').prefetch_related('account_session').first()

        if session is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Error session_id in user",
            )
        return session

    async def get_for_tw_username(
            self,
            twitter_username: str,
    ):
        return await Accounts.filter(username=twitter_username).first()
