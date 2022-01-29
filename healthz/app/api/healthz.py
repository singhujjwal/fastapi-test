from typing import List
from urllib import response
from fastapi import APIRouter, HTTPException
import logging


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
log = logging.getLogger(__name__)


healthz = APIRouter()

# @healthz.post('/', response_model=UrlOut, status_code=201)
# async def get_short_url(payload: UrlIn, 
#     producer: AIOKafkaProducer =  Depends(get_producer)):
#     short_url = await url_manager.get_short_url(payload)
# # Check in database if the short_url and long_url keypair is present
# #   Later ensure collisions is not there
# #   Also set expiry 
# #   update_db(short_url, payload.longUrl)

#     response = {
#         **short_url
#     }
#     return response

@healthz.get('/')
async def get_health_status():
    return {"Hello": "World"}
