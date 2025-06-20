from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
from app.models.amenity import Amenity
from app.models.review import Review


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()


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
    
    def get_all_users(self):
        return self.user_repo.get_all()
    
    def update_user(self, user_id, update_data):
        #user = self.user_repo.get(user_id)
        #if not user:
        #    return None
        #for key, value in update_data.items():
        #    setattr(user, key, value)
        #    self.user_repo.update(user)
        #    return user
        
        """Update an amenity."""
        user = self.get_user(user_id)
        if not user:
            raise ValueError("User not found")

        user.update(update_data)
        self.user_repo.save(user)
        return user
        
    # Review Facade
    def create_review(self, review_data, user_id, rating, place_id):
        user = self.get_user(user_id)
        if not user:
            raise ValueError("User not found." + str(user_id))

        place = self.get_place(place_id)
        if not place:
            raise ValueError("Place not found.")

        review = Review(
            text=review_data["text"],
            user_id=user.id,
            place_id=place.id,
            rating=rating
        )
        self.review_repo.add(review)
        return review

def get_review(self, review_id):
    return self.review_repo.get(review_id)


def get_all_reviews(self):
    return self.user_repo.get_all()


def get_reviews_by_place(self, place_id):
    return self.review_repo

def update_review(self, review_id, review_data):
    return self.review_repo.update(review_id, review_data) 

def delete_review(self, review_id):
    return self.review_repo.delete(review_id)