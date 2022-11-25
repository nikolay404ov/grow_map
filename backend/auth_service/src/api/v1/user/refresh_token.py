from http import HTTPStatus

from api.v1 import routes
from api.v1.common import ResponseSchema
from constants.doc_params import params_auth_default
from constants.response import MESSAGE
from flask_apispec import doc, marshal_with
from flask_jwt_extended import get_jwt_identity, jwt_required, get_jwt

from core.init import redis_db
from handler.jwt_handler import generate_jwt
from marshmallow import fields


class RefreshResponseSchema(ResponseSchema):
    access_token = fields.String(required=True)


@routes.route('/refresh', methods=['POST'])
@marshal_with(RefreshResponseSchema())
@doc(description='Get new tokens with refresh token', tags=['users'], params=params_auth_default)
@jwt_required(refresh=True)
def refresh():
    user_id = get_jwt_identity()
    jwt = generate_jwt(user_id)

    jti = get_jwt().get("jti")
    if redis_db.get(str(jti)):
        redis_db.delete(str(jti))
    return {MESSAGE: 'Successful refresh', **jwt}, HTTPStatus.OK
