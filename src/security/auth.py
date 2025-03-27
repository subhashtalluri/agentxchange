from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey, Ed25519PublicKey
)
from cryptography.hazmat.primitives import serialization
import base64

def generate_keys():
    private_key = Ed25519PrivateKey.generate()
    public_key = private_key.public_key()
    return private_key, public_key

def sign_message(private_key, message_bytes):
    signature = private_key.sign(message_bytes)
    return base64.b64encode(signature).decode()

def verify_signature(public_key, message_bytes, signature_str):
    signature = base64.b64decode(signature_str)
    try:
        public_key.verify(signature, message_bytes)
        return True
    except Exception:
        return False

def export_keys(private_key, public_key):
    private_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return private_bytes.decode(), public_bytes.decode()
