from flask import Flask
from flask_restx import Api

from app.api.v1.users import user_ns
from app.api.v1.places import place_ns
from app.api.v1.amenities import amenity_ns
from app.api.v1.reviews import review_ns

api = Api(
    title="HBnB RESTful API",
    version="1.0",
    description="A REST API for managing users, places, amenities, and reviews in the HBnB application."
)


def create_app():
    app = Flask(__name__)

    # Register namespaces
    api.init_app(app)
    api.add_namespace(user_ns, path="/users")
    api.add_namespace(place_ns, path="/places")
    api.add_namespace(amenity_ns, path="/amenities")
    api.add_namespace(review_ns, path="/reviews")

    return app
