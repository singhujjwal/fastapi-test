from app.api.models import UrlIn, UrlOut


async def get_short_url(payload: UrlIn):
    print ("Getting short url....")
    result_json = {}
    result_json['longUrl'] = 'my_short_url'
    return result_json

async def get_long_url(short_url: str):
    print ("Getting Long url....")
    result_json = {}
    result_json['longUrl'] = 'my_long_url'
    return result_json
