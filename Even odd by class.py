class Number:
    even=[]
    odd=[]
    def __init__(self,num):
        self.num=num
        if num%2==0:
            Number.even.append(num)
        else:
            Number.odd.append(num)
N1=Number(21)
N2=Number(32)
N3=Number(43)
N4=Number(54)
N5=Number(65)
print("Even numbers are: ",Number.even)
print("Odd numbers are: ",Number.odd)