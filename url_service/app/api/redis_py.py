import redis
import sys

redis_client = None

def redis_connect() -> redis.client.Redis:
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