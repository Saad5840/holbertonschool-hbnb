from app.models.base_model import BaseModel
from app.extensions import bcrypt

class User(BaseModel):
    """Represents a user in the system with secure password handling."""

    def __init__(self, name=None, email=None, password=None, is_admin=False, **kwargs):
        super().__init__(**kwargs)

        if not name or len(name) > 100:
            raise ValueError("Name is required and must be <= 100 characters.")
        if not email or "@" not in email:
            raise ValueError("A valid email is required.")
        if not password:
            raise ValueError("Password is required.")

        self.name = name
        self.email = email
        self.is_admin = is_admin
        self.hash_password(password)

    def hash_password(self, password):
        """Hashes the password and stores it internally."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies a given password against the stored hash."""
        return bcrypt.check_password_hash(self.password, password)

    def to_dict(self):
        """Override to_dict to exclude the password."""
        data = super().to_dict()
        if 'password' in data:
            del data['password']
        return data
