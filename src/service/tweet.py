from src.models import Tweet, TweetQueryCreator


class TweetService:
    async def get_for_tw_id(
            self,
            twitter_id: int,
    ) -> TweetQueryCreator:
        tweets = Tweet.filter(account__twitter_id=twitter_id).all()
        return await TweetQueryCreator.from_queryset(tweets)
