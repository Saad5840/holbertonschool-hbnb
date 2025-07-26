from flask_restx import Api
from routes.user_routes import api as user_ns
from routes.auth_routes import api as auth_ns
from routes.place_routes import api as place_ns
from routes.review_routes import api as review_ns
from routes.amenity_routes import api as amenity_ns

api = Api(
    title="HBnB API",
    version="1.0",
    description="HBnB API"
)

api.add_namespace(user_ns, path='/api/v1/users')
api.add_namespace(auth_ns, path='/api/v1/auth')
api.add_namespace(place_ns, path='/api/v1/places')
api.add_namespace(review_ns, path='/api/v1/reviews')
api.add_namespace(amenity_ns, path='/api/v1/amenities')

