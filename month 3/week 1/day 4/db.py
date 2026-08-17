# pip install sqlalchemy pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:root@localhost/db"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()