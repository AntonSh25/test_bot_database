from sqlalchemy import select
from models import UsersORM, ActivitiesORM
from db import engine
from db import session_factory
from models import Base



async def create_table():
    async with engine.begin() as conn:
        # Drop existing tables and create new ones
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def insert_users(user_id: int, username: str):
    async with session_factory() as session:
        result = await session.execute(
            select(UsersORM).where(UsersORM.user_id == user_id)
        )
        existing_user = result.scalar_one_or_none()

        if existing_user is None:
            user = UsersORM(user_id=user_id, username=username)
            session.add(user)
            try:
                await session.commit()
            except:
                await session.rollback()
                print(f"Ошибка при добавлении пользователя")


async def insert_activities(user_id, username, message_type, message_text):
    async with session_factory() as session:
        activity = ActivitiesORM(
            user_id=user_id,
            username=username,
            message_type=message_type,
            message_text=message_text,
        ) 
        session.add(activity)
        await session.commit()
