from typing import List
# from ..dependencies import get_producer
from aiokafka.producer.producer import AIOKafkaProducer
from fastapi import APIRouter, HTTPException
import logging
import redis
from starlette import responses

from .redis_py import redis_connect

# from ..dependencies import get_producer

from fastapi.param_functions import Depends


from .models import UrlOut, UrlIn
from . import url_manager


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
log = logging.getLogger(__name__)


urls = APIRouter()

@urls.post('/', response_model=UrlOut, status_code=201)
async def get_short_url(payload: UrlIn, 
    # producer: AIOKafkaProducer =  Depends(get_producer),
    # redis_client: redis.client.Redis= redis_connect()
    ):
    redis_client = redis_connect()

    # # check if the long url is already present return it
    # # else create a new one and return it

    # if redis_client.exists(payload.longUrl):
    #     log.debug("The short url is already present in cache, returning...")
    #     tiny_url = redis_client.get(payload.longUrl).decode('utf-8')
    #     result_json = {}
    #     result_json['shortUrl'] = f"https://u.co/{tiny_url}"
    #     return result_json
    short_url = await url_manager.get_short_url(redis_client, payload)
    # print (f"This is the producer .. {producer}")
    # print (f"This is redis_client {redis_client}")

# Check in database if the short_url and long_url keypair is present
#   Later ensure collisions is not there
#   Also set expiry 
#   update_db(short_url, payload.longUrl)

    response = {
        **short_url
    }
    return response

@urls.get('/{in_url}/', response_model=UrlIn)
async def get_long_url(in_url: str):
    redis_client = redis_connect()
    longUrl = await url_manager.get_long_url(redis_client, in_url)

  
    if not longUrl:
        raise HTTPException(status_code=404, 
                detail="No long url mapped to this short url")

    longUrl = longUrl.decode('utf-8')
    print (f"returned long url: {longUrl} from the url_manager")

    print (f"the long url is {longUrl}")
    result = {}
    result['longUrl'] = longUrl
    
    response = {
        **result
    }
    return response
