import uuid

from models.base import DefaultModel


class Person(DefaultModel):
    id: uuid.UUID
    name: str
