<<<<<<< HEAD
<<<<<<< HEAD
=======
from app import create_app
<<<<<<< HEAD

<<<<<<< HEAD
<<<<<<< HEAD
app = create_app('development')
=======
app = create_app('DevelopmentConfig')
>>>>>>> 52f027e (fix: update create_app function to use config_name and correct config reference)
=======
app = create_app('development')
>>>>>>> 19486a6 (fix: correct configuration name in create_app call)
=======
from flask_bcrypt import Bcrypt

app = create_app('development')
bcrypt = Bcrypt()

app = create_app()
app = create_app('development')
>>>>>>> 284bc61 (fix: resolve merge conflicts in __init__.py, config.py, and run.py)

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> a9e2282 (fix: update create_app function to accept config_name argument and add production config)
=======
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 55418de (feat: added all folders/files from part2 to part3)
