#!/usr/bin/env python3
"""
Script to create comprehensive test data for the HBnB application.
This includes places, amenities, reviews, and their relationships.
"""

import sys
import os
import uuid
import random

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from app.config import DevelopmentConfig
from services.facade import create_user, create_place, create_amenity, create_review
from app.extensions import db
from infrastructure.models import User, Place, Amenity, Review

def create_test_data():
    """Create comprehensive test data for the HBnB application."""
    
    print("Creating comprehensive test data for HBnB...")
    print("=" * 60)
    
    # Create Flask app context
    app = create_app(DevelopmentConfig)
    
    with app.app_context():
        # Create all tables using Base metadata
        from infrastructure.models.base import Base
        Base.metadata.create_all(db.engine)
        print("✅ Database tables created")
        
        # Clear existing data (optional - comment out if you want to keep existing data)
        # db.session.query(Review).delete()
        # db.session.query(Place).delete()
        # db.session.query(Amenity).delete()
        # db.session.query(User).delete()
        # db.session.commit()
        
        # Create test users if they don't exist
        users = create_test_users()
        
        # Create amenities
        amenities = create_test_amenities()
        
        # Create places
        places = create_test_places(users)
        
        # Create reviews
        create_test_reviews(places, users)
        
        print("=" * 60)
        print("✅ Test data created successfully!")
        print(f"   Users: {len(users)}")
        print(f"   Places: {len(places)}")
        print(f"   Amenities: {len(amenities)}")
        print("\nYou can now test the application with rich data!")

def create_test_users():
    """Create test users if they don't exist."""
    users_data = [
        {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'password': 'password123',
            'is_admin': False
        },
        {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'jane@example.com',
            'password': 'password123',
            'is_admin': False
        },
        {
            'first_name': 'Admin',
            'last_name': 'User',
            'email': 'admin@example.com',
            'password': 'admin123',
            'is_admin': True
        },
        {
            'first_name': 'Sarah',
            'last_name': 'Johnson',
            'email': 'sarah@example.com',
            'password': 'password123',
            'is_admin': False
        },
        {
            'first_name': 'Mike',
            'last_name': 'Wilson',
            'email': 'mike@example.com',
            'password': 'password123',
            'is_admin': False
        }
    ]
    
    users = []
    for user_data in users_data:
        existing_user = db.session.query(User).filter_by(email=user_data['email']).first()
        if existing_user:
            users.append(existing_user)
            print(f"⚠️  User {user_data['email']} already exists, using existing user")
        else:
            user = create_user(user_data)
            users.append(user)
            print(f"✅ Created user: {user.email}")
    
    return users

def create_test_amenities():
    """Create test amenities with phosphor icon mappings."""
    amenities_data = [
        {'name': 'WiFi', 'icon': 'ph-wifi-high'},
        {'name': 'Kitchen', 'icon': 'ph-cooking-pot'},
        {'name': 'Free Parking', 'icon': 'ph-car'},
        {'name': 'Air Conditioning', 'icon': 'ph-wind'},
        {'name': 'Swimming Pool', 'icon': 'ph-swimming-pool'},
        {'name': 'Gym', 'icon': 'ph-dumbbell'},
        {'name': 'TV', 'icon': 'ph-television'},
        {'name': 'Washer/Dryer', 'icon': 'ph-washing-machine'},
        {'name': 'Balcony', 'icon': 'ph-house-line'},
        {'name': 'Fireplace', 'icon': 'ph-fire'},
        {'name': 'Pet Friendly', 'icon': 'ph-dog'},
        {'name': 'Breakfast', 'icon': 'ph-bread'},
        {'name': 'Hot Tub', 'icon': 'ph-bathtub'},
        {'name': 'Garden', 'icon': 'ph-tree'},
        {'name': 'Workspace', 'icon': 'ph-laptop'}
    ]
    
    amenities = []
    for amenity_data in amenities_data:
        existing_amenity = db.session.query(Amenity).filter_by(name=amenity_data['name']).first()
        if existing_amenity:
            amenities.append(existing_amenity)
            print(f"⚠️  Amenity {amenity_data['name']} already exists, using existing amenity")
        else:
            amenity = create_amenity({
                'id': str(uuid.uuid4()),
                'name': amenity_data['name']
            })
            # Add icon attribute to amenity object for frontend use
            amenity.icon = amenity_data['icon']
            amenities.append(amenity)
            print(f"✅ Created amenity: {amenity.name} ({amenity.icon})")
    
    return amenities

