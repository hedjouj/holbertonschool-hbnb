from app.models.base_model import BaseModel
<<<<<<< HEAD
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
=======

>>>>>>> 55418de (feat: added all folders/files from part2 to part3)

class User(BaseModel):
    emails_seen = set()  # pour valider les mails

<<<<<<< HEAD
    def __init__(self, first_name: str, last_name: str, email: str, password: str,
=======
    def __init__(self, first_name: str, last_name: str, email: str,
>>>>>>> 55418de (feat: added all folders/files from part2 to part3)
                 is_admin=False):
        super().__init__()

        if not first_name or len(first_name) > 50:
            raise ValueError(
                "First name is required and must be ≤ 50 characters.")
        if not last_name or len(last_name) > 50:
            raise ValueError(
                "Last name is required and must be ≤ 50 characters.")
        if not email or len(email) > 100:
            raise ValueError("Email is required and must be ≤ 100 characters.")
        if email in User.emails_seen:
            raise ValueError("Email must be unique.")
        if '@' not in email:
            raise ValueError("Invalid email format.")

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.places = []
<<<<<<< HEAD
        self.password = self.hash_password(password) 

        User.emails_seen.add(email)

    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)

=======

        User.emails_seen.add(email)

>>>>>>> 55418de (feat: added all folders/files from part2 to part3)
    def __str__(self):
        """
        Used to return object as we want
        """
        return "{} {}".format(self.first_name, self.last_name)
    
    def to_dict(self):
        """Convert the Place object to a dictionary."""
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "is_admin": self.is_admin,
<<<<<<< HEAD
            "password": self.password, 
=======
>>>>>>> 55418de (feat: added all folders/files from part2 to part3)
        }