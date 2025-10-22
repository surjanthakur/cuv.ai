from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import List


class Message(SQLModel, table=True):
    role: str
    content: str
    timestamp: datetime = Field(default_factory=datetime.now)
    thread: "Thread" = Relationship(back_populates="messages")


class Thread(SQLModel, table=True):
    threadId: str = Field(default=None, primary_key=True)
    title: str = Field(default="new thread")
    createdAt: datetime = Field(default_factory=datetime.now)
    updatedAt: datetime = Field(default_factory=datetime.now)
    messages: List[Message] = Relationship(back_populates="thread")
