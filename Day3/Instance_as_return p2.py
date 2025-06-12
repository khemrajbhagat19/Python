class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width*self.height

    def combined_rect(self,other):
        new_width=self.width+other.width
        new_height=self.height+other.height
        return Rectangle(new_width,new_height)

    def __repr__(self):
        return f"Rectangle({self.width},{self.height})"

rect1=Rectangle(4,5)
rect2=Rectangle(3,6)

combined_rect=rect1.combined_rect(rect2)
print(combined_rect)