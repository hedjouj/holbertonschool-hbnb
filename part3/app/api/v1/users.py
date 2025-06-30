from flask_restx import Namespace, Resource, fields
from app.services.facade import facade

api = Namespace("users", description="User operations")

user_model = api.model("User", {
    "first_name": fields.String(required=True, max_length=50),
    "last_name": fields.String(required=True, max_length=50),
    "password": fields.String(required=True, max_length=50),
    "email": fields.String(required=True),
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
        return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name, "password": new_user.password, 'email': new_user.email}, 201

    @api.response(200, 'List of users retrieved successfully')
    def get(self):
        """Retrieve a list of all users"""
        users = facade.get_all_users()
        return [user.to_dict()
                for user in users], 200

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
    @api.response(400, 'Invalid input data')
<<<<<<< HEAD
    @api.response(400, 'Invalid input data')
    def put(self, user_id):
=======
    def put(self, user_id):
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> cf9a765 (fix pb on update a user fct put)
>>>>>>> 55418de (feat: added all folders/files from part2 to part3)
        """Update user details with ID"""
        user_data = api.payload
        try:
            updated_user = facade.update_user(user_id, user_data)
            return {
                'id': updated_user.id,
                'first_name': updated_user.first_name,
                'last_name': updated_user.last_name,
                'email': updated_user.email
            }, 200
        except ValueError as e:
<<<<<<< HEAD
            return {'error': str(e)}, 404
=======
<<<<<<< HEAD
<<<<<<< HEAD
            return {'error': str(e)}, 404
=======
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
        'email': updated_user.email
    }, 200
>>>>>>> 1186d9a (pb of label)
=======
            return {'error': str(e)}, 404
>>>>>>> cf9a765 (fix pb on update a user fct put)
=======
            return {'error': str(e)}, 404
>>>>>>> 4560d9a (fix bug facade)
>>>>>>> 55418de (feat: added all folders/files from part2 to part3)
