# app/models/amenity.py

from app.models.base_model import BaseModel

class Amenity(BaseModel):
    """Represents an amenity that can be associated with a place."""

    def __init__(self, name):
        super().__init__()
        # Validate input
        if not name or len(name) > 50:
            raise ValueError("Name is required and must be <= 50 characters.")

        # Initialize attribute
        self.name = name
