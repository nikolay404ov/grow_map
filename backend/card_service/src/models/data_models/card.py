import uuid
from typing import Union

from models.base import DefaultModel


class Card(DefaultModel):
    id: uuid.UUID
    skill: str
    progress: str
    comment: Union[str, None]
