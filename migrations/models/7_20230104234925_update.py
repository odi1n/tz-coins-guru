from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "accounts" ALTER COLUMN "status" TYPE SMALLINT USING "status"::SMALLINT;
        ALTER TABLE "tweet" ADD "tweet_id" VARCHAR(255);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "tweet" DROP COLUMN "tweet_id";
        ALTER TABLE "accounts" ALTER COLUMN "status" TYPE SMALLINT USING "status"::SMALLINT;"""
