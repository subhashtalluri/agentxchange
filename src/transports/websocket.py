import asyncio
import websockets
import json

class WebSocketTransport:
    def __init__(self, uri):
        self.uri = uri

    async def send(self, message):
        async with websockets.connect(self.uri) as websocket:
            await websocket.send(json.dumps(message))

    async def receive(self, handler):
        async with websockets.serve(handler, "localhost", 8000):
            await asyncio.Future()  # run forever
