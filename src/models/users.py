from tortoise import models, fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Users(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255, unique=True)
    email = fields.CharField(max_length=255)
    password = fields.CharField(max_length=255)
    joined = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.username


User_Pydantic = pydantic_model_creator(
    Users,
    name="User",
    exclude=('password',)
)

UserIn_Pydantic = pydantic_model_creator(
    Users,
    name="UserIn",
    exclude_readonly=True
)
