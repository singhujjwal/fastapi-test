from fastapi import FastAPI
from fastapi import Depends
import logging




from .api.urls import urls
from .dependencies import get_producer, initialize, consume, consumer, consumer_task
import os

consumer = None
consumer_task = None
USE_KAFKA = os.getenv('USE_KAFKA', False)

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
log = logging.getLogger(__name__)


app = FastAPI(openapi_url="/api/v1/urls/openapi.json", 
                docs_url="/api/v1/urls/docs")


# Below code will be used to pass the producer object which is not needed in synchronous 
# process
# app.include_router(
#     urls, prefix='/api/v1/urls',
#     dependencies=[Depends(get_producer)],
#     tags=['urls']
#     )

app.include_router(
    urls, prefix='/api/v1/urls',
    tags=['urls']
    )


@app.on_event("startup")
async def startup_event():
    log.info('Initializing URL service  ...')
    if USE_KAFKA:
        await initialize()
        await consume()
    # await get_producer().start()

@app.on_event("shutdown")
async def shutdown_event():
    log.info('Shutting down API')
    if USE_KAFKA:
        consumer_task.cancel()
        await consumer.stop()