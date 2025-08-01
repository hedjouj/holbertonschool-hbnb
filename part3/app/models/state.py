from models.base_model import Base

from sqlalchemy import Column, Integer, String

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
