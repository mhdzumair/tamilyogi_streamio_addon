from typing import List

from pydantic import BaseModel, Field


class Catalog(BaseModel):
    id: str
    name: str
    type: str


class Meta(BaseModel):
    id: str
    name: str
    type: str = Field(default="movie")
    poster: str

    class Config:
        orm_mode = True


class Movie(BaseModel):
    metas: List[Meta] | list = []


class Stream(BaseModel):
    title: str
    url: str


class Streams(BaseModel):
    streams: List[Stream] | list = []
