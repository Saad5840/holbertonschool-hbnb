from flask_restx import Namespace, Resource, fields
from app.services import facade

user_ns = Namespace('users', description='User operations')

# Define the user model
user_model = user_ns.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user')
})

@user_ns.route('/')
class UserList(Resource):
    @user_ns.expect(user_model, validate=True)
    @user_ns.response(201, 'User successfully created')
    @user_ns.response(400, 'Email already registered')
    @user_ns.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = user_ns.payload

        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        new_user = facade.create_user(user_data)
        return {
            'id': new_user.id,
            'first_name': new_user.first_name,
            'last_name': new_user.last_name,
            'email': new_user.email
        }, 201

    @user_ns.response(200, 'List of users retrieved successfully')
    def get(self):
        """Retrieve a list of all users"""
        users = facade.user_repo.get_all()
        result = [{
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        } for user in users]
        return result, 200

@user_ns.route('/<string:user_id>')
class UserResource(Resource):
    @user_ns.response(200, 'User details retrieved successfully')
    @user_ns.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }, 200

    @user_ns.expect(user_model, validate=True)
    @user_ns.response(200, 'User updated successfully')
    @user_ns.response(404, 'User not found')
    @user_ns.response(400, 'Invalid input data')
    def put(self, user_id):
        """Update user information by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        update_data = user_ns.payload

        if update_data.get('email') and update_data['email'] != user.email:
            existing_user = facade.get_user_by_email(update_data['email'])
            if existing_user:
                return {'error': 'Email already registered'}, 400

        user.first_name = update_data['first_name']
        user.last_name = update_data['last_name']
        user.email = update_data['email']

        facade.user_repo.update(user)
        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }, 200
