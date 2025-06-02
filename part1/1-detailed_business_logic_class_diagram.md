classDiagram
class BaseModel {
    +UUID4 id
    +datetime created_at
    +datetime updated_at
    +save() void
    +to_dict() dict
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
    +List~Amenity~ amenities
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

Place --> User : "1 owner"
Review --> User : "1 reviewer"
Review --> Place : "1 place"
Place --> "0..*" Amenity : "has"

