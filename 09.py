__author__ = 'segordon'

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a**2 + b**2 = c**2
#
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Euclid's formula


def find_triplets(i):
    m = 2
    n = 1
    for x in range(i):
        a = (m ** 2) - (n ** 2)
        b = 2 * (m*n)
        c = (m ** 2) + (n ** 2)
        m += 1
        n += 1
        return a,b,c

print find_triplets(3)