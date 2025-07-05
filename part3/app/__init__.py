from flask import Flask
from flask_restx import Api
from app.extensions import db, bcrypt, jwt
from routes import api

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    api.init_app(app)

    return app

