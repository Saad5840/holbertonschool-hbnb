from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(String, primary_key=True)
    text = Column(Text, nullable=False)
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    place_id = Column(String, ForeignKey('places.id'), nullable=False)

    user = relationship('User', back_populates='reviews')
    place = relationship('Place', back_populates='reviews')

