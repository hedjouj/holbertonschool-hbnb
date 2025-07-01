import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = False
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bd0056d (fix: add JWT_SECRET_KEY to the Config class)
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt_secret')
    
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
    'production': ProductionConfig,
=======

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
<<<<<<< HEAD
    'default': DevelopmentConfig
>>>>>>> 55418de (feat: added all folders/files from part2 to part3)
=======
    'default': DevelopmentConfig,
    'production': ProductionConfig,
>>>>>>> a9e2282 (fix: update create_app function to accept config_name argument and add production config)
}