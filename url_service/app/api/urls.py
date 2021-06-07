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

## Logging code
from ..utils.formatlogs import CustomFormatter

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
log.addHandler(ch)

## Logging end


urls = APIRouter()

@urls.post('/', response_model=UrlOut, status_code=201)
async def get_short_url(payload: UrlIn, 
    # producer: AIOKafkaProducer =  Depends(get_producer),
    # redis_client: redis.client.Redis= redis_connect()
    ):
    redis_client = redis_connect()
    if redis_client:
        short_url = await url_manager.get_short_url(redis_client, payload)

        response = {
            **short_url
        }
        return response
    else:
        raise HTTPException(status_code=500, 
                detail="Redis cache connection problem")
    

@urls.get('/{in_url}/', response_model=UrlIn)
async def get_long_url(in_url: str):
    redis_client = redis_connect()
    longUrl = await url_manager.get_long_url(redis_client, in_url)
    if not longUrl:
        raise HTTPException(status_code=404, 
                detail="No long url mapped to this short url")
    longUrl = longUrl.decode('utf-8')
    log.debug (f"returned long url: {longUrl} from the url_manager")
    result = {}
    result['longUrl'] = longUrl
    
    response = {
        **result
    }
    return response

