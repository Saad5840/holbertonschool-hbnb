from flask import request
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt
from services import facade

api = Namespace('amenities', description='Amenity operations')

amenity_model = api.model('Amenity', {
    'id': fields.String(readOnly=True),
    'name': fields.String(required=True),
})

@api.route('/')
class AmenityList(Resource):
    @jwt_required()
    def post(self):
        claims = get_jwt()
        if not claims.get('is_admin'):
            return {'message': 'Admin only'}, 403
        data = request.get_json()
        amenity = facade.create_amenity(data)
        return amenity.to_dict(), 201

