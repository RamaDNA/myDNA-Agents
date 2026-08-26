from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

from typing import list, Annotated, TypedDict as typedDict

class AgentState(typedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    next_agent: str
