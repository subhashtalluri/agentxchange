import asyncio
from transports.websocket import WebSocketTransport
from agent import Agent

async def main():
    agent = Agent("agent1", WebSocketTransport("ws://localhost:8000"))
    await asyncio.sleep(1)  # wait for server
    await agent.send("agent2", "GREETING", {"text": "Hello, Agent2!"})

asyncio.run(main())
