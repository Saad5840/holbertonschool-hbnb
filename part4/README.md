# HBnB Authentication System

This project implements a complete authentication system for the HBnB application with a modern, responsive UI.

## Features

- **User Authentication**: Login/logout functionality with JWT tokens
- **Form Validation**: Client-side email validation and error handling
- **User Feedback**: Toast notifications for success/error messages
- **Session Management**: Automatic token storage and retrieval
- **Responsive Design**: Modern UI with loading states and animations

## How to Use

### Running the Application

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python3 run.py
   ```

3. Open your browser and navigate to `http://localhost:5001`

### Authentication Flow

1. **Login**: Navigate to `/login` or click the "Login" button in the header
2. **Enter Credentials**: Fill in your email and password
3. **Submit**: Click "Login to HBnB" to authenticate
4. **Success**: You'll be redirected to the home page with a success message
5. **Logout**: Click "My Account" in the header to log out

### API Endpoints

#### Authentication
- **POST** `/api/v1/auth/login` - Authenticate user
  - Body: `{"email": "user@example.com", "password": "password"}`
  - Returns: `{"access_token": "jwt_token"}`

#### Places
- **GET** `/api/v1/places/` - Get all places with amenities
- **GET** `/api/v1/places/{id}` - Get specific place with reviews
- **POST** `/api/v1/places/` - Create new place (requires authentication)

#### Amenities
- **GET** `/api/v1/amenities/` - Get all amenities with icons
- **POST** `/api/v1/amenities/` - Create new amenity (admin only)

#### Reviews
- **GET** `/api/v1/reviews/` - Get all reviews with user and place info
- **POST** `/api/v1/reviews/` - Create new review (requires authentication)

### JavaScript Functions

The authentication system provides several utility functions:

- `handleLogin(event)` - Handles login form submission
- `checkAuthStatus()` - Checks if user is authenticated
- `updateAuthUI(isLoggedIn)` - Updates UI based on auth status
- `handleLogout()` - Handles user logout
- `showMessage(message, type)` - Shows toast notifications
- `getAuthToken()` - Retrieves stored JWT token
- `authenticatedFetch(url, options)` - Makes authenticated API requests

### Security Features

- JWT token-based authentication
- Password hashing with bcrypt
- Client-side form validation
- Secure token storage in localStorage
- Automatic token inclusion in API requests

### UI Components

- **Login Form**: Clean, modern design with validation
- **Loading States**: Visual feedback during authentication
- **Toast Notifications**: Success/error messages with auto-dismiss
- **Responsive Design**: Works on desktop and mobile devices

## File Structure

```
app/
├── static/
│   ├── scripts.js          # Authentication logic
│   └── styles.css          # UI styles
├── templates/
│   └── login.html          # Login page template
routes/
└── auth_routes.py          # Backend authentication API
```

## Testing

### Adding Test Users

Before testing the authentication system, you need to add test users to the database. You have several options:

#### Option 1: Create Multiple Test Users (Recommended)
```bash
# Make sure the Flask app is running first
python3 run.py

# In another terminal, run:
python3 scripts/create_user_via_api.py
```

This will create 4 test users:
- `john@example.com` / `password123`
- `jane@example.com` / `password123`
- `admin@example.com` / `admin123`
- `test@example.com` / `test123`

#### Option 2: Create a Single Custom User
```bash
# Make sure the Flask app is running first
python3 run.py

# In another terminal, run:
python3 scripts/create_single_user.py
```

This will prompt you for user details interactively.

#### Option 3: Direct Database Access
```bash
python3 scripts/add_test_users.py
```

#### Option 4: Comprehensive Test Data (Recommended)
```bash
python3 scripts/create_test_data.py
```

This creates a complete dataset with:
- 5 test users
- 8 diverse places with various amenities
- 15 different amenities with phosphor icons
- 25 reviews across all places

This creates users directly in the database (requires the app to be configured but not running).

### Testing the Application

1. **Create test data first** (recommended):
   ```bash
   python3 scripts/create_test_data.py
   ```

2. **Test the models** (optional):
   ```bash
   python3 scripts/test_models.py
   ```

3. Start the application: `python3 run.py`

4. Test the different pages:
   - **Home page**: `http://localhost:5001/` - View all places with images, prices, and amenities
   - **Login page**: `http://localhost:5001/login` - Test authentication
   - **Place details**: `http://localhost:5001/place?id={place_id}` - View specific place with images, reviews, and rating system
   - **Reviews page**: `http://localhost:5001/reviews` - View all reviews

5. Test the APIs:
   - `http://localhost:5001/api/v1/places/` - Get all places with images and prices
   - `http://localhost:5001/api/v1/amenities/` - Get all amenities with icons
   - `http://localhost:5001/api/v1/reviews/` - Get all reviews with ratings

### New Features Implemented

✅ **Price Filtering**: Filter places by maximum price on the home page
✅ **Place Images**: High-quality Unsplash images for each place
✅ **Price Display**: Show prices on place cards and detail pages
✅ **Star Rating System**: Interactive 5-star rating for reviews
✅ **Owner Information**: Display "Hosted by" information on place details
✅ **Authentication UI**: Login/logout button with proper state management
✅ **Review Submission**: Add reviews with ratings (requires authentication)
✅ **Enhanced UI**: Modern card design with hover effects and responsive layout

The system includes comprehensive error handling for:
- Invalid email formats
- Missing fields
- Network errors
- Authentication failures

## Troubleshooting

### SQLAlchemy Model Errors

If you encounter SQLAlchemy relationship errors like:
```
sqlalchemy.exc.InvalidRequestError: One or more mappers failed to initialize
```

**Solution**: The models are now properly configured to avoid circular import issues. If you still encounter problems:

1. Delete the database file: `rm instance/hbnb.db`
2. Restart the application: `python3 run.py`
3. Run the test script: `python3 scripts/test_models.py`

### Database ID Errors

If you encounter errors like:
```
sqlalchemy.exc.IntegrityError: NOT NULL constraint failed: users.id
```

**Solution**: The models now automatically generate UUIDs for missing IDs. This has been fixed in the service layer.

### Port Issues

If the application doesn't start on the expected port, check:
- The port configuration in your Flask app
- Update the API scripts to use the correct port (currently set to 5001)
