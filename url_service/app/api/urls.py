from typing import List
from ..dependencies import get_producer
from aiokafka.producer.producer import AIOKafkaProducer
from fastapi import APIRouter, HTTPException
import logging

# from ..dependencies import get_producer

from fastapi.param_functions import Depends


from .models import UrlOut, UrlIn
from . import url_manager


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
log = logging.getLogger(__name__)


urls = APIRouter()

@urls.post('/', response_model=UrlOut, status_code=201)
async def get_short_url(payload: UrlIn, producer: AIOKafkaProducer =  Depends(get_producer)):
    short_url = await url_manager.get_short_url(payload)
    print(producer)

# Check in database if the short_url and long_url keypair is present
#   Later ensure collisions is not there
#   Also set expiry 
#   update_db(short_url, payload.longUrl)

    response = {
        'shortUrl': short_url,
        **payload.dict()
    }
    return response

@urls.get('/{in_url}/', response_model=UrlOut)
async def get_long_url(in_url: str):
    long_url = await url_manager.get_long_url(in_url)
    print ("rturned long url from the url_manager")
    if not long_url:
        raise HTTPException(status_code=404, 
                detail="No long url mapped to this short url")
    return long_url
