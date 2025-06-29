from flask import Flask
from flask_restx import Api
from config import DevelopmentConfig  # default fallback

from app.api.v1.users import api as user_ns
from app.api.v1.places import api as place_ns
from app.api.v1.amenities import api as amenity_ns
from app.api.v1.reviews import api as review_ns

api = Api(
    title="HBnB RESTful API",
    version="1.0",
    description="A REST API for HBnB"
)

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    api.init_app(app)
    api.add_namespace(user_ns, path="/api/v1/users")
    api.add_namespace(place_ns, path="/api/v1/places")
    api.add_namespace(amenity_ns, path="/api/v1/amenities")
    api.add_namespace(review_ns, path="/api/v1/reviews")

    return app
