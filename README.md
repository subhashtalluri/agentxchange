# AgentXchange

**AgentXchange** is an open-source framework for standardized agent communication and data exchange.

## Features
- Modular transport abstraction (HTTP, WebSocket, Kafka, etc.)
- Common agent messaging schema
- Pluggable data exchange format
- Agent registry for discovery

## Getting Started
```bash
pip install -r requirements.txt
python examples/simple_chat/agent1.py
```

## 🔧 CLI Usage

```bash
# Generate keys
python -m cli.main keygen

# Start an agent
python -m cli.main start --name agent2 --port 8002

# Send a message
python -m cli.main send --sender agent1 --receiver agent2 --transport http --msg "Hello"
```

## 📂 Example Agent Config (.agentx.json)

```json
{
  "name": "agent1",
  "transport": "http",
  "port": 8001,
  "receiver": "agent2",
  "message": "Hello from config!"
}
```