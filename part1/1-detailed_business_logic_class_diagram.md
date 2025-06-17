```mermaid
classDiagram
    class User {
        +string email
        +string password
        +string first_name
        +string last_name
		+bool is_admin
		+register()
		+update_profile()
		+delete()
		+login()
		
    }

    class Place {
        +string name
        +string description
        +float latitude
        +float longitude
		+float price
        +int number_rooms
        +User owner
		+create()
		+update()
		+delete()
		+list()
    }

    class Review {
		+int rating
        +string text
        +User reviewer
        +Place place
		+create()
        +update()
        +delete()
        +list()
    }

    class Amenity {
        +string name
		+create()
        +update()
        +delete()
        +list()
    }

	class BaseModel {
    +UUID4 id
    +datetime created_atAdd commentMore actions
    +datetime updated_at
    +save() void
    +to_dict() dict

	}

	More actions
	User --|> BaseModel
	Place --|> BaseModel
	Review --|> BaseModel
	Amenity --|> BaseModel


    Place --> User : "1 owner"
    Review --> User : "1 reviewer"
    Review --> Place : "1 place"
    Place --> "0..*" Amenity : "has"

