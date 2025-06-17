import re
from .base_model import BaseModel

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        if len(first_name) > 50 or len(last_name) > 50:
            raise ValueError("First and last names must be <= 50 characters")

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format")

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = None  # To be set separately
        self.is_admin = is_admin

    def register(self, password):
        self.password = password

    def login(self, email, password):
        return self.email == email and self.password == password

    def update_profile(self, data):
        self.update(data)

    def delete(self):
        # logic for deletion (in-memory or database)
        pass

