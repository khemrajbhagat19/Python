from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def description(self):
        return "This is a shape"

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius**2

    def perimeter(self):
        return 2*3.14*self.radius

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*(self.length+self.width)

circle=Circle(5)
rect=Rectangle(4,6)

print(f"Circle area: {circle.area()}\nCircle perimeter: {circle.perimeter()}\nCircle Description: {circle.description()}\nRectangle Area: {rect.area()}\nRectangle perimeter: {rect.perimeter()}\nRectangle Description: {rect.description()}")
