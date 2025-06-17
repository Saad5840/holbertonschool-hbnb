from flask_restx import Namespace, Resource, fields
from flask import request
from app.services import facade

review_ns = Namespace('reviews', description='Review operations')

review_model = review_ns.model('Review', {
    'text': fields.String(required=True),
    'rating': fields.Integer(required=True),
    'user_id': fields.String(required=True),
    'place_id': fields.String(required=True)
})

@review_ns.route('/')
class ReviewList(Resource):
    @review_ns.expect(review_model)
    @review_ns.response(201, 'Review created')
    @review_ns.response(400, 'Invalid input')
    def post(self):
        try:
            review = facade.create_review(request.json)
            return review, 201
        except ValueError as e:
            return {"error": str(e)}, 400

    @review_ns.response(200, 'All reviews retrieved')
    def get(self):
        return facade.get_all_reviews(), 200

@review_ns.route('/<string:review_id>')
class ReviewResource(Resource):
    @review_ns.response(200, 'Review retrieved')
    @review_ns.response(404, 'Not found')
    def get(self, review_id):
        try:
            return facade.get_review(review_id), 200
        except ValueError:
            return {"error": "Review not found"}, 404

@review_ns.route('/places/<string:place_id>/reviews')
class PlaceReviewList(Resource):
    @review_ns.response(200, 'Reviews for place retrieved')
    @review_ns.response(404, 'Place not found')
    def get(self, place_id):
        try:
            return facade.get_reviews_by_place(place_id), 200
        except ValueError:
            return {"error": "Place not found"}, 404
