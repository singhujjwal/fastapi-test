from pydantic.errors import AnyStrMaxLengthError
import requests
from random import randint
import asyncio


def start_firing():
    '''
    Startin firing
    '''

    randstring = f'googlemy-{randint(0, 1000000)}'

    payload = {'longUrl': f'https://{randstring}.com'}
    headers = {'Content-Type': 'application/json', 'accept': 'application/json'}
    r = requests.post(url="http://127.0.0.1:8121/api/v1/urls/", 
                json=payload, 
                headers=headers, 
                verify=False)
    print (r.text)

# loop = asyncio.get_event_loop()


if __name__ == '__main__':
    start_firing()

