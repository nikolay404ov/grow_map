from sqlalchemy import Column, ForeignKey, String, DATETIME
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from .base import Base


class Person(Base):
    __tablename__ = "person"

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    created = Column(DATETIME, nullable=False, default=datetime.now())
    modified = Column(DATETIME, nullable=False, default=datetime.now())


class Card(Base):
    __tablename__ = "card"

    id = Column(UUID(as_uuid=True), primary_key=True)
    person_id = Column(UUID(as_uuid=True), ForeignKey("person.id"), nullable=False)
    skill = Column(String, nullable=False)
    progress = Column(String)
    comment = Column(String)
    created = Column(DATETIME, nullable=False, default=datetime.now())
    modified = Column(DATETIME, nullable=False, default=datetime.now())
