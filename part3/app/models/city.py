#!/usr/bin/python3
""" City Module for HBNB project with SQLAlchemy """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from part3.app.models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """Representation of a City"""
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    # One-to-many: a city has many places
    places = relationship("Place", backref="city", cascade="all, delete")
