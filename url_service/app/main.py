#~/url-service/app/main.py

from fastapi import FastAPI
from app.api.urls import urls

app = FastAPI(openapi_url="/api/v1/urls/openapi.json", docs_url="/api/v1/urls/docs")
app.include_router(urls, prefix='/api/v1/urls', tags=['urls'])
