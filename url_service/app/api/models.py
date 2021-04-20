#~/movie-service/app/api/models.py

from pydantic import BaseModel
from typing import List, Optional

class UrlIn(BaseModel):
    url: str

class UrlOut(UrlIn):
    shortUrl: str

