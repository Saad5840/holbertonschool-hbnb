from app.models.base_model import BaseModel

class User(BaseModel):
    """Represents a user in the system."""

    def __init__(self, name=None, email=None, is_admin=False, **kwargs):
        super().__init__(**kwargs)

        if not name or len(name) > 100:
            raise ValueError("Name is required and must be <= 100 characters.")
        if not email or "@" not in email:
            raise ValueError("A valid email is required.")

        self.name = name
        self.email = email
        self.is_admin = is_admin

        # Optionally, split name into first_name and last_name internally
        name_parts = name.split()
        self.first_name = name_parts[0] if name_parts else ""
        self.last_name = " ".join(name_parts[1:]) if len(name_parts) > 1 else ""
