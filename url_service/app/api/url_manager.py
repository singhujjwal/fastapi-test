from app.api.models import UrlIn, UrlOut


async def get_short_url(payload: UrlIn):
    print ("Getting short url....")
    return "short_url"

async def get_long_url():
    print ("Getting Long url....")
    return "long_url"
