from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "sessions" ADD "user_id" INT NOT NULL;
        ALTER TABLE "sessions" ADD CONSTRAINT "fk_sessions_users_0c63f6d3" FOREIGN KEY ("user_id") REFERENCES "users" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "sessions" DROP CONSTRAINT "fk_sessions_users_0c63f6d3";
        ALTER TABLE "sessions" DROP COLUMN "user_id";"""
