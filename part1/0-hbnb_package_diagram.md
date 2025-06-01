# HBnB Evolution – High-Level Package Diagram

## 📌 Objective

This document presents the high-level package diagram for the HBnB Evolution application. It shows the three-layer architecture — **Presentation**, **Business Logic**, and **Persistence** — and how these layers interact using the **Facade Pattern**.

---

## 🧱 Architecture Overview

### 1. Presentation Layer
- Responsible for user interaction.
- Includes API endpoints and service interfaces.
- Sends requests to the Business Logic layer via the Facade.

### 2. Business Logic Layer
- Contains core application logic and models:
  - `User`, `Place`, `Review`, and `Amenity`.
- Acts as the centralized brain of the system.
- Provides a **Facade Interface** to expose controlled access to its functionalities.

### 3. Persistence Layer
- Handles data access and storage.
- Includes database connectors, data mappers, or repositories.
- Business Logic delegates data operations to this layer.

---

## 🎯 Facade Pattern Role

The **Facade Pattern** is used between:
- **Presentation → Business Logic**

It simplifies the interaction by exposing a unified interface (e.g., `HBnBService`) that aggregates operations on Users, Places, Reviews, and Amenities. This hides internal complexity and makes the system easier to use and test.

---

## 📊 Mermaid.js Package Diagram

```mermaid
classDiagram
    class PresentationLayer {
        <<Interface>>
        +APIService
        +UserController
        +PlaceController
        +ReviewController
        +AmenityController
    }

    class BusinessLogicLayer {
        +HBnBFacade
        +User
        +Place
        +Review
        +Amenity
    }

    class PersistenceLayer {
        +UserRepository
        +PlaceRepository
        +ReviewRepository
        +AmenityRepository
        +DatabaseConnector
    }

    PresentationLayer --> BusinessLogicLayer : Facade Interface
    BusinessLogicLayer --> PersistenceLayer : Data Access
