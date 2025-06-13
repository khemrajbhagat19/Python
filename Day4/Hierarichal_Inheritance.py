class parent:
    def feature1(self):
        print("Feature 1 of parent")

    def feature2(self):
        print("Feature 2 of parent")
class you(parent):  # mother is inheriting methods of parent
    def feature3(self):
        print("Feature 3 of you")

    def feature4(self):
        print("Feature 4 of you")

class brother(parent):   # child is inheriting methods of mother or we can directly pass mother and parent both as argument to access their methods
    def feature5(self):
        print("Feature 5 of brother")

    def feature6(self):
        print("Feature 6 of brother")

class sister(parent):   # child is inheriting methods of mother or we can directly pass mother and parent both as argument to access their methods
    def feature7(self):
        print("Feature 7 of sister")

    def feature8(self):
        print("Feature 8 of sister")
p=parent()
y=you()
b=brother()
s=sister()
y.feature1()
y.feature2()
y.feature3()
y.feature4()

b.feature1()
b.feature2()
b.feature5()
b.feature6()

s.feature1()
s.feature2()
s.feature7()
s.feature8()


