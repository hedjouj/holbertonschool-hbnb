from app import create_app
<<<<<<< HEAD
from flask_bcrypt import Bcrypt

app = create_app('development')
bcrypt = Bcrypt()
=======

app = create_app()
>>>>>>> 55418de (feat: added all folders/files from part2 to part3)

if __name__ == '__main__':
    app.run(debug=True)