# app/models/review.py
from app.models.base_model import BaseModel
from app import db

class Review(BaseModel):
    __tablename__ = 'review'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=False)

    user = db.relationship('User', backref='reviews')
    place = db.relationship('Place', backref='reviews')

    def __init__(self, text, rating, user, place):
        super().__init__()
        if not text:
            raise ValueError("Review text is required.")
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        self.text = text
        self.rating = rating
        self.user = user
        self.place = place

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'user_id': self.user_id,
            'place_id': self.place_id,
            'rating': self.rating
        }
