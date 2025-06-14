class Bird:
    def fly(self):
        print("fly with wings")

class Airplane:
    def fly(self):
        print("fly with fuel")

class fish:
    def swim(self):
        print("fish swim in sea")

for obj in Bird(),Airplane(),fish():
    obj.fly() # since fly function is not in fish therefore ana error will be raised