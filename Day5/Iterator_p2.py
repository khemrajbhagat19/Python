l=[5,8,7,3,6,2]

iter_obj1=iter(l)
print(type(iter_obj1))
print("id of iter_obj1: ",id(iter_obj1))

iter_obj2=iter(iter_obj1)
print(type(iter_obj2))
print("id of iter_obj2: ",id(iter_obj2))


