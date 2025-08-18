#!/usr/bin/env python3
"""
Simplified script to create basic test data for the HBnB application.
"""

import sys
import os
import uuid

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from app.config import DevelopmentConfig
from services.facade import create_user, create_place, create_amenity, create_review
from app.extensions import db
from infrastructure.models import User, Place, Amenity, Review

def create_simple_test_data():
    """Create basic test data for the HBnB application."""
    
    print("Creating basic test data for HBnB...")
    print("=" * 50)
    
    # Create Flask app context
    app = create_app(DevelopmentConfig)
    
    with app.app_context():
        # Create all tables
        db.create_all()
        print("✅ Database tables created")
        
        # Create a simple test user
        try:
            user = create_user({
                'first_name': 'Test',
                'last_name': 'User',
                'email': 'test@example.com',
                'password': 'password123',
                'is_admin': False
            })
            print(f"✅ Created user: {user.email}")
        except Exception as e:
            print(f"❌ Error creating user: {e}")
            return
        
        # Create a simple test amenity
        try:
            amenity = create_amenity({
                'name': 'WiFi'
            })
            print(f"✅ Created amenity: {amenity.name}")
        except Exception as e:
            print(f"❌ Error creating amenity: {e}")
            return
        
        # Create a simple test place
        try:
            place = create_place({
                'name': 'Test Place',
                'description': 'A test place for demonstration',
                'owner_id': user.id
            })
            print(f"✅ Created place: {place.name}")
        except Exception as e:
            print(f"❌ Error creating place: {e}")
            return
        
        # Create a simple test review
        try:
            review = create_review({
                'text': 'Great place!',
                'user_id': user.id,
                'place_id': place.id
            })
            print(f"✅ Created review")
        except Exception as e:
            print(f"❌ Error creating review: {e}")
            return
        
        print("=" * 50)
        print("✅ Basic test data created successfully!")

if __name__ == '__main__':
    create_simple_test_data()
