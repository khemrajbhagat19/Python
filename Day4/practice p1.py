class Animal:
    name=""

    def eat(self):
        print("I can eat")

class Dog(Animal):

    def display(self):
        print("My name is ",self.name)

labrador=Dog()
labrador.name="Rohu"
labrador.eat()
labrador.display()