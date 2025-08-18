#!/usr/bin/env python3
"""
Test script to debug database table creation.
"""

import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from app.config import DevelopmentConfig
from app.extensions import db

def test_db_creation():
    """Test database table creation."""
    
    print("Testing database table creation...")
    print("=" * 40)
    
    # Create Flask app context
    app = create_app(DevelopmentConfig)
    
    with app.app_context():
        print("✅ App context created")
        
        # Import models
        from infrastructure.models.base import Base
        from infrastructure.models import User, Place, Review, Amenity
        
        # Check if models are imported
        print(f"✅ Base: {Base}")
        print(f"✅ User model: {User}")
        print(f"✅ Place model: {Place}")
        print(f"✅ Review model: {Review}")
        print(f"✅ Amenity model: {Amenity}")
        
        # Try to create tables
        try:
            # Import all models to ensure they're registered
            from infrastructure.models import User, Place, Review, Amenity
            print("✅ Models imported")
            
            # Create tables using Base metadata
            from infrastructure.models.base import Base
            Base.metadata.create_all(db.engine)
            print("✅ Base.metadata.create_all() completed")
        except Exception as e:
            print(f"❌ Error in table creation: {e}")
            return
        
        # Check what tables were created
        try:
            inspector = db.inspect(db.engine)
            tables = inspector.get_table_names()
            print(f"✅ Tables created: {tables}")
        except Exception as e:
            print(f"❌ Error checking tables: {e}")

if __name__ == '__main__':
    test_db_creation()
