from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime

class Amenity(Base):
    __tablename__ = 'amenities'

    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    name = Column(String(128), nullable=False)

    places = relationship('Place', secondary='place_amenity', back_populates='amenities')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

