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
    version: str = "1.0"

def handle_message(msg: AgentMessage):
    if msg.type == MessageType.REQUEST:
        print(f"Handling request from {msg.sender}")
    elif msg.type == MessageType.RESPONSE:
        print(f"Handling response from {msg.sender}")
    elif msg.type == MessageType.EVENT:
        print(f"Event received from {msg.sender}")
    elif msg.type == MessageType.ERROR:
        print(f"Error reported by {msg.sender}: {msg.payload}")
