from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new review"""
        data = api.payload
        user = facade.get_user(data["user_id"])
        place = facade.get_place(data["place_id"])

        if not user:
            return {"error": "User not found"}, 404
        if not place:
            return {"error": "Place not found"}, 404

        review = facade.create_review(data)
        return {
            "id": review.id,
            "text": review.text,
            "user_id": review.user_id,
            "place_id": review.place_id,
            "created_at": review.created_at,
            "updated_at": review.updated_at,
        }, 201

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self, review_id):
        """Retrieve a list of all reviews"""
        review = facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404
        return {
            "id": review.id,
            "text": review.text,
            "user_id": review.user_id,
            "place_id": review.place_id,
            "created_at": review.created_at,
            "updated_at": review.updated_at,
        }, 200
        pass

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        review = facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404
        return {
            "id": review.id,
            "text": review.text,
            "user_id": review.user_id,
            "place_id": review.place_id,
            "created_at": review.created_at,
            "updated_at": review.updated_at,
        }, 200

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    def put(self, review_id):
        """Update a review's information"""
        data = api.payload
        review = facade.update_review(review_id, data)
        if not review:
            return {"error": "Review not found"}, 404
        return {
            "id": review.id,
            "text": review.text,
            "user_id": review.user_id,
            "place_id": review.place_id,
            "updated_at": review.updated_at,
        }, 200

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review"""
        success = facade.delete_review(review_id)
        if not success:
            return {"error": "Review not found"}, 404
        return '', 204

@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place"""
        # Placeholder for logic to return a list of reviews for a place
        pass