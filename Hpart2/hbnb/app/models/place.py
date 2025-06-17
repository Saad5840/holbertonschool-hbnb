"""
A Place class that represent place model (entity)
"""

from base import BaseModel

class Place(BaseModel):

    _existing_places = set()

    def __init__(self, title: str, description: str, price: float, latitude: float, longitude: float, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []
        self.amenities = []

        Place._existing_places.add(self)

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
    
    @classmethod
    def exists(cls, place: 'Place') -> bool:
        """Check if a place exists."""
        return place in cls._existing_places