__author__ = 'segordon'

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


def prime_check(n):
    if n == 0 or n == 1:
        return False
    if n == 2 or n == 3:
        return True
    else:
        for i in range(2,n-1):
            if n % i == 0:
                return False
            else:
                return True

primes = []

while len(primes) <= 10001:
