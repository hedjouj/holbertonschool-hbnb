from flask import request
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token
from app.services.facade import facade
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt


api = Namespace('auth', description='Authentication operations')
api = Namespace('admin', description='Admin operations')

# Model for input validation
login_model = api.model('Login', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

@api.route('/login')
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        """Authenticate user and return a JWT token"""
        credentials = api.payload  # Get the email and password from the request payload
        
        print(f"=== DEBUG LOGIN ===")
        print(f"Email reçu: {credentials['email']}")
        print(f"Password reçu: {credentials['password']}")
        
        # Debug: Lister tous les utilisateurs
        all_users = facade.get_all_users()
        print(f"Nombre d'utilisateurs dans la DB: {len(all_users)}")
        for u in all_users:
            print(f"  - ID: {u.id}, Email: {u.email}, Admin: {u.is_admin}")
        
        # Step 1: Retrieve the user based on the provided email
        user = facade.get_user_by_email(credentials['email'])
        print(f"Utilisateur trouvé: {user}")
        
        # Step 2: Check if the user exists and the password is correct
        if not user:
            print("❌ Utilisateur non trouvé")
            return {'error': 'Invalid credentials - User not found'}, 401
            
        print(f"✅ Utilisateur trouvé - ID: {user.id}")
        
        # Vérifier le mot de passe
        password_valid = user.verify_password(credentials['password'])
        print(f"Password valide: {password_valid}")
        
        if not password_valid:
            print("❌ Mot de passe incorrect")
            return {'error': 'Invalid credentials - Wrong password'}, 401

        # Step 3: Create a JWT token with the user's id and is_admin flag
        access_token = create_access_token(identity={'id': str(user.id), 'is_admin': user.is_admin})
        
        print(f"✅ Token créé avec succès pour l'utilisateur {user.id}")
        
        # Step 4: Return the JWT token to the client
        return {'access_token': access_token}, 200
    
@api.route('/protected')
class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        """A protected endpoint that requires a valid JWT token"""
        current_user = get_jwt_identity()  # Retrieve the user's identity from the token
        return {'message': f'Hello, user {current_user["id"]}'}, 200
    
@api.route('/users/<user_id>')
class AdminUserResource(Resource):
    @jwt_required()
    def put(self, user_id):
        current_user = get_jwt_identity()
        
        # If 'is_admin' is part of the identity payload
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        data = request.json
        email = data.get('email')

        if email:
            # Check if email is already in use
            existing_user = facade.get_user_by_email(email)
            if existing_user and existing_user.id != user_id:
                return {'error': 'Email is already in use'}, 400

        # Logic to update user details, including email and password
        pass