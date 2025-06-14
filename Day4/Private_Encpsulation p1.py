class Computer:
    def __init__(self):
        self.__maxprice=900 # private variable
    def sell(self):
         print(f"Selling Price: {self.__maxprice}")
    def setMaxPrice(self,price):  #function to change private variable as it can't be accessed outside the class
        self.__maxprice=price

c=Computer()
c.sell()
c.setMaxPrice(1000)
c.sell()