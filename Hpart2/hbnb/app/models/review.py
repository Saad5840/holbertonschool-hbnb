"""
A Review class that represent review model (entity)
"""

from base import BaseModel
from place import Place
from user import User

class Review(BaseModel):
    def __init__(self, text: str, rating: int, place: Place, user: User):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
    

    @text.setter
    def text(self, value: str):
        if not isinstance(value, str):
            raise TypeError('Text must be a string')
        if not value.strip():
            raise ValueError('Required')

        self.text = value
    
    @rating.setter
    def rating(self, value: int):
        if not isinstance(value, int):
            raise TypeError('Rating must be an integer number')
        if not value.strip():
            raise ValueError('Required')
        if value < 1 and value > 5:
            raise ValueError('Rating must be between 1 and 5')

        self.rating = value
    
    @place.setter
    def place(self, value: Place):
        if not isinstance(value, Place):
            raise ValueError('Ensure place is a Place instance')
        if not Place.exists(value):
            raise ValueError('Place must be exsits')
        
        self.place = value

    @user.setter
    def user(self, value: User):
        if not isinstance(value, User):
            raise ValueError('Ensure user is a User instance')
        if not User.exists(value):
            raise ValueError('user must be exsits')
        
        self.user = value