class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def compute(self):
        self.total=sum(self.marks)
        self.average=self.total/len(self.marks)

    def display(self):
        print(f"Student name : {self.name}")
        print(f"Marks : {self.marks}")
        print(f"Total Marks : {self.total}")
        print(f"Average : {self.average}")
student1=Student("Khemraj",[80,95,99])
student1.compute()
student1.display()