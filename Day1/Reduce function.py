from functools import reduce
num_list=[20,15,52,22,72,19,7]
large=reduce(lambda x,y:x if x>y else y,num_list)
print (large)

least=reduce(lambda x,y:x if x<y else y,num_list)
print (least)

numbers=[1,2,3,4,5]
total_sum=reduce(lambda x,y:x+y,numbers)
print(total_sum)