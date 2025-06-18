from flask_restx import Namespace, Resource, fields
from flask import request
from app.services.facade import HBnBFacade

place_ns = Namespace('places', description='Place related operations')
facade = HBnBFacade()

place_model = place_ns.model('Place', {
    'id': fields.String(readOnly=True),
    'title': fields.String(required=True, description="Title of the place"),
    'description': fields.String(description="Optional description"),
    'price': fields.Float(required=True, description="Price per night"),
    'latitude': fields.Float(required=True, description="Latitude"),
    'longitude': fields.Float(required=True, description="Longitude"),
    'owner_id': fields.String(required=True, description="User ID of the owner"),
    'amenity_ids': fields.List(fields.String, description="List of amenity IDs"),
})

@place_ns.route('/')
class PlaceList(Resource):
    @place_ns.marshal_list_with(place_model)
    def get(self):
        """List all places"""
        return facade.get_all_places()

    @place_ns.expect(place_model, validate=True)
    @place_ns.marshal_with(place_model, code=201)
    def post(self):
        """Create a new place"""
        data = place_ns.payload
        return facade.create_place(data), 201

@place_ns.route('/<string:id>')
@place_ns.param('id', 'The Place identifier')
class Place(Resource):
    @place_ns.marshal_with(place_model)
    def get(self, id):
        """Get a place by ID"""
        return facade.get_place(id)

    @place_ns.expect(place_model, validate=True)
    @place_ns.marshal_with(place_model)
    def put(self, id):
        """Update a place by ID"""
        data = place_ns.payload
        return facade.update_place(id, data)

    def delete(self, id):
        """Delete a place by ID"""
        facade.delete_place(id)
        return {'message': f'Place {id} deleted successfully'}, 204
