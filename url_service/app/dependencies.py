import os
import logging

import asyncio
import aiokafka



KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', "URL")
KAFKA_CONSUMER_GROUP_PREFIX = os.getenv('KAFKA_CONSUMER_GROUP_PREFIX', 'url-group')
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', '127.0.0.1:9093')


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
log = logging.getLogger(__name__)


loop = asyncio.get_event_loop()

aioproducer = aiokafka.AIOKafkaProducer(loop=loop, 
                    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)


def get_producer() -> aiokafka.AIOKafkaProducer:
    global aioproducer
    return aioproducer

