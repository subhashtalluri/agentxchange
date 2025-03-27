import asyncio
from transports.websocket import WebSocketTransport
from agent import Agent
import json

async def handler(websocket):
    msg = await websocket.recv()
    print("Agent2 received:", json.loads(msg))

async def main():
    agent = Agent("agent2", WebSocketTransport("ws://localhost:8000"))
    await agent.start_server(handler)

asyncio.run(main())
