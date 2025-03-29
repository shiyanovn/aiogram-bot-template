from sqlalchemy import Column, Integer, String, DateTime, UUID

from app.data.db import DeclarativeBase as Base
from sqlalchemy.orm import Mapped

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=False)
    username: Mapped[str] = Column(String(32), nullable=True)
    first_name: Mapped[str] = Column(String(64), nullable=False)
    last_name: Mapped[str]= Column(String(64), nullable=True)