import json
from confluent_kafka import Producer, Consumer, KafkaError
from core.protocol import AgentMessage
from transports.base import Transport
import threading
import asyncio
from tenacity import retry, stop_after_attempt, wait_exponential

class KafkaTransport(Transport):
    def __init__(self, agent_name, kafka_config=None):
        self.agent_name = agent_name
        self.kafka_config = kafka_config or {
            'bootstrap.servers': 'localhost:9092',
            'group.id': f'{agent_name}-group',
            'auto.offset.reset': 'earliest'
        }

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=10))
    async def send(self, message: AgentMessage):
        producer = Producer({'bootstrap.servers': self.kafka_config['bootstrap.servers']})
        producer.produce(message.receiver, json.dumps(message.dict()).encode())
        producer.flush()

    async def receive(self, handler):
        def consume_loop():
            consumer = Consumer(self.kafka_config)
            consumer.subscribe([self.agent_name])
            while True:
                msg = consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() != KafkaError._PARTITION_EOF:
                        print("Kafka error:", msg.error())
                else:
                    data = json.loads(msg.value())
                    agent_msg = AgentMessage(**data)
                    asyncio.run(handler(agent_msg))

        thread = threading.Thread(target=consume_loop)
        thread.daemon = True
        thread.start()
