__author__ = 'segordon'
import math

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def prime_check(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


primes = []
i = 1

while len(primes) <= 10001:
    if prime_check(i) == True:
        primes.append(i)
        i += 1
    else:
        i += 1
print primes[-1]