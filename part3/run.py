from app import create_app
from flask_cors import CORS

app = create_app('development')
CORS(app)

@app.route('/api/v1/places', methods=['GET'])
def get_places():
    places = [
        {"id": 1, "name": "Place 1", "price": 100},
        {"id": 2, "name": "Place 2", "price": 150}
    ]
    return {"places": places}


if __name__ == '__main__':
    app.run(debug=True)