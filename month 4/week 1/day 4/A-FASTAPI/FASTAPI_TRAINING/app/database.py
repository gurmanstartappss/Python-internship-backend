from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import Settings


engine = create_engine(Settings.DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

#http- request-> get_db() -> create postgres session 
# -> endpoint uses session -> request completed 
# ->finally(execute) ->db.close()
