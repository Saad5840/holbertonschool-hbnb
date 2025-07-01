from flask import Flask
from flask_restx import Api
from app.extensions import bcrypt


from app.api.v1.users import user_ns
from app.api.v1.places import place_ns
from app.api.v1.amenities import amenity_ns
from app.api.v1.reviews import review_ns


# Initialize API object
api = Api(
    title="HBnB RESTful API",
    version="1.0",
    description="A REST API for managing users, places, amenities, and reviews in the HBnB application."
)

def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions
    bcrypt.init_app(app)
    api.init_app(app)

    # Register API namespaces
    api.add_namespace(user_ns, path="/api/v1/users")
    api.add_namespace(place_ns, path="/api/v1/places")
    api.add_namespace(amenity_ns, path="/api/v1/amenities")
    api.add_namespace(review_ns, path="/api/v1/reviews")

    return app
