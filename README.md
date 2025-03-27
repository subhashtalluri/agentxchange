# AgentXchange

**AgentXchange** is a modular, open-source agent communication framework that supports secure, interoperable messaging between AI and software agents over multiple transports (HTTP, WebSocket, Kafka).

Designed for modern multi-agent architectures, LLM-based systems, IoT coordination, and autonomous agent research.

---

## 🔧 Features

- 🔁 **Multi-transport** support: HTTP, WebSocket, Kafka (pluggable)
- 🔐 **Message signing & verification** with Ed25519
- 📜 **JSON-based protocol schema** with standard message types
- 📡 **Agent registry & discovery** layer
- ⚙️ **CLI Tool** to manage agents, send messages, and test flows
- 🖥️ **Web Dashboard** built in Streamlit
- 🧪 **Test suite + GitHub Actions CI**

---

## 💡 Use Cases

- LLM tool-agent systems (Autogen, LangChain-style)
- IoT sensor/actuator coordination
- Swarm intelligence and multi-agent simulations
- Autonomous drones/robots communication layer
- Research in agent protocols and standardization

---

## 🚀 Getting Started

```bash
pip install agentxchange

# Generate keys
agentx keygen

# Start an agent
agentx start --name agent2 --port 8002

# Send a message
agentx send --sender agent1 --receiver agent2 --msg "Hello"
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