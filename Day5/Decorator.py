def decor(addition):
    def inner():
        result=addition()
        num3=float(input("Enter number 3: "))
        result+=num3
        return result
    return inner
@decor
def addition():
    num1=float(input("Enter number 1: "))
    num2=float(input("Enter number 2: "))
    result =num1+num2
    return result

print(addition())
