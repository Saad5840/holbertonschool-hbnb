from flask import request
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from services import facade
from app.extensions import db
from infrastructure.models import User

api = Namespace('places', description='Place operations')

place_model = api.model('Place', {
    'id': fields.String(readOnly=True),
    'name': fields.String(required=True),
    'description': fields.String,
    'owner_id': fields.String,
})

@api.route('/')
class PlaceList(Resource):
    def get(self):
        """Get all places with their amenities."""
        places = facade.get_all_places()
        places_data = []
        for place in places:
            place_dict = place.to_dict()
            # Add amenities with icons
            place_dict['amenities'] = []
            for amenity in place.amenities:
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
                place_dict['amenities'].append(amenity_dict)
            places_data.append(place_dict)
        return places_data, 200

    @jwt_required()
    @api.expect(place_model)
    def post(self):
        data = request.get_json()
        current_user_id = get_jwt_identity()
        data['owner_id'] = current_user_id
        place = facade.create_place(data)
        return place.to_dict(), 201

@api.route('/<string:place_id>')
class PlaceDetail(Resource):
    def get(self, place_id):
        """Get a specific place with its reviews."""
        place = facade.get_place_by_id(place_id)
        if not place:
            return {'message': 'Place not found'}, 404
        
        place_dict = place.to_dict()
        
        # Add amenities with icons
        place_dict['amenities'] = []
        for amenity in place.amenities:
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
            place_dict['amenities'].append(amenity_dict)
        
        # Add owner information
        owner = db.session.query(User).filter_by(id=place.owner_id).first()
        if owner:
            place_dict['owner_name'] = f"{owner.first_name} {owner.last_name}"
        
        # Add reviews
        reviews = facade.get_reviews_by_place(place_id)
        place_dict['reviews'] = []
        for review in reviews:
            review_dict = review.to_dict()
            # Get user info for the review
            user = db.session.query(User).filter_by(id=review.user_id).first()
            if user:
                review_dict['user_name'] = f"{user.first_name} {user.last_name}"
            place_dict['reviews'].append(review_dict)
        
        return place_dict, 200

