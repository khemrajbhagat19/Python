class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

# Create an instance of the person
person=Person("Khemraj",30)

# Use getattr to get the value of an attribute
name=getattr(person,"name")
print(f"Name : {name}")

#use setattr to set the value of an attribute
setattr(person,"age",31)
print(f"Updated age : {person.age}")

# Use hasattr to chck if an attribute exists
has_name=hasattr(person,"name")
print(f"Has attribute 'name' {has_name}")

# Use delattr to delete an attribute
delattr(person,"age")

# Check if the attribute age still exists
has_age=hasattr(person,"age")
print(f"Has attribute 'age' after deletion {has_name}")
