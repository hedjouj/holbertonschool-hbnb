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
        self.rating = rating
        self.place = place
        self.user = user

        place.reviews.append(self)
