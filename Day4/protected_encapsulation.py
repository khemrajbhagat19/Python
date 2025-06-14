class Student:
    _name= None
    _roll= None
    _branch= None

    def __init__(self,name,roll,branch):
        self._name=name
        self._roll=roll
        self._branch=branch

    def _displayInfo(self):
        print(f"Roll: {self._roll}")
        print(f"Branch: {self._branch}")

class Learnowx(Student):
    def __init__(self,name,roll,branch):
        Student.__init__(self,name,roll,branch)

    def displayDetails(self):
        print("Name: ",self._name)
        self._displayInfo()

obj=Learnowx("Aditya",101203,"Data Science")
obj.displayDetails()
