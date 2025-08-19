// Authentication and form handling logic
console.log('Scripts.js loaded successfully!');

document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM loaded, setting up event listeners...');
    
    // Handle login form submission
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        console.log('Login form found, adding event listener...');
        loginForm.addEventListener('submit', handleLogin);
    } else {
        console.error('Login form not found!');
    }

    // Check if user is already logged in
    checkAuthStatus();
    
    // Load places data if on home page
    if (window.location.pathname === '/' || window.location.pathname === '/index.html') {
        loadPlaces();
        setupPriceFilter();
    }
    
    // Load place details if on place page
    if (window.location.pathname === '/place') {
        loadPlaceDetails();
        setupReviewForm();
    }
    
    // Load reviews if on reviews page
    if (window.location.pathname === '/reviews') {
        loadReviews();
    }
});

/**
 * Handle login form submission
 * @param {Event} event - Form submission event
 */
async function handleLogin(event) {
    console.log('Login form submitted!');
    event.preventDefault();
    
    const form = event.target;
    const email = form.email.value.trim();
    const password = form.password.value;
    
    console.log('Attempting login with email:', email);
    
    // Basic validation
    if (!email || !password) {
        showMessage('Please fill in all fields', 'error');
        return;
    }
    
    if (!isValidEmail(email)) {
        showMessage('Please enter a valid email address', 'error');
        return;
    }
    
    // Show loading state
    const submitButton = form.querySelector('button[type="submit"]');
    const originalText = submitButton.innerHTML;
    submitButton.innerHTML = '<i class="ph-bold ph-spinner"></i><span>Logging in...</span>';
    submitButton.disabled = true;
    
    try {
        console.log('Making API request to /api/v1/auth/login...');
        const response = await fetch('/api/v1/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                email: email,
                password: password
            })
        });
        
        console.log('Response status:', response.status);
        
        const data = await response.json();
        console.log('Response data:', data);
        
        if (response.ok) {
            // Store the JWT token
            localStorage.setItem('authToken', data.access_token);
            
            // Update UI to show logged in state
            updateAuthUI(true);
            
            showMessage('Login successful! Redirecting...', 'success');
            
            // Redirect to home page after a short delay
            setTimeout(() => {
                window.location.href = '/';
            }, 1500);
            
        } else {
            // Handle authentication errors
            const errorMessage = data.message || 'Login failed. Please try again.';
            showMessage(errorMessage, 'error');
        }
        
    } catch (error) {
        console.error('Login error:', error);
        showMessage('Network error. Please check your connection and try again.', 'error');
    } finally {
        // Restore button state
        submitButton.innerHTML = originalText;
        submitButton.disabled = false;
    }
}

/**
 * Check if user is already authenticated
 */
function checkAuthStatus() {
    const token = localStorage.getItem('access_token');
    if (token) {
        updateAuthUI(true);
    } else {
        updateAuthUI(false);
    }
}

/**
 * Update UI based on authentication status
 * @param {boolean} isLoggedIn - Whether user is logged in
 */
function updateAuthUI(isLoggedIn) {
    const loginButton = document.querySelector('.login-button');
    
    if (loginButton) {
        if (isLoggedIn) {
            loginButton.innerHTML = '<i class="ph-bold ph-sign-out"></i><span>Logout</span>';
            loginButton.onclick = () => handleLogout();
            loginButton.href = 'javascript:void(0);';
        } else {
            loginButton.innerHTML = '<i class="ph-bold ph-identification-badge"></i><span>Login</span>';
            loginButton.onclick = null;
            loginButton.href = '/login';
        }
    }
}

/**
 * Handle user logout
 */
function handleLogout() {
    // Remove stored tokens
    localStorage.removeItem('access_token');
    localStorage.removeItem('user_info');
    
    // Update UI
    updateAuthUI(false);
    
    // Show logout message
    showMessage('Logged out successfully', 'success');
    
    // Redirect to home page if on login page
    if (window.location.pathname === '/login') {
        window.location.href = '/';
    }
}

