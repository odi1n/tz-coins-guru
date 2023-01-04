from typing import Union

from fastapi import APIRouter, Depends

from src.service.tweet import TweetService
from src.models import Users, TweetQueryCreator
from src.service.auth import get_current_user

router_tweet = APIRouter(prefix="/tweets", tags=['tweets'])


@router_tweet.get("/{twitter_id}", response_model=TweetQueryCreator)
async def get_twitter_id(
        twitter_id: Union[str, int],
        user: Users = Depends(get_current_user),
        service: TweetService = Depends()
):
    return await service.get_for_tw_id(twitter_id=twitter_id)
