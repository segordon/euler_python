__author__ = 'segordon'
import random

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a**2 + b**2 = c**2
#
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# a real silly implementation that works, but randomly. It may be quick... but it never is.
# unfinished, and never will be.

def list_squares(n):
    list = []
    for i in range(n+1):
        list.append(i**2)
    return list[1:]

def triplet_finder(n):
    list_squares(n)
    c = random.choice(list_squares(n))
    a = random.choice(list_squares(n))
    b = random.choice(list_squares(n))
    while c <= 8:
        c = random.choice(list_squares(n))

    while b >= c:
        b = random.choice(list_squares(n))

    while a >= b:
        a = random.choice(list_squares(n))
    return a,b,c

triplet_list = []

possible_triplet = triplet_finder(32)

# for x in range(10):
#     if possible_triplet not in triplet_list:
#         triplet_list.append(possible_triplet)
#         possible_triplet = triplet_finder(32)
#
# print triplet_list