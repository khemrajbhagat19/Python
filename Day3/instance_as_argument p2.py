class Person:
    def __init__(self,name):
        self.name=name

    def __repr__(self):
        return f"Person {self.name}"

class Greeting:
    def generate_meeting(self,person):
        return f"Hello {person.name}! Welcome!"

person=Person("Alice")
greeting=Greeting()

message=greeting.generate_meeting(person)
print(message)