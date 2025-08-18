#!/usr/bin/env python3
"""
Test script to verify that all SQLAlchemy models are working correctly.
This script will test model creation and relationships.
"""

import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from app.config import DevelopmentConfig
from infrastructure.models import User, Place, Review, Amenity
from app.extensions import db

def test_models():
    """Test that all models can be created and relationships work."""
    
    print("Testing SQLAlchemy models...")
    print("=" * 40)
    
    # Create Flask app context
    app = create_app(DevelopmentConfig)
    
    with app.app_context():
        try:
            # Test User model
            print("✅ Testing User model...")
            user = User(
                id="test-user-1",
                first_name="Test",
                last_name="User",
                email="test@example.com",
                password="hashed_password",
                is_admin=False
            )
            print(f"   Created user: {user.first_name} {user.last_name}")
            
            # Test Place model
            print("✅ Testing Place model...")
            place = Place(
                id="test-place-1",
                name="Test Place",
                description="A test place",
                owner_id="test-user-1"
            )
            print(f"   Created place: {place.name}")
            
            # Test Review model
            print("✅ Testing Review model...")
            review = Review(
                id="test-review-1",
                text="Great place!",
                user_id="test-user-1",
                place_id="test-place-1"
            )
            print(f"   Created review: {review.text[:20]}...")
            
            # Test Amenity model
            print("✅ Testing Amenity model...")
            amenity = Amenity(
                id="test-amenity-1",
                name="WiFi"
            )
            print(f"   Created amenity: {amenity.name}")
            
            # Test relationships
            print("✅ Testing relationships...")
            user.places.append(place)
            place.reviews.append(review)
            print(f"   User has {len(user.places)} places")
            print(f"   Place has {len(place.reviews)} reviews")
            
            print("\n🎉 All models are working correctly!")
            print("SQLAlchemy relationships are properly established.")
            
        except Exception as e:
            print(f"❌ Error testing models: {str(e)}")
            import traceback
            traceback.print_exc()
            return False
    
    return True

if __name__ == '__main__':
    success = test_models()
    if success:
        print("\n✅ Model test completed successfully!")
    else:
        print("\n❌ Model test failed!")
        sys.exit(1)
