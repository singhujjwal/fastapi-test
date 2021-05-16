#~/url-service/app/main.py

from fastapi import FastAPI
from app.api.urls import urls
import logging
import os
import asyncio
from random import randint
import aiokafka
import redis
import sys

redis_client = None

def redis_connect() -> redis.client.Redis:
    return
    global redis_client
    try:
        if not redis_client:
            redis_client = redis.Redis(
                host="212.2.241.224",
                port=6379,
                password="bu1OPozjX4TMMhJItvbCtCo3SG8wm1",
                db=0,
                socket_timeout=5,
            )
            ping = redis_client.ping()
            if ping is True:
                print ("Successfully connected to redis...")
                return redis_client
        else:
            return redis_client
    except redis.AuthenticationError:
        print("AuthenticationError")
        sys.exit(1)



logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
log = logging.getLogger(__name__)

app = FastAPI(openapi_url="/api/v1/urls/openapi.json", docs_url="/api/v1/urls/docs")
app.include_router(urls, prefix='/api/v1/urls', tags=['urls'])


@app.on_event("startup")
async def startup_event():
    log.info('Initializing API ...')
    await initialize()
    await consume()


async def initialize():
    loop = asyncio.get_event_loop()
    log.info("Initialized the Redis Connection........")
    redis_connect()
    return
    global consumer
    group_id = f'{KAFKA_CONSUMER_GROUP_PREFIX}-{randint(0, 10000)}'
    log.debug(f'Initializing KafkaConsumer for topic {KAFKA_TOPIC}, group_id {group_id}'
              f' and using bootstrap servers {KAFKA_BOOTSTRAP_SERVERS}')
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

        log.debug(f'Found log_end_offset: {end_offset} seeking to {end_offset-1}')
        consumer.seek(tp, end_offset-1)
        msg = await consumer.getone()
        log.info(f'Initializing API with data from msg: {msg}')

        # update the API state
        _update_state(msg)
        return


async def consume():
    return
    global consumer_task
    consumer_task = asyncio.create_task(send_consumer_message(consumer))