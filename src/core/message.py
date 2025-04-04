class AgentMessage:
    def __init__(self, to, from_, payload):
        self.to = to
        self.from_ = from_
        self.payload = payload