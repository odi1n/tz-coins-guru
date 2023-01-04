import enum

from tortoise import models, fields
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator


class StatusType(enum.IntEnum):
    NO_CHECK = 0,
    SUCCESS = 1
    FAILED = 2


class Accounts(models.Model):
    id = fields.BigIntField(pk=True)
    twitter_id = fields.BigIntField(default=0)
    name = fields.CharField(max_length=125, null=True)
    username = fields.CharField(max_length=75)
    following_count = fields.IntField(default=0)
    followers_count = fields.IntField(default=0)
    description = fields.TextField(null=True)
    session = fields.ForeignKeyField("models.Sessions", related_name="account_session", on_delete=fields.CASCADE)
    status = fields.IntEnumField(StatusType, default=StatusType.NO_CHECK)

    def __str__(self):
        return self.username

    async def update_params_tw(self, info_twitter):
        self.twitter_id = info_twitter.id
        self.name = info_twitter.username
        self.followers_count = info_twitter.public_metrics.followers_count
        self.following_count = info_twitter.public_metrics.following_count
        self.description = info_twitter.description
        self.status = StatusType.SUCCESS
        await self.save(
            update_fields=['twitter_id',
                           'name',
                           'followers_count',
                           'following_count',
                           'description',
                           'status']
        )

    async def update_status(self, status: StatusType):
        self.status = StatusType.FAILED
        await self.save(update_fields=['status'])


Accounts_Pydantic = pydantic_model_creator(
    Accounts,
    name="Accounts",
)

AccountsIn_Pydantic = pydantic_model_creator(
    Accounts,
    name="AccountsIn",
    exclude_readonly=True
)

AccountsQueryset = pydantic_queryset_creator(
    Accounts,
    exclude=('twitter_id', 'name', 'following_count', 'followers_count', 'description', 'session')
)
