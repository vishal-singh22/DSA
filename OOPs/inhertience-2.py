# Design a class Shape with a method area. Create two subclasses, Circle and Rectangle, 
# that override the area method to calculate the area for each shape.

import math as m

class shape:
    def area(self):
        pass

class Circle(shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return m.pi* self.radius**2
    
class Rectangle(shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length*self.width
    
    
if __name__ == "__main__":
    # Create instances of Circle and Rectangle
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    # Print area of the circle and rectangle
    print(f"Area of the circle: {circle.area():.2f}")
    print(f"Area of the rectangle: {rectangle.area():.2f}")
