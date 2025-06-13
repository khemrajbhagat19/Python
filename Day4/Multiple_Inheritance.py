class parent:
    def feature1(self):
        print("Feature 1 of parent")

    def feature2(self):
        print("Feature 2 of parent")
class mother(parent):  # mother is inheriting methods of parent
    def feature3(self):
        print("Feature 3 of mother")

    def feature4(self):
        print("Feature 4 of mother")

class child(mother):   # child is inheriting methods of mother or we can directly pass mother and parent both as argument to access their methods
    def feature5(self):
        print("Feature 5 of child")

    def feature6(self):
        print("Feature 6 of child")
p=parent()
m=mother()
c=child()
c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()
c.feature6()


