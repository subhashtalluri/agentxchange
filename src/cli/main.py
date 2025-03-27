import typer
from security import auth

app = typer.Typer()

@app.command()
def keygen():
    """Generate a public/private key pair."""
    private_key, public_key = auth.generate_keys()
    priv_pem, pub_pem = auth.export_keys(private_key, public_key)
    with open("agent_private_key.pem", "w") as f:
        f.write(priv_pem)
    with open("agent_public_key.pem", "w") as f:
        f.write(pub_pem)
    print("✅ Keys saved as agent_private_key.pem and agent_public_key.pem")

@app.command()
def send(sender: str, receiver: str, transport: str, msg: str):
    """Send a message to another agent."""
    import asyncio
    import json
    from agent import Agent
    from core.protocol import MessageType
    from transports.http import HTTPTransport
    from security import auth
    from cryptography.hazmat.primitives import serialization

    with open("agent_private_key.pem", "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    transport_obj = HTTPTransport(url=f"http://localhost:8002/")
    agent = Agent(sender, transport_obj, private_key=private_key)
    asyncio.run(agent.send(receiver, MessageType.REQUEST, {"text": msg}))
    print("📨 Message sent.")

@app.command()
def start(name: str, transport: str = "http", port: int = 8001):
    """Start an agent server."""
    import asyncio
    from agent import Agent
    from core.protocol import handle_message
    from transports.http import HTTPTransport
    from security import auth
    from cryptography.hazmat.primitives import serialization

    with open("agent_private_key.pem", "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    transport_obj = HTTPTransport(listen_port=port)
    from transports.http import app as http_app
    http_app.state.transport = transport_obj
    agent = Agent(name, transport_obj, private_key=private_key)
    print(f"🚀 Agent '{name}' starting on port {port}...")
    asyncio.run(agent.start_server(handle_message))

if __name__ == "__main__":
    app()
