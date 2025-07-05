from datetime import datetime
from sqlalchemy.ext.declarative import declared_attr
from app.extensions import db

class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.String(60), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

