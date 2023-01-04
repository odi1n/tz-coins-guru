from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from src.routers import router
from src.schedulers import get_usernames, get_tweets
from src.settings import setting

app = FastAPI(
    title="Tz coins guru",
    version="0.1.0",
    description="Description api",
)
app.include_router(router)

register_tortoise(
    app,
    db_url=setting.db_url,
    modules={"models": ["src.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

scheduler = AsyncIOScheduler()
scheduler.add_job(get_usernames, 'interval', minutes=60)
scheduler.add_job(get_tweets, 'interval', minutes=240)
scheduler.start()
