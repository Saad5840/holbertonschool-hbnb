from abc import ABC, abstractmethod
import threading

class Repository(ABC):
    @abstractmethod
    def add(self, entity_type, obj):
        pass

    @abstractmethod
    def get_by_id(self, entity_type, obj_id):
        pass

    @abstractmethod
    def get_all(self, entity_type):
        pass

    @abstractmethod
    def update(self, entity_type, obj_id, data):
        pass

    @abstractmethod
    def delete(self, entity_type, obj_id):
        pass

    @abstractmethod
    def get_by_attribute(self, entity_type, attr_name, attr_value):
        pass


class InMemoryRepository(Repository):
    def __init__(self):
        self._storage = {
            'users': {},
            'amenities': {},
            'places': {},
            'reviews': {}
        }
        self._id_counter = 1
        self._lock = threading.Lock()

    def _generate_id(self):
        with self._lock:
            new_id = str(self._id_counter)
            self._id_counter += 1
            return new_id

    def add(self, entity_type, obj):
        if entity_type not in self._storage:
            raise ValueError(f"Unknown entity type: {entity_type}")

        if hasattr(obj, 'id') and obj.id:
            if obj.id in self._storage[entity_type]:
                raise ValueError(f"{entity_type} with id {obj.id} already exists")
        else:
            obj.id = self._generate_id()

        self._storage[entity_type][obj.id] = obj
        return obj

    def get_by_id(self, entity_type, obj_id):
        return self._storage.get(entity_type, {}).get(obj_id)

    def get_all(self, entity_type):
        return list(self._storage.get(entity_type, {}).values())

    def update(self, entity_type, obj_id, data):
        obj = self.get_by_id(entity_type, obj_id)
        if not obj:
            raise ValueError(f"{entity_type} with id {obj_id} not found")

        for key, value in data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        return obj

    def delete(self, entity_type, obj_id):
        if obj_id in self._storage.get(entity_type, {}):
            del self._storage[entity_type][obj_id]
        else:
            raise ValueError(f"{entity_type} with id {obj_id} not found")

    def get_by_attribute(self, entity_type, attr_name, attr_value):
        for obj in self._storage.get(entity_type, {}).values():
            if getattr(obj, attr_name, None) == attr_value:
                return obj
        return None


# Single instance for your application
in_memory_repo = InMemoryRepository()
