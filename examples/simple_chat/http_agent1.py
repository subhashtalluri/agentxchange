import asyncio
from transports.http import HTTPTransport
from agent import Agent

async def main():
    transport = HTTPTransport(url="http://localhost:8002/")
    agent = Agent("agent1", transport)
    await agent.send("agent2", "REQUEST", {"query": "status?"})

asyncio.run(main())
