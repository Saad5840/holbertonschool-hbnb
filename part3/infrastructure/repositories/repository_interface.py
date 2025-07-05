from abc import ABC, abstractmethod

class RepositoryInterface(ABC):

    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def delete(self, obj):
        pass

    @abstractmethod
    def all(self):
        pass

