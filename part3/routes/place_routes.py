from flask import request
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from services import facade

api = Namespace('places', description='Place operations')

place_model = api.model('Place', {
    'id': fields.String(readOnly=True),
    'name': fields.String(required=True),
    'description': fields.String,
    'owner_id': fields.String,
})

@api.route('/')
class PlaceList(Resource):
    @jwt_required()
    @api.expect(place_model)
    def post(self):
        data = request.get_json()
        current_user_id = get_jwt_identity()
        data['owner_id'] = current_user_id
        place = facade.create_place(data)
        return place.to_dict(), 201

