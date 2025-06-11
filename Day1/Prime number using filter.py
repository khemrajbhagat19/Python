l1=[2,9,56,87,3,21,45,65,876,12312,654,7768,879]
def prime(l):
    for x in l:
        a=1
        c=0
        while a<=x:
            if x%a==0:
                c+=1
        if c==2:
            return True
print(list(filter(prime,l1)))