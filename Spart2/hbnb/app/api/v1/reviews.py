from flask_restx import Namespace, Resource, fields
from flask import request
from app.services import facade

api = Namespace('reviews', description='Review operations')

review_model = api.model('Review', {
    'text': fields.String(required=True),
    'rating': fields.Integer(required=True),
    'user_id': fields.String(required=True),
    'place_id': fields.String(required=True)
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review created')
    @api.response(400, 'Invalid input')
    def post(self):
        try:
            review = facade.create_review(request.json)
            return review, 201
        except ValueError as e:
            return {"error": str(e)}, 400

    @api.response(200, 'All reviews retrieved')
    def get(self):
        return facade.get_all_reviews(), 200

@api.route('/<string:review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review retrieved')
    @api.response(404, 'Not found')
    def get(self, review_id):
        try:
            return facade.get_review(review_id), 200
        except ValueError:
            return {"error": "Review not found"}, 404

    @api.expect(review_model)
    @api.response(200, 'Review updated')
    @api.response(404, 'Not found')
    @api.response(400, 'Invalid input')
    def put(self, review_id):
        try:
            return facade.update_review(review_id, request.json), 200
        except ValueError as e:
            return {"error": str(e)}, 404 if "not found" in str(e).lower() else 400

    @api.response(200, 'Review deleted')
    @api.response(404, 'Not found')
    def delete(self, review_id):
        try:
            return facade.delete_review(review_id), 200
        except ValueError:
            return {"error": "Review not found"}, 404

@api.route('/places/<string:place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'Reviews for place retrieved')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        try:
            return facade.get_reviews_by_place(place_id), 200
        except ValueError:
            return {"error": "Place not found"}, 404
