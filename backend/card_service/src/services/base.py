from functools import lru_cache

from db.database_models import Person, Card


class BaseService:

    def get_all_persons(self, session):
        return session.query(Person).all()

    def get_card(self, person_id: str, session):
        return session.query(Card).filter(Card.person_id == person_id).all()


@lru_cache()
def get_base_service() -> BaseService:
    return BaseService()
