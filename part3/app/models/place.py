from app.models.base_model import BaseModel
from app import db

class Place(BaseModel):

    __tablename__ = 'Place'

    id = db.Column(db.Integer(50), primary_key=True )
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float(128), nullable=False)
    latitude = db.Column(db.Float, default=False)
    longitude = db.Column(db.Float, default=False)

    def __init__(self, title: str, price: float, latitude: float, longitude: float, owner_id: str, amenities=[], reviews=[], description=""):
        super().__init__()

        if not title or len(title) > 100:
            raise ValueError("Title is required and must be ≤ 100 characters.")
        if price <= 0:
            raise ValueError("Price must be positive.")
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("Latitude must be between -90 and 90.")
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("Longitude must be between -180 and 180.")
        #if not isinstance(owner, User):
        #    raise TypeError("Owner must be a valid User instance.")

        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.reviews = reviews
        self.amenities = amenities

        #owner.places.append(self)

    def to_dict(self):
        """Convert the Place object to a dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner_id,
            "reviews": [review.to_dict() for review in self.reviews],
            "amenities": self.amenities
        }

    def to_dict(self):
        """Convert the Place object to a dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner_id,
            "reviews": [review.to_dict() for review in self.reviews],
            "amenities": self.amenities
        }
