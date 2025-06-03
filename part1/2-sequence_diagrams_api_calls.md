# API Sequence Diagrams

**Author:** Ahmed Dawwari, Saad Alarifi and Haidar Alessa  
**Project:** HBnB - Part 1  
**Task:** Sequence Diagrams for API Calls

---

## 📘 Introduction

This document presents four sequence diagrams representing typical API calls in the HBnB application. These diagrams illustrate the interaction between layers: **Presentation**, **Business Logic**, and **Persistence**, as well as how data flows between components during various operations.

---

## 🔐 1. User Registration

### 📝 Description
This sequence represents the process of registering a new user through the API. It includes data validation, user creation in the model layer, and persistence to the database.

### 📊 Diagram
```mermaid
sequenceDiagram
    participant Client
    participant API
    participant UserModel
    participant DB

    Client->>API: POST /register
    API->>UserModel: validate_register_data()
    UserModel->>DB: create_user(email, password, ...)
    DB-->>UserModel: user_created (UUID, timestamps)
    UserModel-->>API: return success
    API-->>Client: 201 Created + user info
🏠 2. Place Creation
📝 Description
This sequence outlines how a user can create a new place listing. It includes authorization, validation, and saving the place information in the database.

📊 Diagram
mermaid
Copy code
sequenceDiagram
    participant Client
    participant API
    participant PlaceModel
    participant DB

    Client->>API: POST /places
    API->>PlaceModel: validate_place_data()
    PlaceModel->>DB: insert_place(user_id, name, location, ...)
    DB-->>PlaceModel: place_saved (UUID, timestamps)
    PlaceModel-->>API: return success
    API-->>Client: 201 Created + place info
📝 3. Review Submission
📝 Description
This sequence shows how a user submits a review for a specific place. The request is validated and then stored in the database linked to the proper user and place.

📊 Diagram
mermaid
Copy code
sequenceDiagram
    participant Client
    participant API
    participant ReviewModel
    participant DB

    Client->>API: POST /reviews
    API->>ReviewModel: validate_review_data()
    ReviewModel->>DB: insert_review(user_id, place_id, text)
    DB-->>ReviewModel: review_saved
    ReviewModel-->>API: return confirmation
    API-->>Client: 201 Created + review info
📥 4. Fetching List of Places
📝 Description
This sequence illustrates how a client requests a filtered list of places. The API parses parameters, interacts with the model, and retrieves data from the database.

📊 Diagram
mermaid
Copy code
sequenceDiagram
    participant Client
    participant API
    participant PlaceModel
    participant DB

    Client->>API: GET /places?city_id=xyz
    API->>PlaceModel: fetch_by_city(city_id)
    PlaceModel->>DB: query_places(city_id)
    DB-->>PlaceModel: list_of_places
    PlaceModel-->>API: serialize list
    API-->>Client: 200 OK + JSON response
