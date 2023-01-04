from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "accounts" DROP CONSTRAINT "fk_accounts_sessions_1b829dad";
        ALTER TABLE "accounts" RENAME COLUMN "store_id" TO "session_id";
        ALTER TABLE "accounts" ALTER COLUMN "name" DROP NOT NULL;
        ALTER TABLE "accounts" ALTER COLUMN "description" DROP NOT NULL;
        ALTER TABLE "accounts" ADD CONSTRAINT "fk_accounts_sessions_3c5a23c0" FOREIGN KEY ("session_id") REFERENCES "sessions" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "accounts" DROP CONSTRAINT "fk_accounts_sessions_3c5a23c0";
        ALTER TABLE "accounts" RENAME COLUMN "session_id" TO "store_id";
        ALTER TABLE "accounts" ALTER COLUMN "name" SET NOT NULL;
        ALTER TABLE "accounts" ALTER COLUMN "description" SET NOT NULL;
        ALTER TABLE "accounts" ADD CONSTRAINT "fk_accounts_sessions_1b829dad" FOREIGN KEY ("store_id") REFERENCES "sessions" ("id") ON DELETE CASCADE;"""
