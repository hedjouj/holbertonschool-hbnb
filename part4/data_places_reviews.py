#!/usr/bin/env python3
from part3.app.models import storage
from part3.app.models.place import Place
from part3.app.models.amenity import Amenity
from part3.app.models.review import Review
from part3.app.models.user import User
from part3.app.models.city import City
from datetime import datetime

USER_ID = "user-001"
CITY_ID = "city-001"

# Récupération du user et de la ville depuis la DB
user = storage.get(User, USER_ID)
city = storage.get(City, CITY_ID)

if not user or not city:
    print("❌ L'utilisateur ou la ville spécifiés n'existent pas. Crée-les d'abord.")
    exit(1)

# Création des amenities
wifi = Amenity(name="Wi-Fi")
pool = Amenity(name="Piscine")
kitchen = Amenity(name="Cuisine équipée")
jacuzzi = Amenity(name="Jacuzzi")
fireplace = Amenity(name="Cheminée")
netflix = Amenity(name="Netflix Premium")

# Création des lieux
place1 = Place(
    name="La Villa Twix",
    user_id=user.id,
    city_id=city.id,
    description="Charmante villa ensoleillée décorée dans des tons dorés et chocolat.",
    number_rooms=2,
    number_bathrooms=1,
    max_guest=4,
    price_by_night=120,
    latitude=43.6,
    longitude=3.88
)

place2 = Place(
    name="Twix’Loft Paris",
    user_id=user.id,
    city_id=city.id,
    description="Loft moderne avec vue Tour Eiffel. Chocolat offert à l’arrivée.",
    number_rooms=1,
    number_bathrooms=1,
    max_guest=2,
    price_by_night=190,
    latitude=48.85,
    longitude=2.35
)

place3 = Place(
    name="Cabane Twix’n’Chill",
    user_id=user.id,
    city_id=city.id,
    description="Cabane dans les bois, ambiance cocooning, Twix inclus.",
    number_rooms=1,
    number_bathrooms=1,
    max_guest=3,
    price_by_night=85,
    latitude=45.4,
    longitude=1.6
)

# Liaisons amenities ↔ places
place1.amenities.extend([wifi, pool, kitchen])
place2.amenities.extend([wifi, jacuzzi, netflix])
place3.amenities.extend([wifi, fireplace])

# Reviews
review1 = Review(
    user_id=user.id,
    place_id=place1.id,
    text="Super séjour ! La déco est top et les Twix gratuits c’est une masterclass 🍫",
    rating=5,
    created_at=datetime(2025, 7, 20, 10, 30)
)

review2 = Review(
    user_id=user.id,
    place_id=place2.id,
    text="Incroyable. Chocolat sur l’oreiller, vue magique. J’y retourne dès que possible !",
    rating=5,
    created_at=datetime(2025, 7, 25, 14, 0)
)

review3 = Review(
    user_id=user.id,
    place_id=place3.id,
    text="Un coin de paradis. On a mangé des Twix au coin du feu 🥹",
    rating=5,
    created_at=datetime(2025, 7, 28, 19, 0)
)

# Ajout au storage
for obj in [wifi, pool, kitchen, jacuzzi, fireplace, netflix,
            place1, place2, place3,
            review1, review2, review3]:
    storage.new(obj)

storage.save()
print("✅ Données insérées dans la base SQL via SQLAlchemy.")
