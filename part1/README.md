# HBnB Architecture Documentation

**Author:** Ahmed

---

## 📘 Introduction

This document provides a complete technical overview of the HBnB application as part of Part 1 of the Holberton School project. It consolidates all architecture and design documentation, including:

1. High-Level Package Diagram
2. Detailed Class Diagram for the Business Logic Layer
3. Sequence Diagrams for API Calls
4. Explanatory Notes for each component

The purpose of this document is to offer a clear blueprint for the system’s design, facilitating future development and maintenance.

---

## 🧱 0. High-Level Package Diagram

### 📊 Diagram (Mermaid.js)

```mermaid
classDiagram
class PresentationLayer {
    <<Interface>>
    +ServiceAPI
}
class BusinessLogicLayer {
    +ModelClasses
}
class PersistenceLayer {
    +DatabaseAccess
}
PresentationLayer --> BusinessLogicLayer : Facade Pattern
BusinessLogicLayer --> PersistenceLayer : Database Operations
```

### 🧾 Explanation

* **Presentation Layer**: Contains REST APIs and user-facing services.
* **Business Logic Layer**: Houses core logic and domain models (User, Place, Review, Amenity).
* **Persistence Layer**: Handles direct communication with the database.
* **Facade Pattern**: Used between layers to decouple logic and simplify access.

---

## 🧩 1. Business Logic Class Diagram

### 📊 Diagram (Mermaid.js)

```mermaid
classDiagram
class BaseModel {
    +UUID4 id
    +datetime created_at
    +datetime updated_at
    +save()
    +to_dict()
}
class User {
    +string email
    +string password
    +string first_name
    +string last_name
}
class Place {
    +string name
    +string description
    +float latitude
    +float longitude
    +int number_rooms
    +User owner
}
class Review {
    +string text
    +User reviewer
    +Place place
}
class Amenity {
    +string name
}

User --|> BaseModel
Place --|> BaseModel
Review --|> BaseModel
Amenity --|> BaseModel
Place --> User : owned by
Review --> User : written by
Review --> Place : about
```

### 🧾 Explanation

Each model inherits from `BaseModel` to unify ID and timestamp behavior. Relationships:

* User ↔ Place: A user owns places
* User ↔ Review: A user writes reviews
* Place ↔ Review: Reviews are attached to places
* Amenity: Standalone feature linked elsewhere

---

## 🔁 2. API Sequence Diagrams

### 🔐 A. User Registration

```mermaid
sequenceDiagram
participant Client
participant API
participant UserModel
participant DB

Client->>API: POST /register
API->>UserModel: validate_register_data()
UserModel->>DB: create_user()
DB-->>UserModel: success
UserModel-->>API: user_created
API-->>Client: 201 Created
```

### 🏠 B. Place Creation

```mermaid
sequenceDiagram
participant Client
participant API
participant PlaceModel
participant DB

Client->>API: POST /places
API->>PlaceModel: validate_place_data()
PlaceModel->>DB: insert_place()
DB-->>PlaceModel: place_saved
PlaceModel-->>API: success
API-->>Client: 201 Created
```

### 📝 C. Review Submission

```mermaid
sequenceDiagram
participant Client
participant API
participant ReviewModel
participant DB

Client->>API: POST /reviews
API->>ReviewModel: validate_review()
ReviewModel->>DB: insert_review()
DB-->>ReviewModel: ok
ReviewModel-->>API: review_created
API-->>Client: 201 Created
```

### 📥 D. Fetch List of Places

```mermaid
sequenceDiagram
participant Client
participant API
participant PlaceModel
participant DB

Client->>API: GET /places?city_id=abc
API->>PlaceModel: fetch_by_city(city_id)
PlaceModel->>DB: query_places_by_city()
DB-->>PlaceModel: list_of_places
PlaceModel-->>API: return_data
API-->>Client: 200 OK + JSON
```

### 🧾 Explanation

Each API call flows from user input to the API, through validation and logic, then hits the DB layer. Responses are bubbled back through the same path.

---

## 📄 3. Conclusion

This document consolidates the foundational architecture and interaction diagrams for the HBnB application. It is intended to:

* Serve as a **reference blueprint** for the system
* Guide **future enhancements** and maintenance
* Align the team around a **clear architectural structure**

Prepared with care by Ahmed Dawwari, Saad Alarifi and Haidar Alessa

