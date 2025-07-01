from app.models.place import Place
from app.models.user import User
from app.models.amenity import Amenity
from app.models.review import Review
from app.persistence.repository import in_memory_repo


class HBnBFacade:

    # -------------------- USERS --------------------

    def create_user(self, user_data):
        required = ['name', 'email', 'password']
        for field in required:
            if field not in user_data:
                raise ValueError(f"Missing field: {field}")

        user = User(**user_data)
        in_memory_repo.add('users', user)
        return user.to_dict()

    def get_user(self, user_id):
        user = in_memory_repo.get_by_id('users', user_id)
        if not user:
            raise ValueError("User not found")
        return user.to_dict()

    def get_all_users(self):
        users = in_memory_repo.get_all('users')
        return [u.to_dict() for u in users]

    # -------------------- AMENITIES --------------------

    def create_amenity(self, amenity_data):
        if 'name' not in amenity_data:
            raise ValueError("Missing amenity name")

        amenity = Amenity(**amenity_data)
        in_memory_repo.add('amenities', amenity)
        return amenity.to_dict()

    def get_amenity(self, amenity_id):
        amenity = in_memory_repo.get_by_id('amenities', amenity_id)
        if not amenity:
            raise ValueError("Amenity not found")
        return amenity.to_dict()

    def get_all_amenities(self):
        amenities = in_memory_repo.get_all('amenities')
        return [a.to_dict() for a in amenities]

    # -------------------- PLACES --------------------

    def create_place(self, place_data):
        required = ['title', 'price', 'latitude', 'longitude', 'owner_id']
        for field in required:
            if field not in place_data:
                raise ValueError(f"Missing field: {field}")

        if place_data['price'] < 0:
            raise ValueError("Price must be non-negative")
        if not (-90 <= place_data['latitude'] <= 90):
            raise ValueError("Latitude must be between -90 and 90")
        if not (-180 <= place_data['longitude'] <= 180):
            raise ValueError("Longitude must be between -180 and 180")

        owner = in_memory_repo.get_by_id('users', place_data['owner_id'])
        if not owner:
            raise ValueError("Owner not found")

        amenities = []
        if 'amenity_ids' in place_data:
            for amenity_id in place_data['amenity_ids']:
                amenity = in_memory_repo.get_by_id('amenities', amenity_id)
                if amenity:
                    amenities.append(amenity.id)

        place = Place(**place_data)
        place.amenity_ids = amenities
        in_memory_repo.add('places', place)
        return self._enrich_place(place)

    def get_place(self, place_id):
        place = in_memory_repo.get_by_id('places', place_id)
        if not place:
            raise ValueError("Place not found")
        return self._enrich_place(place)

    def get_all_places(self):
        places = in_memory_repo.get_all('places')
        return [self._enrich_place(p) for p in places]

    def update_place(self, place_id, data):
        place = in_memory_repo.get_by_id('places', place_id)
        if not place:
            raise ValueError("Place not found")

        if 'title' in data:
            place.title = data['title']
        if 'description' in data:
            place.description = data['description']
        if 'price' in data:
            if data['price'] < 0:
                raise ValueError("Price must be non-negative")
            place.price = data['price']
        if 'latitude' in data:
            if not (-90 <= data['latitude'] <= 90):
                raise ValueError("Invalid latitude")
            place.latitude = data['latitude']
        if 'longitude' in data:
            if not (-180 <= data['longitude'] <= 180):
                raise ValueError("Invalid longitude")
            place.longitude = data['longitude']
        if 'amenity_ids' in data:
            valid_ids = []
            for aid in data['amenity_ids']:
                if in_memory_repo.get_by_id('amenities', aid):
                    valid_ids.append(aid)
            place.amenity_ids = valid_ids

        return {"message": "Place updated successfully"}

    def delete_place(self, place_id):
        place = in_memory_repo.get_by_id('places', place_id)
        if not place:
            raise ValueError("Place not found")
        in_memory_repo.delete('places', place_id)
        return {"message": "Place deleted successfully"}

    def _enrich_place(self, place):
        place_dict = place.to_dict()

        owner = in_memory_repo.get_by_id('users', place.owner_id)
        place_dict['owner'] = owner.to_dict() if owner else None

        amenities = []
        for aid in getattr(place, 'amenity_ids', []):
            amenity = in_memory_repo.get_by_id('amenities', aid)
            if amenity:
                amenities.append(amenity.to_dict())
        place_dict['amenities'] = amenities

        reviews = [
            r.to_dict() for r in in_memory_repo.get_all('reviews')
            if r.place_id == place.id
        ]
        place_dict['reviews'] = reviews

        return place_dict

    # -------------------- REVIEWS --------------------

    def create_review(self, review_data):
        required = ['text', 'rating', 'user_id', 'place_id']
        for field in required:
            if field not in review_data:
                raise ValueError(f"Missing field: {field}")

        if not (1 <= review_data['rating'] <= 5):
            raise ValueError("Rating must be between 1 and 5")

        if not in_memory_repo.get_by_id('users', review_data['user_id']):
            raise ValueError("User not found")

        if not in_memory_repo.get_by_id('places', review_data['place_id']):
            raise ValueError("Place not found")

        review = Review(**review_data)
        in_memory_repo.add('reviews', review)
        return review.to_dict()

    def get_review(self, review_id):
        review = in_memory_repo.get_by_id('reviews', review_id)
        if not review:
            raise ValueError("Review not found")
        return review.to_dict()

    def get_all_reviews(self):
        reviews = in_memory_repo.get_all('reviews')
        return [r.to_dict() for r in reviews]

    def get_reviews_by_place(self, place_id):
        if not in_memory_repo.get_by_id('places', place_id):
            raise ValueError("Place not found")
        reviews = in_memory_repo.get_all('reviews')
        return [r.to_dict() for r in reviews if r.place_id == place_id]

    def update_review(self, review_id, data):
        review = in_memory_repo.get_by_id('reviews', review_id)
        if not review:
            raise ValueError("Review not found")

        if 'text' in data:
            review.text = data['text']
        if 'rating' in data:
            if not (1 <= data['rating'] <= 5):
                raise ValueError("Rating must be between 1 and 5")
            review.rating = data['rating']

        return {"message": "Review updated successfully"}

    def delete_review(self, review_id):
        review = in_memory_repo.get_by_id('reviews', review_id)
        if not review:
            raise ValueError("Review not found")
        in_memory_repo.delete('reviews', review_id)
        return {"message": "Review deleted successfully"}
