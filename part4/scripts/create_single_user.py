#!/usr/bin/env python3
"""
Interactive script to create a single user with custom credentials.
This script prompts for user input and creates a user via the API.
"""

import requests
import json
import sys
import getpass

def create_user_via_api(user_data):
    """Create a user via the API endpoint."""
    url = "http://localhost:5000/api/v1/users/"
    
    try:
        response = requests.post(url, json=user_data)
        
        if response.status_code == 201:
            print(f"✅ Successfully created user: {user_data['email']}")
            return True
        else:
            print(f"❌ Failed to create user: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print(f"❌ Could not connect to server. Make sure the Flask app is running on http://localhost:5000")
        return False
    except Exception as e:
        print(f"❌ Error creating user: {str(e)}")
        return False

def get_user_input():
    """Get user input for creating a new user."""
    print("Create a new user account")
    print("=" * 30)
    
    first_name = input("First name: ").strip()
    if not first_name:
        print("❌ First name is required")
        return None
    
    last_name = input("Last name: ").strip()
    if not last_name:
        print("❌ Last name is required")
        return None
    
    email = input("Email: ").strip()
    if not email:
        print("❌ Email is required")
        return None
    
    # Basic email validation
    if '@' not in email or '.' not in email:
        print("❌ Please enter a valid email address")
        return None
    
    password = getpass.getpass("Password: ")
    if not password:
        print("❌ Password is required")
        return None
    
    confirm_password = getpass.getpass("Confirm password: ")
    if password != confirm_password:
        print("❌ Passwords do not match")
        return None
    
    is_admin_input = input("Is admin? (y/N): ").strip().lower()
    is_admin = is_admin_input in ['y', 'yes']
    
    return {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,
        'is_admin': is_admin
    }

def main():
    """Main function for interactive user creation."""
    print("HBnB User Creation Tool")
    print("=" * 30)
    print("Make sure the Flask application is running on http://localhost:5000")
    print()
    
    user_data = get_user_input()
    
    if user_data:
        print(f"\nCreating user: {user_data['email']}")
        print(f"Name: {user_data['first_name']} {user_data['last_name']}")
        print(f"Admin: {'Yes' if user_data['is_admin'] else 'No'}")
        
        confirm = input("\nProceed? (Y/n): ").strip().lower()
        if confirm in ['', 'y', 'yes']:
            if create_user_via_api(user_data):
                print(f"\n✅ User created successfully!")
                print(f"You can now login with: {user_data['email']}")
            else:
                print(f"\n❌ Failed to create user. Please try again.")
        else:
            print("User creation cancelled.")
    else:
        print("User creation cancelled due to invalid input.")

if __name__ == '__main__':
    main()
