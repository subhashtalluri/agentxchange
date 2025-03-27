from pydantic import BaseModel, Field
from typing import Any, Optional
from enum import Enum
import uuid
from datetime import datetime

class MessageType(str, Enum):
    REQUEST = "REQUEST"
    RESPONSE = "RESPONSE"
    EVENT = "EVENT"
    ERROR = "ERROR"

class AgentMessage(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    sender: str
    receiver: str
    type: MessageType
    payload: Any
    signature: Optional[str] = None
    version: str = "1.0"

def handle_message(msg: AgentMessage):
    print(f"[{msg.type}] From {msg.sender} to {msg.receiver}: {msg.payload}")
