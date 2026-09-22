from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,create_async_engine)
from app.config import Settings


engine = create_async_engine(Settings.DATABASE_URL)

SessionLocal = async_sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


class Base(DeclarativeBase):
    pass


# database dependency
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session

#http- request-> get_db() -> create postgres session 
# -> endpoint uses session -> request completed 
# ->finally(execute) ->db.close()
