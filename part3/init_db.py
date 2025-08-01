from app import db
from sqlalchemy import create_engine
from app.models.base_model import Base
from app.models.state import State
from app.models.city import City

db.create_all()
"""
Script to initialize the database with sample data
"""
from app import create_app
from app.extensions import db
from app.models.user import User
from app.models.place import Place
from app.models.amenity import Amenity
from app.models.review import Review

def init_database():
    app = create_app('development')
    
    with app.app_context():
        # Create all tables
        db.create_all()
        
        # Check if admin user already exists
        admin_user = User.query.filter_by(email='admin@hbnb.com').first()
        if not admin_user:
            # Create admin user
            admin_user = User(
                first_name='Admin',
                last_name='User',
                email='admin@hbnb.com',
                password='admin123',
                is_admin=True
            )
            db.session.add(admin_user)
            
            # Create regular user
            regular_user = User(
                first_name='John',
                last_name='Doe',
                email='john@example.com',
                password='password123'
            )
            db.session.add(regular_user)
            
            # Create some amenities
            wifi = Amenity(name='WiFi')
            pool = Amenity(name='Swimming Pool')
            parking = Amenity(name='Parking')
            
            db.session.add_all([wifi, pool, parking])
            
            # Commit users and amenities first
            db.session.commit()
            
            # Create a sample place
            sample_place = Place(
                title='Cozy Apartment',
                description='A beautiful place to stay',
                price=120.0,
                latitude=48.8566,
                longitude=2.3522,
                owner_id=admin_user.id
            )
            db.session.add(sample_place)
            db.session.commit()
            
            # Create a sample review
            sample_review = Review(
                text='Great place to stay!',
                rating=5,
                user=regular_user,
                place=sample_place
            )
            db.session.add(sample_review)
            db.session.commit()
            
            print("Database initialized with sample data!")
            print(f"Admin user created: admin@hbnb.com / admin123")
            print(f"Regular user created: john@example.com / password123")
        else:
            print("Database already initialized!")

if __name__ == '__main__':
    init_database()