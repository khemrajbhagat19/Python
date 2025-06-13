class father:
    def feature1(self):
        print("Feature 1 of father")

    def feature2(self):
        print("Feature 2 of father")
class mother:
    def feature3(self):
        print("Feature 3 of mother")

    def feature4(self):
        print("Feature 4 of mother")

class child(mother,father):   # child is inheriting methods of mother and father
    def feature5(self):
        print("Feature 5 of child")

    def feature6(self):
        print("Feature 6 of child")
p=father()
m=mother()
c=child()
c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()
c.feature6()


