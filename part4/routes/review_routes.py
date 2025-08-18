from flask import request
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from services import facade
from app.extensions import db
from infrastructure.models import User, Place

api = Namespace('reviews', description='Review operations')

review_model = api.model('Review', {
    'id': fields.String(readOnly=True),
    'text': fields.String(required=True),
    'place_id': fields.String(required=True),
    'user_id': fields.String,
})

@api.route('/')
class ReviewList(Resource):
    def get(self):
        """Get all reviews with user and place information."""
        reviews = facade.get_all_reviews()
        reviews_data = []
        for review in reviews:
            review_dict = review.to_dict()
            # Get user info
            user = db.session.query(User).filter_by(id=review.user_id).first()
            if user:
                review_dict['user_name'] = f"{user.first_name} {user.last_name}"
            # Get place info
            place = db.session.query(Place).filter_by(id=review.place_id).first()
            if place:
                review_dict['place_name'] = place.name
            reviews_data.append(review_dict)
        return reviews_data, 200

    @jwt_required()
    @api.expect(review_model)
    def post(self):
        data = request.get_json()
        current_user_id = get_jwt_identity()
        data['user_id'] = current_user_id
        review = facade.create_review(data)
        return review.to_dict(), 201

