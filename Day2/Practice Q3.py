class Circle:
    PI=3.14
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return Circle.PI* self.radius*self.radius
    def circum(self):
        return 2*Circle.PI*self.radius

    def display(self):
        print(f"Radius : {self.radius}")
        print(f"Area : {self.area()}")
        print(f"Circumference : {self.circum()}")
s1=Circle(5)
s1.area()
s1.circum()
s1.display()