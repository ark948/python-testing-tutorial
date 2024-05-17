from abc import ABC, abstractmethod

# reminder: abstractmethods are methods that are declared but not defined and must be overridden
# Abstract class: a class that can be declared but not instantiated, only used for other classes to inherit from

class Shape(ABC):
    @abstractmethod
    def area() -> float:
        pass