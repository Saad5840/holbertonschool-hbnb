from flask import request
from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('places', description='Place operations')

# Nested models
user_model = api.model('PlaceUser', {
    'id': fields.String(),
    'name': fields.String()
})

amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(),
    'name': fields.String()
})

review_model = api.model('PlaceReview', {
    'id': fields.String(),
    'text': fields.String(),
    'rating': fields.Integer(),
    'user_id': fields.String()
})

# Full Place model
place_model = api.model('Place', {
    'title': fields.String(required=True),
    'description': fields.String(),
    'price': fields.Float(required=True),
    'latitude': fields.Float(required=True),
    'longitude': fields.Float(required=True),
    'owner_id': fields.String(required=True),
    'owner': fields.Nested(user_model),
    'amenities': fields.List(fields.Nested(amenity_model)),
    'reviews': fields.List(fields.Nested(review_model))
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place created')
    @api.response(400, 'Invalid input')
    def post(self):
        try:
            place = facade.create_place(request.json)
            return place, 201
        except ValueError as e:
            return {'error': str(e)}, 400

    @api.response(200, 'All places retrieved')
    def get(self):
        return facade.get_all_places(), 200

@api.route('/<string:place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place retrieved')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        try:
            return facade.get_place(place_id), 200
        except ValueError:
            return {'error': 'Place not found'}, 404

    @api.expect(place_model)
    @api.response(200, 'Place updated')
    @api.response(400, 'Invalid input')
    @api.response(404, 'Place not found')
    def put(self, place_id):
        try:
            return facade.update_place(place_id, request.json), 200
        except ValueError as e:
            if 'not found' in str(e).lower():
                return {'error': str(e)}, 404
            return {'error': str(e)}, 400

    @api.response(200, 'Place deleted')
    @api.response(404, 'Place not found')
    def delete(self, place_id):
        try:
            return facade.delete_place(place_id), 200
        except ValueError:
            return {'error': 'Place not found'}, 404
