class Registry:
    def __init__(self):
        self.agents = {}

    def register(self, agent_id, address=None):
        self.agents[agent_id] = address or agent_id

    def get(self, agent_id):
        return self.agents.get(agent_id)