# app/models/user.py
from app.models.base_model import BaseModel


class User(BaseModel):
    emails_seen = set()  # pour valider les mails

    def __init__(self, first_name: str, last_name: str, email: str,
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

        User.emails_seen.add(email)

    def __str__(self):
        """
        Used to return object as we want
        """
        return "{} {}".format(self.first_name, self.last_name)
