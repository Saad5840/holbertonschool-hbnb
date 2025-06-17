"""
A User class that represent user model (entity)
"""

from base import BaseModel

class User(BaseModel):

    _existing_users = set()

    def __init__(self, first_name: str, last_name: str, email: str, is_admin: bool = False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.places = []
        self.reviews = []

        User._existing_users.add(self)
    
    def add_place(self, place):
        """Add new place to the given user"""
        self.places.append(place)
    
    def add_review(self, review):
        """Add new review by the given user"""
        self.reviews.append(review)
    

    @classmethod
    def exists(cls, user: 'User') -> bool:
        """Check if a user exists."""
        return user in cls._existing_users