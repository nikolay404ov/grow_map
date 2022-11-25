from http import HTTPStatus

from api.v1 import routes
from api.v1.common import ResponseSchema
from constants.doc_params import params_auth_default
from constants.response import MESSAGE
from flask_apispec import doc, marshal_with
from flask_jwt_extended import jwt_required, get_jwt

from handler.user_handler import is_logout


@routes.route('/is_active', methods=['GET'])
@marshal_with(ResponseSchema())
@doc(description='Check is user still logged in', tags=['users'], params=params_auth_default)
@jwt_required()
def is_active():
    jti = str(get_jwt().get('jti'))
    if is_logout(jti):
        return {MESSAGE: 'Logged out'}, HTTPStatus.NOT_FOUND
    return {MESSAGE: 'Profile not found'}, HTTPStatus.OK
