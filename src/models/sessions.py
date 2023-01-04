from __future__ import annotations
from src.models.accounts import Accounts
from tortoise import models, fields
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator


class Sessions(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.Users", related_name="session_user", on_delete=fields.CASCADE)

    account_session: fields.ReverseRelation["Accounts"]

    def __str__(self):
        return f"{self.id}"


Sessions_Pydantic = pydantic_model_creator(
    Sessions,
    name="Sessions",
    # include=('id', 'user', 'account_session')
)

SessionsIn_Pydantic = pydantic_model_creator(
    Sessions,
    name="SessionsIn",
    exclude_readonly=True
)

SessionsQueryCreator = pydantic_queryset_creator(Sessions, name="SessionsQueryCreator",
                                                 include=('id', 'user', 'account_session'))
