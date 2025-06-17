"""
A Amenity class that represent amenity model (entity)
"""

from base import BaseModel

class Amenity(BaseModel):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
    

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError('Name must be a string')
        if not value.strip():
            raise ValueError('Required')
        if len(value) > 50:
            raise ValueError('Name must not exceed 50 characters')

        self.name = value