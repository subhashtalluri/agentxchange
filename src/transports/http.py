from fastapi import FastAPI, Request
import httpx
from core.protocol import AgentMessage
from transports.base import Transport

app = FastAPI()

class HTTPTransport(Transport):
    def __init__(self, url=None, listen_port=8001):
        self.url = url
        self.listen_port = listen_port
        self.handler = None

    async def send(self, message: AgentMessage):
        async with httpx.AsyncClient() as client:
            response = await client.post(self.url, json=message.dict())
            return response

    async def receive(self, handler):
        self.handler = handler
        app.state.transport = self
        import uvicorn
        config = uvicorn.Config(app, host="0.0.0.0", port=self.listen_port, log_level="info")
        server = uvicorn.Server(config)
        await server.serve()

@app.post("/")
async def receive_message(request: Request):
    data = await request.json()
    msg = AgentMessage(**data)
    if app.state.transport.handler:
        await app.state.transport.handler(msg)
    return {"status": "received"}
