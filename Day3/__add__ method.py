num1=10
x=num1+5
print(x," #using normal addition in integers")

num2=10
y=num2.__add__(5)
print(y," #using __add__ method for addition in integers")


st1='10'
z=st1+'5'
print(z," #using normal concatenation in string")

st2='10'
a=st2.__add__('5')
print(a," #using __add__ method for concatenation in string")