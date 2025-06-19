from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace("users", description="User operations")
facade = HBnBFacade()

user_model = api.model("User", {
    "id": fields.String(readonly=True),
    "first_name": fields.String(required=True, max_length=50),
    "last_name": fields.String(required=True, max_length=50),
    "email": fields.String(required=True),
    "is_admin": fields.Boolean,
    "created_at": fields.DateTime,
    "updated_at": fields.DateTime,
})
@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = api.payload

        # Simulate email uniqueness check (to be replaced by real validation with persistence)
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        new_user = facade.create_user(user_data)
        return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name, 'email': new_user.email, 'created_at': new_user.created_at, 'updated_at': new_user.updated_at}, 201


@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200
    
@api.expect(user_model, validate=True)
@api.response(200, 'User updated successfully')
@api.response(404, 'User not found')
class UserResource(Resource):
    def put(self, user_id):
        """Update user information"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
    
        update_data = api.payload
        updated_user = facade.update_user(user_id, update_data)
    
        return {
        'id': updated_user.id,
        'first_name': updated_user.first_name,
        'last_name': updated_user.last_name,
        'email': updated_user.email,
        'updated_at': updated_user.updated_at
    }, 200