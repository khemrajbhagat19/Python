
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return F"The name is {self.name} and age is {self.age}"

p=Person("Amit",35)
print(p)
