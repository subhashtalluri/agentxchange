class AgentRegistry:
    def __init__(self):
        self._agents = {}

    def register(self, name: str, endpoint: str):
        self._agents[name] = endpoint

    def get(self, name: str):
        return self._agents.get(name)

    def list_agents(self):
        return list(self._agents.items())
