__author__ = 'segordon'

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# a big ugly way to do it.

count = 1
trip = 0
while trip == 0:
    if count % 1 == 0 and count % 2 == 0 and count % 3 == 0 and \
                            count % 4 == 0 and count % 5 == 0 and \
                            count % 6 == 0 and count % 7 == 0 and \
                            count % 8 == 0 and count % 9 == 0 and \
                            count % 10 == 0 and count % 11 == 0 and \
                            count % 12 == 0 and count % 13 == 0 and \
                            count % 14 == 0 and count % 15 == 0 and \
                            count % 16 == 0 and count % 17 == 0 and \
                            count % 18 == 0 and count % 19 == 0 and \
                            count % 20 == 0:
        print count
        trip =+ 1
    else:
        count += 1