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
<<<<<<< HEAD
<<<<<<< HEAD
        user.hash_password(user_data['password'])
=======
>>>>>>> 55418de (feat: added all folders/files from part2 to part3)
=======
>>>>>>> 55418de (feat: added all folders/files from part2 to part3)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
<<<<<<< HEAD
<<<<<<< HEAD
        return self.user_repo.get_by_attribute('id', user_id)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        return self.user_repo.get_by_attribute('id', user_id)
=======
        for i in self.user_repo.get_all():
            print ( "coucou " + str(i) )
=======
>>>>>>> 6c7fa63 (try to fix bug user not found)
        return self.user_repo.get(user_id)
>>>>>>> 154c17d (try review bug bug with get user function)
=======
        return self.user_repo.get_by_attribute('id', user_id)
>>>>>>> 4560d9a (fix bug facade)
>>>>>>> 55418de (feat: added all folders/files from part2 to part3)
=======
        return self.user_repo.get_by_attribute('id', user_id)
>>>>>>> 55418de (feat: added all folders/files from part2 to part3)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)
    
    def get_all_users(self):
        return self.user_repo.get_all()
    
    # Review Facade
    def create_review(self, review_data):
        id_place = review_data["place_id"]

        place = self.place_repo.get(id_place)
        if not place:
            raise ValueError("Place not found.")

        user1 = self.user_repo.get(review_data["user_id"])
        if not user1:
            raise ValueError("User not found.")

        review = Review(
            text=review_data["text"],
            user=user1,
            place=place,
            rating=review_data["rating"]
        )
        self.review_repo.add(review)
        return review

    def update_user(self, user_id, update_data):
        """Update an user."""
        user = self.get_user(user_id)
        if not user:
            raise ValueError("User not found")

        user.update(update_data)
        self.user_repo.save(user)
        return user
        


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
        return [review for review in
                self.review_repo.get_all() if review.place_id == place_id]

    def update_review(self, review_id, review_update):
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError("Review not found")
        for key, value in review_update.items():
            if hasattr(review, key):
                setattr(review, key, value)
        self.review_repo.update(review_id, review.__dict__)
        return review

    def delete_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError("Review not found")
        self.review_repo.delete(review_id)
        return {'message': 'Review deleted succesessfully'}
<<<<<<< HEAD
<<<<<<< HEAD


# Instance globale
facade = HBnBFacade()
=======
<<<<<<< HEAD
=======


# Instance globale
facade = HBnBFacade()
>>>>>>> 4560d9a (fix bug facade)
>>>>>>> 55418de (feat: added all folders/files from part2 to part3)
=======


# Instance globale
facade = HBnBFacade()
>>>>>>> 55418de (feat: added all folders/files from part2 to part3)
