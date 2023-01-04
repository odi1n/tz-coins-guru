from src.settings import setting
from src.models import Accounts, StatusType, Tweet
from src.utils.twitter_api import TwitterApi


async def get_tweets():
    twitter = TwitterApi(setting.api_bearer_token)

    accounts = await Accounts.filter(status=StatusType.SUCCESS).all()

    for account in accounts:
        recent_search = await twitter.get_recent_search(account.username)
        for recent in recent_search.data:
            if await account.tweet_account.filter(tweet_id=recent.id).exists() is False:
                await Tweet.create(tweet_id=recent.id, text=recent.text, account=account)
    return
