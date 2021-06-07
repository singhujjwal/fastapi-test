import redis
import sys
import os
import logging

redis_client = None


from ..utils.formatlogs import CustomFormatter


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
log.addHandler(ch)



REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')


## check for connection and connection pools 
## Locks later 
## one client or more is the question use connection pool ??

def redis_connect() -> redis.client.Redis:
    global redis_client
    log.debug (f"This time the redis_client object is {redis_client}")
    try:
        if not redis_client:
            redis_client = redis.Redis(
                host=REDIS_HOST,
                port=REDIS_PORT,
                password=REDIS_PASSWORD,
                db=0,
                socket_timeout=5,
            )
            ping = redis_client.ping()
            if ping is True:
                log.debug ("Successfully connected to redis...")
                return redis_client
        else:
            log.debug ("Redis client object is already present, returning....")
            return redis_client
    except redis.AuthenticationError:
        log.debug("AuthenticationError")
        sys.exit(1)