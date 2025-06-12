import math

class Fraction:
    def __init__(self,numerator,denominator):
        self.numerator=numerator
        self.denominator=denominator
        self.simplify()

    def simplify(self):
        common_divisior=math.gcd(self.numerator,self.denominator)
        self.numerator//=common_divisior
        self.denominator//=common_divisior

    def __add__(self, other):
        new_numerator=self.numerator*other.denominator+other.numerator*self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator,new_denominator)

    def __eq__(self, other):
        return self.numerator==other.numerator and self.denominator==other.denominator

    def __lt__(self, other):
        return self.numerator*other.denominator<other.numerator*self.denominator

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

s1=Fraction(5,5)
s2=Fraction(5,5)

add=s1.__add__(s2)
eq=s1.__eq__(s2)
lt=s1.__lt__(s2)
print(add,"  ",eq,"  " ,lt)