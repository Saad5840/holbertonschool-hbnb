CREATE TABLE users (
    id VARCHAR(60) PRIMARY KEY,
    first_name VARCHAR(128) NOT NULL,
    last_name VARCHAR(128) NOT NULL,
    email VARCHAR(128) UNIQUE NOT NULL,
    password VARCHAR(128) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    created_at DATETIME,
    updated_at DATETIME
);

CREATE TABLE places (
    id VARCHAR(60) PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    description TEXT,
    owner_id VARCHAR(60),
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY(owner_id) REFERENCES users(id)
);

CREATE TABLE reviews (
    id VARCHAR(60) PRIMARY KEY,
    text TEXT NOT NULL,
    place_id VARCHAR(60),
    user_id VARCHAR(60),
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY(place_id) REFERENCES places(id),
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE amenities (
    id VARCHAR(60) PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    created_at DATETIME,
    updated_at DATETIME
);

CREATE TABLE place_amenity (
    place_id VARCHAR(60),
    amenity_id VARCHAR(60),
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY(place_id) REFERENCES places(id),
    FOREIGN KEY(amenity_id) REFERENCES amenities(id)
);

INSERT INTO users (id, first_name, last_name, email, password, is_admin, created_at, updated_at)
VALUES ('admin-id', 'Admin', 'User', 'admin@example.com', 'hashed_password', TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO amenities (id, name, created_at, updated_at)
VALUES ('amenity1', 'WiFi', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

