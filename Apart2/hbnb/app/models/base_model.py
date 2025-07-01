# app/models/base_model.py

import uuid
from datetime import datetime

class BaseModel:
    """Base class that provides common attributes and methods to all models."""

    def __init__(self):
        # Unique identifier
        self.id = str(uuid.uuid4())
        # Timestamp for creation
        self.created_at = datetime.now()
        # Timestamp for last update
        self.updated_at = datetime.now()

    def save(self):
        """Update the updated_at timestamp when the object is modified."""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update attributes from a dictionary and refresh updated_at timestamp."""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()

    def to_dict(self):
        """Return dictionary representation of the object."""
        return self.__dict__
