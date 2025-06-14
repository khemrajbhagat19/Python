class myclass:
    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s
s=myclass()

print(s.sum(2))
print(s.sum(2,3))
print(s.sum(2,3,5))