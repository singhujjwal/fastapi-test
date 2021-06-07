import os
import logging

import asyncio
import aiokafka

from random import randint
from kafka import TopicPartition


KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', "URL")
KAFKA_CONSUMER_GROUP_PREFIX = os.getenv('KAFKA_CONSUMER_GROUP_PREFIX', 'url-group')
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', '127.0.0.1:9093')


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
log = logging.getLogger(__name__)
loop = asyncio.get_event_loop()
aioproducer = aiokafka.AIOKafkaProducer(loop=loop, 
                    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
consumer = None
consumer_task = None


def get_producer() -> aiokafka.AIOKafkaProducer:
    global aioproducer
    print ("Although producer is not being used and it is not explicitly defined in the router"
    "but still it can be included in a path")
    return aioproducer

async def initialize():
    log.debug("Initializing the kafka consumer....")
    
    global consumer
    global loop

    group_id = f'{KAFKA_CONSUMER_GROUP_PREFIX}-{randint(0, 10000)}'
    log.debug(f'Initializing KafkaConsumer for topic {KAFKA_TOPIC}'
                'group_id {group_id} and using '
                'bootstrap servers {KAFKA_BOOTSTRAP_SERVERS}')
    
    consumer = aiokafka.AIOKafkaConsumer(KAFKA_TOPIC, loop=loop,
                                         bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
                                         group_id=group_id)
    # get cluster layout and join group
    await consumer.start()

    partitions: Set[TopicPartition] = consumer.assignment()
    nr_partitions = len(partitions)
    if nr_partitions != 1:
        log.warning(f'Found {nr_partitions} partitions for topic {KAFKA_TOPIC}. Expecting '
                    f'only one, remaining partitions will be ignored!')
    for tp in partitions:

        # get the log_end_offset
        end_offset_dict = await consumer.end_offsets([tp])
        end_offset = end_offset_dict[tp]

        if end_offset == 0:
            log.warning(f'Topic ({KAFKA_TOPIC}) has no messages (log_end_offset: '
                        f'{end_offset}), skipping initialization ...')
            return


        # ACtual code is above one, if there should be no messages in a graceful shutdown
        # mode so there is not much other than start consumner thread to start consuming

        log.debug(f'Found log_end_offset: {end_offset} seeking to {end_offset-1}')
        consumer.seek(tp, end_offset-1)
        msg = await consumer.getone()
        log.info(f'Initializing API with data from msg: {msg}')
        return

async def send_consumer_message(consumer):
    try:
        async for msg in consumer:
            log.info(f"Consumed message {msg}")
            
    finally:
        log.warning("Stopping consumeer...")
        await consumer.stop()


def done_consuming():
    log.info("Consumer is done consuming the message... so an acknowledgement be sent...")

async def consume():
    
    global consumer_task
    consumer_task = asyncio.create_task(send_consumer_message(consumer))
    consumer_task.add_done_callback(done_consuming())
    return