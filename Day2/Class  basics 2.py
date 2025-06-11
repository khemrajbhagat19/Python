class Computer:
    def __init__(self,name,cpu,ram):
        self.name=name
        self.cpu=cpu
        self.ram=ram

    def configuration(self):
        print(self.name,self.cpu, self.ram)

m1=Computer("HP",16,512)
m2=Computer("HP",28,512)
m1.configuration()
m2.configuration()

class Car_design:
    def __init__(self,name,mil,year):
        self.name=name
        self.mil=mil
        self.year=year

    def info(self):
        print(self.name,self.mil, self.year)

m1=Car_design("Buggati",90,2021)
m2=Car_design("Pagani",95,2023)
m1.info()
m2.info()