def create_test_places(users):
    """Create test places with various amenities."""
    places_data = [
        {
            'name': 'Beautiful Beach House',
            'description': 'A stunning beachfront property with panoramic ocean views. Perfect for families and groups looking for a luxurious coastal getaway.',
            'price': 250.0,
            'latitude': 34.0522,
            'longitude': -118.2437,
            'amenities': ['WiFi', 'Kitchen', 'Free Parking', 'Air Conditioning', 'Swimming Pool', 'TV', 'Balcony'],
            'images': [
                'https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=800',
                'https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=800',
                'https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=800'
            ]
        },
        {
            'name': 'Cozy Mountain Cabin',
            'description': 'Rustic yet modern cabin nestled in the mountains. Features a fireplace, hot tub, and breathtaking mountain views.',
            'price': 180.0,
            'latitude': 39.7392,
            'longitude': -104.9903,
            'amenities': ['WiFi', 'Kitchen', 'Fireplace', 'Hot Tub', 'Pet Friendly', 'Garden', 'TV'],
            'images': [
                'https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=800',
                'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800',
                'https://images.unsplash.com/photo-1518780664697-55e3ad937233?w=800'
            ]
        },
        {
            'name': 'Downtown Luxury Apartment',
            'description': 'Modern apartment in the heart of the city. Walking distance to restaurants, shops, and cultural attractions.',
            'price': 320.0,
            'latitude': 40.7128,
            'longitude': -74.0060,
            'amenities': ['WiFi', 'Kitchen', 'Air Conditioning', 'Gym', 'TV', 'Workspace', 'Balcony'],
            'images': [
                'https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=800',
                'https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=800',
                'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800'
            ]
        },
        {
            'name': 'Riverside Cottage',
            'description': 'Charming cottage by the river with a private garden. Perfect for a peaceful retreat in nature.',
            'price': 140.0,
            'latitude': 45.5152,
            'longitude': -122.6784,
            'amenities': ['WiFi', 'Kitchen', 'Garden', 'Pet Friendly', 'Fireplace', 'TV', 'Washer/Dryer'],
            'images': [
                'https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=800',
                'https://images.unsplash.com/photo-1570129477492-45c003edd2be?w=800',
                'https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=800'
            ]
        },
        {
            'name': 'Ski Resort Condo',
            'description': 'Ski-in/ski-out condo with mountain views. Includes access to resort amenities and nearby ski slopes.',
            'price': 280.0,
            'latitude': 40.7608,
            'longitude': -111.8910,
            'amenities': ['WiFi', 'Kitchen', 'Free Parking', 'Air Conditioning', 'Hot Tub', 'Fireplace', 'TV'],
            'images': [
                'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800',
                'https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=800',
                'https://images.unsplash.com/photo-1518780664697-55e3ad937233?w=800'
            ]
        },
        {
            'name': 'Historic City Loft',
            'description': 'Beautifully restored loft in a historic building. High ceilings, exposed brick, and modern amenities.',
            'price': 200.0,
            'latitude': 41.8781,
            'longitude': -87.6298,
            'amenities': ['WiFi', 'Kitchen', 'Air Conditioning', 'TV', 'Workspace', 'Washer/Dryer'],
            'images': [
                'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800',
                'https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=800',
                'https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=800'
            ]
        },
        {
            'name': 'Tropical Paradise Villa',
            'description': 'Luxurious villa with private pool and tropical gardens. Perfect for a romantic getaway or family vacation.',
            'price': 450.0,
            'latitude': 21.3069,
            'longitude': -157.8583,
            'amenities': ['WiFi', 'Kitchen', 'Swimming Pool', 'Air Conditioning', 'TV', 'Garden', 'Breakfast'],
            'images': [
                'https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=800',
                'https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=800',
                'https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=800'
            ]
        },
        {
            'name': 'Desert Oasis Retreat',
            'description': 'Peaceful retreat in the desert with stunning sunset views. Features a private pool and outdoor dining area.',
            'price': 220.0,
            'latitude': 33.4484,
            'longitude': -112.0740,
            'amenities': ['WiFi', 'Kitchen', 'Swimming Pool', 'Air Conditioning', 'Garden', 'TV', 'Balcony'],
            'images': [
                'https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=800',
                'https://images.unsplash.com/photo-1570129477492-45c003edd2be?w=800',
                'https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=800'
            ]
        }
    ]
    
    places = []
    for i, place_data in enumerate(places_data):
        # Assign random owner from users
        owner = random.choice(users)
        
        # Create place
        place = create_place({
            'id': str(uuid.uuid4()),
            'name': place_data['name'],
            'description': place_data['description'],
            'price': place_data['price'],
            'owner_id': owner.id,
            'latitude': place_data['latitude'],
            'longitude': place_data['longitude'],
            'images': place_data['images']
        })
        
        # Add amenities to place
        for amenity_name in place_data['amenities']:
            amenity = db.session.query(Amenity).filter_by(name=amenity_name).first()
            if amenity:
                place.amenities.append(amenity)
        
        db.session.commit()
        places.append(place)
        print(f"✅ Created place: {place.name} (Owner: {owner.first_name})")
        print(f"   Amenities: {', '.join([a.name for a in place.amenities])}")
    
    return places

def create_test_reviews(places, users):
    """Create test reviews for places."""
    review_texts = [
        "Absolutely amazing place! The views are breathtaking and the amenities are top-notch.",
        "Great location and very clean. Would definitely recommend to others.",
        "Perfect for our family vacation. The kids loved the pool and we enjoyed the peaceful setting.",
        "Beautiful property with everything we needed. The host was very responsive and helpful.",
        "Stunning views and comfortable accommodations. We had a wonderful time!",
        "Excellent value for money. The place was spotless and well-maintained.",
        "Fantastic experience! The location is perfect and the property exceeded our expectations.",
        "Very cozy and welcoming. We felt right at home from the moment we arrived.",
        "Outstanding property with amazing amenities. We can't wait to come back!",
        "Wonderful stay! The place is even better than the photos suggest.",
        "Perfect getaway spot. Quiet, clean, and very comfortable.",
        "Excellent communication with the host and a beautiful property. Highly recommend!",
        "Great amenities and perfect location. We had everything we needed for a relaxing stay.",
        "Beautiful property with stunning views. The attention to detail is impressive.",
        "Fantastic place to stay! We loved every minute of our time here."
    ]
    
    reviews_created = 0
    for place in places:
        # Create 2-4 reviews per place
        num_reviews = random.randint(2, 4)
        for _ in range(num_reviews):
            reviewer = random.choice(users)
            review_text = random.choice(review_texts)
            
            review = create_review({
                'id': str(uuid.uuid4()),
                'text': review_text,
                'user_id': reviewer.id,
                'place_id': place.id
            })
            
            reviews_created += 1
            print(f"✅ Created review by {reviewer.first_name} for {place.name}")
    
    print(f"\n📝 Created {reviews_created} reviews total")

if __name__ == '__main__':
    create_test_data()
