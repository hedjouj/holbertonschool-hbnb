from app.persistence.repository import InMemoryRepository
from app.models.place import Place 
from app.models.amenity import Amenity 

class HBnBFacade:
    def __init__(self):
        self.place_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_place(self, place_data):
            place = Place(**place_data)
            self.place_repo.add(place)
            return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo

    def update_place(self, place_id, place_data):
        # Placeholder for logic to update a place
        pass

    
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo

    def update_amenity(self, amenity_id, amenity_data):
        # Placeholder for logic to update an amenity
        pass
        