/**
 * Validate email format
 * @param {string} email - Email to validate
 * @returns {boolean} - Whether email is valid
 */
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

/**
 * Show message to user
 * @param {string} message - Message to display
 * @param {string} type - Message type ('success', 'error', 'info')
 */
function showMessage(message, type = 'info') {
    // Remove existing messages
    const existingMessage = document.querySelector('.message');
    if (existingMessage) {
        existingMessage.remove();
    }
    
    // Create message element
    const messageElement = document.createElement('div');
    messageElement.className = `message message-${type}`;
    messageElement.innerHTML = `
        <i class="ph-bold ${getMessageIcon(type)}"></i>
        <span>${message}</span>
        <button onclick="this.parentElement.remove()" class="message-close">
            <i class="ph-bold ph-x"></i>
        </button>
    `;
    
    // Add styles
    messageElement.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 12px 16px;
        border-radius: 8px;
        color: white;
        font-weight: 500;
        display: flex;
        align-items: center;
        gap: 8px;
        z-index: 1000;
        max-width: 400px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        animation: slideIn 0.3s ease-out;
    `;
    
    // Set background color based on type
    const colors = {
        success: '#10b981',
        error: '#ef4444',
        info: '#3b82f6'
    };
    messageElement.style.backgroundColor = colors[type] || colors.info;
    
    // Add to page
    document.body.appendChild(messageElement);
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        if (messageElement.parentElement) {
            messageElement.remove();
        }
    }, 5000);
}

/**
 * Get icon for message type
 * @param {string} type - Message type
 * @returns {string} - Icon class name
 */
function getMessageIcon(type) {
    const icons = {
        success: 'ph-check-circle',
        error: 'ph-x-circle',
        info: 'ph-info'
    };
    return icons[type] || icons.info;
}

/**
 * Get authentication token for API requests
 * @returns {string|null} - JWT token or null
 */
function getAuthToken() {
    return localStorage.getItem('authToken');
}

/**
 * Make authenticated API request
 * @param {string} url - API endpoint
 * @param {Object} options - Fetch options
 * @returns {Promise} - Fetch response
 */
async function authenticatedFetch(url, options = {}) {
    const token = getAuthToken();
    
    if (!token) {
        throw new Error('No authentication token available');
    }
    
    const headers = {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
        ...options.headers
    };
    
    return fetch(url, {
        ...options,
        headers
    });
}

//

/**
 * Load and display places data
 */
async function loadPlaces() {
    try {
        console.log('Loading places data...');
        const response = await fetch('/api/v1/places/');
        const places = await response.json();
        
        console.log('Places loaded:', places);
        // Store places globally for filtering
        window.allPlaces = places;
        displayPlaces(places);
        
    } catch (error) {
        console.error('Error loading places:', error);
        showMessage('Error loading places data', 'error');
    }
}

/**
 * Setup price filter functionality
 */
function setupPriceFilter() {
    const filterOptions = document.querySelectorAll('input[name="option"]');
    filterOptions.forEach(option => {
        option.addEventListener('change', function() {
            const maxPrice = parseFloat(this.value);
            filterPlacesByPrice(maxPrice);
        });
    });
}

/**
 * Filter places by maximum price
 */
function filterPlacesByPrice(maxPrice) {
    if (!window.allPlaces) return;
    
    let filteredPlaces;
    if (maxPrice === -1) {
        // Show all places
        filteredPlaces = window.allPlaces;
    } else {
        // Filter by price
        filteredPlaces = window.allPlaces.filter(place => place.price <= maxPrice);
    }
    
    displayPlaces(filteredPlaces);
}

/**
 * Display places in the places list
 */
function displayPlaces(places) {
    const placesList = document.querySelector('.places-list');
    if (!placesList) {
        console.error('Places list container not found');
        return;
    }
    
    // Clear existing content
    placesList.innerHTML = '';
    
    places.forEach(place => {
        const placeCard = createPlaceCard(place);
        placesList.appendChild(placeCard);
    });
}

/**
 * Create a place card element
 */
function createPlaceCard(place) {
    const card = document.createElement('div');
    card.className = 'place-card';
    
    // Create amenities HTML
    const amenitiesHTML = place.amenities.map(amenity => 
        `<i class="ph ${amenity.icon}" style="font-size: 16pt;" title="${amenity.name}"></i>`
    ).join('');
    
    // Get first image or use placeholder
    const imageUrl = place.images && place.images.length > 0 ? place.images[0] : 'https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=800';
    
    card.innerHTML = `
        <div class="place-image">
            <img src="${imageUrl}" alt="${place.name}" loading="lazy">
        </div>
        <div class="place-content">
            <div class="place-header">
                <h3 class="place-name">${place.name}</h3>
                <span class="place-price">$${place.price}</span>
            </div>
            <p>${place.description || 'No description available'}</p>
            <div class="place-amenities">
                ${amenitiesHTML}
            </div>
            <a href="/place?id=${place.id}" class="button">
                <span>View Details</span>
                <i class="ph-bold ph-caret-right"></i>
            </a>
        </div>
    `;
    
    return card;
}

/**
 * Load place details for the place page
 */
async function loadPlaceDetails() {
    const urlParams = new URLSearchParams(window.location.search);
    const placeId = urlParams.get('id');
    
    if (!placeId) {
        showMessage('No place ID provided', 'error');
        return;
    }
    
    try {
        const response = await fetch(`/api/v1/places/${placeId}`);
        const place = await response.json();
        
        displayPlaceDetails(place);
        
    } catch (error) {
        console.error('Error loading place details:', error);
        showMessage('Error loading place details', 'error');
    }
}

/**
 * Display place details
 */
function displayPlaceDetails(place) {
    // Update page title
    document.title = place.name;
    
    // Find and update place details elements
    const placeName = document.querySelector('.place-name');
    if (placeName) placeName.textContent = place.name;
    
    const placePrice = document.querySelector('.place-price');
    if (placePrice) placePrice.textContent = `$${place.price}`;
    
    const placeDescription = document.querySelector('.place-description');
    if (placeDescription) placeDescription.textContent = place.description;
    
    // Update owner information if available
    const placeOwner = document.querySelector('.place-owner');
    if (placeOwner && place.owner_name) {
        placeOwner.textContent = place.owner_name;
    }
    
    // Display images
    const imagesContainer = document.querySelector('.place-images-container');
    if (imagesContainer && place.images && place.images.length > 0) {
        const imagesHTML = place.images.map(imageUrl => `
            <div class="place-image-item">
                <img src="${imageUrl}" alt="${place.name}" loading="lazy">
            </div>
        `).join('');
        imagesContainer.innerHTML = imagesHTML;
    }
    
    // Display amenities
    const amenitiesContainer = document.querySelector('.place-amenities');
    if (amenitiesContainer) {
        const amenitiesHTML = place.amenities.map(amenity => `
            <div class="amenity-card">
                <i class="ph ${amenity.icon}" style="font-size: 16pt;"></i>
                <span>${amenity.name}</span>
            </div>
        `).join('');
        amenitiesContainer.innerHTML = amenitiesHTML;
    }
    
    // Display reviews
    const reviewsContainer = document.querySelector('.place-reviews');
    if (reviewsContainer && place.reviews) {
        const reviewsHTML = place.reviews.map(review => `
            <div class="review-item">
                <div class="review-header">
                    <strong>${review.user_name || 'Anonymous'}</strong>
                    <div class="review-rating-display">
                        ${generateStarRating(review.rating)}
                    </div>
                    <span class="review-date">${new Date(review.created_at).toLocaleDateString()}</span>
                </div>
                <p>${review.text}</p>
            </div>
        `).join('');
        reviewsContainer.innerHTML = reviewsHTML;
    }
}

/**
 * Generate star rating HTML
 */
function generateStarRating(rating) {
    const numRating = parseInt(rating) || 5;
    let starsHTML = '';
    for (let i = 1; i <= 5; i++) {
        if (i <= numRating) {
            starsHTML += '<i class="ph-fill ph-star"></i>';
        } else {
            starsHTML += '<i class="ph ph-star"></i>';
        }
    }
    return starsHTML;
}

/**
 * Setup review form functionality
 */
function setupReviewForm() {
    const ratingStars = document.querySelectorAll('.rating-star');
    const ratingValue = document.getElementById('rating-value');
    const reviewForm = document.getElementById('review-form');
    
    // Handle star rating selection
    ratingStars.forEach(star => {
        star.addEventListener('click', function() {
            const rating = this.getAttribute('data-rating');
            ratingValue.value = rating;
            
            // Update star display
            ratingStars.forEach((s, index) => {
                if (index < rating) {
                    s.className = 'ph-fill ph-star rating-star';
                } else {
                    s.className = 'ph ph-star rating-star';
                }
                s.setAttribute('data-rating', index + 1);
            });
        });
    });
    
    // Handle form submission
    if (reviewForm) {
        reviewForm.addEventListener('submit', handleReviewSubmit);
    }
}

/**
 * Handle review form submission
 */
async function handleReviewSubmit(event) {
    event.preventDefault();
    
    const token = localStorage.getItem('access_token');
    if (!token) {
        showMessage('Please login to add a review', 'error');
        return;
    }
    
    const reviewText = document.getElementById('review-text').value;
    const rating = document.getElementById('rating-value').value;
    const placeId = new URLSearchParams(window.location.search).get('id');
    
    if (!reviewText.trim()) {
        showMessage('Please enter a review', 'error');
        return;
    }
    
    try {
        const response = await fetch('/api/v1/reviews/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({
                text: reviewText,
                rating: rating,
                place_id: placeId
            })
        });
        
        if (response.ok) {
            showMessage('Review added successfully!', 'success');
            document.getElementById('review-text').value = '';
            document.getElementById('rating-value').value = '5';
            
            // Reset stars
            const ratingStars = document.querySelectorAll('.rating-star');
            ratingStars.forEach((star, index) => {
                if (index < 5) {
                    star.className = 'ph-fill ph-star rating-star';
                } else {
                    star.className = 'ph ph-star rating-star';
                }
            });
            
            // Reload place details to show new review
            loadPlaceDetails();
        } else {
            const error = await response.json();
            showMessage(error.message || 'Error adding review', 'error');
        }
    } catch (error) {
        console.error('Error submitting review:', error);
        showMessage('Error adding review', 'error');
    }
}

/**
 * Load and display all reviews
 */
async function loadReviews() {
    try {
        const response = await fetch('/api/v1/reviews/');
        const reviews = await response.json();
        
        displayReviews(reviews);
        
    } catch (error) {
        console.error('Error loading reviews:', error);
        showMessage('Error loading reviews', 'error');
    }
}

/**
 * Display reviews
 */
function displayReviews(reviews) {
    const reviewsContainer = document.querySelector('.reviews-list');
    if (!reviewsContainer) {
        console.error('Reviews container not found');
        return;
    }
    
    // Clear existing content
    reviewsContainer.innerHTML = '';
    
    reviews.forEach(review => {
        const reviewElement = createReviewElement(review);
        reviewsContainer.appendChild(reviewElement);
    });
}

/**
 * Create a review element
 */
function createReviewElement(review) {
    const reviewDiv = document.createElement('div');
    reviewDiv.className = 'review-item';
    
    reviewDiv.innerHTML = `
        <div class="review-header">
            <strong>${review.user_name || 'Anonymous'}</strong>
            <span class="review-place">for ${review.place_name || 'Unknown Place'}</span>
            <span class="review-date">${new Date(review.created_at).toLocaleDateString()}</span>
        </div>
        <p>${review.text}</p>
    `;
    
    return reviewDiv;
}

// Add CSS animation for messages
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    .message-close {
        background: none;
        border: none;
        color: white;
        cursor: pointer;
        padding: 0;
        margin-left: auto;
        opacity: 0.8;
        transition: opacity 0.2s;
    }
    
    .message-close:hover {
        opacity: 1;
    }
`;
document.head.appendChild(style);