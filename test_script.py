from pydantic.errors import AnyStrMaxLengthError
import requests
from random import randint
import asyncio
import json


def start_firing():
    '''
    Startin firing
    '''

    randstring = f'googlemy-{randint(0, 100000)}'
    # randstring = f'googlemy-1'

    payload = {'longUrl': f'https://{randstring}.com'}
    headers = {'Content-Type': 'application/json', 'accept': 'application/json'}
    r = requests.post(url="http://127.0.0.1:8121/api/v1/urls/", 
                json=payload, 
                headers=headers, 
                verify=False)
    print (r.text)
    res = json.loads(r.text)
    return res['shortUrl'][13:]

# loop = asyncio.get_event_loop()


def get_long_url(shortUrl: str):
    '''
    Get the long url from the short url
    '''
    headers = {'accept': 'application/json'}
    r = requests.get(url=f"http://127.0.0.1:8121/api/v1/urls/{shortUrl}/",
                headers=headers, 
                verify=False)
    print (r.text)

if __name__ == '__main__':
    # shortUrl = start_firing()
    shortUrl ='xcasdA3'
    get_long_url(shortUrl)

