from flask import request
from flask_restx import Namespace, Resource, fields
from services import facade
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity

api = Namespace('users', description='User operations')

user_model = api.model('User', {
    'id': fields.String(readOnly=True),
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'email': fields.String(required=True),
    'is_admin': fields.Boolean,
})

user_input_model = api.inherit('UserInput', user_model, {
    'password': fields.String(required=True)
})

@api.route('/')
class UserList(Resource):
    @api.expect(user_input_model)
    @api.marshal_with(user_model, code=201)
    def post(self):
        data = request.get_json()
        user = facade.create_user(data)
        return user.to_dict(), 201

