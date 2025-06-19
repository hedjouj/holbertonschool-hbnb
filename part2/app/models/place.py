from app.models.base_model import BaseModel
from app.models.user import User


class Place(BaseModel):
    def __init__(self,
                 title: str, price: float, latitude: float, longitude: float,
                 owner: User, description=""):
        super().__init__()

        if not title or len(title) > 100:
            raise ValueError("Title is required and must be ≤ 100 characters.")
        if price <= 0:
            raise ValueError("Price must be positive.")
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("Latitude must be between -90 and 90.")
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("Longitude must be between -180 and 180.")
        if not isinstance(owner, User):
            raise TypeError("Owner must be a valid User instance.")

        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []
        self.amenities = []

        owner.places.append(self)
