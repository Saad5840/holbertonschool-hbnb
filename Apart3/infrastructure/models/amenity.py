from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .base import Base

class Amenity(Base):
    __tablename__ = 'amenities'

    id = Column(String, primary_key=True)
    name = Column(String(128), nullable=False)

    places = relationship('Place', secondary='place_amenity', back_populates='amenities')

