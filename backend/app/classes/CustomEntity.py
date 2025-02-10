from abc import ABC, abstractmethod

# Abstract base class (interface in C++ or Java) for all sub-classes to make nested structure
class CustomEntity(ABC):
    def __init__(self):
        pass  # Ensure that the __init__ method has a body
        
    @abstractmethod
    def to_dict(self):
        """Convert the entity to a dictionary."""
        pass

    @abstractmethod
    def add_sub_entity(self, sub_entity):
        """Add a sub-entity (e.g., a shot to a game, a game to a player summary)."""
        pass
