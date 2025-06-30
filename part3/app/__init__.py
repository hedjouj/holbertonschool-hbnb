from flask import Flask
from flask_restx import Api
<<<<<<< HEAD
from config import config
from flask_jwt_extended import JWTManager

=======
>>>>>>> 55418de (feat: added all folders/files from part2 to part3)
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.places import api as places_ns
from app.api.v1.users import api as users_ns
from app.api.v1.reviews import api as review_ns
<<<<<<< HEAD
from flask_bcrypt import Bcrypt
from app.extensions import bcrypt

jwt = JWTManager()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    jwt.init_app(app)
    
    bcrypt.init_app(app)

    
    api = Api(app, version='1.0', title='HBnB API', doc='/api/v1/',
              description='HBnB Application API')

=======


def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API', doc='/api/v1/',
              description='HBnB Application API')
    
>>>>>>> 55418de (feat: added all folders/files from part2 to part3)
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(review_ns, path='/api/v1/reviews')
<<<<<<< HEAD
    
=======
>>>>>>> 55418de (feat: added all folders/files from part2 to part3)
    return app