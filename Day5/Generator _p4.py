def my_gen(x):
    while(x>0):
        if x%2==0:
            yield "Even"
        else:
            yield "Odd"
        x-=1

for i in  my_gen(7):
    print(i)