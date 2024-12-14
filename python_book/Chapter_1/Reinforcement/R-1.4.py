'''
Write a short Python function that takes a positive integer n and returns the sum of the squares of all the positive integers smaller than n. (code_four.py)

'''

def square(n):
    return sum(i**2 for i in range(1,n))

print(square(5))