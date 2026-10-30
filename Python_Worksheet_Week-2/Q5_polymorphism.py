import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


radius = float(input("Enter radius of circle: "))
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))

circle = Circle(radius)
rectangle = Rectangle(length, breadth)

print("Area of Circle:", circle.area())
print("Area of Rectangle:", rectangle.area())