from fastapi import FastAPI
from contextlib import asynccontextmanager
from dbConnection import create_database


# Define the lifespan event to create the database on startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_database()
    yield


app = FastAPI(lifespan=lifespan)
