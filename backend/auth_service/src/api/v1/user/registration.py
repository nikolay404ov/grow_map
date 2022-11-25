import hashlib
import random
from http import HTTPStatus

from api.v1 import routes
from api.v1.common import ResponseSchema
from constants.response import MESSAGE
from db.user import Users
from flask_apispec import doc, marshal_with, use_kwargs
from handler.user_handler import (check_email_correct, check_username_correct,
                                  registrate)
from marshmallow import Schema, fields


class RegistrationSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)
    email = fields.String(required=True)


@routes.route('/registration', methods=['POST'])
@use_kwargs(RegistrationSchema())
@marshal_with(ResponseSchema())
@doc(description='Registration of new user', tags=['users'])
def registration(**kwargs):
    email = kwargs.get('email')
    username = kwargs.get('username')
    password = kwargs.get('password')

    if not check_email_correct(email):
        return {MESSAGE: 'Bad email address'}, HTTPStatus.BAD_REQUEST

    if not check_username_correct(username):
        return {MESSAGE: 'Bad email address'}, HTTPStatus.BAD_REQUEST

    if Users.find_by_email(email):
        return {MESSAGE: 'Such email already exists'}, HTTPStatus.BAD_REQUEST

    if Users.find_by_username(username):
        return {MESSAGE: 'Such username already exists'}, HTTPStatus.BAD_REQUEST

    registrate(username, email, password)

    return {MESSAGE: 'Successfully created'}, HTTPStatus.OK
