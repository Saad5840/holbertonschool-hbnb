from flask import Flask
from flask_restx import Api

from api.user_routes import user_ns
from api.place_routes import place_ns
from api.amenity_routes import amenity_ns
from api.review_routes import review_ns

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
