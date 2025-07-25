# app/models/review.py
from app.models.base_model import BaseModel
from app.models.user import User
from app.models.place import Place


class Review(BaseModel):
    def __init__(self, text: str, rating: int, place: Place, user: User):
        super().__init__()

        if not text:
            raise ValueError("Review text is required.")
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        if not isinstance(place, Place):
            raise TypeError("Place must be a valid Place instance.")
        if not isinstance(user, User):
            raise TypeError("User must be a valid User instance.")

        self.text = text
        self.user = user
        self.place = place
        self.rating = rating
        
        place.reviews.append(self)

    def to_dict(self):
        '''Convert the Review object to a dictionary'''
        return {
            'id': self.id,
            'text': self.text,
            'user_id': self.user.id,
            'place_id': self.place.id,
            'rating': self.rating
        }
