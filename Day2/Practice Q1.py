class pq2:
    def __init__(self):
        print("This is default constructor")


class pq1:

    def __init__(self,name):
        self.name=name
        print("Parameterized constructor called")
    def __del__(self):
        print("Destructor called")
k1=pq2()
k2=pq1("KRB")

