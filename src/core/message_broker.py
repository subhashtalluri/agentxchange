class MessageBroker:
    def __init__(self, registry):
        self.registry = registry
        self.subscribers = {}

    def subscribe(self, agent_id, callback):
        self.subscribers[agent_id] = callback

    def send(self, message):
        callback = self.subscribers.get(message.to)
        if callback:
            callback(message)
        else:
            print(f"[MessageBroker] No subscriber for: {message.to}")