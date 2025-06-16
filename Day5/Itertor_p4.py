import sys
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for num in l:
    print(num**2)
print("for L",sys.getsizeof(l),"Bytes")


var=range(1,16)

print("for var",sys.getsizeof(var),"Bytes")