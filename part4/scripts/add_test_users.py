#!/usr/bin/env python3
"""
Script to add test users to the HBnB database with properly hashed passwords.
Run this script to populate the database with test credentials for authentication.
"""

import sys
import os
from datetime import datetime
import uuid

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from app.config import DevelopmentConfig
from services.facade import create_user, get_user_by_email

def add_test_users():
    """Add test users to the database with properly hashed passwords."""
    
    # Create Flask app context
    app = create_app(DevelopmentConfig)
    
    with app.app_context():
        # Test users data
        test_users = [
            {
                'id': str(uuid.uuid4()),
                'first_name': 'John',
                'last_name': 'Doe',
                'email': 'john@example.com',
                'password': 'password123',
                'is_admin': False
            },
            {
                'id': str(uuid.uuid4()),
                'first_name': 'Jane',
                'last_name': 'Smith',
                'email': 'jane@example.com',
                'password': 'password123',
                'is_admin': False
            },
            {
                'id': str(uuid.uuid4()),
                'first_name': 'Admin',
                'last_name': 'User',
                'email': 'admin@example.com',
                'password': 'admin123',
                'is_admin': True
            },
            {
                'id': str(uuid.uuid4()),
                'first_name': 'Test',
                'last_name': 'User',
                'email': 'test@example.com',
                'password': 'test123',
                'is_admin': False
            }
        ]
        
        print("Adding test users to the database...")
        print("=" * 50)
        
        for user_data in test_users:
            try:
                # Check if user already exists
                existing_user = get_user_by_email(user_data['email'])
                if existing_user:
                    print(f"⚠️  User {user_data['email']} already exists, skipping...")
                    continue
                
                # Create new user
                user = create_user(user_data)
                print(f"✅ Created user: {user.email}")
                print(f"   Name: {user.first_name} {user.last_name}")
                print(f"   Admin: {'Yes' if user.is_admin else 'No'}")
                print(f"   Password: {user_data['password']}")
                print()
                
            except Exception as e:
                print(f"❌ Error creating user {user_data['email']}: {str(e)}")
                print()
        
        print("=" * 50)
        print("Test users added successfully!")
        print("\nYou can now use these credentials to test the login system:")
        print("- john@example.com / password123")
        print("- jane@example.com / password123")
        print("- admin@example.com / admin123")
        print("- test@example.com / test123")

if __name__ == '__main__':
    add_test_users()
