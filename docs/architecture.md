# AgentXchange Architecture

AgentXchange is a modular, extensible framework for secure communication between software agents.

## Components

- **Agent**: The core entity that sends and receives messages.
- **Transport**: Pluggable system (HTTP, WebSocket, Kafka) to route messages.
- **Protocol**: Defines message schema and routing.
- **Registry**: Optional agent discovery layer.
- **Security**: Signatures (Ed25519) ensure message authenticity and integrity.
- **CLI**: Dev tool to manage agents and messages.

## Message Flow

1. Agent sends a message signed with its private key.
2. Transport layer delivers the message.
3. Receiving agent verifies signature using sender’s public key.
