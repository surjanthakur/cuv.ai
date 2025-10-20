from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy import table
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Thread(SQLModel, table=True):
    pass
