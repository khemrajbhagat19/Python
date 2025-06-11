class Student:
    counter =0
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        Student.counter=Student.counter+1
    def msg(self):
        print("Hello "+self.name+" you got ",self.marks,"% marks")
    @classmethod
    def object_count(cls):
        return cls.counter
s1=Student("Abhishek",65)
s2=Student("Amit",89)
print(Student.object_count())
print(s1.object_count())