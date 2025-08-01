from app.models.user import User
from app.models.place import Place
from app.models.amenity import Amenity
from app.models.review import Review
from app.persistence.repository import UserRepository, PlaceRepository, ReviewRepository, AmenityRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = UserRepository()
        self.place_repo = PlaceRepository()
        self.review_repo = ReviewRepository()
        self.amenity_repo = AmenityRepository()

    # Place methods
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
        """Update a place."""
        place = self.get_place(place_id)
        if not place:
            raise ValueError("Place not found")
        
        return self.place_repo.update(place_id, place_data)

    # Amenity methods
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
        
        return self.amenity_repo.update(amenity_id, amenity_data)

    def get_amenity_by_name(self, name):
        """Retrieve an amenity by name."""
        return self.amenity_repo.get_by_attribute('name', name)
    
    # User methods
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
        """Update a user."""
        user = self.get_user(user_id)
        if not user:
            raise ValueError("User not found")
        
        return self.user_repo.update(user_id, update_data)
    
    # Review methods
    def create_review(self, review_data):
        place_id = review_data["place_id"]
        user_id = review_data["user_id"]

        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError("Place not found.")

        user = self.user_repo.get(user_id)
        if not user:
            raise ValueError("User not found.")

        review = Review(
            text=review_data["text"],
            user=user,
            place=place,
            rating=review_data["rating"]
        )
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError("Review not found")
        return review

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError("Place not found")
        return [review for review in self.review_repo.get_all() 
                if review.place_id == place_id]

    def update_review(self, review_id, review_update):
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError("Review not found")
        
        return self.review_repo.update(review_id, review_update)

    def delete_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError("Review not found")
        
        self.review_repo.delete(review_id)
        return {'message': 'Review deleted successfully'}

# Instance globale
facade = HBnBFacade()