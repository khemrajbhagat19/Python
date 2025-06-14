from abc import ABC, abstractmethod
class Computer (ABC):
    @abstractmethod
    def process(self):
        pass
    def message(self):
        print("Computer is an electronic device")

class Laptop (Computer):
    def process(self):
        print("Executing Laptop Process")
class  Desktop(Computer):
    def process(self):
        print("Executing Desktop Process")

com1=Laptop()
com2=Desktop()
com1.process()
com2.message()
com2.process()