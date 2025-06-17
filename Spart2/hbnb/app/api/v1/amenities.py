from flask_restx import Namespace, Resource, fields
from app.services import facade

amenity_ns = Namespace('amenities', description='Amenity operations')

amenity_model = amenity_ns.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

@amenity_ns.route('/')
class AmenityList(Resource):
    @amenity_ns.expect(amenity_model)
    @amenity_ns.response(201, 'Amenity successfully created')
    @amenity_ns.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        try:
            amenity = facade.create_amenity(amenity_ns.payload)
            return amenity.to_dict(), 201
        except ValueError as e:
            return {'error': str(e)}, 400

    @amenity_ns.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        amenities = facade.get_all_amenities()
        return amenities, 200

@amenity_ns.route('/<string:amenity_id>')
class AmenityResource(Resource):
    @amenity_ns.response(200, 'Amenity details retrieved successfully')
    @amenity_ns.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        amenity = facade.get_amenity(amenity_id)
        if amenity:
            return amenity, 200
        return {'error': 'Amenity not found'}, 404

    @amenity_ns.expect(amenity_model)
    @amenity_ns.response(200, 'Amenity updated successfully')
    @amenity_ns.response(404, 'Amenity not found')
    @amenity_ns.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        updated = facade.update_amenity(amenity_id, amenity_ns.payload)
        if updated:
            return {'message': 'Amenity updated successfully'}, 200
        return {'error': 'Amenity not found'}, 404
