from shapes import *


rectangle = Rectangle(10, 5)
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")

square = Square(10)
print(f"Area: {square.area()}")
print(f"Perimeter: {square.perimeter()}")

circle = Circle(10)
print(f"Area: {circle.area():.3f}")
print(f"Perimeter: {circle.perimeter():.3f}")