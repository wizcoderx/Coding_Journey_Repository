#Write a function that calculates the factorial of a non-negative integer.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

import sys
sys.setrecursionlimit(100010)
print(factorial(5)) # 120