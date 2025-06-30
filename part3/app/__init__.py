from flask import Flask
from flask_restx import Api
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from config import config
from flask_jwt_extended import JWTManager

=======
>>>>>>> 55418de (feat: added all folders/files from part2 to part3)
=======
from config import config
from flask_jwt_extended import JWTManager

>>>>>>> a9e2282 (fix: update create_app function to accept config_name argument and add production config)
=======
>>>>>>> 55418de (feat: added all folders/files from part2 to part3)
=======
from config import config
from flask_jwt_extended import JWTManager

>>>>>>> a9e2282 (fix: update create_app function to accept config_name argument and add production config)
=======

from config import config
from flask_jwt_extended import JWTManager
from config import config
from flask_jwt_extended import JWTManager

>>>>>>> 284bc61 (fix: resolve merge conflicts in __init__.py, config.py, and run.py)
=======
>>>>>>> 55418de (feat: added all folders/files from part2 to part3)
=======
from config import config

>>>>>>> a9e2282 (fix: update create_app function to accept config_name argument and add production config)
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.places import api as places_ns
from app.api.v1.users import api as users_ns
from app.api.v1.reviews import api as review_ns
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from flask_bcrypt import Bcrypt
from app.extensions import bcrypt

jwt = JWTManager()

<<<<<<< HEAD
def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
<<<<<<< HEAD
    jwt.init_app(app)
    
    bcrypt.init_app(app)

    
    api = Api(app, version='1.0', title='HBnB API', doc='/api/v1/',
              description='HBnB Application API')

=======

jwt = JWTManager()

def create_app(config_class=config.DevelopmentConfig):
    app = Flask(__name__)
<<<<<<< HEAD
    app.config.from_object(config[config_name])
=======
>>>>>>> a9e2282 (fix: update create_app function to accept config_name argument and add production config)
=======
    app.config.from_object(config_class)
>>>>>>> 55f278a (fix: modify the argument in the create app)
=======
jwt = JWTManager()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
<<<<<<< HEAD
>>>>>>> c5cac65 (fix: modify the argument in the create app)
    
    api = Api(app, version='1.0', title='HBnB API', doc='/api/v1/',
              description='HBnB Application API')
<<<<<<< HEAD
    
>>>>>>> 55418de (feat: added all folders/files from part2 to part3)
=======
=======
from flask_bcrypt import Bcrypt
>>>>>>> 3d4122e (task 01 : add password)

bcrypt = Bcrypt()

def create_app(config_name='default'):
    app = Flask(__name__)
<<<<<<< HEAD
=======
    app.config.from_object(config[config_name])
>>>>>>> a9e2282 (fix: update create_app function to accept config_name argument and add production config)
    
    api = Api(app, version='1.0', title='HBnB API', doc='/api/v1/',
              description='HBnB Application API')
    
>>>>>>> 55418de (feat: added all folders/files from part2 to part3)
=======
    jwt.init_app(app)
=======
    jwt.init_app(app)

    
    api = Api(app, version='1.0', title='HBnB API', doc='/api/v1/',
              description='HBnB Application API')
>>>>>>> d120c30 (fix: move jwt.init_app call to the correct position in create_app function)

>>>>>>> 9594fa4 (fix: add auth namespace to the API in create_app function)
=======
=======
from flask_bcrypt import Bcrypt
>>>>>>> 3d4122e (task 01 : add password)

bcrypt = Bcrypt()

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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    
=======
>>>>>>> 55418de (feat: added all folders/files from part2 to part3)
=======
>>>>>>> 55418de (feat: added all folders/files from part2 to part3)
=======
    bcrypt.init_app(app)
    
>>>>>>> 3d4122e (task 01 : add password)
=======
>>>>>>> 55418de (feat: added all folders/files from part2 to part3)
=======
    bcrypt.init_app(app)
    
>>>>>>> 3d4122e (task 01 : add password)
    return app