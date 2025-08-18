#!/usr/bin/env python3
"""
Script to create test users via the API endpoint.
This approach uses the same API that the frontend would use.
"""

import requests
import json
import sys

def create_user_via_api(user_data):
    """Create a user via the API endpoint."""
    url = "http://localhost:5001/api/v1/users/"
    
    try:
        response = requests.post(url, json=user_data)
        
        if response.status_code == 201:
            print(f"✅ Created user: {user_data['email']}")
            return True
        else:
            print(f"❌ Failed to create user {user_data['email']}: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print(f"❌ Could not connect to server. Make sure the Flask app is running on http://localhost:5001")
        return False
    except Exception as e:
        print(f"❌ Error creating user {user_data['email']}: {str(e)}")
        return False

def main():
    """Main function to create test users."""
    
    # Test users data
    test_users = [
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
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'password': 'test123',
            'is_admin': False
        }
    ]
    
    print("Creating test users via API...")
    print("=" * 50)
    print("Make sure the Flask application is running on http://localhost:5001")
    print()
    
    success_count = 0
    
    for user_data in test_users:
        if create_user_via_api(user_data):
            success_count += 1
        print()
    
    print("=" * 50)
    if success_count > 0:
        print(f"✅ Successfully created {success_count} test users!")
        print("\nYou can now use these credentials to test the login system:")
        print("- john@example.com / password123")
        print("- jane@example.com / password123")
        print("- admin@example.com / admin123")
        print("- test@example.com / test123")
    else:
        print("❌ No users were created. Please check the error messages above.")

if __name__ == '__main__':
    main()
