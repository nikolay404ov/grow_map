from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from db.base import get_session
from models.data_models.card import Card
from models.data_models.person import Person
from services.base import BaseService
from services.base import get_base_service

router = APIRouter()


@router.get("/card_person/{person_id}",
            response_model=List[Card],
            response_description='Get person card')
async def card_person(
        person_id: str,
        card_service: BaseService = Depends(get_base_service),
        db_session: AsyncSession = Depends(get_session)
) -> List[Card]:
    """
    Response list of objects:
    - **id**: UUID of object in DB
    - **skill**: Name of skill
    - **progress**: Progress in skill
    - **comment**: Some comments
    """

    list_of_skills = card_service.get_card(person_id, db_session)
    if not list_of_skills:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)

    return [Card(id=c.id,
                 skill=c.skill,
                 progress=c.progress,
                 comment=c.comment) for c in list_of_skills]


@router.get("/persons", response_model=List[Person], response_description='Get all persons')
async def person(
        card_service: BaseService = Depends(get_base_service),
        db_session: AsyncSession = Depends(get_session)
) -> List[Person]:
    """
    Response list of objects:
    - **id**: UUID of object in DB
    - **name**: Person name
    """

    person_list = card_service.get_all_persons(db_session)
    if not person_list:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)
    return [Person(id=p.id,
                   name=p.name) for p in person_list]
