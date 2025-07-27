from app import create_app
from app import db


app = create_app('development')

if __name__ == '__main__':
    app.run(debug=True)
    db.create_all()