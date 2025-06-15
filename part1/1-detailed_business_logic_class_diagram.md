```mermaid
classDiagram
    class User {
  		+UUID4 id
        +datetime created_at
        +datetime updated_at
        +string email
        +string password
        +string first_name
        +string last_name
		+register()
		+update_profile()
		+delete()
		+login()
		
    }

    class Place {
		+UUID4 id
        +datetime created_at
        +datetime updated_at
        +string name
        +string description
        +float latitude
        +float longitude
        +int number_rooms
        +User owner
		+create()
		+update()
		+delete()
		+list()
    }

    class Review {
		+UUID4 id
        +datetime created_at
        +datetime updated_at
        +string text
        +User reviewer
        +Place place
		+create()
        +update()
        +delete()
        +list()
    }

    class Amenity {
  		+UUID4 id
		+Place place
        +datetime created_at
        +datetime updated_at
        +string name
		+create()
        +update()
        +delete()
        +list()
    }


    Place --> User : "1 owner"
    Review --> User : "1 reviewer"
    Review --> Place : "1 place"
    Place --> "0..*" Amenity : "has"

