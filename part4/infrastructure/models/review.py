from sqlalchemy import Column, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    text = Column(Text, nullable=False)
    rating = Column(String(1), nullable=False, default='5')  # 1-5 rating
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    place_id = Column(String, ForeignKey('places.id'), nullable=False)

    user = relationship('User', back_populates='reviews')
    place = relationship('Place', back_populates='reviews')

    def to_dict(self):
        return {
            "id": self.id,
            "text": self.text,
            "rating": self.rating,
            "user_id": self.user_id,
            "place_id": self.place_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

