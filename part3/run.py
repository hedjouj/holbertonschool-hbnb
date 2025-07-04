from app import create_app, db
from app.models.base_model import BaseModel

app = create_app('development')


class Review(BaseModel):
    __tablename__ = 'review'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    place_id = db.Column(db.Integer, db.ForeignKey('places.id'), nullable=False)

if __name__ == '__main__':
    app.run(debug=True)