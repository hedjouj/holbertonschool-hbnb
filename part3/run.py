from app import create_app
<<<<<<< HEAD
from flask_bcrypt import Bcrypt

app = create_app('development')
bcrypt = Bcrypt()
=======

<<<<<<< HEAD
app = create_app()
>>>>>>> 55418de (feat: added all folders/files from part2 to part3)
=======
app = create_app('development')
>>>>>>> a9e2282 (fix: update create_app function to accept config_name argument and add production config)

if __name__ == '__main__':
    app.run(debug=True)