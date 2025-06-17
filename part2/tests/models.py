# test_models.py

from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
from datetime import datetime

# === Test User ===
print("Testing User...")

user = User("Alice", "Wonder", "alice@example.com")
assert user.first_name == "Alice"
assert user.last_name == "Wonder"
assert user.email == "alice@example.com"
assert user.is_admin == False
assert isinstance(user.id, str)
assert isinstance(user.created_at, datetime)
assert isinstance(user.updated_at, datetime)

try:
    User("Bob", "Builder", "alice@example.com")  # Duplicate email
    assert False, "Duplicate email should raise an error"
except ValueError:
    pass

print("User OK ✅")

# === Test Place ===
print("Testing Place...")

place = Place(
    title="Cozy Cabin",
    price=150.0,
    latitude=45.0,
    longitude=10.0,
    owner=user,
    description="A quiet getaway"
)

assert place.title == "Cozy Cabin"
assert place.price == 150.0
assert place.owner == user
assert place in user.places
assert isinstance(place.id, str)

print("Place OK ✅")

# === Test Amenity ===
print("Testing Amenity...")

wifi = Amenity("Wi-Fi")
pool = Amenity("Pool")
place.add_amenity(wifi)
place.add_amenity(pool)

assert len(place.amenities) == 2
assert place.amenities[0].name == "Wi-Fi"

print("Amenity OK ✅")

# === Test Review ===
print("Testing Review...")

review = Review("Great stay!", 5, place=place, user=user)

assert review.text == "Great stay!"
assert review.rating == 5
assert review.place == place
assert review.user == user
assert review in place.reviews

print("Review OK ✅")

# === Final Output ===
print("\n🎉 Tous les tests sont passés avec succès !")
