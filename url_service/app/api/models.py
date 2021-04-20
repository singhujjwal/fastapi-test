#~/movie-service/app/api/models.py

from pydantic import BaseModel
from typing import List, Optional

class UrlIn(BaseModel):
    longUrl: str

class UrlOut(BaseModel):
    longUrl: str

