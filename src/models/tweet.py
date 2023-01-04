from tortoise import models, fields
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator


class Tweet(models.Model):
    id = fields.IntField(pk=True)
    tweet_id = fields.CharField(max_length=255, null=True)
    text = fields.TextField()
    account = fields.ForeignKeyField('models.Accounts', related_name="tweet_account", on_delete=fields.CASCADE)

    def __str__(self):
        return self.text


Tweet_Pydantic = pydantic_model_creator(
    Tweet,
    name="Tweet",
    exclude=('account',)
)

TweetIn_Pydantic = pydantic_model_creator(
    Tweet,
    name="TweetIn",
    exclude_readonly=True
)

TweetQueryCreator = pydantic_queryset_creator(
    Tweet,
    exclude=("account",)
)
