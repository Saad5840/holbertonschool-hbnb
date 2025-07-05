from flask import request
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token
from services import facade

api = Namespace('auth', description='Authentication operations')

login_model = api.model('Login', {
    'email': fields.String(required=True),
    'password': fields.String(required=True)
})

@api.route('/login')
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = facade.get_user_by_email(email)
        if not user or not user.check_password(password):
            return {'message': 'Invalid email or password'}, 401

        access_token = create_access_token(identity=user.id, additional_claims={"is_admin": user.is_admin})
        return {'access_token': access_token}, 200

