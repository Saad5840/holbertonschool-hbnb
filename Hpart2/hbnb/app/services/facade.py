from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
from app.models.review import Review

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Creating a user
    def create_user(self, user_data):
        user = User(user_data)
        self.user_repo.add(user)
        return user
    
    # Fetching user by ID
    def get_user(self, user_id):
        return self.user_repo.get(user_id)
    
    # Fetching all users
    def get_all_users(self):
        return self.user_repo.get_all()
    
    # Updating user's data by ID
    def update_user(self, user_id, user_data):
        self.user_repo.update(user_id,  user_data)
        return self.get_user(user_id)

    # Creating a place
    def create_place(self, user_id, place_data):
        user = self.get_user(user_id)
        place = Place(place_data, user)
        self.place_repo.add(place)
        return place

    # Fetching a place by ID
    def get_place(self, place_id):
        return self.place_repo.get(place_id)
    
    # Fetching all places
    def get_all_places(self):
        return self.place_repo.get_all()
    
    # Updating place's data by ID
    def update_place(self, place_id, place_data):
        self.place_repo.update(place_id,  place_data)
        return self.get_place(place_id)
    
    # Creating a review
    def create_review(self, user_id, place_id, review_data):
        user = self.user_repo.get(user_id)
        place = self.place_repo.get(place_id)
        review = Review(review_data, place, user)
        self.review_repo.add(review)
        return review
    
    # Fetching a review
    def get_review(self, review_id):
        return self.review_repo.get(review_id)
    
    # Fetching all reviews
    def get_all_reviews(self):
        return self.review_repo.get_all()