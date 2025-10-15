import math

# Creating base class called Shape
class Shape:
    def calculate_area(self):
        raise NotImplementedError("Child classes must implement this method")
    def calculate_perimeter(self):
        raise NotImplementedError("Child classes must implement this method")

# Creating a child class called Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def calculate_perimeter(self):
        return math.pi * self.radius * 2

# Creating a child class called Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return 2 * (self.height + self.width)

# Creating a child class called Triangle
class Triangle(Shape):
    def __init__(self, base, height, side_a, side_b, side_c):
        self.base = base
        self.height = height
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def calculate_perimeter(self):
        return self.side_a + self.side_b + self.side_c

# Testing outputs
my_circle = Circle(5)
print(f"Circle area: {my_circle.calculate_area()}")
print(f"Circle perimeter: {my_circle.calculate_perimeter()}")
my_rectangle = Rectangle(4, 6)
print(f"Rectangle area: {my_rectangle.calculate_area()}")
print(f"Rectangle area: {my_rectangle.calculate_perimeter()}")
my_triangle = Triangle(4, 3, 3, 4, 5)
print(f"Triangle area: {my_triangle.calculate_area()}")
print(f"Triangle area: {my_triangle.calculate_perimeter()}")