# abc: abstract base class
from abc import ABC, abstractmethod
# import math module as math.pi is required
from math import pi

class shape(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def area(self):
        print("Generic area() called")
    
    @abstractmethod
    def perimeter(self):
        print("Generic perimeter() called")
    
class Rectangle(shape):
    def __init__(self, width = 0, length = 0):
        self.width = width
        self.length = length
    
    def area(self):
        return (self.width * self.length)
    
    def perimeter(self):
        return 2 * (self.width + self.length)


class Circle(shape):
    def __init__(self, radius = 0):
        self.radius = radius
    
    def area(self):
        return (pi * (self.radius^2))
    
    def perimeter(self):
        return 2 * pi * self.radius

class Square(Rectangle):
    def __init__(self, length=0):
        super().__init__(length, length)