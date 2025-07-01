<<<<<<< HEAD
=======
from app import create_app

<<<<<<< HEAD
app = create_app('development')
=======
app = create_app('DevelopmentConfig')
>>>>>>> 52f027e (fix: update create_app function to use config_name and correct config reference)

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> a9e2282 (fix: update create_app function to accept config_name argument and add production config)
