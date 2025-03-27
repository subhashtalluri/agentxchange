import streamlit as st
import os
import sys
import subprocess

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from cryptography.hazmat.primitives import serialization

from security import auth

st.set_page_config(page_title="AgentXchange Dashboard", layout="centered")

st.title("🤖 AgentXchange Dashboard")

st.header("🔐 Key Generation")
if st.button("Generate New Key Pair"):
    private_key, public_key = auth.generate_keys()
    priv_pem, pub_pem = auth.export_keys(private_key, public_key)
    with open("agent_private_key.pem", "w") as f:
        f.write(priv_pem)
    with open("agent_public_key.pem", "w") as f:
        f.write(pub_pem)
    st.success("New keys generated and saved!")

st.header("📨 Message Builder")
sender = st.text_input("Sender", "agent1")
receiver = st.text_input("Receiver", "agent2")
message = st.text_area("Message Content", '{"text": "Hello from UI!"}')

env = os.environ.copy()
env["PYTHONPATH"] = os.path.abspath("src")

if st.button("Simulate Send (CLI style)"):
    subprocess.run([
    "python", "src/cli/main.py",
    "send",
    "--sender", sender,
    "--receiver", receiver,
    "--transport", "http",
    "--msg", message
], env=env)
    st.success("Message sent (simulated via CLI)")
