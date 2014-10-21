# coding=utf-8
__author__ = 'segordon'

# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

palindromes = []

def palindrome_check(n):
    return str(n) == str(n)[::-1]


for i in range (999,100,-1):
    for x in range(999,100,-1):
        product = i*x
        if palindrome_check(product) == True:
            palindromes.append(product)

print max(palindromes)