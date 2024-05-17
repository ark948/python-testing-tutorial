import math
from shapes.shape import Shape

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        if radius < 0:
            raise ValueError('The radius cannot be negative.')
        
        self._radius = radius
        super().__init__()

    def area(self) -> float:
        return math.pi * math.pow(self._radius, 2)
