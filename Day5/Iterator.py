list=[20,80,40,75,93]
iter_obj=iter(list)
print(iter_obj)
print(type(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))

for i in iter_obj:
    print(i) # 93 is being printed by loop
