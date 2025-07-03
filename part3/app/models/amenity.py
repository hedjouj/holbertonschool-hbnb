# app/models/amenity.py
''' Amenity Class represents an amenity, inheriting from BaseModel'''

from app.models.base_model import BaseModel
from app import db


class Amenity(BaseModel):


    __tablename__='Amenity'
    id = db.Column(db.Integer(50), primary_key=True )
    title = db.Column(db.String(50), nullable=False)
    
    '''Represents an amenity with attributes and restrictions'''
    def __init__(self, name):
        '''Initialize a new Amenity instance with restrictions'''
        super().__init__()
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Amenity name must be a string of characters.")
        if not value or len(value) > 50:
            raise ValueError(
                "Amenity name must be a string of 1 to 50 characters."
            )
        self._name = value

    def to_dict(self):
        """Convert the Amenity object to a dictionary."""
        return {
            "id": self.id,
            "name": self.name
        }
