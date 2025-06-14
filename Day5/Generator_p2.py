def is_prime(num):
    if num<2:
        return False
    for i in range (2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def generate_primes(start,end):
    for num in range(start,end+1):
        if is_prime(num):
            yield num

primes_generator=generate_primes(5,50)

for primes in primes_generator:
    print(primes,end=" ")