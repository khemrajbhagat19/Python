n=[2,4,5,6,8,11,14,25,27,31]
for x in n:
    i=1
    flag=0
    while i<=x:
        if x%i==0:
            flag+=1
        i+=1
    if flag==2:
         print(x)
