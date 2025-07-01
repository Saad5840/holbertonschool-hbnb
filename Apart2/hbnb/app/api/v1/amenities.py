from flask_restx import Namespace, Resource, fields
from flask import request
from app.services.facade import HBnBFacade

amenity_ns = Namespace('amenities', description='Amenity related operations')
facade = HBnBFacade()

amenity_model = amenity_ns.model('Amenity', {
    'id': fields.String(readOnly=True),
    'name': fields.String(required=True, description='Amenity name'),
})

@amenity_ns.route('/')
class AmenityList(Resource):
    @amenity_ns.marshal_list_with(amenity_model)
    def get(self):
        """List all amenities"""
        return facade.get_all_amenities()

    @amenity_ns.expect(amenity_model, validate=True)
    @amenity_ns.marshal_with(amenity_model, code=201)
    def post(self):
        """Create a new amenity"""
        data = amenity_ns.payload
        return facade.create_amenity(data), 201

@amenity_ns.route('/<string:id>')
@amenity_ns.param('id', 'The Amenity identifier')
class Amenity(Resource):
    @amenity_ns.marshal_with(amenity_model)
    def get(self, id):
        """Get an amenity by ID"""
        return facade.get_amenity(id)

    def delete(self, id):
        """Delete an amenity by ID"""
        # You can implement facade.delete_amenity(id) here
        return {'message': 'Delete not implemented'}, 405
