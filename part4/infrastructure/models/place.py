from sqlalchemy import Column, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime

class Place(Base):
    __tablename__ = 'places'

    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    price = Column(Float, nullable=False, default=0.0)
    latitude = Column(Float)
    longitude = Column(Float)
    owner_id = Column(String, ForeignKey('users.id'), nullable=False)
    images = Column(String(2000))  # JSON string of image URLs

    owner = relationship('User', back_populates='places')
    reviews = relationship('Review', back_populates='place', cascade='all, delete-orphan')
    amenities = relationship('Amenity', secondary='place_amenity', back_populates='places')

    def to_dict(self):
        import json
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner_id,
            "images": json.loads(self.images) if self.images else [],
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

