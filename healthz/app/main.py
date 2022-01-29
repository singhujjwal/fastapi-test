from fastapi import FastAPI
from fastapi import Depends
import logging

from .api.healthz import healthz
import os

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
log = logging.getLogger(__name__)


app = FastAPI(openapi_url="/api/v1/healthz/openapi.json", 
                docs_url="/api/v1/healthz/docs")

app.include_router(
    healthz, prefix='/api/v1/healthz',
    tags=['healthz']
    )


@app.on_event("startup")
async def startup_event():
    log.info('Initializing healthz service  ...')


@app.on_event("shutdown")
async def shutdown_event():
    log.info('Shutting down healthz service.......')
