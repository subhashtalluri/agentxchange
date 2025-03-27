from pydantic import BaseModel
from typing import Any

class AgentMessage(BaseModel):
    sender: str
    receiver: str
    type: str
    payload: Any
