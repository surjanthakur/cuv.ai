from sqlmodel import Session, SQLModel, create_engine
from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv("DB_URL")

engine = create_engine(database_url)  # type: ignore


# create database models here as needed
def create_database():
    SQLModel.metadata.create_all(engine)


# Dependency to get a session
def get_session():
    with Session(engine) as session:
        yield session
