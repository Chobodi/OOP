from abc import ABC, abstractmethod

# Abstract class for Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method (no implementation)

    @abstractmethod
    def perimeter(self):
        pass  # Abstract method (no implementation)

# Concrete subclass for Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Concrete subclass for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Example Usage
rect = Rectangle(5, 3)
circle = Circle(8)

print(f"Rectangle Area: {rect.area()}")        # Output: Rectangle Area: 15
print(f"Rectangle Perimeter: {rect.perimeter()}")

