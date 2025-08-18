from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from .base import Base
from app.extensions import bcrypt
from datetime import datetime

class User(Base):
    __tablename__ = 'users'

    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    is_admin = Column(Boolean, default=False)

    places = relationship('Place', back_populates='owner', cascade='all, delete-orphan')
    reviews = relationship('Review', back_populates='user', cascade='all, delete-orphan')

    def set_password(self, raw_password):
        self.password = bcrypt.generate_password_hash(raw_password).decode("utf-8")

    def check_password(self, raw_password):
        return bcrypt.check_password_hash(self.password, raw_password)

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "is_admin": self.is_admin,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

