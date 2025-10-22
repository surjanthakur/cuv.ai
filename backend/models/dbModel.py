from sqlmodel import Field, SQLModel
from datetime import datetime


class Message(SQLModel, table=True):
    role: str
    content: str
    timestamp: datetime = Field(default_factory=datetime.now)


class Thread(SQLModel, table=True):
    thread_id: int = Field(default=None, primary_key=True)
    title: str = Field(default="new thread")
    messages: Message
    createdAt: datetime = Field(default_factory=datetime.now)
    updatedAt: datetime = Field(default_factory=datetime.now)
