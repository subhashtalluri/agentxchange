from core.protocol import AgentMessage
from security import auth
import asyncio
import json

class Agent:
    def __init__(self, name, transport, private_key=None, public_keys=None):
        self.name = name
        self.transport = transport
        self.private_key = private_key
        self.public_keys = public_keys or {}

    async def send(self, receiver, msg_type, payload):
        msg = AgentMessage(
            sender=self.name,
            receiver=receiver,
            type=msg_type,
            payload=payload
        )
        message_bytes = json.dumps(msg.dict(exclude={'signature'})).encode()
        msg.signature = auth.sign_message(self.private_key, message_bytes)
        await self.transport.send(msg)

    async def start_server(self, handler):
        async def wrapped_handler(msg):
            sender_key = self.public_keys.get(msg.sender)
            if sender_key:
                message_bytes = json.dumps(msg.dict(exclude={'signature'})).encode()
                if auth.verify_signature(sender_key, message_bytes, msg.signature):
                    await handler(msg)
                else:
                    print("Signature verification failed.")
            else:
                print("Unknown sender.")
        await self.transport.receive(wrapped_handler)
