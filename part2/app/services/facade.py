from app.persistence.repository import InMemoryRepository
from app.models.place import Place 
from app.models.amenity import Amenity 
from app.models.user import User 


class HBnBFacade:
    def __init__(self):
        self.place_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self.user_repo = InMemoryRepository()

    def create_place(self, place_data):
        """Create a new place."""
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        """Update an amenity."""
        place = self.get_place(place_id)
        if not place:
            raise ValueError("Place not found5")

        place.update(place_data)
        self.place_repo.save(place)
        return place

    
    # Amenity Facade
    def create_amenity(self, amenity_data):
        """Create a new amenity."""
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        """Retrieve an amenity by ID."""
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        """Retrieve all amenities."""
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        """Update an amenity."""
        amenity = self.get_amenity(amenity_id)
        if not amenity:
            raise ValueError("Amenity not found")

        amenity.update(amenity_data)
        self.amenity_repo.save(amenity)
        return amenity

    def get_amenity_by_name(self, name):
        """Retrieve an amenity by name."""
        return self.amenity_repo.get_by_attribute('name', name)
    
    # Placeholder method for creating a user
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)