from flask import request
from flask_restx import Namespace, Resource, fields
from app.services import facade

place_ns = Namespace('places', description='Place operations')

# Nested models
user_model = place_ns.model('PlaceUser', {
    'id': fields.String(),
    'name': fields.String()
})

amenity_model = place_ns.model('PlaceAmenity', {
    'id': fields.String(),
    'name': fields.String()
})

review_model = place_ns.model('PlaceReview', {
    'id': fields.String(),
    'text': fields.String(),
    'rating': fields.Integer(),
    'user_id': fields.String()
})

# Full Place model
place_model = place_ns.model('Place', {
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

@place_ns.route('/')
class PlaceList(Resource):
    @place_ns.expect(place_model)
    @place_ns.response(201, 'Place created')
    @place_ns.response(400, 'Invalid input')
    def post(self):
        try:
            place = facade.create_place(request.json)
            return place, 201
        except ValueError as e:
            return {'error': str(e)}, 400

    @place_ns.response(200, 'All places retrieved')
    def get(self):
        return facade.get_all_places(), 200

@place_ns.route('/<string:place_id>')
class PlaceResource(Resource):
    @place_ns.response(200, 'Place retrieved')
    @place_ns.response(404, 'Place not found')
    def get(self, place_id):
        try:
            return facade.get_place(place_id), 200
        except ValueError:
            return {'error': 'Place not found'}, 404

    @place_ns.expect(place_model)
    @place_ns.response(200, 'Place updated')
    @place_ns.response(400, 'Invalid input')
    @place_ns.response(404, 'Place not found')
    def put(self, place_id):
        try:
            return facade.update_place(place_id, request.json), 200
        except ValueError as e:
            if 'not found' in str(e).lower():
                return {'error': str(e)}, 404
            return {'error': str(e)}, 400

    @place_ns.response(200, 'Place deleted')
    @place_ns.response(404, 'Place not found')
    def delete(self, place_id):
        try:
            return facade.delete_place(place_id), 200
        except ValueError:
            return {'error': 'Place not found'}, 404
