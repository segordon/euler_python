__author__ = 'segordon'

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a**2 + b**2 = c**2
#
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def find_triplets():
    for c in range(2, 1000):
        for a in range(1,c):
            b = 1000 - c - a
            if (a ** 2) + (b ** 2) == (c ** 2):
                print a,b,c,a+b+c,a*b*c
find_triplets()