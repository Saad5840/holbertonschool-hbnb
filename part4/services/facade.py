from app.extensions import db
from domain.user import User
from infrastructure.models.user import User
from infrastructure.repositories.sqlalchemy_repository import SQLAlchemyRepository

user_repo = SQLAlchemyRepository(User)

def create_user(data):
    user = User(
        id=data.get('id'),
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        email=data.get("email"),
        is_admin=data.get("is_admin", False)
    )
    user.set_password(data.get("password"))
    user_repo.add(user)
    return user

def get_user_by_email(email):
    return db.session.query(User).filter_by(email=email).first()

