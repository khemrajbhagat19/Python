class Student:
    def __init__(self):
        print("Default constructor called")

    def __init__(self,name,marks,age):
        self.name=name
        self.marks=marks
        self.age=age
        print("Parameterized constructor called")
    def show_info(self):
        print("Name", self.name)
        print("Marks", self.marks)
        print("Age", self.age)
    def __del__(self):
        print("Destructors called")

s1=Student("Khemraj",119,19)
s2=Student("Meghraj",150,19)
s3=Student("Ashish",120,19)
s1.show_info()
s2.show_info()
s3.show_info()
