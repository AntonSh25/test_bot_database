import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import text
from sqlalchemy.orm import DeclarativeBase
from config import settings


engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True,
)

session_factory = async_sessionmaker(engine)


class Base(DeclarativeBase):
    pass


async def get_data():
    async with engine.connect() as conn:
        res = await conn.execute(text("SELECT 1,2,3"))
        print(f"{res.first()=}")
