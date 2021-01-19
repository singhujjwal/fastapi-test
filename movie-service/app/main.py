#~/movie-service/app/main.py

from fastapi import FastAPI
from app.api.movies import movies
from app.api.db import metadata, database, engine

metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


#app.include_router(movies)

app.include_router(movies, prefix='/api/v1/movies', tags=['movies'])
