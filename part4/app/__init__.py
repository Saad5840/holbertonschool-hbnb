from flask import Flask, render_template
from flask_restx import Api
from app.extensions import db, bcrypt, jwt
from routes import api

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/login')
    def login():
        return render_template('login.html')
    
    @app.route('/place')
    def place():
        return render_template('place.html')
    
    @app.route('/reviews')
    def reviews():
        return render_template('add_review.html')
    
    # Initialize API with custom documentation path
    api.init_app(app, doc='/api/docs/')
    
    with app.app_context():
        db.create_all()

    return app

