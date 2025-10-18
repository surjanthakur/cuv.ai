from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from typing import List, Annotated
from typing_extensions import TypedDict
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import os

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")


class State(TypedDict):
    messages: Annotated[List, add_messages]


llm = init_chat_model(model_provider="groq", model="")
