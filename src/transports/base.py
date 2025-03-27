from abc import ABC, abstractmethod
from core.protocol import AgentMessage

class Transport(ABC):
    @abstractmethod
    async def send(self, message: AgentMessage):
        pass

    @abstractmethod
    async def receive(self, handler):
        pass
