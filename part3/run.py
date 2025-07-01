from app import create_app
from flask_bcrypt import Bcrypt

app = create_app('development')
bcrypt = Bcrypt()

if __name__ == '__main__':
    app.run(debug=True)