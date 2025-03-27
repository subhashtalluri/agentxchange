import asyncio
from transports.http import HTTPTransport
from agent import Agent
from core.protocol import handle_message
from transports.http import app

async def main():
    transport = HTTPTransport(listen_port=8002)
    app.state.transport = transport
    agent = Agent("agent2", transport)
    await agent.start_server(handle_message)

asyncio.run(main())
