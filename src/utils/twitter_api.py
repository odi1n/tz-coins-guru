import asyncio
from typing import List

import aiohttp
from pydantic import BaseModel

LINK = "https://api.twitter.com/2"
USERS = LINK + "/users/"
TWEETS = LINK + "/tweets/"


class PublicMetrics(BaseModel):
    followers_count: int
    following_count: int
    tweet_count: int
    listed_count: int


class User(BaseModel):
    name: str
    id: str
    username: str
    description: str
    public_metrics: PublicMetrics


class UserModel(BaseModel):
    data: User


class UsersModel(BaseModel):
    data: List[User]


class Datum(BaseModel):
    edit_history_tweet_ids: List[str]
    id: str
    text: str


class Meta(BaseModel):
    newest_id: str = None
    oldest_id: str = None
    result_count: int
    next_token: str = None


class TweetsModel(BaseModel):
    data: List[Datum] = []
    meta: Meta


class TwitterApi:
    def __init__(self, token: str) -> None:
        self.token = token
        self.headers = {'authorization': f'Bearer {token}'}

    async def get_user_by_username(self, username: str) -> UserModel:
        """
        Get infomation user
        :param username: Username Twitter
        :return:
        """
        params = {'user.fields': 'public_metrics,description'}

        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f"{USERS}by/username/{username}",
                    params=params,
                    headers=self.headers,
            ) as response:
                data = await response.json()
                return UserModel(**data)

    async def get_users_by_username(self, users: List[str]) -> UsersModel:
        """
        Get information users
        :param users: List user Twitter
        :return:
        """
        params = {
            'usernames': ','.join(users),
            'user.fields': 'public_metrics,description'
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f"{USERS}by/",
                    params=params,
                    headers=self.headers,
            ) as response:
                data = await response.json()
                return UsersModel(**data)

    async def get_recent_search(self, username: str):
        """
        Get twitt user
        :param username: Username
        :return:
        """
        params = {"query": f"from:{username}"}

        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f'{TWEETS}search/recent',
                    params=params,
                    headers=self.headers
            ) as response:
                data = await response.json()
                return TweetsModel(**data)


if __name__ == "__main__":
    TOKEN = ""
    twitter = TwitterApi(token=TOKEN)
    asyncio.run(twitter.get_users_by_username(["elonmusk", 'tyler', 'novogratz']))
