a=int(input("Enter a :"))
b=int(input("Enter b :"))
c=int(input("Enter c :"))
if a>b:
    if a>c:
        print(f"{a} is largest")
elif b>a:
    if b>c:
        print(f"{b} is largest")
else:
        print(f"{c} is largest")