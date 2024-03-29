from .models import UrlIn, UrlOut
import hashlib
import logging

from datetime import timedelta


# def get_routes_from_cache(key: str) -> str:
#     """Get data from redis."""

#     val = client.get(key)
#     return val


# def set_routes_to_cache(key: str, value: str) -> bool:
#     """Set data to redis."""

#     state = client.setex(key, timedelta(seconds=3600), value=value, )
#     return state



logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
log = logging.getLogger(__name__)


# import string

# BASE_LIST = string.digits + string.letters 
BASE_LIST = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGGHIJKLMNOPQRSTUVWXYZ'
BASE_DICT = dict((c, i) for i, c in enumerate(BASE_LIST))

def base_encode(hash_val: int, base=BASE_LIST) -> str:
    if hash_val == 0:
        return base[0]
    length = len(base)
    ret = ''
    while hash_val != 0:
        ret = base[hash_val % length] + ret
        hash_val = int(hash_val/length)
    return ret


def get_tiny_url(input_url: str) -> str:
    '''
    Design :
    1. Suppose we have a-z, A-Z and 0-9 and _ and @ as the characters in the tinyurl there will total of
    26+26+10 characters == 62 characters and let's suppose we need to have a tinyurl of 8 characters so total of pow(62,8) combinations of the input set which is 
    218 340 105 584 896 which is 218 trillion records wooah should be enough

    1000 000 requests per day * it will take years so lets move to a lower number say 6 characters long
    pow(62,6) == 56,800 235,584 56 billion records 

    '''
    
    h = hashlib.md5(input_url.encode('ascii'))
    hexnumber = h.hexdigest()[:11]
    # import pdb
    # pdb.set_trace()
    decimal_value = int(hexnumber, 16)
    return base_encode(decimal_value)

async def does_exists_in_redis():
    print ("Is it present in redis..")
    return True

async def get_short_url(payload: UrlIn):
    print ("Getting short url....")
    print (payload.longUrl)
    result_json = {}
    result_json['shortUrl'] = f"https://u.co/{get_tiny_url(payload.longUrl)}"
    print ("the tinyurl returned is {}".format(result_json['shortUrl']))
    return result_json

async def get_long_url(short_url: str):
    print ("Getting Long url....")
    result_json = {}
    result_json['longUrl'] = 'my_long_url'
    return result_json
