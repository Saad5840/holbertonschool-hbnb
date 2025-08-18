# Import all models to ensure they are registered with SQLAlchemy
from .base import Base, place_amenity
from .user import User
from .place import Place
from .review import Review
from .amenity import Amenity

# This ensures all models are loaded and relationships are properly established
__all__ = ['Base', 'User', 'Place', 'Review', 'Amenity', 'place_amenity']
