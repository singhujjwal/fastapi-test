from .models import UrlIn, UrlOut
import hashlib
import logging
from ..utils.formatlogs import CustomFormatter


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
log.addHandler(ch)



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
    log.debug ("Is it present in redis..")
    return True

async def get_short_url(redis_client, payload: UrlIn):
    log.debug ("Getting short url....")
    log.debug (payload.longUrl)
    result_json = {}
   
    # TODO: convert to async await
    tiny_url = get_tiny_url(payload.longUrl)
    
    # Make below atomic ??
    # TODO put a lock think how ??
    if redis_client.exists(tiny_url):
        log.info("tiny url already present in the cache, not putting it again...")
    else:
        redis_client.set(tiny_url, payload.longUrl)

    # save some space by having the part http://u.co/
    result_json['shortUrl'] = f"https://u.co/{tiny_url}"
    log.debug ("the tinyurl returned is {}".format(result_json['shortUrl']))
    return result_json

async def get_long_url(redis_client, short_url: str):
    longUrl = None
    if redis_client.exists(short_url):
        longUrl = redis_client.get(short_url)
        log.debug (f"Getting Long url....{longUrl}")
    else:
        log.info(f"No long url mapped to the short url {short_url}")

    return longUrl
