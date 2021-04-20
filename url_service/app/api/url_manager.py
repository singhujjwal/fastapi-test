from app.api.models import UrlIn, UrlOut


async def get_short_url(payload: UrlIn):
    print ("Getting short url....")
    return 'my_short_url'

async def get_long_url(short_url: str):
    print ("Getting Long url....")    
    return 'my_long_url'

