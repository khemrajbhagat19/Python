'''numbers=[1,2,3,4,5,6,7,8,9,10]

def is_even(n):
    if n%2==0:
        return True

even_numbers=filter(is_even,numbers)
even_numbers_list=list(even_numbers)
print(even_numbers_list)'''

numbers=[1,2,3,4,5,6,7,8,9,10]

even_numbers=filter(lambda n:n%2==0,numbers)
even_numbers_list=list(even_numbers)
print(even_numbers_list)

age=[5,18,23,15,25,65,74,85,12]
adults=filter(lambda n:n>=18,age)
print(list(adults))