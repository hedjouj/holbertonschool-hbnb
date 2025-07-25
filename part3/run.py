from app import create_app
from flask_cors import CORS
from app.extensions import db


app = create_app('development')
CORS(app, resources={r"/api/*": {"origins": "*"}})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)