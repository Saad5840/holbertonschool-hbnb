```mermaid
erDiagram
    USER ||--o{ PLACE : owns
    PLACE ||--o{ REVIEW : has
    PLACE ||--o{ PLACE_AMENITY : links
    AMENITY ||--o{ PLACE_AMENITY : linked

