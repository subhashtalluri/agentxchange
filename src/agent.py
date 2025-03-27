from core.protocol import AgentMessage
import asyncio
import json

class Agent:
    def __init__(self, name, transport):
        self.name = name
        self.transport = transport

    async def send(self, receiver, msg_type, payload):
        msg = AgentMessage(sender=self.name, receiver=receiver, type=msg_type, payload=payload)
        await self.transport.send(msg.dict())

    async def start_server(self, handler):
        await self.transport.receive(handler)
