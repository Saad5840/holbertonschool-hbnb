from flask_restx import Namespace, Resource, fields
from flask import request
from app.services.facade import HBnBFacade

review_ns = Namespace('reviews', description='Review related operations')
facade = HBnBFacade()

review_model = review_ns.model('Review', {
    'id': fields.String(readOnly=True),
    'text': fields.String(required=True, description="Review content"),
    'rating': fields.Integer(required=True, min=1, max=5, description="Rating from 1 to 5"),
    'user_id': fields.String(required=True, description="ID of the reviewer"),
    'place_id': fields.String(required=True, description="ID of the reviewed place"),
})

@review_ns.route('/')
class ReviewList(Resource):
    @review_ns.marshal_list_with(review_model)
    def get(self):
        """List all reviews"""
        return facade.get_all_reviews()

    @review_ns.expect(review_model, validate=True)
    @review_ns.marshal_with(review_model, code=201)
    def post(self):
        """Create a new review"""
        data = review_ns.payload
        return facade.create_review(data), 201

@review_ns.route('/<string:id>')
@review_ns.param('id', 'The Review identifier')
class Review(Resource):
    @review_ns.marshal_with(review_model)
    def get(self, id):
        """Get a review by ID"""
        return facade.get_review(id)

    @review_ns.expect(review_model, validate=True)
    @review_ns.marshal_with(review_model)
    def put(self, id):
        """Update a review by ID"""
        data = review_ns.payload
        return facade.update_review(id, data), 200

    def delete(self, id):
        """Delete a review by ID"""
        facade.delete_review(id)
        return {'message': f'Review {id} deleted successfully'}, 204
