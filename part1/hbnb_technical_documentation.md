# HBnB Technical Documentation

**Author:** Ahmed Dawwari, Saad Alarifi and Haidar Alessa  
**Project:** HBnB - Holberton BnB Application  
**Date:** 2025-06-02  
**Purpose:** This document serves as a comprehensive blueprint for the HBnB project. It gathers all architectural and design diagrams alongside explanatory notes to guide implementation and provide a clear reference for the system's structure and behavior.

---

## Table of Contents

1. [Introduction](#introduction)  
2. [High-Level Architecture](#high-level-architecture)  
3. [Business Logic Layer](#business-logic-layer)  
4. [API Interaction Flow](#api-interaction-flow)  
5. [Summary](#summary)

---

## Introduction

The HBnB project is a web-based application designed to facilitate the rental and booking of places, similar to Airbnb. This document compiles key design elements and diagrams developed to model the system's architecture, business logic, and API interactions.

The goal is to provide developers and stakeholders with a clear understanding of how the system's components interact, ensuring a smooth implementation phase and maintainable codebase.

---

## High-Level Architecture

### Overview

The system is designed using a layered architecture pattern, separating concerns into distinct layers:

- **Presentation Layer:** Handles HTTP requests and responses, user interface, and client interactions.
- **Business Logic Layer:** Contains core domain entities and business rules.
- **Persistence Layer:** Manages data storage and retrieval, interacting with the database.

This layered approach promotes maintainability, scalability, and testability.

### High-Level Package Diagram

```mermaid
classDiagram
class API {
  +handleRequest()
}
class BusinessLogic {
  +validateData()
  +processBusinessRules()
}
class Persistence {
  +save()
  +retrieve()
}
API --> BusinessLogic : uses
BusinessLogic --> Persistence : accesses
Explanation:

The API layer receives and processes user requests.

It delegates business validations and operations to the Business Logic layer.

The Persistence layer handles all database operations, ensuring data is saved or fetched as needed.

This separation allows clear flow and modular design.

Business Logic Layer
Detailed Class Diagram
mermaid
Copy code
classDiagram
class User {
  +UUID id
  +string email
  +string password
  +datetime created_at
  +datetime updated_at
  +register()
  +authenticate()
}
class Place {
  +UUID id
  +string name
  +string description
  +float price
  +datetime created_at
  +datetime updated_at
  +addAmenity()
  +removeAmenity()
}
class Review {
  +UUID id
  +string text
  +UUID user_id
  +UUID place_id
  +datetime created_at
  +datetime updated_at
  +submitReview()
}
class Amenity {
  +UUID id
  +string name
  +datetime created_at
  +datetime updated_at
  +getDetails()
}

User "1" -- "*" Review : writes >
Place "1" -- "*" Review : receives >
Place "1" -- "*" Amenity : has >
Explanation:

User: Represents system users with unique identifiers and authentication methods.

Place: Represents rental listings, each linked to amenities and reviews.

Review: Holds user-generated feedback tied to users and places.

Amenity: Defines features or facilities available at places.

Relationships illustrate that users can write multiple reviews, places have multiple reviews and amenities.

API Interaction Flow
Sequence Diagrams for API Calls
1. User Registration
mermaid
Copy code
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
Explanation:
Shows the flow from receiving user data, validation, saving to the database, and responding with confirmation.

2. Place Creation
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
Explanation:
Details how a new place listing is validated and stored in the database.

3. Review Submission
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
Explanation:
Describes the steps for submitting a new review, including validation and saving.

4. Fetching List of Places
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
Explanation:
Illustrates fetching a filtered list of places, showing request handling and data retrieval.


