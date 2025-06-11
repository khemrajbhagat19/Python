class Apple_design:
    count=0 #class variables or static variables
    def __init__(self,cpu,ram):  # self is default Constructor
        self.cpu=cpu
        self.ram=ram
    def mobile(self,cpu,ram):
        print("this apple phone 1")
        print(self.cpu,self.ram)
        print(type(self))

m1=Apple_design(3.5,8)
m2=Apple_design(4.5,16)
m1.mobile(3.5,8)
m2.mobile(4.5,16)