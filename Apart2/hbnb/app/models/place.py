# app/models/place.py

from app.models.base_model import BaseModel

class Place(BaseModel):
    """Represents a place listed by a user."""

    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        # Validate inputs
        if not title or len(title) > 100:
            raise ValueError("Title is required and must be <= 100 characters.")
        if price < 0:
            raise ValueError("Price must be positive.")
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("Latitude must be between -90.0 and 90.0.")
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("Longitude must be between -180.0 and 180.0.")
        if owner is None:
            raise ValueError("Owner (User) is required.")

        # Initialize attributes
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner  # Should be a User instance
        self.reviews = []   # Will hold Review instances
        self.amenities = [] # Will hold Amenity instances

    def add_review(self, review):
        """Link a review to this place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Link an amenity to this place."""
        self.amenities.append(amenity)
