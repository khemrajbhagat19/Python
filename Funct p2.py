def sum_num(num1,*num):
    result=num1
    for i in num:
        result+=i
    return result
r=sum_num(10,20,30)
print(f"The sum of numbers is: {r}")

r=sum_num(10,20,30,40,50)
print(f"The sum of numbers is: {r}")