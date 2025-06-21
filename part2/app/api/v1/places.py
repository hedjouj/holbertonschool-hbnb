from flask_restx import Namespace, Resource, fields
from app.services.facade import facade


api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

# Adding the review model
review_model = api.model('PlaceReview', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Text of the review'),
    'rating': fields.Integer(description='Rating of the place (1-5)'),
    'user_id': fields.String(description='ID of the user')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
<<<<<<< HEAD
<<<<<<< HEAD
    'amenities': fields.List(fields.Nested(amenity_model), description='List of amenities')
=======
    'amenities': fields.List(fields.Nested(amenity_model), description='List of amenities'),
    'reviews': fields.List(fields.Nested(review_model), description='List of reviews')
>>>>>>> 6f33dcb (last update with review)
=======
    'amenities': fields.List(fields.Nested(amenity_model), description='List of amenities')
>>>>>>> 4560d9a (fix bug facade)
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        # data = api.payload
        # title = data.get('title')
        # description = data.get('description')
        # price = data.get('price')
        # latitude = data.get('latitude')
        # longitude = data.get('longitude')
        # owner_id = data.get('owner_id')
        # amenities = data.get('amenities', [])
        place_data = api.payload
        try:
            new_place = facade.create_place(place_data)
            return new_place.to_dict(), 201
        except ValueError as e:
            api.abort(400, 'Failed to create place: ' + str(e))
        except TypeError as e:
            api.abort(400, 'Invalid input data: ' + str(e))

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        places = facade.get_all_places()
        return [place.to_dict()
                for place in places], 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found3')
    def get(self, place_id):
        '''Get amenity details with ID'''
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'place not found4'}, 404
        return place.to_dict(), 200

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found2')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        '''Update amenity details with ID'''
        place_data = api.payload
        try:
            updated_place = facade.update_place(place_id, place_data)
            return updated_place.to_dict(), 200
        except ValueError as e:
            api.abort(400, str(e))
        except KeyError as e:
            api.abort(404, str(e))