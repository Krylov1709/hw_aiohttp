from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


PG_DSN = 'postgresql+asyncpg://postgres:Rhskjd@localhost:5432/hw_aiohttp'
engine = create_async_engine(PG_DSN)
Base = declarative_base()


class ArticleModel(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    creation_time = Column(DateTime, default=datetime.now)


Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
