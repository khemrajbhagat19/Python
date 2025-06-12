class Person:
    def __new__(self):
        print("This is new method")
        self.__init__(self)
    def __init__(self):
        print("This is init method")

s1=Person()