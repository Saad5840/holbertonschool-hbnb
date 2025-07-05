from flask import request
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from services import facade

api = Namespace('reviews', description='Review operations')

review_model = api.model('Review', {
    'id': fields.String(readOnly=True),
    'text': fields.String(required=True),
    'place_id': fields.String(required=True),
    'user_id': fields.String,
})

@api.route('/')
class ReviewList(Resource):
    @jwt_required()
    @api.expect(review_model)
    def post(self):
        data = request.get_json()
        current_user_id = get_jwt_identity()
        data['user_id'] = current_user_id
        review = facade.create_review(data)
        return review.to_dict(), 201

