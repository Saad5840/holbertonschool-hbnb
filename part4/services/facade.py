import uuid
from app.extensions import db
from infrastructure.models.user import User
from infrastructure.models.place import Place
from infrastructure.models.review import Review
from infrastructure.models.amenity import Amenity
from infrastructure.repositories.sqlalchemy_repository import SQLAlchemyRepository

user_repo = SQLAlchemyRepository(User)

def create_user(data):
    user = User(
        id=data.get('id') or str(uuid.uuid4()),
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        email=data.get("email"),
        is_admin=data.get("is_admin", False)
    )
    user.set_password(data.get("password"))
    user_repo.add(user)
    return user

def get_user_by_email(email):
    return db.session.query(User).filter_by(email=email).first()

def create_place(data):
    import json
    place = Place(
        id=data.get('id') or str(uuid.uuid4()),
        name=data.get("name"),
        description=data.get("description"),
        price=data.get("price", 0.0),
        owner_id=data.get("owner_id"),
        images=json.dumps(data.get("images", []))
    )
    db.session.add(place)
    db.session.commit()
    return place

def create_review(data):
    review = Review(
        id=data.get('id') or str(uuid.uuid4()),
        text=data.get("text"),
        rating=data.get("rating", "5"),
        user_id=data.get("user_id"),
        place_id=data.get("place_id")
    )
    db.session.add(review)
    db.session.commit()
    return review

def create_amenity(data):
    amenity = Amenity(
        id=data.get('id') or str(uuid.uuid4()),
        name=data.get("name")
    )
    db.session.add(amenity)
    db.session.commit()
    return amenity

def get_all_places():
    """Get all places with their amenities and owner information."""
    return db.session.query(Place).all()

def get_place_by_id(place_id):
    """Get a specific place by ID with all related data."""
    return db.session.query(Place).filter_by(id=place_id).first()

def get_all_amenities():
    """Get all amenities."""
    return db.session.query(Amenity).all()

def get_all_reviews():
    """Get all reviews with user and place information."""
    return db.session.query(Review).all()

def get_reviews_by_place(place_id):
    """Get all reviews for a specific place."""
    return db.session.query(Review).filter_by(place_id=place_id).all()

