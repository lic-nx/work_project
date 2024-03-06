import os

from sqlalchemy.orm import sessionmaker
from sqlmodel import create_engine, SQLModel, Session
from config import Config

DATABASE_URL = (
    "postgresql+psycopq2://127.0.0.1:5432/"
    # "postgresql://{Config.USER_BD}:{Config.PASS_BD}@{Config.DB_CONTAINER_NAME}:{Config.PORT_BD}/{Config.NAME_BD}"

)

engine = create_engine(DATABASE_URL, echo=True)

session = sessionmaker(engine, expire_on_commit=False, class_=Session)


def get_db() -> sessionmaker:
    return session()
