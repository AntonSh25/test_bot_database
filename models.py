from sqlalchemy import Table, Column, Integer, String, MetaData, BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from db import Base
from datetime import datetime

metadata_obj = MetaData()


users_table = Table(
    "users",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", BigInteger, nullable=False),
    Column("username", String, nullable=False),
    Column("created_at", DateTime, default=datetime.utcnow),
)

activity_table = Table(
    "activities",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", BigInteger, nullable=False),
    Column("username", String, nullable=False),
    Column("message_type", String(50)),
    Column("message_text", String(200)),
    Column("created_at", DateTime, default=datetime.utcnow),
)


class UsersORM(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    username: Mapped[str]


class ActivitiesORM(Base):
    __tablename__ = "activities"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    username: Mapped[str]
    message_type: Mapped[str]
    message_text: Mapped[str]
