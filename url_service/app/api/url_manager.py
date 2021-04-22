from app.api.models import UrlIn, UrlOut
import hashlib
import logging


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
log = logging.getLogger(__name__)


# import string

# BASE_LIST = string.digits + string.letters 
BASE_LIST = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGGHIJKLMNOPQRSTUVWXYZ'
BASE_DICT = dict((c, i) for i, c in enumerate(BASE_LIST))

def base_encode(integer, base=BASE_LIST):
    if integer == 0:
        return base[0]

    length = len(base)
    ret = ''
    while integer != 0:
        ret = base[integer % length] + ret
        integer /= length

    return ret


def get_tiny_url(input_url):
    '''
    Design :
    1. Suppose we have a-z, A-Z and 0-9 and _ and @ as the characters in the tinyurl there will total of
    26+26+10 characters == 62 characters and let's suppose we need to have a tinyurl of 8 characters so total of pow(62,8) combinations of the input set which is 
    218 340 105 584 896 which is 218 trillion records wooah should be enough

    1000 000 requests per day * it will take years so lets move to a lower number say 6 characters long
    pow(62,6) == 56,800 235,584 56 billion records 

    '''
    
    h = hashlib.md5(input_url.encode())
    hexnumber = h.hexdigest()[:11]
    decimal_value = int(hexnumber, 16)
    return base_encode(decimal_value)

async def get_short_url(payload: UrlIn):
    print ("Getting short url....")
    print ("The url input is {}".format(UrlIn.longUrl))
    result_json = {}
    result_json['tinyUrl'] = get_tiny_url(UrlIn.longUrl)
    return result_json

async def get_long_url(short_url: str):
    print ("Getting Long url....")
    result_json = {}
    result_json['longUrl'] = 'my_long_url'
    return result_json
