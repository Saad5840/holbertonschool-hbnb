from .base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        if len(name) > 50:
            raise ValueError("Amenity name must be <= 50 characters")
        self.name = name

    def update(self, data):
        super().update(data)

    def delete(self):
        # logic for deletion
        pass

