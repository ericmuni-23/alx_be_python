#!/usr/bin/env python3
import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


# main.py (Provided for Testing)
from polymorphism_demo import Rectangle, Circle

# Create instances of Rectangle and Circle
rect = Rectangle(4, 5)
circle = Circle(3)

# Calculate and print the areas
print(f"Rectangle area: {rect.area()}")
print(f"Circle area: {circle.area()}")
