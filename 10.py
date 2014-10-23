__author__ = 'segordon'
import math

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def prime_check(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


primes = []
i = 1

while len(primes) <= 150000:
    if prime_check(i) == True:
        primes.append(i)
        i += 1
    else:
        i += 1

primes_less_than_2m = [i for i in primes if i <= 2000000]
primes_less_than_2m.remove(1)
print sum(primes_less_than_2m)