# app/models/review.py

from app.models.base_model import BaseModel

class Review(BaseModel):
    """Represents a user review for a place."""

    def __init__(self, text, rating, place, user):
        super().__init__()
        # Validate inputs
        if not text:
            raise ValueError("Review text is required.")
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        if place is None or user is None:
            raise ValueError("Place and User are required.")

        # Initialize attributes
        self.text = text
        self.rating = rating
        self.place = place  # Should be a Place instance
        self.user = user    # Should be a User instance
