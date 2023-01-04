from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "accounts" ADD "store_id" INT NOT NULL;
        ALTER TABLE "accounts" ADD CONSTRAINT "fk_accounts_sessions_1b829dad" FOREIGN KEY ("store_id") REFERENCES "sessions" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "accounts" DROP CONSTRAINT "fk_accounts_sessions_1b829dad";
        ALTER TABLE "accounts" DROP COLUMN "store_id";"""
