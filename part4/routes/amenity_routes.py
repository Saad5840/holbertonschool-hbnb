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
    def get(self):
        """Get all amenities."""
        amenities = facade.get_all_amenities()
        amenities_data = []
        for amenity in amenities:
            amenity_dict = amenity.to_dict()
            # Map amenity names to phosphor icons
            icon_mapping = {
                'WiFi': 'ph-wifi-high',
                'Kitchen': 'ph-cooking-pot',
                'Free Parking': 'ph-car',
                'Air Conditioning': 'ph-wind',
                'Swimming Pool': 'ph-swimming-pool',
                'Gym': 'ph-dumbbell',
                'TV': 'ph-television',
                'Washer/Dryer': 'ph-washing-machine',
                'Balcony': 'ph-house-line',
                'Fireplace': 'ph-fire',
                'Pet Friendly': 'ph-dog',
                'Breakfast': 'ph-bread',
                'Hot Tub': 'ph-bathtub',
                'Garden': 'ph-tree',
                'Workspace': 'ph-laptop'
            }
            amenity_dict['icon'] = icon_mapping.get(amenity.name, 'ph-check')
            amenities_data.append(amenity_dict)
        return amenities_data, 200

    @jwt_required()
    def post(self):
        claims = get_jwt()
        if not claims.get('is_admin'):
            return {'message': 'Admin only'}, 403
        data = request.get_json()
        amenity = facade.create_amenity(data)
        return amenity.to_dict(), 201

