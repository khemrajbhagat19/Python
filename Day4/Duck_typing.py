class Duck:
    def quack(self):
        print("Quack!")
class Person:
    def quack(self):
        print("I'm quacking like a duck!")

    def eat(self):
        print("Person is eating")

duck=Duck()
person=Person()

duck.quack()
person.quack()
person.eat()