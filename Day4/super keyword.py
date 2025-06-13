class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        print((f"First name is {fname} and last name is {lname}"))

class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        print("Inside Student class init")

s=Student("Mohit","Kumar")