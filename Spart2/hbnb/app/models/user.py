# app/models/user.py

from app.models.base_model import BaseModel

class User(BaseModel):
    """Represents a user in the system."""

    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        # Validate inputs
        if not first_name or len(first_name) > 50:
            raise ValueError("First name is required and must be <= 50 characters.")
        if not last_name or len(last_name) > 50:
            raise ValueError("Last name is required and must be <= 50 characters.")
        if not email or "@" not in email:
            raise ValueError("A valid email is required.")

        # Initialize attributes
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
