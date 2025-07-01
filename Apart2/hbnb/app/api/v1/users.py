from flask_restx import Namespace, Resource, fields
from flask import request
from app.services.facade import HBnBFacade

user_ns = Namespace('users', description='User related operations')
facade = HBnBFacade()

# Model for input (includes password)
user_input_model = user_ns.model('UserInput', {
    'name': fields.String(required=True, description="Full name of the user"),
    'email': fields.String(required=True, description="Email address of the user"),
    'password': fields.String(required=True, description="User password", min_length=6),
})

# Model for output (no password included)
user_output_model = user_ns.model('User', {
    'id': fields.String(readOnly=True, description="User ID"),
    'name': fields.String(description="Full name of the user"),
    'email': fields.String(description="Email address of the user"),
})

@user_ns.route('/')
class UserList(Resource):
    @user_ns.marshal_list_with(user_output_model)
    def get(self):
        """List all users"""
        return facade.get_all_users()

    @user_ns.expect(user_input_model, validate=True)
    @user_ns.marshal_with(user_output_model, code=201)
    def post(self):
        """Create a new user"""
        data = request.json
        return facade.create_user(data), 201

@user_ns.route('/<string:id>')
@user_ns.param('id', 'The User identifier')
class User(Resource):
    @user_ns.marshal_with(user_output_model)
    def get(self, id):
        """Get a user by ID"""
        return facade.get_user(id)
