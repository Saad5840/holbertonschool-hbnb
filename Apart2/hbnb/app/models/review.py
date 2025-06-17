from .base_model import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")

        self.text = text
        self.rating = int(rating)
        self.place = place
        self.user = user  # reviewer

    def update(self, data):
        super().update(data)

    def delete(self):
        # logic for deletion
        pass

