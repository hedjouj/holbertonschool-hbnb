<<<<<<< HEAD
=======
from app import create_app

app = create_app('development')

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> a9e2282 (fix: update create_app function to accept config_name argument and add production config)
