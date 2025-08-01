from app import create_app
from flask_cors import CORS
from app.extensions import db

app = create_app('development')

# Configuration CORS plus permissive pour le développement
CORS(app, resources={
    r"/api/*": {
        "origins": [
            "http://localhost:8000",
            "http://127.0.0.1:8000", 
            "http://localhost:3000",
            "http://127.0.0.1:3000",
            "null",  # Pour les fichiers ouverts directement
            "*"  # Pour le développement uniquement
        ],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
        "supports_credentials": True
    }
})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)