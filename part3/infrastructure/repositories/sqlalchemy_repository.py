from app.extensions import db
from infrastructure.repositories.repository_interface import RepositoryInterface

class SQLAlchemyRepository(RepositoryInterface):
    def __init__(self, model):
        self.model = model

    def get(self, id):
        return db.session.get(self.model, id)

    def add(self, obj):
        db.session.add(obj)
        db.session.commit()

    def delete(self, obj):
        db.session.delete(obj)
        db.session.commit()

    def all(self):
        return db.session.query(self.model).all()

