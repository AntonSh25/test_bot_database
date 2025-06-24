from sqlalchemy import Table, Column, Integer, String, MetaData, BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from db import Base
from datetime import datetime


class UsersORM(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    username: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)


class ActivitiesORM(Base):
    __tablename__ = "activities"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    username: Mapped[str]
    message_type: Mapped[str] 
    message_text: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
