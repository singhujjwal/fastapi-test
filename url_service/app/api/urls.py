#~/python-microservices/movie-service/app/api/movies.py

from typing import List
from fastapi import APIRouter, HTTPException
from app.api.models import UrlOut, UrlIn

urls = APIRouter()

@urls.post('/', response_model=UrlOut, status_code=201)
async def get_short_url(payload: UrlIn):
    short_url = await url_manager.get_short_url(payload)
    response = {
        'shortUrl': short_url,
        **payload.dict()
    }
    return response

@movies.get('/{shortUrl}/', response_model=UrlOut)
async def get_long_url(in_url: str):
    long_url = await url_manager.get_long_url(in_url)
    if not long_url:
        raise HTTPException(status_code=404, detail="No long url mapped to this short url")
    return long_url
