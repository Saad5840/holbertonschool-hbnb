from flask_restx import Namespace, Resource, fields
from flask import request
from app.services.facade import HBnBFacade

user_ns = Namespace('users', description='User related operations')
facade = HBnBFacade()

user_model = user_ns.model('User', {
    'id': fields.String(readOnly=True, description="User ID"),
    'name': fields.String(required=True, description="Full name of the user"),
    'email': fields.String(required=True, description="Email address of the user"),
})

@user_ns.route('/')
class UserList(Resource):
    @user_ns.marshal_list_with(user_model)
    def get(self):
        """List all users"""
        return facade.get_all_users()

    @user_ns.expect(user_model, validate=True)
    @user_ns.marshal_with(user_model, code=201)
    def post(self):
        """Create a new user"""
        data = user_ns.payload
        return facade.create_user(data), 201

@user_ns.route('/<string:id>')
@user_ns.param('id', 'The User identifier')
class User(Resource):
    @user_ns.marshal_with(user_model)
    def get(self, id):
        """Get a user by ID"""
        return facade.get_user(id)
