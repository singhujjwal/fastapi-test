#~/movie-service/app/main.py

from fastapi import FastAPI
from app.api.movies import movies
from app.api.db import metadata, database, engine

metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/urls/openapi.json", docs_url="/api/v1/urls/docs")
app.include_router(movies, prefix='/api/v1/urls', tags=['urls'])
