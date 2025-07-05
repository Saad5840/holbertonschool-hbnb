from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Place(Base):
    __tablename__ = 'places'

    id = Column(String, primary_key=True)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    latitude = Column(Float)
    longitude = Column(Float)
    owner_id = Column(String, ForeignKey('users.id'), nullable=False)

    owner = relationship('User', back_populates='places')
    reviews = relationship('Review', back_populates='place', cascade='all, delete-orphan')
    amenities = relationship('Amenity', secondary='place_amenity', back_populates='places')

