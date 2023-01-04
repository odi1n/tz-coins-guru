from src.models import Accounts, StatusType
from src.utils.twitter_api import TwitterApi
from src.settings import setting


async def get_usernames() -> None:
    accounts = await Accounts.filter(status=StatusType.NO_CHECK).all()
    if len(accounts) > 30:
        accounts = accounts[:30]

    if len(accounts) == 0:
        return

    usernames = list(set([account.username for account in accounts]))

    twitter = TwitterApi(setting.api_bearer_token)
    get_info_users = await twitter.get_users_by_username(usernames)

    for account in accounts:
        if account.twitter_id != 0:
            continue

        user = (info for info in get_info_users.data if account.username == info.username)

        try:
            await account.update_params_tw(next(user))
        except StopIteration as error:
            await account.update_status(StatusType.FAILED)
            continue

    await  get_usernames()
