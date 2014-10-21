__author__ = 'segordon'

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_squares():
    squares = []
    for i in range(1,101):
        squares.append(i**2)
    return sum(squares)

def square_sum():
    numbers = []
    for i in range(1,101):
        numbers.append(i)
    return sum(numbers) ** 2

print square_sum() - sum_squares()