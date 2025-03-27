from core.protocol import AgentMessage, MessageType
from security import auth
import json

def test_signature_verification():
    private_key, public_key = auth.generate_keys()

    msg = AgentMessage(
        sender="agent1",
        receiver="agent2",
        type=MessageType.REQUEST,
        payload={"command": "ping"}
    )
    message_bytes = json.dumps(msg.dict(exclude={"signature"})).encode()
    sig = auth.sign_message(private_key, message_bytes)

    assert auth.verify_signature(public_key, message_bytes, sig)
